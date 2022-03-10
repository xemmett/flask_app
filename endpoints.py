# endpoints.py
# contains functions API performs.
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from json import loads

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["post" ,'get'],
    allow_credentials=True,
    allow_headers=["*"],
)

@app.get("/") # add url path
async def hello():
    return {"msg": "Hello World!"}

@app.post("/course-submit") # add url path
async def course_submit(incoming_request: Request):
    body_binary_string = await incoming_request.body()
    print(body_binary_string)
    body_dict = loads(body_binary_string.decode())  
    course_code = body_dict['course_code']
    msg = "You take: " + course_code
    return {"msg": msg}