#quizgame

#ini membuat soal di tuple
questions = ("how many element are in the periodic table?: ",
            "which animal lays the largest eggs?: ",
            "what is the most abundant gas in the earth's atmosphere?: ",)

#lalu ini jawaban di 2d list
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elepant", "D. OStrich"),
           ("A. Nitrogen", "B. Oxygin", "C. Carbondioxcida", "D. Hydrogen" ))

#jawaban
answers = ("C", "D", "A")

#tebakan kita di list
guesses = []

#nilai hasil
score = 0

#
question_num = 0

#kita menggunakan for loop untuk mengeluarkan is soal
for question in questions:
    print("---------------------------------------------------") #ini untuk tampilan doang
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the right answer")
    question_num += 1


print("--------------------------------------------------------")
print("--------------------------RESULT------------------------")
print("--------------------------------------------------------")


print("answer: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guess: ", end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")

