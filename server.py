# The Main Method to serve the pages

import os
from fastapi import FastAPI
from datetime import datetime
import pandas


app = FastAPI()

@app.get('/')
def getPage():
    return {'message': 'Welcome To Server'}


@app.get('/about')
def getAbout():
    return {'message': 'This is the About Page'}