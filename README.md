# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## API Documention

### Introduction

This API serve trivia react app which allow the user to browse through avaliable questions, search for question, filter questions by category, post new question, and play quiz for specific category.

### Getting started

This API is hosted in localhost http://127.0.0.1:5000/ .

### Error

1. Code: 422, Message: Unprocessable Entity,
Response: {
      "success" : False,
      "status_code" : 422,
      "message" : "Unprocessable Entity"
    }
2. Code: 404, Message: Not Found,
Response: {
      "success" : False,
      "status_code" : 404,
      "message" : "Not Found"
    }
3. Code: 400, Message: Bad Request,
Response: {
      "success" : False,
      "status_code" : 400,
      "message" : "Bad Request"
    }  
    
### Resourse endpoints    

1. Method: GET, URI: '/categories'  
Description: This endpoint to handle GET requests for all available categories.
Parameters: None
Request: ```curl -X GET http://127.0.0.1:5000/categories```
Response: ```{
  "categories": [
    "Science",
    "Art",
    "Geography",
    "History",
    "Entertainment",
    "Sports"
  ],
  "success": true
}```

2. Method: GET, URI: '/questions' 
Description: This endpoint to handle GET requests for questions, including pagination (every 10 questions). 
Parameters: None
Request: ```curl -X GET http://127.0.0.1:5000/questions```
Response: ```{
  "categories": [
    "Science",
    "Art",
    "Geography",
    "History",
    "Entertainment",
    "Sports"
  ],
  "current_category": null,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist???initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Gary Lineker",
      "category": 1,
      "difficulty": 3,
      "id": 24,
      "question": " Which England footballer was famously never given a yellow card?"
    },
    {
      "answer": "Gary Lineker",
      "category": 1,
      "difficulty": 3,
      "id": 25,
      "question": " Which England footballer was famously never given a yellow card?"
    }
  ],
  "success": true,
  "total_questions": 18
}```

3. Method: DELETE, URI: '/questions/<int:question_id>'  
Description: This endpoint to DELETE question using a question ID. 
Parameters: question_id
Request: ```curl -X DELETE http://127.0.0.1:5000/questions/16```
Response: ```{
  "deleted": 16,
  "success": true,
  "total_questions": 17
}```

4. Method: POST, URI: '/questions'  
Description: This endpoint to POST a new question.
Parameters: question, answer, difficulty, category
Request: ```curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"what"}'```
Response: ```{
    "current_category": null,
    "questions": [
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 3
}```

5. Method: POST, URI: '/questions/search'  
Description: This endpoint to get questions based on a search term.
Parameters: searchTerm
Request: ```curl -X POST http://127.0.0.1:5000/questions/search -d '{"searchTerm":"what"}'```
Response: ```{
    "current_category": null,
    "questions": [
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 3
}``` 

6. Method: GET, URI: '/categories/<int:category_id>/questions'  
Description: This endpoint to get questions based on category.
Parameters: category_id
Request: ```curl -X GET http://127.0.0.1:5000/categories/4/questions```
Response: ```{
  "current_category": "History",
  "questions": [
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 1
}

C:\Users\6700>curl -X GET http://127.0.0.1:5000/categories/3/questions
{
  "current_category": "Geography",
  "questions": [],
  "success": true,
  "total_questions": 0
}

C:\Users\6700>curl -X GET http://127.0.0.1:5000/categories/2/questions
{
  "current_category": "Art",
  "questions": [
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 3
}```

7. Method: POST, URI: '/quizzes'  
Description: This endpoint to get questions to play the quiz.
Parameters: previous_questions, quiz_category
Request: ```curl -X POST http://127.0.0.1:5000/quizzes -d '{"previous_questions":"[]", "quiz_category" : "{id: 1}" }'```
Response: ```{
          "success" : True,
          "question": question
        }```

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)
