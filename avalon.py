#!/usr/bin/python3

import av_assign as av
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
import os


# # Choosing player numbers must be between 10 and 5

print("Hi! Welcome to online Avalon!")
player_number = int(input("How many players do you want to play with today? "))
if player_number >11: 
    print( "Oh no that is too many players! This game has to have less than 11 players. \n Tell the extras to concentrate on drinking wine ")
    player_number = int(input("Did you bench some of your friends? How many players do you want to play with now? "))
if player_number <5: 
    print( "Oh no that is  not enough players! This game has to have 5 or more  players. \n Time to start making new friends")
    player_number = int(input("Did you make new friends? How many players do you want to play with now? "))
player_names = [ ] 
email_dict = {}  

# Inputting the players name and email 
for i in range(0, player_number): 
    player = input("Player name: ")
    email = input("Player email: ")
    player_names.append(player)
    email_dict[player] = email


# Confirm players
print("\n")
print("The players for this game are:")
print("------------------------------")
for key, value in email_dict.items():
    print("Player: ", key, "Email: ", value)


# Special player selections 
special_input = (input("Did you want to play with any special players (Percival, Morgana or Oberon)? Y/N ")).upper()
if special_input == "N": 
    percival = False
    morgana = False
    oberon = False 

# Selecting if playing with Percival 
if special_input == "Y":
    perc_in = (input("Did you want to play with Percival? Y/N ")).upper()
    if perc_in == "Y":
        percival = True
        print("Great, We will play with Percival")
    elif perc_in == "N":
        percival = False
    else: 
        print("That is not a valid input, please try again")
        perc_in = (input("Did you want to play with Percival? Y/N ")).upper()

# Selecting if playing with Morgana     
    if percival == True: 
        morg_in = (input("Did you want to play with Morgana? Y/N ")).upper()
        if morg_in == "Y":
            morgana = True
            print("Great, We will play with Morgana")
        elif morg_in == "N":
            morgana = False
        else: 
            print("That is not a valid input, please try again")
            morgana = (input("Did you want to play with Percival? Y/N ")).upper()

# Selecting if playing with Oberon         
    ob_in = (input("Did you want to play with Oberon? Y/N ")).upper()
    if ob_in == "Y":
        oberon = True
        print("Great, We will play with Oberon")
    elif ob_in == "N":
        oberon = False
    else: 
        print("That is not a valid input, please try again")
        ob_in = upper(input("Did you want to play with Oberon? Y/N "))

        


# Randomly assigning roles and information 
av.assigning_roles(player_names, percival, morgana, oberon)


# Email information to send to players 
sender_email = (input("What is your gmail email address: ")).lower()
sender_email_pswd = (getpass("What is your gmail email password: "))


# Sending emails to players 
for player in list(email_dict.keys()): 
    filename = player
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    
    s.login(sender_email, sender_email_pswd)


    msg = MIMEMultipart()      
    
    msg['From']=email_dict[player]
    msg['To']= email_dict[player]
    msg['Subject']="Avalon Role Assignment"


    msg.attach(MIMEText(file_content, 'plain'))
    

    s.send_message(msg)
    
    #deleting things 
    os.remove(filename)
    del msg
    
      

    s.quit()



