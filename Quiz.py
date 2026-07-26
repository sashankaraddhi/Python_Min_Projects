import random as rd

def choose_Question() -> str:
    question_type = ["Addition","Subtraction","Multiplication","Mix"]
    print(f"Choose a question type {' , '.join(question_type)}\n")
    choice = input("enter choice :").title()

    while choice not in question_type:
        choice = input("try again :").title()
    else :
        return choice


def choose_difficulty_level () -> int :
    while True:
        try :
            difficulty_level = int(input("choose a level from 1 - 5 :"))
        except ValueError:
            print("Invaild format,Try Again ")
            continue
        else:
            if difficulty_level in range(1,6):
                return difficulty_level
            print("Number  ust be in 1-5")
            continue


def choose_question() -> int :
    try :
        number_of_Question = int(input("How many Question ?"))
    except ValueError:
        print("Incorrect,default to 10")
        return 10
    else :
        if number_of_Question <= 0:
            print("Incoorect,default to 10")
            return 10 
        
        return number_of_Question

def generate_number_for_question(difficulty_level : int) -> tuple:
    operand_a = rd.randint(difficulty_level * 2 ,difficulty_level * 20)
    operand_b = rd.randint(difficulty_level * 2 ,difficulty_level * 20)
    return operand_a,operand_b


def Addition_question ( operand_a : int, operand_b : int) -> int :
    try :
        question = int(input(f"what is {operand_a} plus {operand_b} : "))
    except ValueError:
        print("Invalid format, moving to next question ")
        return False
    else :
        return True if (question == operand_a + operand_b) else False

def Subtraction_question ( operand_a : int, operand_b : int) -> int :
    try :
        question = int(input(f"what is {operand_a} minus {operand_b} : "))
    except ValueError:
        print("Invalid format, moving to next question ")
        return False
    else :
        return True if (question == operand_a - operand_b) else False

def Multiplication_question ( operand_a : int, operand_b : int) -> int :
    try :
        question = int(input(f"what is {operand_a} Multipication {operand_b} : "))
    except ValueError:
        print("Invalid format, moving to next question ")
        return False
    else :
        return True if (question == operand_a * operand_b) else False


def main_game_loop (question_type : str,num_question : int ,difficulty_level : int) -> int:
    no_of_correct_answer = 0
    for i in range (1,num_question+1):
        operand_a, operand_b = generate_number_for_question(difficulty_level)
        print(operand_a, operand_b)
        print(f"Question : {i}")
        if question_type == "Addition":
            response = Addition_question(operand_a,operand_b)
        elif question_type == "Subtration":
            response = Subtraction_question(operand_a,operand_b)

        elif question_type == "Multiplication":
            response = Multiplication_question(operand_a,operand_b)

        elif question_type == "Mix":
            q_type = [Addition_question, Subtraction_question, Multiplication_question]
            response = rd.choice(q_type)(operand_a,operand_b)

        if response:
            print("correct")
            no_of_correct_answer += 1
        else :
            print("Sorry,Incorrect")


def main() -> None :
    question_type = choose_Question()
    if question_type == "Mix" :
        print("You will recieve variable question ")
    else :
        print(f"You chose {question_type} question. ")
    num_question =choose_question()
    print(f"you will be answering {num_question} question.\n")

    difficulty_level = choose_difficulty_level()
    print(f"You chose for : {difficulty_level}")

    correct_answer = main_game_loop(question_type,num_question,difficulty_level)
    print(f"Quiz finished, with {correct_answer} correct answer out of {num_question} question.")

if __name__ == "__main__":
    main()