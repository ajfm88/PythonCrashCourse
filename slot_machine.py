from random import choice

numbers = [1, 2, 3, 4, 5] #This is a list.

otherNumbers = (6, 7, 8, 9, 10) #This is a tuple.

sum = 0
count = len(numbers)

for index in range(count):
    sum += numbers[index]

people = {
    'Mike':'949-555-8412',
    'Steve':'949-555-0008',
    "Jess":"N/A"
}

SYMBOL_SET = ('7', '!', '$', '*', '?', '#')

THREE_OF_A_KIND = {
    "7": 2,
    "*": 1.5,
    "?": 1.5,
    "$": 3,
    "#": 1.5,
    "!": 0
}

TWO_OF_A_KIND = {
    "7": 50,
    "*": 10,
    "?": 10,
    "$": 100,
    "#": 10,
    "!": 0
}

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

def pow(a,b):
    return a ** b
    
def spin():
    symbol1 = choice(SYMBOL_SET)
    symbol2 = choice(SYMBOL_SET)
    symbol3 = choice(SYMBOL_SET)

    return (symbol1,symbol2,symbol3)

def evaluate(bet,spin):
    if spin.count('!') > 1:
        return 0
    else:
        for symbol in SYMBOL_SET:
            if spin.count(symbol) > 1:
                if spin.count(symbol) == 2:
                    return bet + TWO_OF_A_KIND[symbol]
                else:
                    return bet * THREE_OF_A_KIND[symbol]
        return 0

def slot_machine(bank=500):
    while True:
        print(f"Current Bank amount: ${bank}")
        bet = int(input("Please enter your bet: $"))
        bank -= bet
        result = spin()
        bank += evaluate(bet,result)
        winnings = evaluate(bet,result)
        print(result)
        if winnings > 0:
            print(f"Congratulations, you won ${winnings}!")
        else:
            print("Ohhhh, tough break!")