import random
import shelve
import os
from blessings import Terminal
term = Terminal()

#Start of Enemy List
normal_troll = ["Troll", 10, 5, 1, 5, 50, "enemies/troll.txt"]
elite_troll = ["Elite Troll", 20, 10, 1, 10, 100, "enemies/elitetroll.txt"]
normal_skelly = ["Skelly", 5, 1, 1, 1, 1, "enemies/skelly.txt"]
#End Enemy List

#Boss List
#End of Boss List


def battle_sequence(name, strength, defense, intelligence, agility, health, enemy_graphic):
    os.system(['clear','cls'][os.name == 'nt'])
    fight_enemy_stats = [name, strength, defense, intelligence, agility, health, enemy_graphic]
    print fight_enemy_stats[0]
    hp = fight_enemy_stats[5]
    while hp > 0:
        f = open(fight_enemy_stats[6], 'r')
        s = f.read()
        print s
        print ("")
        print ("Health: ", hp)
        print ("Attack Power: ", fight_enemy_stats[1])
        print ("1. Attack")
        print ("2. Run like a girl")
        hero_action = raw_input("Action: ")
        if hero_action == "1":
            hp = hp - 10
        elif hero_action == "2":
            hp = hp - 500
            print ("You run like a little bitch!!!!!!!")

def new_hero(name):
    os.system(['clear','cls'][os.name == 'nt'])
    #Base stats for each class : Strength, Defense, Intelligence, Agility, Health
    warrior = ["warrior", 10, 8, 1, 4, 200]
    rogue = ["rogue", 5, 3, 3, 10, 120]
    mage = ["mage", 2, 2, 10, 3, 100]
    hero_name = name
    print ("1.Warrior - This is a brute force fighter with shiny armor and sword")
    print ("2.Rouge - This sneaky bastard can catch you by suprise.")
    print ("3.Mage - He'll shoot lightning bolts up your ass....Nuff said")
    choose_hero_class = raw_input("Pick your class. ")
    create_hero = shelve.open(hero_name, writeback=True)
    hero_list = open("herolist.txt", "a")
    hero_list.write(hero_name + "   " )
    if choose_hero_class == "1":
        print ""
        print ""
        print hero_name
        print ("The mighty night. High in strength and stamina, but lacking in")
        print ("brains. But hey, shiny armor and stuff!")
        f = open('resources/knight.txt', 'r')
        s = f.read()
        print s
        print ("")
        create_hero[hero_name] = (warrior[0:6])
    elif choose_hero_class == "2":
        print ""
        print ""
        print hero_name
        print ("Ahh the sneaky Rogue. You'll never see him co..........")
        f = open('resources/rogue.txt', 'r')
        s = f.read()
        print s
        print ("")
        create_hero[hero_name] = (rogue[0:6])
    elif choose_hero_class == "3":
        print ("The Mage is not available yet.")
    else:
        print ("Returning to Title Screen")




f = open('resources/brokenatlas.txt', 'r')
s = f.read()
print (s),
print ("")
pause_for_logo = raw_input('Press enter to continue..............')


create_new_hero = raw_input("Do you want to create a new hero? Enter 'Y' or 'N'  ")
create_new_hero.upper()
if create_new_hero == "Y":
    hero_create = raw_input("New Hero Name:  ")
    new_hero(hero_create)

os.system(['clear','cls'][os.name == 'nt'])


print term.bold("*****************************************")
print term.bold("************ Choose Your Hero ***********")
print term.bold('*****************************************')
print
load_hero_list = open("herolist.txt", "r")
hero_list_display = load_hero_list.read()
print hero_list_display
login_name = raw_input("Choose Hero:  ")
load_hero = shelve.open(login_name, writeback=True)
game_loop = 1
hero_data = load_hero[login_name]

while game_loop != 0:
    os.system(['clear','cls'][os.name == 'nt'])
    with term.location():
        print term.blue_on_yellow + term.move(1, 60) + (login_name) + term.normal
        print term.move(2, 60) + "Class: " + hero_data[0]
        print term.move(3, 60) + "Str: " + str(hero_data[1])
        print term.move(4, 60) + "Def: " + str(hero_data[2])
        print term.move(5, 60) + "Int: " + str(hero_data[3])
        print term.move(6, 60) + "Agi: " + str(hero_data[4])
        print term.move(7, 60) + "Health: " + str(hero_data[5])
    home_castle = open("resources/homecastle.txt", "r")
    show_home_castle = home_castle.read()
    print show_home_castle
    
    pause_loop = raw_input("Press Enter to Continue")



