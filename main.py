import random

def russian_roulette():
    print("Welcome to Russian Roulette!")
    print("You are playing against the computer. Good luck!")
    
    chambers = [0, 0, 0, 0, 0, 1]  # 5 empty chambers, 1 bullet
    random.shuffle(chambers)  # Shuffle the chambers
    
    player_alive = True
    while player_alive:
        input("Press Enter to pull the trigger...")
        bullet = chambers.pop()  # Remove a chamber
        if bullet == 1:
            print("You're dead!")
            player_alive = False
        else:
            print("You survived!")
            if not chambers:
                print("You've survived all the chambers. You win!")
                break
            print("Next round...")
    
    print("Game over.")

if __name__ == "__main__":
    russian_roulette()
