command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
           print("Car is already started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else: 
            started = False
            print("Car is stopped")
    elif command == "help":
        print("""
Start:- To start the car
Stop:- To stop the car
Exit:- To exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand this")
        print("Start:- To start the car")
        print("Stop:- To stop the car")
        print("Exit:- To exit")

