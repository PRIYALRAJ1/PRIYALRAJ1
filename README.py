def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = int(input("Your answer (1-4): "))
    if options[answer - 1] == correct_answer:
        print("Correct! Moving to the next level...\n")
        return True
    else:
        print("Incorrect. Try again...\n")
        return False

def level_1():
    question = "What is GitHub primarily used for?"
    options = ["Online code execution", "Version control and collaboration", "Data analysis", "Social media platform"]
    correct_answer = "Version control and collaboration"
    return ask_question(question, options, correct_answer)

def level_2():
    question = "What command is used to initialize a new Git repository in a project folder?"
    options = ["git create", "git init", "git start", "git new"]
    correct_answer = "git init"
    return ask_question(question, options, correct_answer)

def level_3():
    question = "What is the command to clone a repository from GitHub to your local machine?"
    options = ["git clone <repository-url>", "git pull <repository-url>", "git copy <repository-url>", "git fetch <repository-url>"]
    correct_answer = "git clone <repository-url>"
    return ask_question(question, options, correct_answer)

def level_4():
    question = "What Git command creates a new branch called 'feature-branch'?"
    options = ["git create branch feature-branch", "git branch feature-branch", "git new branch feature-branch", "git checkout -b feature-branch"]
    correct_answer = "git checkout -b feature-branch"
    return ask_question(question, options, correct_answer)

def level_5():
    question = "When contributing to a project on GitHub, how do you propose changes to the main project?"
    options = ["Push changes directly to the main branch", "Fork the repository and submit a pull request", "Create an issue in the repository", "Send an email to the repository owner"]
    correct_answer = "Fork the repository and submit a pull request"
    return ask_question(question, options, correct_answer)

def main():
    print("Welcome to the GitHub Quiz Game!\n")
    
    levels = [level_1, level_2, level_3, level_4, level_5]
    for level in levels:
        if not level():
            print("You lost the game. Better luck next time!")
            return
    
    print("Congratulations! You are a GitHub expert!")

if __name__ == "__main__":
    main()
