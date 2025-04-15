# Import the random module to generate random numbers

import random 

# Define the name of the person asking the question
name = "Ana"

# Define the question being asked
question = "Will I win the lottery?"

# Initialize the answer variable to store the Magic 8 Ball's response
answer = ""

# Generate a random number between 1 and 9 (inclusive)
random_number = random.randint(1, 9)
# Uncomment the next line to see the generated random number for debugging
# print(random_number)

# Determine the answer based on the random number generated
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"  # This case should never occur due to the range of random_number

# Alternative approach using a dictionary for cleaner code
"""
answers = {
    1: "Yes - definitely",
    2: "It is decidedly so",
    3: "Without a doubt",
    4: "Reply hazy, try again",
    5: "Ask again later",
    6: "Better not tell you now",
    7: "My sources say no",
    8: "Outlook not so good",
    9: "Very doubtful"
}
answer = answers.get(random_number, "Please try again.")  # Get the answer from the dictionary
"""

# Print the question and the Magic 8 Ball's answer
print(name + " asks: " + question)
print("Magic 8 Ball's answer: " + answer)
