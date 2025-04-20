import time

def main():
    print("Welcome to the countdown timer!")
    while True:
        time_input = input("Please enter the time in seconds: ")
        if time_input.isdigit():
            time_input = int(time_input)
            break
        else:
            print("Please enter a valid number.")
    print("\nStarting countdown...")
    
    while time_input >= 0:
        mins, secs = divmod(time_input, 60)
        timeformat = f"{mins:02}:{secs:02}"
        print(timeformat, end='\r')
        time.sleep(1)
        time_input -= 1

    print("Time's up!")

if __name__ == "__main__":
    main()