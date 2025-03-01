import random
# change python3 to python if use windows in eval.sh of line 15 
# =========================
# Part 1: Quiz and Question Classes
# =========================

class Question:
    # Todo
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def get_question_text(self):
        return self.question_text
    
    def get_options(self):
        if type(self.options) == list:
            l = []
            for i in self.options:
                l.append(i)
            return l
        else:
            return self.options
        

    def get_correct_answer(self):
        return self.correct_answer
    
    def set_question_text(self, question_text):
        self.question_text =question_text
    
    def set_options(self, options):
        self.options = options
    
    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer
    
    def validate_answer(self, answer):
        if self.correct_answer == answer:
            return True
        return False


class MultipleChoiceQuestion(Question):
    # Todo
    def __init__(self, question_text, options, correct_answer):
        super().__init__(question_text, options, correct_answer)

    def validate_answer(self, answer):
        # print(self.correct_answer)
        # print(answer)
        return self.correct_answer.lower() == answer.lower()


class TrueFalseQuestion(Question):
    # Todo
    def __init__(self, question_text, correct_answer, options = ["True", "False"]):
        super().__init__(question_text, options, correct_answer)
    
    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class FillInTheBlankQuestion(Question):
    # Todo
    def __init__(self, question_text, correct_answer, options = None):
        super().__init__(question_text, options, correct_answer)
    
    def validate_answer(self, answer):
        return self.correct_answer.lower() == answer.lower()


class Quiz:
    # Todo write the remaining methods
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        l = []
        for i in self.questions:
            # print(i.get_question_text(), "aaaaaaaaaaaaaaaa")
            if i.get_question_text() == question.get_question_text():
                continue
            else:
                l.append(i)
        self.questions = l
                
        
    
    def get_questions(self):
        return self.questions

    def shuffle_questions(self) -> None:
        random.shuffle(self._questions)

    def get_total_questions(self):
        return len(self.questions)


# =========================
# Part 2: Person, Student, and Leaderboard Classes
# =========================

class Person:
    # Todo
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

class Student(Person):
    # Todo
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.score = 0

    def simulate_quiz(self, quiz, simulated_answers):
        print()
        print(f"--- {self.name} is taking the quiz ---")
        valid = quiz.get_questions()
        # l = []
        j = 0
        for i in (valid):
            # for j in simulated_answers:
            
            if i.validate_answer(simulated_answers[j]):
                # print(i, simulated_answers[j])
                print("Correct!")
                self.score += 1
                # j += 1    
            else:
                print(f"Incorrect! Correct answer: {i.get_correct_answer()}")
            
            j += 1
                
                    

        print()
        print(f"{self.name} scored {self.score} out of {len(valid)}.")
    
            


    def get_score(self):
        return self.score

class Leaderboard:
    # Todo
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_leaderboard(self):
        # Student: Alice | Score: 2
        print()
        print("=== Leaderboard ===")
        for i in self.students:
            print(f"Student: {i.get_name()} | Score: {i.get_score()}")
