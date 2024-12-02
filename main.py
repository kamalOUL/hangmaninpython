import random
from random import choice


def spin_row():
    symbols =['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbols) for symbol in range(3)]
def print_row(row):
    print(" ".join(row))
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
      if row[0]=='🍒':
          return bet*3
      elif row[0]== '🍉':
          return bet*4
      elif row[0]== '🍋':
          return bet*4
      elif row[0]== '🔔':
          return bet*5
      elif row[0]=='⭐':
          return bet*6
    return 0

def main():
    balance = 100
    print("Welcome to Phyton slots ")
    while balance > 0:
        print(f"current balance is {balance}")
        bet= input("place your bet amount: ")
        if not bet.isdigit() :
            print("Please enter a numeric value")
        bet=int(bet)
        if bet>balance :
            print("You don't have enough money")
            continue
        if bet<=0:
            print("bet must be greater than 0")
            continue
        balance-=bet
        row = spin_row()
        print("spinning....\n")
        print_row(row)
        payout = get_payout(row,bet)
        if payout>0:
            print("congrats you won")
        else:
            print("you lost this spin")
        balance+=payout
        play_again = input("play again? (y/n): ").lower()
        if play_again != 'y':
          break
        print(f"Thank you for playing your final balance is {balance}")

if __name__ == '__main__':
    main()