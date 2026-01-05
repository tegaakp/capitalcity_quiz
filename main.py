# this section covers the flow of the quiz

# Greet the user

print("Welcome to the geography quiz! Today you will be tested on the capital city of European Countries")

# Explain the rules
print(" For each country shown please input your desired capital city")

print(input("Are you ready to begin, yes/no: "))


from data import countries_and_capitals
from question import ask_question

def run_quiz():
    score = 0

    for country, capital in countries_and_capitals.items():
        print()
        if ask_question(country, capital):
            score += 1

    print("\nQuiz complete!")
    print(f"Your final score is {score} out of {len(countries_and_capitals)}")

run_quiz()
