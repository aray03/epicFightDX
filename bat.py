import os


def printPerson(charStat):
    print("-------------------")
    print("Name: ", charStat.name)
    print("HP: ", charStat.hp)
    print("MP: ", charStat.mp)
    print("Speed: ", charStat.speed)
    print("Power: ", charStat.power)    
    print("Defense: ", charStat.defense)
    print("Special Move Count: ", charStat.spc)
    print("-------------------")
    
    
def noSaveData(goodStat, goodSpecial, badStat, badSpecial, itemList):
    os.system('cls')
    error=input('No Save Data, Creating Files')
    extract = open('epicfightdata.txt', "w+")
    extract.write('goodStat.txt\n')
    extract.write('badStat.txt\n')
    extract.write('items.txt')
    extract.close()

    #  goodStat = Fighterstats("Johnny", 200, 15, 10, 30, 3, 1)
    extract = open('goodStat.txt',"w+")
    extract.write(goodStat.name+', ')
    extract.write(str(goodStat.hp)+', ')
    extract.write(str(goodStat.mp)+', ')
    extract.write(str(goodStat.speed)+', ')
    extract.write(str(goodStat.power)+', ')
    extract.write(str(goodStat.defense)+', ')
    extract.write(str(goodStat.spc)+'\n')
    
    for x in range(goodStat.spc):
        print(str(goodSpecial[0]))
    
        extract.write(str(goodSpecial[x].movename)+', ')
        extract.write(str(goodSpecial[x].damage)+', ')
        extract.write(str(goodSpecial[x].effect)+', ')
        extract.write(str(goodSpecial[x].mpcost)+'\n')
    extract.close()


    
    extract = open('badStat.txt',"w+")
    extract.write(badStat.name+', ')
    extract.write(str(badStat.hp)+', ')
    extract.write(str(badStat.mp)+', ')
    extract.write(str(badStat.speed)+', ')
    extract.write(str(badStat.power)+', ')
    extract.write(str(badStat.defense)+', ')
    extract.write(str(badStat.spc)+'\n')
    
    for x in range(badStat.spc):
        print(str(badSpecial[0]))
    
        extract.write(str(badSpecial[x].movename)+', ')
        extract.write(str(badSpecial[x].damage)+', ')
        extract.write(str(badSpecial[x].effect)+', ')
        extract.write(str(badSpecial[x].mpcost)+'\n')
    extract.close()
    extract = open('items.txt',"w+")
    extract.write('\n')
    
    extract = open('items.txt',"w+")
    extract.write('\n')
    for p in range(len(itemList)):
        extract = open('items.txt',"a+")
        extract.write(itemList[p].itemname+', ')
        extract.write(itemList[p].description+', ')
        extract.write(str(itemList[p].damage)+', ')
        extract.write(itemList[p].effect+' \n')
        extract.close()
    print('Files Created')
    
    
    
    
    
    
    
def gameEditor(grab1, grab2, grab3):
    custominput=input("Would you like to select different files for the battle? Y/N: ").upper()
    #This grabs the data from the various files
    
    
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

def printFightMenu(currentPos):
    os.system('cls')
    
    if (currentPos == 1):
        print('> 1: Fight')
        print("  2: Special")
        print("  3: Item")
        print("  4: Defend")
    elif (currentPos == 2):
        print('  1: Fight')
        print("> 2: Special")
        print("  3: Item")
        print("  4: Defend")
    elif (currentPos == 3):
        print('  1: Fight')
        print("  2: Special")
        print("> 3: Item")
        print("  4: Defend")
    elif (currentPos == 4):
        print('  1: Fight')
        print("  2: Special")
        print("  3: Item")
        print("> 4: Defend")
        