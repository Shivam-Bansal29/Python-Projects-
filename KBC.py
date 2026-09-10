money = 0
x = input(" Enter Your Name : ")
print(f" Welcome to the game {x}\n")
print(" 🛑 Press 0 to quit the game \n\n")

questions = [
    {
        "que": "What is the capital of India ?",
        "ans": "a. Delhi    b. Chandigarh\nc. goa    d. mumbai",
        "correct": "a",
        "prize": 1000
    },
    {
        "que": "Who is the PM of India ?",
        "ans": "a. Narinder Modi    b. Dropti murmu\nc. Rahul Gandhi   d. Neerav Modi",
        "correct": "a",
        "prize": 10000
    },
    {
        "que": "Which is the largest state of India on basis of area ?",
        "ans": "a. Gujarat    b. Maharashtra\nc. Punjab    d. Rajasthan",
        "correct": "d",
        "prize": 50000
    },
    {
        "que": "Who is the first president of India ?",
        "ans": "a. Jawaharlal Nehru    b. Rajendra Prasad\nc. Dr. Radhakrishnan    d. Mahatma Gandhi",
        "correct": "b",
        "prize": 100000
    },
    {
        "que": "Which is the largest river of India ?",
        "ans": "a. Kaveri     b. Godawari\nc. Ganga     d. Yamuna",
        "correct": "a",
        "prize": 500000
    }
]

for y in questions:
    print(y["que"], "\n")
    print(y["ans"], "\n")
    answer = input("Enter the option: ").lower()

    if answer == "0":
        print("\nYou chose to exit the game")
        break
    elif answer == y["correct"]:
        print("\nWell done!! Your answer is right")
        money += y["prize"]
        print(f"You win {money}\n")
    else:
        print(f"\nYour answer is wrong\nRight answer is {y['correct']}\nGame is over now")
        break

print(f"You won {money}")
