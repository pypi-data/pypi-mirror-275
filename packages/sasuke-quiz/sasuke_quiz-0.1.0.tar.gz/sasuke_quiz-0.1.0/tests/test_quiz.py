import unittest
from quiz_app.quiz import Quiz
import os

class TestQuiz(unittest.TestCase):
    def setUp(self):
        questions_file = os.path.join(os.path.dirname(__file__), '../quiz_app/questions.json')
        self.quiz = Quiz(questions_file)

    def test_quiz_initialization(self):
        self.assertEqual(len(self.quiz.questions), 2)

    def test_quiz_scoring(self):
        self.quiz.score = 1
        self.assertEqual(self.quiz.score, 1)

if __name__ == '__main__':
    unittest.main()
