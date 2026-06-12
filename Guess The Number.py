import random

print("=" * 50)
print("             NUMBER GUESSING GAME")
print("=" * 50)

player = input("Enter your name: ")

total_wins = 0
total_losses = 0
best_streak = 0
current_streak = 0

while True:

    print("\nChoose Difficulty")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        start, end = 1, 10
        chances = 3
    elif choice == "2":
        start, end = 1, 50
        chances = 7
    elif choice == "3":
        start, end = 1, 100
        chances = 10
    else:
        print("Invalid choice! Easy mode selected.")
        start, end = 1, 10
        chances = 5

    secret = random.randint(start, end)

    print(f"\nGuess a number between {start} and {end}")

    for attempt in range(1, chances + 1):

        print(f"\nChance {attempt}/{chances}")

        try:
            guess = int(input("Enter your guess: "))
        except:
            print("Please enter a valid number.")
            continue

        if guess == secret:
            print("🎉 Congratulations! You guessed correctly.")

            total_wins += 1
            current_streak += 1

            if current_streak > best_streak:
                best_streak = current_streak

            score = (chances - attempt + 1) * 10
            print("Score Earned:", score)
            break

        elif guess < secret:
            print("📈 Too Low!")
        else:
            print("📉 Too High!")

    else:
        print("\n❌ You Lost!")
        print("Correct Number is:", secret)

        total_losses += 1
        current_streak = 0

    print("\n" + "-" * 40)
    print("Player:", player)
    print("Wins:", total_wins)
    print("Losses:", total_losses)
    print("Best Winning Streak:", best_streak)
    print("-" * 40)

    again = input("\nPlay Again? (yes/no): ").lower()

    if again != "yes":
        break

print("\n" + "=" * 50)
print("                   GAME OVER")
print("=" * 50)

print("Player:", player)
print("Total Wins:", total_wins)
print("Total Losses:", total_losses)
print("Best Streak:", best_streak)

if total_wins >= 10:
    print("🏆 Master Guesser")
elif total_wins >= 5:
    print("🔥 Pro Player")
elif total_wins >= 1:
    print("👍 Good Try")
else:
    print("🌱 Beginner Level")

print("Thank you for playing!")
     
