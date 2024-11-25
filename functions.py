import os
import random
from pydantic import BaseModel

class LoginPage(BaseModel):
    username: str = ''

class Question(BaseModel):
    easy_question : str = ''
    med_question : str = ''
    hard_question : str = ''

def readFiles(path: str =''):
    if os.path.exists(path):
        return (path, list(os.listdir(path)))
    else:
        return (path, [])

def readFile(path: str = ''):
    if os.path.exists:
        with open(path, 'r') as file:
            return file.read()
    return ''

def obtainQuestion():
    low, med, high = readFiles('questions/high'), readFiles('questions/medium'), readFiles('questions/low')
    question = Question
    question.easy_question, question.med_question, question.hard_question = random.choice(low), random.choice(med), random.choice(high)
    return question
        
path = "src/html"
res = readFiles(path)
print(res)