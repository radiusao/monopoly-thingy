class Player:

   #initiate + instances
    def __init__(self, name:str):
        '''Creating Player; 
        name: player name(str)'''
        self.__name = name
        self.__stocks = []
        self.__dividend = 0
    
    
    #-------------------------------------#        
    #SETTER AND GETTER
    
    # Setter and getter for name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        else:
            self.__name = name
    #
    
    
    #Setter and getter for stock    
    @property
    def stocks(self):
        return self.__stocks
    
    @stocks.setter
    def stocks(self, stock):
        if not isinstance(stock, Company):
            raise TypeError('Stocks must be an object of Company.')
        else:
            #`stocks` is a list type
            #setting `stocks` will only appends `Company` to the list
            #to remove item use `remove_stock(`Company`)`
            self.__stocks.append(stock)
    #
    
    
    #Setter and getter for dividend // incomplete
    @property
    def dividend(self):
        # run `calculateDividend()` //incomplete
        #`calculateDividend()` will retun a int that will be set to self.__dividend
        # this will calculate the dividend everytime this properties is called
        return self.__dividend
    
    @dividend.setter
    def dividend(self, dividend): #just a back up; this might not be needed since calling `dividend` will automatically assign new dividend value
        if not isinstance(dividend, int):
            raise TypeError('Dividend must be a number.')
        else:
            self.__dividend = dividend
    #
    #-------------------------------------#        
    
    
    #-------------------------------------#        
    #METHODS
            
    def remove_stock(self, stock): #removing stock from `__stocks` list
        if not stock in self.__stocks:
            raise ValueError('Stock does not exist.')
        else:
            self.__stocks.remove(stock)
                    
    def __str__(self):
        return f'name: {self.name}\nstocks: {self.stocks}\ndividend: {self.__dividend}'
    #-------------------------------------#        



class Company:
    
    #class attribute
    _groupBlock = [] #class attribute for groupBlock
    
    
    #initiate + instances
    def __init__(self, groupName:str, name:str, price:int):
        '''Creating Company; 
        groupName: company group (str)
        name: company name (str)
        price: company price (int)
        '''
        self.groupName = groupName
        self.__name = name
        self.__price = price
        self.__majorityHolder = ''
        self.__availableShares = 9
        
    #-------------------------------------#       
    #CLASS METHOD
    
    #Creating group for the block (e.g. yellow, green, etc...)
    @classmethod
    def createGroup(cls, groupName:str):
        cls._groupBlock.append(groupName)       
        cls._groupBlock.append([])       
         
    #     

    #-------------------------------------#        
    #SETTER AND GETTER
    
    #Setter and getter for name    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        else:
            self.__name = name
    #
    
    
    #Setter and getter for price    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError('Price must be a number.')
        else:
            self.__price = price
    #
    

    #Setter and getter for availableShares   
    @property
    def availableShares(self):
        return self.__availableShares

    @availableShares.setter
    def availableShares(self, availableShares):
        if not isinstance(availableShares, int):
            raise TypeError('AvailableShares must be a number.')
        else:
            self.__availableShares = availableShares
    #
    
    
    #Setter and getter for majorityHolder   
    @property
    def majorityHolder(self):
        return self.__majorityHolder
    
    @majorityHolder.setter
    def majorityHolder(self, player):
        if not isinstance(player, Player):
            raise TypeError('majorityHolder must be an object of Player.')
        else:
            self.__majorityHolder = player
    #
    
    
    #Setter and getter for groupName // incomplete
    @property
    def groupName(self):
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName): #// incomplete
        #check if group exist in `_groupBlock`
        #if exist append this object to `groupName.companyList[]`
        #else print group doesnt exist use Company(createGroup(groupName)) to create new group
        indexOfGroupName = self._groupBlock.index(groupName) + 1
        self._groupBlock[indexOfGroupName].append(self)
        print(self._groupBlock)
    #
       
    #-------------------------------------#       



#TESTING
#-------------------------------------#        
boots = Player("Boots")
print(boots)
#-------------------------------------#
#Company Test
Company.createGroup('Yellow')
leicesterSquare = Company('Yellow', 'Leicester Square', 100)

#-------------------------------------#        
        

