print("Welcome to Nadi's Treasure Island")
print("""
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                      
                                                      
                                                      
                                                      
 ,adPPYba, 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   
a8P_____88 88P'   "88"    "8a ""     `Y8 88P'    "8a  
8PP""""""" 88      88      88 ,adPPPPP88 88       d8  
"8b,   ,aa 88      88      88 88,    ,88 88b,   ,a8"  
 `"Ybbd8"' 88      88      88 `"8bbdP"Y8 88`YbbdP"'   
                                         88           
                                         88           
""")
choice = input("Choose, left or right! ").lower()
if choice == "right":
    print("Game Over.")
elif choice == "left":
    choice = input("Choose, swim or wait! ").lower()
    if choice == "swim":
        print("Game Over.")
    elif choice == "wait":
        choice = input("Choose a door, yellow, red or blue! ").lower()
        if choice == "red" or choice == "blue":
            print("Game Over.")
        elif choice == "yellow":
            print("You won! YAY! You get wine and cheese tehe!")
            print('''
                    _
       |-|
       |~|
       |:|   WINE AND CHEESE
      .'.'.
     /   ::\
     |_____|     __          _
     |:.:;.|   <:__:>     .-'o\
     |_____|   \  ::/  .o' O. o\
     |   ::|    '..'  |--o.--o--|
     |   ;:|     ||   |._._o_._.|
     \_____/    .''.
               '----'     pjb
            ''')