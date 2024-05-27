from fastapi import FastAPI, WebSocket, Request, File, UploadFile, Form, Request, HTTPException
from flask import request, jsonify
from pydantic import BaseModel
from llama_index.llms.llama_cpp import LlamaCPP
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import asyncio
import os
import json
from fastapi.middleware.cors import CORSMiddleware
import vertexai
from vertexai.generative_models import GenerativeModel
from openai import AzureOpenAI
from fastapi.responses import JSONResponse
from langchain.document_loaders import CSVLoader, PDFMinerLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import hashlib
import re
from datetime import datetime, timedelta



app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


max_new_tokens = 512
prompt_template = "<s>[INST] {prompt} [/INST]"
config_path = "model/config.json"
vertex_config_path = "model/vertex_config.json"
azure_config_path = "model/azure_config.json"

class Message(BaseModel):
    userInput: str
    model: str
    temperature: float

class Response(BaseModel):
    response: str

class ModelConfig(BaseModel):
    temp: float
    model: str
    gpu: bool
    agent: str

def load_config():
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    else:
        return {
            "temperature": 0.5,
            "model": "",
            "model_path": "",
            "gpu": False
        }
    
def load_vertex_config():
    if os.path.exists(vertex_config_path):
        with open(vertex_config_path, "r") as f:
            return json.load(f)
    else:
        return {
            "projectId": "",
            "modelInput": "gemini-1.0-pro-002",
            "region": "",
        }
    
def load_azure_config():
    if os.path.exists(azure_config_path):
        with open(azure_config_path, "r") as f:
            return json.load(f)
    else:
        return {
            "apikey": "",
            "modelInput": "gemini-1.0-pro-002",
            "version": "",
            "endpoint": ""
        }

def save_config(config):
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
def save_azure_config(config):
    with open(azure_config_path, "w") as f:
        json.dump(config, f, indent=4)
def save_vertex_config(config):
    with open(vertex_config_path, "w") as f:
        json.dump(config, f, indent=4)

# Database setup function
def setup_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        fullname TEXT NOT NULL           
    )
    ''')

    conn.commit()
    conn.close()

config = load_config()

def sanitize_email(email):
    # Replace invalid characters with underscores
    return re.sub(r'[^a-zA-Z0-9]', '_', email)

@app.websocket("/model_config")
async def websocket_model_config(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            print("Received model config:", data)
            is_vertex_model = "projectId" in data or "region" in data
            is_azure_model = "key" in data  or "version" in data or "endpoint" in data
            if is_vertex_model:
                vertex_config = {
                    "project_id" : data["projectId"],
                    "model" : data["modelInput"],
                    "region" : data["region"]
                }
                save_vertex_config(vertex_config)
            if is_azure_model:
                azure_config = {
                    "apikey" : data["key"],
                    "version" : data["version"],
                    "endpoint" : data["endpoint"],
                    "modelInput" : data["modelInput"]
                }
                save_azure_config(azure_config)
            else:

                model_config = load_config()
                temp = model_config["temperature"]
                model = model_config["model"]
                gpu = model_config["gpu"]
                
                if model != data["model"] or temp != data["temperature"]:
                    model_config["model"] = data["model"]
                    model_config["temperature"] = data["temperature"]

                    model_directory = "model"
                    for file in os.listdir(model_directory):
                        if file.endswith('.gguf') and config["model"].lower() in file:
                            config["model_path"] = os.path.join(model_directory, file)
                            break

                    save_config(config)

                model_kwargs = {"n_gpu_layers": -1 if gpu else 0}
                # llm = LlamaCPP(
                #     model_path=config["model_path"],
                #     temperature=config["temperature"],
                #     max_new_tokens=max_new_tokens,
                #     context_window=3900,
                #     model_kwargs=model_kwargs,
                #     verbose=False,
                # )
            await websocket.send_json({"status": "success", "message": "Model configuration updated."})

    except Exception as e:
        print(e)
    # finally:
    #     await websocket.close()


    
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            print("ws route")
            user_input = data["userInput"]
            print(user_input)
            if user_input.lower() == "exit":
                print("Exiting chat.")
                break

            prompt = prompt_template.format(prompt=user_input)
            model_kwargs = {"n_gpu_layers": -1 if config["gpu"] else 0}
            llm = LlamaCPP(
                model_path=config["model_path"],
                temperature=config["temperature"],
                max_new_tokens=max_new_tokens,
                context_window=3900,
                model_kwargs=model_kwargs,
                verbose=False,
            )
            response_iter = llm.stream_complete(prompt)

            for response in response_iter:
                await websocket.send_text(response.delta)
                await asyncio.sleep(0)
                if websocket.client_state.name != 'CONNECTED':
                    break

            await websocket.close()
            

    except Exception as e:
        print(e)
    # finally:
    #     await websocket.close()


@app.websocket("/available_agents")
async def agentinfo(websocket: WebSocket):
    await websocket.accept()
    agents = os.listdir('db')
    dict = {
        'agentinfo': agents
    }
    await websocket.send_json(dict)

@app.websocket("/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        config=load_config()
        model_kwargs = {"n_gpu_layers" : -1 if config["gpu"] else 0}
        llm = LlamaCPP(
            model_path=config["model_path"],
            temperature=config["temperature"],
            max_new_tokens=max_new_tokens,
            context_window=3900,
            model_kwargs=model_kwargs,
            verbose=False,
        )
        while True:
            data = await websocket.receive_json()
            print(data)
            print("agent route")
            user_input = data["userInput"]
            
            if user_input.lower() == "exit":
                print("Exiting chat.")
                break

            agent = data['agent']
            persist_directory = os.path.join('db', agent)
            embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
            db = Chroma(embedding_function=embeddings, persist_directory=persist_directory)

            docs = db.similarity_search(user_input, k=3)
            context = docs[0].page_content
            prompt_template = "You are a friendly assistant, who gives context aware responses on user query. Kindly analyse the provided context and give proper response\n   Context: {context}\n query:<s>[INST] {prompt} [/INST]"
            prompt = prompt_template.format(context=context, prompt=user_input)

            # model_kwargs = {"n_gpu_layers" : -1 if config["gpu"] else 0}
            # llm = LlamaCPP(
            #     model_path=config["model_path"],
            #     temperature=config["temperature"],
            #     max_new_tokens=max_new_tokens,
            #     context_window=3900,
            #     model_kwargs=model_kwargs,
            #     verbose=False,
            # )

            response_iter = llm.stream_complete(prompt)

            for response in response_iter:
                await websocket.send_text(response.delta)
                await asyncio.sleep(0)


                save_config(config)
            await websocket.close()

        
    except Exception as e:
        print(e)
    # finally:
    #     await websocket.close()

@app.websocket("/vertex")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        config=load_vertex_config()
        while True:
            data = await websocket.receive_json()
            print(data)
            print("vertex route")
            prompt = data["userInput"]
            
            if prompt.lower() == "exit":
                print("Exiting chat.")
                break

            agent = data['agent']
            projectid=config["project_id"]
            region=config["region"]
            model=config["model"]
            vertexai.init(project=projectid, location=region)
            multimodal_model = GenerativeModel(model_name=model)
            if agent == "None":
                response = multimodal_model.generate_content(prompt)
                await websocket.send_text(response.text)
                await websocket.close()
            else:

                persist_directory = os.path.join('db', agent)
                embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
                db = Chroma(embedding_function=embeddings, persist_directory=persist_directory)

                docs = db.similarity_search(prompt, k=3)
                context = docs[0].page_content
                prompt_template = "You are a friendly assistant, who gives context aware responses on user query. Kindly analyse the provided context and give proper response\n   Context: {context}\n query:<s>[INST] {prompt} [/INST]"
                prompt = prompt_template.format(context=context, prompt=prompt)
                response = multimodal_model.generate_content(prompt)
                await websocket.send_text(response.text)
                await websocket.close()
           

    except Exception as e:
        print(e)
    # finally:
    #     await websocket.close()

@app.websocket("/azure")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        config=load_azure_config()

        while True:
            data = await websocket.receive_json()
            print(data)
            print("azure route")
            prompt = data["userInput"]
            
            if prompt.lower() == "exit":
                print("Exiting chat.")
                break

            agent = data['agent']
            key=config['apikey']
            version=config['version']
            model=config['modelInput']
            endpoint=config['endpoint']


            client = AzureOpenAI(
                api_key = (key),
                api_version = version,
                azure_endpoint = (endpoint)
            )

            if agent == "None":
                response = client.chat.completions.create(
                    model=model, # model = "deployment_name".
                    messages=[
                        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                        {"role": "user", "content": prompt}
                        
                    ]
                )
                for choice in response.choices:
                    await websocket.send_text(choice.message.content)
                    await websocket.close()
            else:
                persist_directory = os.path.join('db', agent)
                if os.path.exists(persist_directory):
                    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
                    db = Chroma(embedding_function=embeddings, persist_directory=persist_directory)
                    docs = db.similarity_search(prompt, k=3)
                    context = docs[0].page_content
                    prompt_template = "You are a friendly assistant, who gives context aware responses on user query. Kindly analyse the provided context and give proper response\n   Context: {context}\n query:<s>[INST] {prompt} [/INST]"
                    prompt = prompt_template.format(context=context, prompt=prompt)
                    response = client.chat.completions.create(
                            model=model, # model = "deployment_name".
                            messages=[
                                {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                                {"role": "user", "content": prompt}
                                
                            ]
                        )
                    for choice in response.choices:
                        await websocket.send_text(choice.message.content)
                    await websocket.close()
                        


           

    except Exception as e:
        print(e)
    # finally:
    #     await websocket.close()


# class RequestData(BaseModel):
#     agent: str
#     file: UploadFile
@app.post("/create_agent")
async def upload_file(name: str = Form(...),file: UploadFile = File(...)):
        try:
            agentname = name
            uploaded_file = file
            # Process the uploaded file
            # Example: Save the file locally
            if not os.path.exists("uploads"):
                os.mkdir("uploads")
            file_path = f"uploads/{uploaded_file.filename}"
            with open(file_path, "wb") as file_object:
                file_object.write(await uploaded_file.read())
            persist_directory = 'db'
            doc_path = os.path.normpath(file_path)
            agent_directory = os.path.join(persist_directory, agentname)
            if not os.path.exists(agent_directory):
                os.makedirs(agent_directory)

            # Load the document
            if doc_path.endswith(".csv"):
                loader = CSVLoader(doc_path)
            elif doc_path.endswith(".pdf"):
                loader = PDFMinerLoader(doc_path)
            elif doc_path.endswith(".docx"):
                loader = TextLoader(doc_path)
            else:
                raise ValueError("Unsupported file format. Supported formats are CSV, PDF, and DOCX.")

            documents = loader.load()

            # Split the document into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=500)
            texts = text_splitter.split_documents(documents)

            # Create embeddings
            embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

            # Create ChromaDB and store document IDs
            db = Chroma.from_documents(texts, embeddings, persist_directory=agent_directory)
            db.persist()

            doc_ids_path = os.path.join(agent_directory, f"{agentname}_docids.txt")

            # Store document IDs in a file
            with open(doc_ids_path, "a") as f:
                for text_id, _ in enumerate(texts):
                    document_id = f"doc_{text_id}"
                    f.write(f"{document_id}\n")
            return JSONResponse(content={"agentname": name, "message": "agent created successfully"}) 
        



        except Exception as e:
            print(e)

@app.websocket("/configdata")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        data = await websocket.receive_json()
        print(data)
        if data == "Azure":
            azure_config=load_azure_config()
            await websocket.send_json(azure_config)
        elif data == "Vertex":
            vertex_config=load_vertex_config()
            await websocket.send_json(vertex_config)
        else:
            config=load_config()
            await websocket.send_json(config)

    except Exception as e:
        print(e)
    finally:
        await websocket.close()

@app.route('/signup', methods=['POST'])
async def signup(request: Request):
    data = await request.json()
    print(data)
    fullname = data.get('fullname')
    email = data['email']
    password = data.get('password')

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    if '@' in email:
        try:
            cursor.execute('''
            INSERT INTO users (email, password, fullname) VALUES (?, ?, ?)
            ''', (email, hashed_password, fullname))

            sanitized_table_name = sanitize_email(email)
            cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {sanitized_table_name} (
                chat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                messageheader TEXT,
                chats TEXT                   
            )
        ''')
            conn.commit()
            response = {'message': 'User signed up successfully!'}
        except sqlite3.IntegrityError:
            response = {'message': 'Username already exists!'}
    else:
        response = {'message': 'Invalid email format.'}
    
    

    conn.close()
    return JSONResponse(content=response)

# Route for user login
@app.route('/login', methods=['POST'])
async def login(request: Request):
    data = await request.json()
    email = data['email']
    password = data['password']

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id, fullname FROM users WHERE email = ? AND password = ?
    ''', (email, hashed_password))

    user = cursor.fetchone()

    if user:
        print(user)
        user_id = user[0]
        fullname = user[1]
        print(fullname, user_id)
        response = {'message': f"Welcome, {fullname}!","status": True, "user_id": user_id}
    else:
        response = {'message': 'Invalid username or password.'}

    conn.close()
    return JSONResponse(content=response)

@app.post('/newchat')
async def update_chat_history(request: Request):
    data = await request.json()
    print(data)
    user_email = data['userEmail']
    message_header = data['messageheader']
    chats = data['chats']
    
    # Convert the chats array to a JSON string
    chats_json = json.dumps(chats)

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        # Execute query to insert data into the specified user's table
        cursor.execute(f'''
            INSERT INTO {user_email} (messageheader, chats)
            VALUES (?, ?)
        ''', (message_header, chats_json))

        cursor.execute(f'''
            SELECT chat_id FROM {user_email}
            WHERE messageheader = ?
        ''', (message_header,))
        
        # Fetch the chat_id
        chat_id = cursor.fetchone()[0]

        # Commit the transaction
        conn.commit()

        # Close the database connection
        conn.close()

        return JSONResponse(content={'message': 'Chat history updated successfully.', 'chat_id': chat_id})
    except Exception as e:
        # Rollback changes if an error occurs
        conn.rollback()
        conn.close()
        raise HTTPException(status_code=500, detail=f'Error updating chat history: {str(e)}')
    

@app.post('/fetchchat')
async def fetch_chat_history(request: Request):
    data = await request.json()
    print(data)
    user_email = data['userEmail']
    chat_id = data['chat_id']

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        # Execute query to fetch chat history based on userEmail and chat_id
        cursor.execute(f'''
            SELECT chats FROM {user_email}
            WHERE chat_id = ?
        ''', (chat_id,))
        
        # Fetch the chat history
        chat_history = cursor.fetchone()

        if chat_history:
            # Parse the chat history from JSON
            chat_history_json = json.loads(chat_history[0])
            return JSONResponse(content={'chat': chat_history_json})
        else:
            raise HTTPException(status_code=404, detail='Chat history not found.')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error fetching chat history: {str(e)}')
    finally:
        # Close the database connection
        conn.close()

@app.post('/updatechat')
async def update_chat_history(request: Request):
    data = await request.json()
    user_email = data['userEmail']
    chat_id = data['chat_id']
    updated_chats = data['chats']
    
    # Convert the updated chats array to a JSON string
    updated_chats_json = json.dumps(updated_chats)

    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        # Execute query to update the chat data for the specified chat_id
        cursor.execute(f'''
            UPDATE {user_email}
            SET chats = ?
            WHERE chat_id = ?
        ''', (updated_chats_json, chat_id))

        # Check if any rows were affected
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Chat not found.")
        
        # Commit the transaction
        conn.commit()

        return JSONResponse(content={'message': 'Chat history updated successfully.'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating chat history: {str(e)}')
    finally:
        # Close the database connection
        conn.close()

def get_start_of_day(date):
    return date.replace(hour=0, minute=0, second=0, microsecond=0)

def get_date_x_days_ago(days):
    return get_start_of_day(datetime.now() - timedelta(days=days))

@app.post('/fetchchatsidebar')
async def fetch_chat_sidebar(request: Request):
    data = await request.json()
    print(data)
    user_email = data.get('userEmail')

    if not user_email:
        raise HTTPException(status_code=400, detail='userEmail is required')

    email_safe = user_email.replace('.', '_').replace('@', '_')
    today_start = get_start_of_day(datetime.now())
    seven_days_ago = get_date_x_days_ago(7)

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f'''
            SELECT chat_id, messageheader, timestamp
            FROM {email_safe}
        ''')

        chats = cursor.fetchall()

        today_chats = []
        past_seven_days_chats = []

        for chat in chats:
            chat_id, message_header, timestamp = chat
            chat_date = datetime.fromisoformat(timestamp)

            if chat_date >= today_start:
                today_chats.append({
                    'chat_id': chat_id,
                    'message_header': message_header,
                    'timestamp': timestamp
                })
            elif chat_date >= seven_days_ago:
                past_seven_days_chats.append({
                    'chat_id': chat_id,
                    'message_header': message_header,
                    'timestamp': timestamp
                })

        print(today_chats, past_seven_days_chats)
        return JSONResponse(content={
            'today': today_chats,
            'past_seven': past_seven_days_chats
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error fetching chat sidebar: {str(e)}')
    finally:
        conn.close()

def main():
    import uvicorn
    setup_database()
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()