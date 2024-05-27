import json

class Quiz:
    def __init__(self, questions_file):
        with open(questions_file, 'r') as file:
            self.questions = json.load(file)
        self.score = 0

    def start(self):
        for question in self.questions:
            self.ask_question(question)
        print(f"Your final score is {self.score}/{len(self.questions)}")

    def ask_question(self, question):
        print(question["question"])
        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")
        answer = input("Enter the number of your answer: ")
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print()
