print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a crossroad, which direction do you want to head?")
cross_road = input('Type "left" or "right". \n')

if cross_road.lower() == "left":
    lake = input("You've made it to a lake, "
          "do you want to wait for a boat or swim across? "
                 'Type "wait" or "swim" \n')
    if lake.lower() == "wait":
        house = input("You made it to a house with 3 doors! "
                      "There is a red, yellow, and blue door."
                      " Which one do you open? "
                      'Type "red" "yellow" or "blue" \n')
        if house.lower() == "yellow":
            print("you found the treasure!")
        elif house.lower() == "red":
            print("you entered a room of fire. game over.")
        elif house.lower() == "blue":
            print("you was attacked by lions. game over.")
        else:
            print("That door doesn't exist. game over.")
    else:
        print("you were attacked by a shark. game over." )
else:
    print("You fell into a pit. game over.")
