def main():
    #I put text in variable just beacuse it's annoying to have horizontal slider
    text = "Enter a number and we will find number of prime twins smallar than it: "
    maximum = int(input(text))
    arr = sieve(maximum)
    number_of_twins = 0
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 2:
            number_of_twins+=1
    print(f"Number of prime twins is: {number_of_twins}")

def sieve(value):
    temp = list(range(2, value))
    for i in temp:
        temp = list(filter(lambda x: x == i or not x % i == 0, temp))
    return temp


if __name__ == "__main__":
    main()