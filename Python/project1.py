import random
def get_guess():
    return list(input("What is your guess : "))

def generate_code():
    digit = [str(num) for num in range(10)]
    
    random.shuffle(digit)
    return digit[:3]

def generate_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED"
    
    clues = []
    
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues == []:
        return ["Nope"]
    else:
        return clues
    

print("Welcome code breaker ")

secrete_code = generate_code()

clue_report = []
while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = generate_clues(guess,secrete_code)
    print("here is the result of your guess : ")
    for clue in clue_report:
        print(clue)