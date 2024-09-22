def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()

def main():
    score = 0
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What color is the sky?": "blue",
        "Which players had the biggest impact on CSK's success in the 2023 IPL?": "jadeja"
    
    }

    for question, answer in questions.items():
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
