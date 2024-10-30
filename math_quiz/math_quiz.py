import random

def create_random_integer(min_val, max_val):
    """
    Create a random integer between a min_val and max_val.
    
    Args:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.
    
    Returns:
        int: A random integer between min_val and max_val.

    """
    return random.randint(min_val, max_val)


def select_random_mathoperator():
    """
    Select a random mathematical operator.
    
    Returns:
        str: A string representing a mathematical operator ('+','-','*')

    """
    return random.choice(['+', '-', '*'])


def create_problem_and_answer(number_1, number_2, math_operator):
    """
     Create a math problem based on two numbers and an operator and compute the answer.
    
    Args:
        number_1 (int): The first number in the problem.
        number_2 (int): The second number in the problem.
        math_operator (str): The operator to use in the problem ('+', '-', '*').
        
    Returns:
        tuple: A tuple containing the problem as a string and the correct answer as an integer.
    """
    
    problem = f"{number_1} {math_operator} {number_2}"
    if math_operator == '+':
        answer = number_1 + number_2
    elif math_operator == '-':
        answer = number_1 - number_2
    elif math_operator == '*':
        answer = number_1 * number_2
    else:
        raise ValueError ("Invalid math operator")
    return problem, answer

def math_quiz():
    """
    Main function. Ask user to solve math problems and returns score out of total_questions.

    """
    score = 0
    total_questions = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number_1 = create_random_integer(1, 10)
        number_2 = create_random_integer(1, 10)
        math_operator = select_random_mathoperator()

        problem, answer = create_problem_and_answer(number_1, number_2, math_operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except:
            print("Invalid input. Enter a number")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
