import division as dv

MAP_WIDTH = 15
MAP_LENGTH = 15
NORNAME = "Empire of Japan"
SOUTHNAME = "Senatus Populusque Romanus"
CHOICE_LIST = ["Q","Move","Attack","Defence"]

warmap = {}
upmil = {}
downmil = {}
sucess = False
turn = 0

for i in range(MAP_WIDTH):
    for d in range(MAP_LENGTH):
        warmap[(i , d)] = "".ljust(6)



def print_map():
    print("                        {0} Side".format(NORNAME))
    for i in range(MAP_WIDTH):
        print("   {0}".format(str(i + 1).ljust(4)), end = "")
    print(" ")
    print("┌──────┬", end = "")
    for i in range(MAP_WIDTH - 1):
        print("──────┬", end = "")
    print("──────┐")
    for d in range(MAP_LENGTH - 1):
        for i in range(MAP_WIDTH):
            print("│{0}".format(warmap[(i , d)]), end = "")
        print("│  {0}│".format(str(d + 1).ljust(4)))
        print("├", end = "")
        for i in range(MAP_WIDTH):
            print("──────┼", end = "")
        print("──────┤")
    for i in range(MAP_WIDTH):
        print("│{0}".format(warmap[(i , MAP_LENGTH - 1)]), end = "")
    print("│  {0}│".format(str(MAP_LENGTH).ljust(4)))
    print("└", end = "")
    for i in range(MAP_WIDTH):
        print("──────┴", end = "")
    print("──────┘")
    for i in range(MAP_WIDTH):
        print("   {0}".format(str(i + 1).ljust(4)), end = "")
    print("")    
    print("                      {0} Side".format(SOUTHNAME))



def init_mil(file):
    switch = 0
    i = 0
    r = 0
    for lines in file:
        if lines.startswith("-"):
            we_temp = lines.split()
            if switch == 0:
                we_temp[1] = "N_" + we_temp[1]
                upmil[we_temp[1]] = dv.division(we_temp[1] , name_temp , NORNAME , we_temp[2:])
            else:
                we_temp[1] = "S_" + we_temp[1]
                downmil[we_temp[1]] = dv.division(we_temp[1] , name_temp , SOUTHNAME , we_temp[2:])
        elif lines.rstrip == "":
            break
        elif not lines.rstrip() == "S.W.I.T.C.H":
            name_temp = lines.rstrip()
        else:
            switch = 1
    for identity in upmil:
        if i > MAP_WIDTH - 1:
            r += 1
        warmap[(i , r)] = upmil[identity].id.ljust(6)
        upmil[identity].set_location(i , r) 
        i += 1
    i = MAP_WIDTH - 1
    r = MAP_LENGTH - 1
    for identity in downmil:
        if i < 0:
            r -= 1
        warmap[(i , r)] = downmil[identity].id.ljust(6)
        downmil[identity].set_location(i , r) 
        i -= 1
    


def game_input(side):
    choice = ""
    correctunit = False 
    print("───────────────────────────────────────────────")
    print("We will be printing your division information")
    useless = input("Press any Key to continue")
    move_list = []
    doing_list = []
    if side == NORNAME:
        for unit in upmil:
            print("───────────────────────────────────────────────")
            for lines in upmil[unit].info_get():
                print(lines)
        print("───────────────────────────────────────────────")
    else:
        for unit in downmil:
            print("───────────────────────────────────────────────")
            for lines in downmil[unit].info_get():
                print(lines)
        print("───────────────────────────────────────────────")
    print("If you're wishing to combine unit, Please input C now")
    print("Otherwise press Any Key")
    combine = input("")
    if combine.lower() == "c":
        game_combine(side)
    while not choice == "Q" or not choice in CHOICE_LIST or not correctunit:
        print("───────────────────────────────────────────────" )
        print("Its {0}'s Leader's Term! Leads your army now!".format(side))
        for ch in CHOICE_LIST:
            print(ch , " " , end="")
        print("")
        choice = input(">>>>")
        if not choice == "Q":
            print("Choose the Corresponding Military Group From above")
            correctunit = input(">>>>")
            if correctunit in doing_list and not choice == "Move":
                correctunit == False
            elif side == NORNAME:
                unitid = correctunit
                correctunit = upmil.get(correctunit , False)
            else:
                unitid = correctunit
                correctunit = downmil.get(correctunit , False)
            if correctunit == False:
                print("NOT_A_CHOICE , Please return")
        else:
            correctunit = True
        if not choice in CHOICE_LIST:
            print("NOT_A_CHOICE , Please return")
        elif correctunit:
            if choice == "Defence":
                correctunit.defence_change()
                if correctunit.defence:
                    print("Now {0} is in Fortification".format(self.name))
                else:
                    print("Now {0} is leaving its Fortress".format(self.name))
                doing_list.append(unitid)
            elif choice == "Attack":
                game_attack(side , correctunit)
            elif choice == "Move":
                if correctunit.defence:
                    print("Sorry, Military in Fortress are not allowed to move. Please Try again")
                elif unitid in move_list:
                    print("Sorry, This Division has move in this round.")
                else:
                    (cux , cuy) = correctunit.location
                    cuxw = cux - 1
                    cuxe = cux + 1
                    cuyn = cuy - 1
                    cuys = cuy + 1
                    roundcount = 0
                    if cuxe == MAP_WIDTH:
                        if not warmap[(cuxw , cuy)] == "".ljust(6):
                            roundcount += 2
                        else:
                            roundcount += 1
                    else:
                        if cuxw == -1:
                            if not warmap[(cuxe , cuy)] == "".ljust(6):
                                roundcount += 2
                            else:
                                roundcount += 1
                        else:
                            if warmap[(cuxe , cuy)] == "".ljust(6):
                                roundcount += 1
                            if warmap[(cuxw , cuy)] == "".ljust(6):
                                roundcount += 1
                    if cuys == MAP_LENGTH:
                        if not warmap[(cux , cuyn)] == "".ljust(6):
                            roundcount += 2
                        else:
                            roundcount += 1
                    else:
                        if cuyn == -1:
                            if not warmap[(cux , cuys)] == "".ljust(6):
                                roundcount += 2
                            else:
                                roundcount += 1
                        else:
                            if warmap[(cux , cuyn)] == "".ljust(6):
                                roundcount += 1
                            if warmap[(cux , cuys)] == "".ljust(6):
                                roundcount += 1
                    if roundcount == 4:
                        print("Sorry , The current unit is being rounded, please select another one")
                    else:
                        game_move(correctunit)
                        move_list.append(unitid)





def game_attack(side , unit):
    good = False
    while not good:
        print("Please input the ENEMY you want {0} to attack!".format(unit.id))
        print("If you figure out you choose the wrong military, input Q")
        enemy = input(">>>>")
        if enemy == "Q":
            break
        if side == NORNAME:
            enemy = downmil.get(enemy , False)
        else:
            enemy = upmil.get(enemy , False)
        if enemy:
            if dist_cal(unit , enemy.location) == 2:
                if unit.type == "Artillery":
                    good = True
                    unit.attack(enemy , "artillery")
                else:
                    print("Sorry, You're not close enough. Please Try again")
            elif dist_cal(unit , enemy.location) == 1:
                good = True
                if unit.defence:
                    unit.attack(enemy , "defence")
                    enemy.attack(unit , "strike_back")
                else:
                    (x1 , y1) = unit.location
                    (x2 , y2) = enemy.location
                    if not y1 == y2 and ((y1 - y2) / abs(y1 - y2)) == enemy.back:
                        unit.attack(enemy , "outflank")
                    else:
                        unit.attack(enemy , "normal")
                        enemy.attack(unit , "strike_back")
            else:
                print("Sorry, You're not close enough. Please Try again")
        else:
            print("Incorrect Unit Name. Try Agian")
    if not enemy == "Q":
        print("───────────────────────────────────────────────")
        print("War Between {0} and {1}".format(unit.id , enemy.id))
        print("Here is the Result : ")
        print("──────────────────Attack Side──────────────────")
        for lines in unit.info_get():
            print(lines)
        print("─────────────────Defence Side──────────────────")
        for lines in enemy.info_get():
            print(lines)
        print("───────────────────────────────────────────────")
        if enemy.type == "Dead":
            if side == NORNAME:
                del downmil[enemy.id]
            else:
                del upmil[enemy.id]
            warmap[enemy.location] = "".ljust(6)
            print("We are sorry to announce that the Division {0} is dead".format(enemy.id))
        if unit.type == "Dead":
            if side == NORNAME:
                del upmil[unit.id]
            else:
                del downmil[unit.id]
            warmap[unit.location] = "".ljust(6)    
            print("We are sorry to announce that the Division {0} is dead".format(unit.id))    
    
 










def game_move(correctunit):
    good = False
    while not good:
        print("Please input the location you would like {0} to go".format(correctunit.id))
        x = int(input("The X-Coordinate:"))
        y = int(input("The Y-Coordinate:"))
        x -= 1
        y -= 1
        if x < MAP_WIDTH and y < MAP_LENGTH and dist_cal(correctunit , (x , y)) <= correctunit.move and x >= 0 and y >= 0 and warmap[(x , y)] == "".ljust(6):            
            good = True
            print("You've sucessfully move {0} to {1},{2}!".format(correctunit.id , x + 1 , y + 1))
            (c , d) = correctunit.location
            warmap[(c , d)] = "".ljust(6)
            if not y == d:
                correctunit.set_back((y - d) / abs(y - d))
            else:
                correctunit.set_back(0)
            correctunit.set_location(x , y)
            warmap[(x , y)] = correctunit.id.ljust(6)
        else:
            print("FAIL_ON_MOVE, Please return")

        
    
 

        


    



def game_combine(side):
    print("Remark : Due to the lasyness of some one")
    print("You have only 1 chance to sucess combine")
    first = input("Please input the codename of the main division\n>>>>")
    second = input("Please input the codename of the division being combined\n>>>>") 
    if side == NORNAME:
        first_div = upmil.get(first , False)
        second_div = upmil.get(second , False)
        if first_div and second_div and dist_cal(first_div , second_div.location) == 1:
            first_div.combine(second_div)
            warmap[second_div.location] = "".ljust(6)
            del upmil[second_div]
            print("Sucess Combine!")
            return None
    elif side == SOUTHNAME:
        first_div = downmil.get(first , False)
        second_div = downmil.get(second , False)
        if first_div and second_div and dist_cal(first_div , second_div.location) == 1:
            first_div.combine(second_div)
            warmap[second_div.location] = "".ljust(6)
            del downmil[second_div]
            print("Sucess Combine!")
            return None
    print("Combine Insucessfull")
         
        






def dist_cal(unit , point):
    (x1 , y1) = unit.location
    (x2 , y2) = point
    return abs(x1 - x2) + abs(y1 - y2)







if __name__ == "__main__":
    
    print("======='WAR' Start now=======")
    print("==Press any key to continue==")
    print("\nIf you can't find the any key on the keybord\nPlease consult your computer factory")
    useless = input()
    print("Please type in the name of the file where division information is stored")
    print("The way the file is organized is strictly controled")
    print("Default name: mill.txt")
    name = input()
    file = open(name)
    init_mil(file)
    
    
    while not sucess:
        turn += 1
        print("\n\n\nTurn {0}\n\n".format(turn))
        print_map()
        
        if turn % 2 == 0:
            game_input(NORNAME)
        else:
            game_input(SOUTHNAME)
        if upmil == {}:
            sucess = True
            print("───────────────────────────────────────")
            print("Game Over in {0} turns")
            print("The Greate {0} Win the War!".format(SOUTHNAME))
        elif downmil == {}:
            sucess = True
            print("───────────────────────────────────────")
            print("Game Over in {0} turns")
            print("The Greate {0} Win the War!".format(NORNAME))

    useless = input()
