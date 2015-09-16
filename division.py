ATTACK = [40,40,0,200,20,20]
SUPATTACK = [0,20,55,20,60,80]
DEFENCE = [0,0,0,10,45,70] 
LIFE = [50,150,150,100,300,500]
MOV_A = 2
MOV_E = 4
MOV_F = 3
TYPE_ATTACK = {"strike_back":0.3 , "outflank":2 , "artillery":0.8 , "defence":1.6}


class division(object):

    def __init__(self , identity , fullname , belong , squad):
        '''(str , str , list of 6 int) -> NoneType
        Initialize the division
        '''
        self.id = identity
        self.name = fullname
        self.belong = belong
        for i in range(len(squad)):
            squad[i] = int(squad[i])
        self.squad = squad
        self.type = ""
        self.location = 0
        self.move = 0
        self.back = 0
        self.defence = False
        self.typeget()

    def typeget(self):
        '''(division) -> NoneType
        Get the Type of division
        '''
        if not self.squad[3] == 0:
            self.type = "Artillery"
            self.move = MOV_A
        else:
            if self.squad[4] == 0 and self.squad[5] == 0:
                self.type = "Infantry"
                self.move = MOV_A
            elif self.squad[4] == 0:
                self.type = "Heavy Armored"
                self.move = MOV_F
            else:
                self.type = "Armored"
                self.move = MOV_E
        if self.squad == [0,0,0,0,0,0]:
            self.type = "Dead"



    def info_get(self):
        '''(division) - > list of str
        Division Information Get
        '''
        first = "{0} - {1} [{2}] , Type : {3}".format(self.belong , self.name , self.id , self.type)
        second = "Militia Squadron : " + str(self.squad[0])
        third = "Infantry Squadron : " + str(self.squad[1])
        forth = "Anti-Tank Infantry Squadron : " + str(self.squad[2])
        fifth = "Artillery Squadron : " + str(self.squad[3])
        sixth = "Main Battle Tank Squadron : " + str(self.squad[4])
        seventh = "Heavy Tank Squadron : " + str(self.squad[5])
        eighth = "--Fortification : " + str(self.defence) + "--"
        return [first , second , third , forth , fifth , sixth , seventh , eighth]


    def set_location(self , xcord , ycord):
        '''(division , int , int) -> Nonetype
        Set location of Division
        '''
        self.location = (xcord , ycord)


    def set_back(self , xdirection):
        '''(division , int , int) -> Nonetype
        Set back of Division
        '''
        self.back = xdirection


    def attack(self , enemy , attacktype):
        '''(division , division , str) -> Nonetype
        Attack counting'''
        constant = TYPE_ATTACK.get(attacktype, 1)
        attackvalue = 0
        supattackvalue = 0
        defence_base = 0
        defence_init = 0
        if not attacktype == "artillery":
            for i in range(len(self.squad)):
                attackvalue += self.squad[i] * ATTACK[i] * constant
                supattackvalue += self.squad[i] * SUPATTACK[i] * constant
        else:
            attackvalue = self.suqad[3] * ATTACK[3] * constant
            supattackvalue = self.squad[3] * SUPATTACK[3] * constant
        for i in range(len(enemy.squad)):
            defence_base += enemy.squad[i] * 100
            defence_init += enemy.squad[i] * DEFENCE[i]
        real_value = defence_init  * attackvalue / defence_base + supattackvalue
        for i in range(len(enemy.squad)):
              left_life = enemy.squad[i] * LIFE[i] - real_value
              enemy.squad[i] = round(left_life / LIFE[i])
              if enemy.squad[i] > 0:
                  break
              else:
                  enemy.squad[i] = 0
                  real_value = 0 - left_life
        self.typeget()
        enemy.typeget()


    def combine(self , another):
        for i in range(len(self.squad)):
            self.squad[i] += another.suqad[i]            
        self.typeget()

    def defence_change(self):
        self.defence = not self.defence
        self.back = 0
