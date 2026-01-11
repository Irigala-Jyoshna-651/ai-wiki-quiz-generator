# AI Wiki Quiz Generator

## Objective
Build a web application that takes a Wikipedia article URL and automatically generates a quiz using AI.  
The system scrapes article content, sends it to a Large Language Model (Gemini API), generates quiz questions, and stores them in a PostgreSQL database.

---

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** PostgreSQL  
- **LLM:** Gemini API  
- **Scraping:** BeautifulSoup  

---

## Features
- Generate quiz from Wikipedia URL  
- AI-based multiple-choice questions  
- Difficulty levels (easy, medium, hard)  
- Explanations for each answer  
- History of past quizzes  
- Modal popup to view quiz details  
- Responsive UI  

---

## How to Run the Project

### Backend
```bash
cd backend
python -m uvicorn main:app --reload

Server runs at: http://127.0.0.1:8000

## Frontend
Open index.html
using Live Server or directly in the browser.
API Endpoints
Generate Quiz
GET /generate?url=<wikipedia_url>


Example:

http://127.0.0.1:8000/generate?url=https://en.wikipedia.org/wiki/Alan_Turing

Quiz History
GET /history

Prompt Used for AI

"Create multiple choice questions from the given text.
Each question must include:

Question
4 options
Correct answer
Difficulty level
Short explanation
Related topics
Return the output in JSON format only."

Database Structure

Table: quizzes

Column	Type
id	SERIAL
url	TEXT
title	TEXT
quiz	JSONB
created_at	TIMESTAMP
Screenshots

Generate Quiz Page

Past Quizzes Page

Quiz Details Modal

Screenshots are available in the /screenshots folder.

Sample Data

Folder: sample_data/

urls.txt – Example Wikipedia URLs

alan_turing.json – Sample API response

Notes

Backend is implemented strictly in Python using FastAPI

No Node.js used

Wikipedia content is scraped using HTML parsing (no API)

Data is stored and retrieved from PostgreSQL

Frontend is kept clean and minimal

Author
Developed by: Jyoshna