import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'admin', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        response = self.client().get('/categories')
        data = json.loads(response.data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['categories']))


    def test_get_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['categories']))
        self.assertEqual(data['current_category'],None)

    def test_404_sent_requesting_beyond_valid_pages(self):
        response = self.client().get('/questions?page=500')
        data = json.loads(response.data)

        self.assertEqual(response.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertTrue(data['message'],"Not Found")

    def test_delete_question(self):
        response = self.client().delete('/questions/2')
        data = json.loads(response.data)

        question = Question.query.get(2)

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],2)
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

    def test_404_if_question_does_not_exist(self):
        response = self.client().get('/questions/1000')
        data = json.loads(response.data)

        self.assertEqual(response.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertTrue(data['message'],"Not Found")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()