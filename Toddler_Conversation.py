from random import choice

questions = ["Why is the sky blue? ", "How are babies made? ", "How are clouds made? ", "Where are all the dinosaurs? "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... okay.")
