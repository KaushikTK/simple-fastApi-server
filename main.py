from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from starlette.requests import Request


app = FastAPI()

# this is for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET REQUESTS
# default route
@app.get('/')
def root():
    return 'server is running'

# returns a list
@app.get('/list')
async def root():
    return [1,2,3,4,5]

# returns a dictionary/object
@app.get('/dict')
async def root():
    DICTIONARY = {
        1: 'A',
        2: 'B',
        3: 'C'
    }
    return DICTIONARY

# returns an object
@app.get('/json')
async def root():
    return {
        'status':'success',
        'hello':'world'
    }

# sum of 2 integers present in the request url
@app.get('/sum/{a}/{b}')
async def root(a:int, b:int):
    return a+b
    #return int(a)+int(b) # if u do not specify the data type as int

# product of numbers sent as params in the request where c is optional and should be of type int
@app.get('/product')
async def root(a:int, b:int, c:Optional[int] = None):
    if c: return a*b*c
    return a*b

# POST REQUESTS
@app.post('/login')
async def loginFunction(request:Request):
    formdata = await request.json()
    fakeUsername = 'kaushik'
    fakePassword = 'python'
    if formdata['username'] == fakeUsername and formdata['password'] == fakePassword: return 'valid'
    return 'invalid'