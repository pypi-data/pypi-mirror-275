from quiz_app.quiz import Quiz
import os

def main():
    questions_file = os.path.join(os.path.dirname(__file__), 'questions.json')
    quiz = Quiz(questions_file)
    quiz.start()

if __name__ == "__main__":
    main()
