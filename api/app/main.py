### Code adapted from https://github.com/AssemblyAI-Examples/ml-fastapi-docker-heroku
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import recommender_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class StudentData(BaseModel):
    student_guid: str
    name: str
    research_interests: str
    university_field: str

class StudentDataWithSimilarity(BaseModel):
    student_guid: str
    name: str
    research_interests: str
    university_field: str
    similarity_score: float


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=StudentDataWithSimilarity)
def predict(payload: StudentData):
    best_match = recommender_pipeline(payload)
    
    student_guid = best_match["Student GUID"]
    name = best_match["Name"]
    research_interests = best_match["Research Interests"]
    university_field = best_match["University Field"]
    similarity_score = best_match["Similarity Score"]

    return StudentDataWithSimilarity(
        student_guid=student_guid,
        name=name,
        research_interests=research_interests,
        university_field=university_field,
        similarity_score=similarity_score
    )