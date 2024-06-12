class PyQuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "Which is the smallest planet in our solar system?",
                "options": ["A. Mars", "B. Mercury", "C. Venus", "D. Earth"],
                "answer": "B"
            },
            {
                "question": "Who wrote the play 'Romeo and Juliet'?",
                "options": ["A. William Shakespeare", "B. Mark Twain", "C. Charles Dickens", "D. J.K. Rowling"],
                "answer": "A"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": ["A. O2", "B. CO2", "C. H2O", "D. NaCl"],
                "answer": "C"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["A. 1912", "B. 1916", "C. 1905", "D. 1920"],
                "answer": "A"
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
                "answer": "C"
            },
            {
                "question": "Which organ in the human body is primarily responsible for pumping blood?",
                "options": ["A. Brain", "B. Liver", "C. Lungs", "D. Heart"],
                "answer": "D"
            },
            {
                "question": "Which programming language is known as the language of the web?",
                "options": ["A. Python", "B. Java", "C. C++", "D. JavaScript"],
                "answer": "D"
            },
            {
                "question": "Which language is primarily used for Android app development?",
                "options": ["A. Swift", "B. Kotlin", "C. Ruby", "D. JavaScript"],
                "answer": "B"
            },
            {
                "question": "Who is known as the father of the Python programming language?",
                "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
                "answer": "C"
            },
            {
                "question": "Which programming language is used for statistical computing and graphics?",
                "options": ["A. R", "B. MATLAB", "C. Java", "D. PHP"],
                "answer": "A"
            },
            {
                "question": "Which language is used for developing iOS applications?",
                "options": ["A. Kotlin", "B. Swift", "C. C#", "D. Java"],
                "answer": "B"
            }
        ]
        self.score = 0

    def display_questions(self, question_data):
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)

    def get_user_answer(self):
        while True:
            answer = input("Enter your answer (A, B, C, or D): ").upper()
            if answer in ["A", "B", "C", "D"]:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")

    def give_feedback(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")

    def display_final_score(self):
        print(f"Your final score is {self.score}/{len(self.questions)}")

    def start(self):
        for question_data in self.questions:
            self.display_questions(question_data)
            user_answer = self.get_user_answer()
            self.give_feedback(user_answer, question_data["answer"])
        self.display_final_score()

if __name__ == "__main__":
    quiz_game = PyQuizGame()
    quiz_game.start()
