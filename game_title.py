# This is my title module for my car game
# ANSI Shadow font
from time import sleep

part_1 = """
 █████╗ ████████╗
██╔══██╗╚══██╔══╝
███████║   ██║   
██╔══██║   ██║   
██║  ██║   ██║   
╚═╝  ╚═╝   ╚═╝   
"""

part_2 = """
    ████████╗██╗  ██╗███████╗
    ╚══██╔══╝██║  ██║██╔════╝
       ██║   ███████║█████╗  
       ██║   ██╔══██║██╔══╝  
       ██║   ██║  ██║███████╗
       ╚═╝   ╚═╝  ╚═╝╚══════
"""

part_3 = """
           ████████╗██████╗  █████╗  ██████╗██╗  ██╗
           ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
              ██║   ██████╔╝███████║██║     █████╔╝ 
              ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
              ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
              ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝                                      
"""


def title():
    print(f"{part_1} ", end="")
    sleep(.5)
    print(f"{part_2} ", end="")
    sleep(.5)
    print(f"{part_3} ")


def main():
    title()



# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()