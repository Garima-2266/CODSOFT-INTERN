import time
import random
import sys


def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def typing_speed_test():
    target_text = load_text()
    print("Type the following:")
    print(target_text)

    input("Press Enter when you are ready to start...")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    if user_input == target_text:
        time_taken = end_time - start_time
        words_per_minute = (len(target_text.split()) / time_taken) * 60
        print(f"Congratulations! Your typing speed: {words_per_minute:.2f} WPM")
    else:
        print("Incorrect typing. Try again.")


if __name__ == "__main__":
    print("Welcome to the Typing Speed Test!")

    while True:
        typing_speed_test()
        play_again = input("Do you want to try again? (yes/no): ").lower()

        if play_again != 'yes':
            print("Thank you for playing. Goodbye!")
            sys.exit()
