import os
import dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# nos permite cargar las variables desde .env "variables": Unknown word.
dotenv.load_dotenv()

# instciantiate the FastApiclass "instciantiate": unknown word.
app = FastAPI(

    title ="Mi primer BOT",
    description=""""
            mi primer bot basico

            1,- consultas a un modelo cohere
    """,
    version="0.1.0"
    
)


# modelo schema
class Agente(BaseModel):
    prompt: str 
    


@app.get("/") 
async def hola_mundo():
    return {"message": f"Hola Mundo"}

@app.post("/agente")
async def agente( request: Agente):


    COHERE_API_KEY = os.getenv("COHERE_API_KEY")
    prompt = request.prompt

    # 1- instaciate the ChatCohere class (API_KEY)
    chat = ChatCohere(
        api_key=COHERE_API_KEY
        
    )
    # 2- create a list of messages in the conversasion.
    list_messages = [
        SystemMessage(content="Eres experto en IA, te llamaras Pepito."),
        HumanMessage(content=prompt)
    ]
        
    # 3- invoke the model
    response = chat.invoke(list_messages)

    list_messages.append(response)

    return {
        "agente": list_messages[-1].content, 
        }