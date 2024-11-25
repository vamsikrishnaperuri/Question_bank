# The Main Method to serve the pages

try:
    import os
    from typing import List
    import sys
    import functions as func
    import uvicorn
    from fastapi.staticfiles import StaticFiles
    from fastapi import FastAPI, Response, Form, Cookie, Request
    from fastapi.templating import Jinja2Templates
    from fastapi.responses import HTMLResponse
    from random import random
except Exception as e:
    exit()

app = FastAPI()
templates = Jinja2Templates(directory="src/html")
app.mount("/img", StaticFiles(directory="src/img"), name="img")
app.mount('/css', StaticFiles(directory="src/css"), name="css")
app.mount('/questions', StaticFiles(directory="questions"), name='questions')

@app.get('/')
def loginPage():
    content = func.readFile("src/html/loginPage.html")
    content = f'{content}'
    resp = Response(content,  media_type="text/html", status_code=200)
    # print(resp, dir(resp))
    return resp

@app.post('/login')
def loginUser(username: str = Form(...), request: Request = None, response: Response = None):
    # Obtain the question (assumed to be defined elsewhere)
    question = func.obtainQuestion()
    # print(question, question.easy_question, question.med_question, question.hard_question)
    return templates.TemplateResponse("questions.html", {
        "request": request,
        'question_hard': '/questions/'+question.hard_question,
        'question_med': '/questions/'+question.med_question,
        'question_easy': '/questions/'+question.easy_question
    }, cookies={'username': username})

@app.post("/register-question")
def register_question(request: Request, question: list[str] = Form(...), username: str = Form(None)):
    # Print the received data to the console
    print("Received questions:", question)
    print("Username:", username)

    # Return the success HTML page
    return HTMLResponse(content=func.readFile("src/html/questions.html"))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        registered_students = []
        excel_data = {'Roll Number': [], 'Level': []}
        subject_name = sys.argv[1]
    else:
        print("No Subject Given")
        exit()
    uvicorn.run("server:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
