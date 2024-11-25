# The variables required for the program

from pydantic import BaseModel
generatedQuestions = dict()
registeredQuestions = dict()

class QuestionSelection(BaseModel):
  easy: bool
  medium: bool
  hard: bool

