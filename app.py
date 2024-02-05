from fastapi import FastAPI, Request
from model import llm_chain
from PerfectLlama import PerfectLlama
import asyncio


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "world"}


@app.post("/chat")
def get_body(request: Request):
    chain = PerfectLlama("llama2/llama-2-7b-chat-quantized/ggml-model-f16.gguf")
    request = request.json()
    message = chain.give_prompt(request)

    return message 

# @app.post("/chat")
# async def chat(query: Query, response: StreamingResponse):
#   pass

# async def stream():
#  async for token in callback_handler:
#  yield token
# streaming_iterator = stream()
# task = asyncio.create_task(agent(query, streaming_iterator))
# return StreamingResponse(streaming_iterator)

