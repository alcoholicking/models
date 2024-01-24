from fastapi import FastAPI
from model import llm_chain

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/prompts/{prompt}")
def give_prompt(prompt: str):

    # get LLM returned grapes
    return llm_chain(prompt)["text"]
    # 

    # return 
