import random
class Saads_Guess_House:
    def __init__(self):
        self.alpha=random.choice('abcdefghijklmnopqrstuvwxyz')
        print('Guess an alphabet. You have 5 guesses only','\n','\t','**** Good Luck ****')
    def no_of_guesses(self):
        global x
        for x in range(1,6):
            global y
            y=input('enter the alphabet:')
            if y>self.alpha:
                print('you guess is high ')
            elif y<self.alpha:
                print('your guess is low ')
            else:
                break
    def end(self):
        if y==self.alpha:
            print('****you gotcha fam. The guesses you took:',x,'\n','Thanks for playing nigga.Sending a gift :) **** ')
        else:
            print('**** Thats it! Game over you lost ****')
g=Saads_Guess_House()
g.no_of_guesses()
g.end()