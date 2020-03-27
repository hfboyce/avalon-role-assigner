#!/usr/bin/python3
import random
import string

def get_value(dictionary,value):
    '''
     Gets the dictionary keys depending on the value 
    '''
    for key in dictionary:
        if dictionary[key] == value:
            return key


def assigning_roles(player_names, percival=False, morgana=False, oberon=False):
    
    """
    Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    player_names : list
        The lists of all the players in the game 
    percival : bool, optional
        Whether or not the players decide to play with the special role of Percival. Good player in favour of good. 
    morgana :  bool, optional
        Whether or not the players decide to play with the special role of Morgana.  Evil player in favour of bad.
    oberon :  bool, optional
        Whether or not the players decide to play with the special role of Oberon Evil player in favour of good.   

   
    """
    
    
    num_player = len(player_names)
    print("Playing with", num_player, "players" )
    assert num_player >= 5, "You need at least 5 players to plsy Avalon"
    assert num_player <= 12, "You need less than 11 players to play Avalon"
    
    if morgana == True: 
        assert percival == True, "You need Percival to be playing to use Morgana"
        
    
    
    game_roles = ["Merlin",
                  "Assasin",
                  "Minion of Mordred",
                  "Loyal Servant of Arthur",
                  "Loyal Servant of Arthur"]
    
    players_to_roles= dict()

    # 6 players add good
    if num_player >5:
        game_roles.append("Loyal Servant of Arthur")

    # 7 players add bad
    if num_player >6:
        game_roles.append("Minion of Mordred")

    # 8 players add good
    if num_player >7:
        game_roles.append("Loyal Servant of Arthur")

    # 9 players add good
    if num_player >8:
        game_roles.append("Loyal Servant of Arthur")

    # 10 players add bad
    if num_player >9:
        game_roles.append("Minion of Mordred")
    
    
    # Special Roles 
    
    if percival == True: 
        game_roles.insert(1,"Percival")
        game_roles.remove("Loyal Servant of Arthur")
        
    if morgana == True: 
        try:
            game_roles.remove("Minion of Mordred")
        except ValueError as error:
            print("You do not have enough players to add this role")
        else:
            game_roles.insert(2,"Morgana")
        
    if oberon == True: 
        try:
            game_roles.remove("Minion of Mordred")
        except ValueError as error:
            print("You do not have enough players to add this role")
        else:
            game_roles.insert(2,"Oberon")
        if "Morgana" in game_roles:
            print('You can either have Morgana or Oberon for this amount of players')
    

    
    # Let's assign a role to each player randomly 
    
    for player in player_names:
        role_selected = random.choice(game_roles)
        game_roles.remove(role_selected)
        players_to_roles[player] = role_selected
    
    
    evil_roles_to_merlin = ['Oberon', "Morgana", "Assasin", "Minion of Mordred"]
    evil_roles_to_evil = ["Morgana", "Assasin", "Minion of Mordred"]
    evil_players_to_merlin = [] 
    evil_players_to_evil = []
    
    for key, value in players_to_roles.items():
        if value in evil_roles_to_merlin:
            evil_players_to_merlin.append(key)
        if value in evil_roles_to_evil:
            evil_players_to_evil.append(key)
            
    
            
    
    # OK now assign viewing ability to everyone. 
    
    for key, value in players_to_roles.items():
        file = open(key + ".txt", "w") 
        file.write("Hi " + key.capitalize() +", \n")
        file.write("Your role in this game is: "+ value + '\n')  
        file.write('\n')  
        file.write("The players in this game are:"  + '\n')  
        for player in player_names: 
             file.write("- " + player.capitalize()  + '\n')
        file.write('\n')         
        if percival == True:
            file.write("You are playing with the Percival character"  + '\n') 

        if morgana == True: 
            file.write("You are playing with the Morgana character"  + '\n')
      
        if oberon == True:
            file.write("You are playing with the Oberon character"  + '\n') 
        
        file.write('\n')  
        if value == "Morgana":
            file.write("As Morgana, you appear to Percival as Merlin."  + '\n')
        
     
        file.write('\n')   
        if value == "Merlin":
            file.write("The servants of Mordred are:"  + '\n')
            for bad_guy in evil_players_to_merlin:
                 file.write( "- " + bad_guy.capitalize() + '\n') 
        
        if value in evil_roles_to_evil:
            file.write("The servants of Mordred are:"  + '\n')
            for bad_guy in evil_players_to_evil:
                 file.write( "- " + bad_guy.capitalize()  + '\n') 
            if oberon == True:
                file.write("Since you are playing with Oberon, there is a third unknown evil player "  + '\n')
        
        if value == "Oberon":
            file.write("You are evil but you are unable to know who else is evil as the Oberon role."  + '\n')
                
        if value == "Percival":
            file.write("As Percival you get insight into who Merlin is." +'\n')
            merlin_player = get_value(players_to_roles, "Merlin")
            if morgana == True:
                morgana_player = get_value(players_to_roles, "Morgana")
                merlins = [merlin_player.capitalize(), morgana_player.capitalize()]
                random.shuffle(merlins)
                file.write("Since you are playing with Morgana, one of the following players is Merlin the other is \n Morgana, a servant of Mordred" + "\n") 
                file.write( "- " + merlins[0] + '\n')
                file.write( "- " + merlins[1] +'\n')
            else:
                 file.write("In this case, Merlin is " +  merlin_player.capitalize() +'\n')
                        
                    
        if value == "Loyal Servant of Arthur":
            file.write("As a Loyal Servant of Arthur, you do not get insight into the other player's roles"  + '\n')
                    
        return 
        file.close() 

   