# The Main Method to serve the pages

try:
    import os
    import sys
    import functions as func
    import uvicorn
    from fastapi.staticfiles import StaticFiles
    from fastapi import FastAPI, Response
    from random import random
except Exception as e:
    exit()

app = FastAPI()
app.mount("/img", StaticFiles(directory="src/img"), name="img")
app.mount('/css', StaticFiles(directory="src/css"), name="css")

@app.get('/')
def loginPage():
    content = func.readFile("src/html/loginPage.html")
    content = f'{content}'
    resp = Response(content,  media_type="text/html", status_code=200)
    # print(resp, dir(resp))
    return resp

@app.post('/')
def loginUser(data: func.LoginPage):
    print(data)
    # Take one question each from the high/medium/low
    question = func.obtainQuestion()
    # Here we have obtained the questions that the user needs to send
    # Now we add checkboxes to make indicate the choices of the user
    # And submit the data
    return 'Recieved the Question'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        global subject_name
        subject_name = sys.argv[1]
    else:
        print("No Subject Given")
        exit()
    uvicorn.run("server:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
