#creating a madlib game
import random
# def madlib():
#     print("Welcome to the Madlib game!")
#     name = input("Enter a name: ")
#     adjective = input("Enter an adjective: ")
#     verb = input("Enter a verb: ")
#     noun = input("Enter a noun: ")

#     story = f"Once upon a time, {name} was very {adjective}. They decided to {verb} a {noun}."
#     print(story)
# madlib()
# using random words
def random_madlib():
    name = ["Alice", "Bob", "Charlie", "Diana"]
    adjective = ["happy", "sad", "excited", "bored"]
    verb = ["run", "jump", "swim", "dance"]
    noun = ["cat", "dog", "car", "house"]
    story = f"Once upon a time, {random.choice(name)} was very {random.choice(adjective)}. They decided to {random.choice(verb)} a {random.choice(noun)}."
    print(story)
random_madlib()