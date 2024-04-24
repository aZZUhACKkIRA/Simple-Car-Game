command = ''
while True:
    command = input("> ")
    if command.lower() == "help":
        print("""
start - to start the car.
stop - to stop the car.
quit - to exit the program
        """)
    elif command.lower() == "start":
        print("Car started, Ready to go!")
    elif command.lower() == "stop":
        print("Car Stopped")
    elif command.lower() == "quit":
        print("Have a good day!")
        break
    else:
        print("I didn't understand. ")
