# The functions to support the Server

import random
import os

def readFile(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            return file.read()
    return ""

def readDirectory(directory_path):
    if os.path.exists(directory_path):
        return os.listdir(directory_path)
    else:
        return []

def renderFile(path: str = '', params: dict = dict()):
    content = readFile(path)
    #print(params)
    for param in params:
        replace_string = params[param]
        query_string = '{' + param + '}'
        #print(query_string, replace_string)
        content = content.replace(query_string, replace_string)
    return content

def generateQuestions():
    easy, medium, hard = readDirectory('questions/easy'), readDirectory('questions/medium'), readDirectory('questions/hard')
    return ['/questions/easy/' + random.choice(easy), '/questions/medium/' + random.choice(medium), '/questions/hard/' + random.choice(hard)]
