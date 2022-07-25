import random

num = 3
max_guess = 10



def get_secret_no():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_no = ''
    for i in range(num):
        secret_no +=(str(numbers[i])) 
        return secret_no

def clues(guess, secret_no):
    if guess == secret_no:
        return 'you won'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_no[i]:
            clues.append("fermi")
        elif guess[i] in secret_no:
            clues.append("pico")
    if len(clues) == 0:
        return 'bagles'
    else:
        clues.sort()
        return ''.join(clues)




def main():
    print("-------guess game-------\n")
    print("pico -> 1 dig is correct but at wrong position \n ")
    print("fermi -> 1 dig is correct and wright position \n")
    print("bangles -> no degit is correct \n")

    secret_no = get_secret_no()

    
    while True:
        print("number genrated\n")
        print("you have -> ",max_guess ," gusses." )
        
        numGuess = 1
        guess = ''
        while len(guess) != num or guess.isdecimal() :
            guess = input('>')
        
            clues = clues(guess , secret_no)
            print(clues)
            numGuess += 1

            if guess == secret_no:
                break

            if numGuess > max_guess:
                print('you ran out of gusses...')
                print("answer was > ", secret_no)
        print("do you want to continue :")
        y = input("y/n")
        if y !='y':  
            break





main()