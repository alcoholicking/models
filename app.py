from fastapi import FastAPI
from model import llm_chain

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.get("/prompts/{prompt}")
def give_prompt(prompt: str):
    return llm_chain(prompt)
