#Created by Aidan Andersen
import os
import random
import battle

os.system('cls')

print("EEEEEEEEEEEEEEE   PPPPPPPPPPPPPPP   IIIIIIIIIIIIIII   CCCCCCCCCCCCCCC          RRRRRRRRRRRRRRR   PPPPPPPPPPPPPPP    GGGGGGGGGGGGG ")
print("EEEEEEEEEEEEEEE   PPPPPPPPPPPPPPP   IIIIIIIIIIIIIII   CCCCCCCCCCCCCCC          RRRRRRRRRRRRRRR   PPPPPPPPPPPPPPP   GGGGGGGGGGGGGGG")
print("EEEEE             PPPPP     PPPPP        IIIII        CCCCC                    RRRRR     RRRRR   PPPPP     PPPPP   GGGGG          ")
print("EEEEE             PPPPP     PPPPP        IIIII        CCCCC                    RRRRR     RRRRR   PPPPP     PPPPP   GGGGG          ")
print("EEEEEEEEEEEEEEE   PPPPP     PPPPP        IIIII        CCCCC                    RRRRR     RRRRR   PPPPP     PPPPP   GGGGG   GGGGGGG")
print("EEEEEEEEEEEEEEE   PPPPPPPPPPPPPPP        IIIII        CCCCC                    RRRRR     RRRRR   PPPPPPPPPPPPPPP   GGGGG   GGGGGGG")
print("EEEEE             PPPPPPPPPPPPPPP        IIIII        CCCCC                    RRRRRRRRRRRRRR    PPPPPPPPPPPPPPP   GGGGG     GGGGG")
print("EEEEE             PPPPP                  IIIII        CCCCC                    RRRRRRRRRRRRR     PPPPP             GGGGG     GGGGG")
print("EEEEEEEEEEEEEEE   PPPPP             IIIIIIIIIIIIIII   CCCCCCCCCCCCCCC          RRRRR   RRRRRR    PPPPP             GGGGGGGGGGGGGGG")
print("EEEEEEEEEEEEEEE   PPPPP             IIIIIIIIIIIIIII   CCCCCCCCCCCCCCC          RRRRR     RRRRR   PPPPP              GGGGGGGGGGGGG ")


print("                                                                 By: Aidan Andersen")
stall=input("                                                              Press Enter To Continue ")

#This part of the code creates a class for all of the fighter values, special moves and items.
class Fighterstats:
    def __init__(self, name, hp, mp, speed, power, defense, spc):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.speed= speed
        self.power = power
        self.defense = defense
        self.spc = spc
class SpecialMoves:
    def __init__(self, movename, damage, effect, mpcost):
        self.movename = movename
        self.damage = damage
        self.effect = effect
        self.mpcost = mpcost
class Items:
    def __init__(self, itemname, description, damage, effect):
        self.itemname = itemname
        self.description = description
        self.damage = damage
        self.effect = effect

#This portion of the code is the stats/Moves for all of the characters
BaseBadStats = Fighterstats("Badguy", 200, 15, 10, 30, 3, 0)
BaseGoodStats = Fighterstats("Raymond", 200, 15, 10, 30, 3, 1)
rayheal = SpecialMoves("Health Snap", 100, 'heal', 3)
GoodSpecial=[rayheal]
BadSpecial=[]
itemlist=[]
turnender=[]
crackers = Items("Crackers", "Yummy crackers that restore 10 MP", 10, 'mpheal')
fruitsnacks = Items("Fruitsnacks", "Tasty bundles of pure sugar that heal 150 HP", 150, 'heal')
itemlist= [crackers, fruitsnacks]


while True:
    try:
        os.system('cls')
        extract = open('epicfightdata.txt', 'r')
        extract.close()
        break
    except FileNotFoundError:
        os.system('cls')
        error=input('No Save Data, Creating Files')
        extract = open('epicfightdata.txt', "w+")
        extract.write('BaseGoodStats.txt\n')
        extract.write('BaseBadStats.txt\n')
        extract.write('items.txt')
        extract.close()

        extract = open('BaseGoodStats.txt',"w+")
        extract.write(BaseGoodStats.name+', ')
        extract.write(str(BaseGoodStats.hp)+', ')
        extract.write(str(BaseGoodStats.mp)+', ')
        extract.write(str(BaseGoodStats.speed)+', ')
        extract.write(str(BaseGoodStats.power)+', ')
        extract.write(str(BaseGoodStats.defense)+', ')
        extract.write(str(BaseGoodStats.spc)+'\n')
        extract.write(str(rayheal.movename)+', ')
        extract.write(str(rayheal.damage)+', ')
        extract.write(str(rayheal.effect)+', ')
        extract.write(str(rayheal.mpcost))
        extract.close()

        BaseBadStats = Fighterstats("Johnny", 500, 15, 10, 40, 6, 1)
        BadSpecial = SpecialMoves("Epic Shredder!", BaseBadStats.power, 'hurt', 4)
        GoodSpecial=[rayheal]
        extract = open('BaseBadStats.txt',"w+")
        extract.write(BaseBadStats.name+', ')
        extract.write(str(BaseBadStats.hp)+', ')
        extract.write(str(BaseBadStats.mp)+', ')
        extract.write(str(BaseBadStats.speed)+', ')
        extract.write(str(BaseBadStats.power)+', ')
        extract.write(str(BaseBadStats.defense)+', ')
        extract.write(str(BaseBadStats.spc)+'\n')
        extract.write(str(BadSpecial.movename)+', ')
        extract.write(str(BadSpecial.damage)+', ')
        extract.write(str(BadSpecial.effect)+', ')
        extract.write(str(BadSpecial.mpcost))
        extract.close()

        extract = open('items.txt',"w+")
        extract.write('\n')
        for p in range(len(itemlist)):
            extract = open('items.txt',"a+")
            extract.write(itemlist[p].itemname+', ')
            extract.write(itemlist[p].description+', ')
            extract.write(str(itemlist[p].damage)+', ')
            extract.write(itemlist[p].effect+' \n')
            extract.close()
        print('Files Created')
    else:
        pass
custominput=input("Would you like to select different files for the battle? Y/N: ").upper()
#This grabs the data from the various files
maininsert = open('epicfightdata.txt', 'r')
grab1= maininsert.readline()
grab2= maininsert.readline()
grab3= maininsert.readline()
maininsert.close()
if custominput == "Y":
    while custominput == "Y":
        BaseGoodStats=[]
        GoodSpecial=[]
        #Raymond Stats/Moves
        os.system('cls')
        print("What file do you want to change")
        print("1: GoodSide File")
        print("2: BadSide File")
        print("3: Item File")
        print("4: Check File Names")
        print("5: Done")
        filechanger= input("Choose: ").strip()
        if filechanger == '1':
            while True:
                try:
                    os.system('cls')
                    grab1=input("What is the file of the GoodSide called?: ")
                    test = open(grab1, 'r')
                    test.close()
                    break
                except FileNotFoundError:
                    os.system('cls')
                    error=input('Error file not found')
        elif filechanger == '2':
            while True:
                try:
                    os.system('cls')
                    grab2=input("What is the file of the BadSide called?: ")
                    test = open(grab2, 'r')
                    test.close()
                    break
                except FileNotFoundError:
                    os.system('cls')
                    error=input('Error file not found')
        elif filechanger == '3':
            while True:
                try:
                    os.system('cls')
                    grab3=input("What is the Item file called?: ")
                    test = open(grab3, 'r')
                    test.close()
                    break
                except FileNotFoundError:
                    os.system('cls')
                    error=input('Error file not found')
        elif filechanger == '4':
            #This is where the rest of the code will go to save and stuff
            os.system('cls')
            grab1=grab1.replace('\n','')
            grab2=grab2.replace('\n','')
            grab3=grab3.replace('\n','')
            grab1=grab1.replace('.txt','.txt\n')
            grab2=grab2.replace('.txt','.txt\n')
            grab3=grab3.replace('.txt','.txt\n')
            print(grab1,grab2,grab3)
            stall=input("")
        elif filechanger == '5':
            #This streamline all the files to be formatted the same
            os.system('cls')
            grab1=grab1.replace('\n','')
            grab2=grab2.replace('\n','')
            grab3=grab3.replace('\n','')
            grab1=grab1.replace('.txt','.txt\n')
            grab2=grab2.replace('.txt','.txt\n')
            grab3=grab3.replace('.txt','.txt\n')
            break
        else:
            pass

while True:
    try:
        maininsert = open('epicfightdata.txt', 'w+')
        maininsert.close()
        maininsert = open('epicfightdata.txt', 'a+')
        for check in range(3):
            if check == 0:
                maininsert.write(grab1)
            elif check == 1:
                maininsert.write(grab2)
            elif check == 2:
                    maininsert.write(grab3)
            else:
                pass
        maininsert.close()
        grab1= grab1.replace('\n','')
        grab2= grab2.replace('\n','')
        grab3= grab3.replace('\n','')
        break
    except FileNotFoundError:
        os.system('cls')
        error=input('Error file not found')

#This is Goodside's Stats Code
insert = open(grab1, 'r')
insertstuff = insert.readline().split(',')
BaseGoodStats=[]
BaseGoodStats.append(insertstuff[0])
for m in range(1,7):
    BaseGoodStats.append(int(insertstuff[m].replace('\n','')))
BaseGoodStats= Fighterstats(BaseGoodStats[0].strip(),BaseGoodStats[1],BaseGoodStats[2],BaseGoodStats[3],BaseGoodStats[4],BaseGoodStats[5],BaseGoodStats[6])
#Goodside's Special Move Code
GoodSpecial=[]
for m in range(BaseGoodStats.spc):
    iteminsert=[]
    insertstuff = insert.readline().split(',')
    iteminsert.append(insertstuff[0].strip())
    iteminsert.append(int(insertstuff[1]))
    iteminsert.append(insertstuff[2].strip())
    iteminsert.append(int(insertstuff[3].replace('\n','')))
    iteminsert= SpecialMoves(iteminsert[0],iteminsert[1],iteminsert[2],iteminsert[3])
    GoodSpecial.append(iteminsert)


insert = open(grab2, 'r')
insertstuff = insert.readline().split(',')
#This is code for the Badside stats
BaseBadStats=[]
BadSpecial=[]
BaseBadStats.append(insertstuff[0])
for m in range(1,7):
    BaseBadStats.append(int(insertstuff[m].replace('\n','')))
BaseBadStats= Fighterstats(BaseBadStats[0].strip(),BaseBadStats[1],BaseBadStats[2],BaseBadStats[3],BaseBadStats[4],BaseBadStats[5],BaseBadStats[6])
for m in range(BaseBadStats.spc):
    insertstuff = insert.readline().split(',')
    BadSpecial.append(insertstuff[0].strip())
    BadSpecial.append(int(insertstuff[1]))
    BadSpecial.append(insertstuff[2].strip())
    BadSpecial.append(int(insertstuff[3].replace('\n','')))
BadSpecial= SpecialMoves(BadSpecial[0],BadSpecial[1],BadSpecial[2],BadSpecial[3])
BadSide = BaseBadStats
BadSpecial = [BadSpecial]

#There are all the items used in the game
insert = open(grab3, 'r')
stall = insert.readline()
itemlist=[]
for m in range(2):
    iteminsert = []
    insertstuff = insert.readline().split(',')
    iteminsert.append(insertstuff[0].strip())
    iteminsert.append(insertstuff[1].strip())
    iteminsert.append(int(insertstuff[2]))
    iteminsert.append(insertstuff[3].strip().replace('\n',''))
    iteminsert = Items(iteminsert[0],iteminsert[1],iteminsert[2],iteminsert[3])
    itemlist.append(iteminsert)
#This part of the code is what the player does during the duration of their turn

#This is the fight code
def fight1(GoodSide, BadSide):
    os.system('cls')
    BadSide.hp = (BadSide.hp-(GoodSide.power-BadSide.defense))
    print("You attacked",BadSide.name+", they took", (GoodSide.power-BadSide.defense), "damage")
    stall=input("")

#This is the special move selectin code    
def special2(GoodSide, BadSide):
    a = 1
    while a == 1:
        os.system('cls')
        for p in range(len(GoodSpecial)):
            print(str(p+1)+':', str(GoodSpecial[p].movename), ':', str(GoodSpecial[p].mpcost)+'MP')
        print(str(p+2)+(": <-- Back"))
        print('\n',str(GoodSide.mp)+"/"+str(BaseGoodStats.mp),'MP')
        specialchoice=input("\nPick a special move: ")
        if specialchoice == str(len(GoodSpecial)+1):
            break
        elif specialchoice > str(len(GoodSpecial)+1):
            pass
        elif specialchoice <= str(0):
            pass
        else:
            if GoodSide.mp-rayheal.mpcost >= 0:
                if GoodSpecial[int(specialchoice)-1].effect == 'damage':
                    os.system('cls')
                    print("You used", GoodSpecial[int(specialchoice)-1].movename,", you did", GoodSpecial[int(specialchoice)-1].damage, 'damage')
                    GoodSide.hp = GoodSide.hp - GoodSpecial[int(specialchoice)-1].damage
                    GoodSide.mp = GoodSide.mp - GoodSpecial[int(specialchoice)-1].mpcost
                    turnender.append('END')
                    stall = input("")
                elif GoodSpecial[int(specialchoice)-1].effect == 'heal':
                    os.system('cls')
                    print("You used", GoodSpecial[int(specialchoice)-1].movename+", you healed", GoodSpecial[int(specialchoice)-1].damage, 'HP')
                    GoodSide.hp = rayheal.damage+GoodSide.hp
                    GoodSide.mp = GoodSide.mp - rayheal.mpcost
                    turnender.append('END')
                    stall = input("")
            else:
                os.system('cls')
                print("Not Enough MP")
                stall= input('')
            break

#The Item Selection Code
def items3(GoodSide, BadSide, turn):
    os.system('cls')
    c=1
    while c == 1:
        os.system('cls')
        for p in range(len(itemlist)):
            print(str(p+1)+':', itemlist[p].itemname, '-', itemlist[p].description)
        print(str(len(itemlist)+1)+": <-- Back")
        itemchoice=input("\nPick an item: ")
        if itemchoice == str(len(itemlist)+1):
            break
        elif itemchoice > str(len(itemlist)+1):
            pass
        elif itemchoice <= str(0):
            pass
        else:
            os.system('cls')
            #This part of the code controls how the various items work
            if itemlist[int(itemchoice)-1].effect == 'heal':
                print('The', itemlist[int(itemchoice)-1].itemname, 'healed', itemlist[int(itemchoice)-1].damage, "HP.")
                GoodSide.hp += itemlist[int(itemchoice)-1].damage
                itemlist.pop(p)
                turnender.append('END')

            elif itemlist[int(itemchoice)-1].effect == 'mpheal':
                print('The', itemlist[int(itemchoice)-1].itemname, 'restored', itemlist[int(itemchoice)-1].damage, "MP.")
                GoodSide.mp += itemlist[int(itemchoice)-1].damage
                itemlist.pop(p)
                turnender.append('END')

            elif itemlist[int(itemchoice)-1].effect == 'damage':
                print("TRY LATER")
            food=input('')
            turn='b'
            break

def battle(GoodSide, BadSide):
    if GoodSide.speed >= BadSide.speed:
        turn = 'g'
    else:
        turn = 'b'
    #Start game loop here
    gameloop=1
    while gameloop==1:
        os.system('cls')
        if BadSide.hp <= 0:
            print("You Win!")
            break
        elif GoodSide.hp <= 0:
            print("GAME OVER")
            break
        else:
            pass
        if GoodSide.hp > BaseGoodStats.hp:
            GoodSide.hp = BaseGoodStats.hp
        if GoodSide.mp > BaseGoodStats.mp:
            GoodSide.mp = BaseGoodStats.mp

        #This is the code for the players fighting selection
        if turn == 'g':
            u = 1
            while u == 1:
                os.system('cls')
                print('1: Fight')
                print("2: Special")
                print("3: Item")
                print("4: Defend")
                print("\nHP:", GoodSide.hp,"       ", BadSide.name+":",BadSide.hp)
                print("MP:", GoodSide.mp)
                optionselect=input("\nChoose: ").capitalize()
                if optionselect == "1" or optionselect == "Fight":
                    fight1(GoodSide, BadSide)
                    turn='b'
                    break
                elif optionselect == "2" or optionselect == "Special":
                    special2(GoodSide, BadSide)
                    if len(turnender) == 1:
                        turn='b'
                        break
                elif optionselect == "3" or optionselect == "Item":
                    print("Yay 3")
                    items3(GoodSide, BadSide, turn)
                    if len(turnender) == 1:
                        turn = 'b'
                        break
                    break
                elif optionselect == "4" or optionselect == "Defend":
                    os.system('cls')
                    GoodSide.defense = GoodSide.defense*3                   
                    stall=input("You defended! (Your defense tripled) ")
                    turn='b'
                    break
                else:
                    os.system('cls')
                    stall= input("\n\n\nChoice invalid ")

    #Code for the Badside's Turn
        elif turn == 'b':
            os.system('cls')
            if len(turnender) == 1:
                turnender.pop(0)
            badchose=random.randint(1,2)
            if badchose == 1:
                DamageTaken = (BadSide.power-GoodSide.defense)
                if DamageTaken < 0:
                    DamageTaken=0
                GoodSide.hp = GoodSide.hp-DamageTaken
                print(BadSide.name,"attacked you, you took", DamageTaken, "damage")
            elif badchose == 2:
                badchose=random.randint(1,2)
                DamageTaken = (BadSide.power-GoodSide.defense)
                if DamageTaken < 0:
                    DamageTaken=0
                GoodSide.hp = GoodSide.hp-DamageTaken
                print(BadSide.name, "used", BadSpecial[0].movename+',', 'You took', DamageTaken, "damage!")
            stall=input("")
            GoodSide.defense = BaseGoodStats.defense
            turn='g'

while True:
    try:
        os.system('cls')
        MG=input('How many battles do you want to have?: ')
        if MG == '':
            MG=1
        MG=int(MG)
        break
    except ValueError:
        os.system('cls')
        error=input('Error! Not a number')
Count=0
for x in range(MG):
    GoodSide=BaseGoodStats
    BadSide=BaseBadStats
    GoodSide = Fighterstats(GoodSide.name,GoodSide.hp,GoodSide.mp,GoodSide.speed,GoodSide.power,GoodSide.defense,GoodSide.spc)
    BadSide = Fighterstats(BadSide.name,BadSide.hp,BadSide.mp,BadSide.speed,BadSide.power,BadSide.defense,BadSide.spc)
    battle(GoodSide, BadSide)
    Count+=1
    input("\nHit ENTER to begin next Battle!")
end=input("\n\nThis is the end of the code")
