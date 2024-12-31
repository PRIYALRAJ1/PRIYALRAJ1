def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = int(input("Your answer (1-4): "))
    if options[answer - 1] == correct_answer:
        print("Correct! Let's move to the next level...\n")
        return True
    else:
        print("Oops! That’s not quite right. Let’s try again...\n")
        return False

def level_1():
    question = "Where did we first meet?"
    options = ["At the park", "At a party", "At work", "At a mutual friend's house"]
    correct_answer = "At a mutual friend's house"  # Customize with your actual answer
    return ask_question(question, options, correct_answer)

def level_2():
    question = "Where did we go on our first date?"
    options = ["A restaurant", "A movie theater", "A beach walk", "A coffee shop"]
    correct_answer = "A coffee shop"  # Customize with your actual answer
    return ask_question(question, options, correct_answer)

def level_3():
    question = "What’s our favorite thing to do together?"
    options = ["Watch movies", "Travel", "Play games", "Cook together"]
    correct_answer = "Travel"  # Customize with your actual answer
    return ask_question(question, options, correct_answer)

def level_4():
    question = "What was the most memorable moment we've shared?"
    options = ["Our first kiss", "Our trip together", "When we moved in together", "When we both made each other laugh"]
    correct_answer = "Our trip together"  # Customize with your actual answer
    return ask_question(question, options, correct_answer)

def level_5():
    question = "What would make me the happiest in the world?"
    options = ["A romantic dinner", "A trip around the world", "You saying 'Yes'", "A lifetime of love and laughter together"]
    correct_answer = "You saying 'Yes'"
    return ask_question(question, options, correct_answer)

def main():
    print("Welcome to the 'Journey of Us' Quiz Game!\n")
    
    levels = [level_1, level_2, level_3, level_4, level_5]
    for level in levels:
        if not level():
            print("You lost the game. No worries! Let’s try again.\n")
            return
    
    print("\nCongratulations! You’ve completed the journey... and now, I have one last question...")
    print("Will you marry me? 💍")

if __name__ == "__main__":
    main()
