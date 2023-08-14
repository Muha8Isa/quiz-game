class Quiz:

    def __init__(self, list):
        self.number = 0
        self.list = list
        self.score = 0

    def still(self):
        return self.number < len(self.list)

    def question(self):
        current_question = self.list[self.number]
        self.number += 1

        while True:
            answer = input(f"Q.{self.number}: {current_question.text} (True/False): ").lower()

            if answer == "true" or answer == "false":
                if answer == current_question.answer:
                    self.score += 1
                    print(f"Right answer, your score is: {self.score}")
                    break
                else:
                    print(f"Wrong answer, your score is: {self.score}")
                    break
            else:
                print("Invalid input. Please enter 'True' or 'False'.")
