def generate_quiz(text):
    return {
        "quiz": [
            {
                "question": "Who was Alan Turing?",
                "options": ["Mathematician", "Doctor", "Artist", "Writer"],
                "answer": "Mathematician",
                "difficulty": "easy",
                "explanation": "Alan Turing was a famous mathematician."
            },
            {
                "question": "Where did Turing work during WWII?",
                "options": ["NASA", "Bletchley Park", "Google", "Oxford"],
                "answer": "Bletchley Park",
                "difficulty": "medium",
                "explanation": "He worked at Bletchley Park cracking Enigma codes."
            }
        ],
        "related_topics": ["Cryptography", "Computer Science"]
    }
