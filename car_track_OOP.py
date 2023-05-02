from time import sleep

# TODO Create class
class Car():
    # Use __init__ method to initialize the
    # two attributes as parameters
    def __init__(self):
            self._car = "car"
            self._color = "Blue"
            self._speed = 50

    # Method for testing
    def car_name(self):
         print("This is the car class")


class Mustang:
    # Use __init__ method to initialize the
    # two attributes as parameters
    def __init__(self):
            self._speed = 0
            self._nos_use = "y"    # To keep track of one shot of NOS

    # Method for testing
    def car_name(self):
            print("You've chosen the 2012 Mustang Boss 302 Laguna Seca edition.")
            sleep(3)
            print("You're gonna have fun.\n")
            sleep(1)

    # Define class methods
    def take_off(self):
        # Use sleep to imitate take 0ff
        sleep(.5)
        print("20 mph")
        sleep(1)
        print("40 mph")
        sleep(1)
        print("60 mph!")

        self._speed += 60
        sleep(.5)
        print(f"Current speed is {self._speed}")
    
    def accelerate(self):       
            self._speed += 20
            print(f"Current speed is {self._speed}")

    def decelerate(self):
            self._speed -= 20
            print(f"Current speed is {self._speed}")

    def nos(self):
        # Use while loop since only one NOS shot may be used
        if self._nos_use == "x":
            print("Sorry. NOS shot already used.")
            print(f"Current speed remains {self._speed}")
        elif self._nos_use == "y":
            # Increment speed by 10, total of +40 mph
            for i in range (4): 
                self._speed += 10
                print(self._speed)
                sleep(.5)

            print("NOS used!")
            print(f"Current speed is {self._speed}")
            self._nos_use = "x"
        

    def pull_over(self):
        while self._speed > 0:
            self._speed -= 25
            if self._speed >=0: 
                print(self._speed)
            sleep(.5)

        self._speed = 0
        print("Pulled over.")
        print(f"Current speed is {self._speed}")

          
    



class GTR:
    # Use __init__ method to initialize the
    # two attributes as parameters
    def __init__(self):
            self._speed = 0
    
    def car_name(self):
          print("This is a GTR")


class Corvette:
    # Use __init__ method to initialize the
    # two attributes as parameters
    def __init__(self):        
        self._speed = 0 

    def car_name(self):
        print("This is a Corvette")




# ------------------------------------------- MAIN --------------------------------------------- #
def main():
    # Create object from Car classs
    car = Car()
    car.car_name()

    # Ask for driver name
    driver_name = input("What's your name, driver: ")

    # Print car inventory and specs
    print(f"\n{driver_name}, here are your car choices:")
    print("1 - 2012 Mustang Boss 302: Laguna Seca Edition")
    print("         Horse power: 444    0-60 in: 4.6 secs    Top Speed: 145 mph ")  # Actually 146 mph
    print("2 - 2011 Nissan GTR - aka The Supercar Killer")
    print("         Horse power: 485    0-60 in: 3.5 secs    Top Speed: ?? mph ")
    print("3 - Corvette ZR1 ")
    print("         Horse power: ??     0-60 in: ??    Top Speed: ?? mph ")

    # Ask for user car choice
    print('')
    user_car = input("Which car do you want to drive? (1, 2, or 3): ")

    # Create object from Class based on user choice
    if user_car == "1":
        user_car = Mustang()
    elif user_car == "2":
        user_car = GTR()
    elif user_car == "3":
        user_car = Corvette()

    # Let them know what they're getting into
    user_car.car_name()

    # Start while loop to get user input for car control
    drive = "a"
    while drive != "p":
          
        action = input("(T)ake off | (A)ccelerate | (D)ecelerate | (N)OS! | (P)ull over: ")
    
        if action == "t": 
              user_car.take_off()
        
        elif action == "a":
              user_car.accelerate()
        
        elif action == "d":
              user_car.decelerate()

        elif action == "n":
              user_car.nos()

        elif action == "p":
              user_car.pull_over()
              drive = "p"
    
    print()
    print(f"Thanks for driving, {driver_name}!")
              
          



main()