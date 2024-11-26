# The Backend Server Logic

import pandas as pd
import sys
import functions as func
from variables import generatedQuestions, QuestionSelection, registeredQuestions
from fastapi import FastAPI, Response, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Mount directories for static files
app.mount("/img", StaticFiles(directory="src/img"), name="img")
app.mount('/css', StaticFiles(directory="src/css"), name="css")
app.mount('/questions', StaticFiles(directory="questions"), name='questions')

origins = [
    "http://localhost",  # Local frontend application
    "http://localhost:8000",  # If your frontend is running on port 3000
    "*",  # Allow all origins (not recommended for production)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def loginPage():
    return Response(content=func.renderFile("src/html/index.html", {'subject_name': "AITT"}), media_type="text/html")

@app.get("/generate-question")
def generateQuestion(rollNumber: str):
    if rollNumber not in generatedQuestions:
        generatedQuestions[rollNumber] = func.generateQuestions()
    content = func.renderFile("src/html/generate-question.html", {"easy_question": generatedQuestions[rollNumber][0], "medium_question": generatedQuestions[rollNumber][1], "hard_question": generatedQuestions[rollNumber][2]})
    resp =  Response(content=content, media_type="text/html")
    resp.set_cookie(key="rollNumber", value=rollNumber)
    return resp


@app.post("/register-questions")
def registerQuestions(question: QuestionSelection, request: Request):
    rollNumber = request.cookies.get('rollNumber')
    if question.easy and question.medium:
        level = 3
    elif question.easy and question.hard:
        level = 2
    elif question.medium and question.hard:
        level = 1
    print(rollNumber, level)

    registeredQuestions[rollNumber] = level
    return JSONResponse(content={"message": "Selection submitted successfully!"}, status_code=200)
    
@app.get('/get-Data')
def getExcelSheet():
    data = dict()
    data["Registered Numbers"] = registeredQuestions.keys()
    data["Level"] = []
    for roll in data["Registered Numbers"]:
        data["Level"].append(registeredQuestions[roll])
    df = pd.DataFrame(data)
    file_path = 'students.xlsx'
    df.to_excel("sheet.xlsx", index=False, engine='openpyxl')
    return FileResponse("sheet.xlsx", media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename="students.xlsx")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)