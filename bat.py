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