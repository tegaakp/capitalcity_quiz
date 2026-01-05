def ask_question(country, capital):
    print(f"What is the capital of {country}?")
    answer = input("Your answer: ").strip()

    if answer.lower() == capital.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The capital of {country} is {capital}.")
        return False


