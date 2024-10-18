class Player:
    __name = ''
    __stocks = []
    __dividend = 0
    def __init__(self, name:str):
        '''Creating Player; 
        name: player name(str)'''
        self.name = name
    
    
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
    __name = ''
    __price = 0
    __availableShares = 0
    __majorityHolder = ''
    def __init__(self, name:str, price:int):
        '''Creating Company; 
        name: company name (str)
        price: company price (int)
        '''
        self.name = name
        self.price = price
        
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
    #-------------------------------------#       



#TESTING
#-------------------------------------#        
boots = Player("Boots")
print(boots)
#-------------------------------------#        

