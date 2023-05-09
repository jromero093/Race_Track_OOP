# import game_title for title
import game_title_unused
import game_title

from time import sleep

# Import Console for console text printing
from rich.console import Console

# Initialize rich.console
console = Console()

# TODO Create class (Car_Mustang will be my parent class)
class Car_Mustang:
    # Use __init__ method to initialize the
    # three attributes as parameters
    def __init__(self, driver_name):
            self._speed = 0
            self._nos_use = "y"     # To keep track of one shot of NOS
            self._take_off = "y"    # Too keep track of whether you've already taken off
            self._driver_name = driver_name

    # Introduce car
    def car_name(self):
            console.print("\nYou've chosen the [bold blue]2012 Mustang Boss 302: Laguna Seca Edition[/bold blue].")
            sleep(3)
            print("You're gonna have fun.\n")
            sleep(1)

    def take_off(self):
        # Check if car has taken off already
        if self._take_off == "x":
            print("The car's already moving. Duh")
            print(f"Speed remains {self._speed}")        
        elif self._take_off == "y":
            sleep(.5)
            print("20 mph")
            sleep(.5)
            print("40 mph")
            sleep(.5)
            print("60 mph!")
            self._take_off = "x"

            self._speed += 60
            sleep(.5)
            print(f"Current speed is {self._speed}")
    
    def accelerate(self):
            #Make sure car has taken off first:
            if self._take_off == "x":
                self._speed += 20
                print(f"Current speed is {self._speed}")

                # Check speed
                self.top_speed_situation()
            # If it has not taken off yet
            elif self._take_off == "y":
                print("You have to take off first.")

    def decelerate(self):
            #Make sure car has taken off first:
            if self._take_off == "x":
                self._speed -= 20
                print(f"Current speed is {self._speed}")
                if self._speed < 60:
                    # Encourage them to step! on! it!
                    sleep(.5)
                    print(f"\n(You know, you can go a little faster if you want, {self._driver_name})")
                    sleep(.5)
            # If it has not taken off yet
            elif self._take_off == "y":
                print("You have to take off first.")

    def nos(self):
            #Make sure car has taken off first:
            if self._take_off == "x":
                # Use if statements since only one NOS shot may be used
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
            elif self._take_off == "y":
                print("You have to take off first.")

            # Check speed
            self.top_speed_situation()
            
        

    def pull_over(self):
        #Make sure car has taken off first:
            if self._take_off == "x":
                while self._speed > 0:
                    self._speed -= 25
                    if self._speed >=0: 
                        print(self._speed)
                        sleep(.5)

                self._speed = 0
                print("Pulled over.")
                print(f"Current speed is {self._speed}")
                sleep(2)
            
            elif self._take_off == "y":
                print("Very funny. Try taking off first.")

    def top_speed_situation(self):
            # if statements to check for top speed situation
            if self._speed >= 165:
                sleep(1)
                console.print("[red]Warning. Warning.[/red] Engine overheat.")
                print("Engine imploding.")
                sleep(2.5)
                for i in range (3):
                    print("...")
                    sleep(1)
                print("*Crash crash bang bang*")
                sleep(3)
                print("You've crashed. A total wreck.")
                sleep(3)
                print("But you'll recover. And you'll drive again.")
                sleep(2.5)
                print("It's what you do.")
                sleep(2.5)
                quit()
            elif self._speed >= 140:
                sleep(1)
                console.print("[red]Warning[/red]: Top Speed Reached\n[red]Do no accelerate[/red] (Unless you can't help it)")
    


# Define child class w specifics of GTR
class GTR(Car_Mustang):
    # Enter car_name specific to the GTR
    def car_name(self):
        console.print("\nYou've chosen the [bold blue]2011 Nissan GTR[/bold blue].")
        sleep(3)
        print("It's a dangerous car. " , end="")
        sleep(2)
        print("Have fun!\n")
        sleep(1)

    # A little faster acceleration than Mustang
    def accelerate(self):
            #Make sure car has taken off first:
            if self._take_off == "x":
                self._speed += 30               # +30  as opposed to 20
                print(f"Current speed is {self._speed}")

                # Check speed
                self.top_speed_situation()
            # If it has not taken off yet
            elif self._take_off == "y":
                print("You have to take off first.")

    def top_speed_situation(self):
        # Overriding parent class bc GTR has higher top speed (190mph)
            if self._speed >= 200:
                sleep(1)
                console.print("[red]Warning. Warning.[/red] Engine overheat.")
                print("Engine imploding.")
                sleep(2.5)
                for i in range (3):
                    print("...")
                    sleep(1)
                print("*Crash crash bang bang*")
                sleep(3)
                print("You've crashed. A total wreck.")
                sleep(3)
                print("But you'll recover. And you'll drive again.")
                sleep(2.5)
                print("It's what you do.")
                sleep(2.5)
                quit()
            elif self._speed >= 180:
                sleep(1)
                console.print("[red]Warning[/red]: Top Speed Almost Reached\n[red]Do no accelerate[/red] (Unless you can't help it)")
         

# Define child class w specifics of the Testarossa
class Ferrari(Car_Mustang):
    def car_name(self):
        console.print("\nYou've chosen the [bold blue]1984[/bold blue][bold red] Ferrari Testarossa[/bold red].")
        sleep(3)
        print("Honestly, this car's such a legend, you probably shouldn't be driving it.")
        sleep(2)
        print("Enjoy!\n")
        sleep(1)

    # A little faster acceleration than Mustang
    def accelerate(self):
            #Make sure car has taken off first:
            if self._take_off == "x":
                self._speed += 25               # +25  as opposed to 20
                print(f"Current speed is {self._speed}")

                # Check speed
                self.top_speed_situation()
            # If it has not taken off yet
            elif self._take_off == "y":
                print("You have to take off first.")

    def top_speed_situation(self):
        # Overriding parent class for Testarossa top speed (180mph)
            if self._speed >= 190:
                sleep(1)
                console.print("[red]Warning. Warning.[/red] Engine overheat.")
                print("Engine imploding.")
                sleep(2.5)
                for i in range (3):
                    print("...")
                    sleep(1)
                print("*Crash crash bang bang*")
                sleep(3)
                print("You've crashed. A total wreck.")
                sleep(3)
                print("But you'll recover. And you'll drive again.")
                sleep(2.5)
                print("It's what you do.")
                sleep(2.5)
                quit()
            elif self._speed >= 170:
                sleep(1)
                console.print("[red]Warning[/red]: Top Speed Almost Reached\n[red]Do no accelerate[/red] (Unless you can't help it)")


# ---------------------------------------------- MAIN ------------------------------------------------ #
def main():
    # TODO Make and call game title from module
    game_title.title()
    sleep(1)
    print()
    print("                A Day At The Track All To Yourself")
    sleep(1.5)

    # Ask for driver name
    driver_name = input("\nWhat's your name, driver: ")

    # Start loop in case user wants to have multiple turns:
    user_turn = "y"
    while user_turn == "y":
        
        # Print car inventory and specs
        print(f"\n{driver_name}, here are your car choices:")
        sleep(1)
        console.print("1 - [bold blue]2012 Mustang Boss 302: Laguna Seca Edition[/bold blue]")
        print("         Horse power: 444    0-60 in: 4.6 secs    Top Speed: 145 mph ")  # Actually 146 mph
        sleep(1)
        console.print("2 - [bold blue]2011 Nissan GTR - aka 'The Supercar Killer'[/bold blue]")
        print("         Horse power: 485    0-60 in: 3.3 secs    Top Speed: 190 mph ")  # Actually 193 mph
        sleep(1)
        console.print("3 - [bold blue]1984[/bold blue][bold red] Ferrari Testarossa[/bold red][bold blue] - The Legend[/bold blue]")
        print("         Horse power: 385    0-60 in: 5.2 secs    Top Speed: 180 mph ")
        sleep(2)

        # Ask for user car choice
        print('')
        user_car = input("Which car do you want to drive? (1, 2, or 3): ")

        # Create object from Class based on user choice
        if user_car == "1":
            user_car = Car_Mustang(driver_name)
        elif user_car == "2":
            user_car = GTR(driver_name)
        elif user_car == "3":
            user_car = Ferrari(driver_name)


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
        print(f"That was some nice driving, {driver_name}.")
        sleep(1.5)
        print("There's still a couple of hours of sunlight left.")
        sleep(1)
        # Ask if they want to drive again
        user_turn = input("Wanna drive again? You can pick another car if you want. (y)es/(n)o: ")
    
    # If not, say goodbye
    print("\nWell, hope you enjoyed your run. Come back some time.")
    sleep(1.5)
    print("I'll pull some strings, get you the track to yourself again.")
    sleep(3)
    print("Seeya next time, kid.")
    sleep(3)
          



main()