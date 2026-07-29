#Safari Camp Bible Character Game
print ("Welcome to Safari Camp 2026")

# Enter user's name
child_name = input("What is your name?")
print ("Nice to meet you ", child_name, "let us play a game")

bible_characters = ("Moses", "Elijah", "Esther", "Paul")
guess = input("Guess a Bible Character: ")
if guess in bible_characters:
    print ("Great Job!")
else:
    print("Try Again")

# Step 1: Create a list of basketball players
basketball_players = ["LeBron", "Curry", "Jordan", "Kobe", "Giannis"]

# Step 2: Start with a score of 0
score = 0
rounds_played = 0
max_rounds = 5

print("🏀 Welcome to the Basketball Guessing Game!")
print("Try to guess a famous basketball player. You have 5 chances!")

# Step 3: Start the game loop
while rounds_played < max_rounds:
    guess = input(f"\nRound {rounds_played + 1}: Who is your guess? ")

    if guess in basketball_players:
        print("✅ Nice! You got it!")
        score += 1
    else:
        print("❌ Oops! Not in our list.")

    rounds_played += 1

# Step 4: End of game
print(f"\n🏁 Game Over! You scored {score} out of {max_rounds}.")
if score == max_rounds:
    print("🔥 Amazing! You're a basketball expert!")
elif score >= 3:
    print("🏀 Good job!")
else:
    print("🧠 Keep practicing and try again!")





