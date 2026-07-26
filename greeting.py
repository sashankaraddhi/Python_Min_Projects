
import random as rd 

greetings = [
    "Hello, {}! Welcome!",
    "Hi there, {}! It's great to see you!",
    "Greetings, {}! How are you doing today?"
]
dicts = range(1, len(greetings) + 1)

greetings_dict = dict(zip(dicts, greetings))

def choose_random_greeting_template() -> str:
    random_key = rd.choice(dicts)
    return greetings_dict[random_key]

def choose_greeting_template() -> str:
    try:
        choice = int(input(f"choose an integer between 1 & {max(dicts)}: "))
        greetingss = greetings_dict[choice]
    except ValueError:
        print("Invalid input, returning a random greeting.")
        return choose_random_greeting_template()        
    except KeyError:
        print("The value you entered is not in the dictionary, returning a random greeting.")
        return choose_random_greeting_template()
    return greetingss

def run_all() -> None:
    name = input("Please enter your name: ")
    if not name:
        print("Name must contain at least one character")
        return
    greeting_style = input("Enter 1 for a random greeting, or enter 2 to choose from a list: ")
    if greeting_style == "1":
        random_greeting = choose_random_greeting_template()
        print(random_greeting.format(name.title()))
    elif greeting_style == "2":
        selective_greeting = choose_greeting_template()
        print(selective_greeting.format(name.title()))
    else:
        print(f"{name.title()}, You entered an invalid choice")

run_all()