#Players first input number of numbers they wanna play with (n)
#Next n rows is input of index in array and number it hold for first player
#Next n rows is same for second player

#Will eed chain later to find maximum int
from itertools import chain

def main():
    #Assigining points and dictionaries
    player_one_points = 0
    player_two_points = 0
    player_one_dict = {}
    player_two_dict = {}

    #Getting the number of elements in each dicitonary
    number_of_numbers = int(input("Enter the number if numbers players will guess"))

    #Just indicating that player one should insert his numbers
    print("Hey , player one! It's your turn to enter the numbers: ")

    #Populating the dicitonaries
    temp_counter = 0
    while temp_counter < number_of_numbers:
        key = int(input("Enter index of number: "))
        value = int(input("Enter the value: "))
        player_one_dict[key] = value
        temp_counter+=1

    #Just indicating that player two should insert his numbers
    print("Hey , player two! Now it's your turn to enter the numbers: ")

    temp_counter = 0
    while temp_counter < number_of_numbers:
        key = int(input("Enter index of number: "))
        value = int(input("Enter the value: "))
        player_two_dict[key] = value
        temp_counter+=1

    #Maximum number we got form joining value sfrom both dictionaries
    maximum = max(list(chain(player_one_dict, player_two_dict)))
    
    #Now, we will use sieve of Erastathos (I guess that's how you wtite is) to generate
    #prime numbers from 2 to maximum

    arr = sieve(maximum)

    #Now we calcualte points for players
    #Player one goes first


    for index in player_one_dict:
        value = player_one_dict[index]
        for i in arr:
            if value == i:
                player_one_points+=1
                break

    for index in player_two_dict:
        value = player_two_dict[index]
        for i in arr:
            if value == i:
                player_two_points+=1
                break
    
    if player_one_points > player_two_points:
        print("Player one is the winner")
    elif player_one_points < player_two_points:
        print("Player two is the winner")
    else:
        print("It's a tie")


def sieve(value):
    temp = list(range(2,value))
    for i in temp:
        temp = list(filter(lambda x: x == i or not x % i == 0, temp))
    return temp

if __name__ == "__main__":
    main()