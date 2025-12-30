# Slot Machine game in Python
import random
def row_spin():
    symbols = ["🍎","🎠","🥕","🍌","💠"]
    return [random.choice(symbols) for _ in range(3)]
    
def print_row(row):
    print("****************")
    print("|"," | ".join(row),"|")
    print("****************\n")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍎":
            return bet * 2
        elif row[0] == "🎠":
            return bet * 10
        elif row[0] == "🥕":
            return bet * 3
        elif row[0] == "🍌":
            return bet * 4
        elif row[0] == "💠":
            return bet * 20
    return 0
            
def main():
    balance = 100
    print("*****************************")
    print("** Welcome to Slot Machine **")
    print("*****************************")
    print()
    print ("Symbols: 🍎 🎠 🥕 🍌 💠")
    print()
    while balance > 0:
        print(f"\nYour Balance : ${balance} ")
        
        bet = input("Enetr your bet amount : $")
        
        if not bet.isdigit():
            print("Please Enter a valid amount !")
            continue
        
        bet = int(bet)
        
        if bet  >   balance:
            print("Insufficient Fund!")
            continue
        
        if bet <= 0:
            print("The amount should be greater than 0! ")
            continue
        
        balance -= bet
        
        row = row_spin()
        print("Spinning.....\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
            print(f"Your Bet was ${bet}")
        else:
            print("You lost!")
        balance += payout
        
        if balance == 0:
            print("Your Balance is empty !\nquiting......")
            break
        
        usr_inpt = input("Do you want to play again? (Y/N): ").upper()
        if usr_inpt == "Y":
            continue
        else:
            print("quiting....")
            break
        

if __name__ == '__main__':
    main()