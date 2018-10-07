
import time
import random
class Number_game():
    def __heart(self):
        heart=str(input("do you want to play this game y/n:"))
        return heart
    def __random_number(self):
        
        random_number=random.randint(1,2000)
        return random_number
    def __guess_number(self):
        guess_number=int(input("guess a number:"))
        return guess_number
    def __show(self,t1,t2):
        print("you are so smart")
        print("you spend %s ms"%(t2-t1))    
    def go(self):
        
        t1=time.time()
        while True:
            heart=self.__heart() 
            if heart=="y":
                random_number=self.__random_number()
                guess_number=self.__guess_number()
                try:
                    while True:
                        if random_number<guess_number:
                            guess_number=int(input("guess a smaller number:"))
                        elif random_number>guess_number:
                            guess_number=int(input("guess a bigger number:"))
                        else:
                            t2=time.time()
                            self.__show(t1,t2)
                            break
                except:
                    print("input a number")
               
            else:
                print("sb")
                break
number_game=Number_game()
number_game.go()                
