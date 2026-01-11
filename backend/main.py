from fastapi import FastAPI
from scraper import scrape_wikipedia
from llm import generate_quiz
from database import SessionLocal, Quiz
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/generate")
def generate(url: str):
    title, text = scrape_wikipedia(url)
    quiz = generate_quiz(text)

    db = SessionLocal()
    new_quiz = Quiz(url=url, title=title, quiz=quiz)
    db.add(new_quiz)
    db.commit()
    db.close()

    return {
        "title": title,
        "quiz": quiz
    }

@app.get("/history")
def history():
    db = SessionLocal()
    quizzes = db.query(Quiz).order_by(Quiz.id.desc()).all()
    db.close()

    return quizzes
