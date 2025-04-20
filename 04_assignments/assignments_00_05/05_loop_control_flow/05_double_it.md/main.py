# Prompt user for a starting number
curr_value = int(input("Enter a number: "))

# Double the number until it reaches or exceeds 100
while curr_value < 100:
    curr_value *= 2  # Double the current value
    print(curr_value, end=" ")
