#Game:  multiplication table
# start , end ---> multiplication table [start:end]

'''
start= int(input("Enter Start: ")) #cast
end= int(input("Enter Start: "))
for x in range(start,end+1):
    for y in range(1,11):
        print(f"{x} * {y} = {x*y}")
    print("----------------------") 


#Improve Game:  multiplication table As a function
#  start , end ---> multiplication table [start:end] 

def mul_table(start,end,mstart=1,mstop=10):
    for x in range(start,end+1):
        for y in range(mstart,mstop+1):
            print(f"{x} * {y} = {x*y}")
        print("----------------------")

        
mul_table(2,6,2,20)


#Game:  count words
# sentence : count words
sentence= input('Enter Sentence: ')
print(len(sentence.split()))


#improve Game:  count words as a function

# sentence : count words
def count_words(sentence):
    word_count=len(sentence.split())
    return word_count

sentence = "my name is mohammad"

print(count_words(sentence))
'''





# Improve games As OOP
'''
    Game:
        -print: welcome
        -game number
        -run game
'''

class Game:
    def __init__(self):
        while True:
            print('''
    Welcome In Our Game
        1:Multiplication Table Game
        2: Word count game
        3: press X to exit
    ''')
            
            user_choice= input("Enter Your Choice: ")
            if user_choice == 'X':
                break
            if int(user_choice) ==1:
                start= int(input("Enter Start: ")) #cast
                end= int(input("Enter Start: "))
                self.mul_table(start,end)

                
            elif int(user_choice) == 2:
                sentence= input('Enter Sentence: ')
                count=self.count_words(sentence)
                print(count)
            play_again= input("press any key to play again, N for exit")
            if play_again == 'N':
                break
                
    def mul_table(self,start,end,mstart=1,mstop=10):
        for x in range(start,end+1):
            for y in range(mstart,mstop+1):
                print(f"{x} * {y} = {x*y}")
            print("----------------------")
            

    def count_words(self,sentence):
        word_count=len(sentence.split())
        return word_count
    

g1= Game()













