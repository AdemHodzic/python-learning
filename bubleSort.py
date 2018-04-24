def main():
    arr = [5,2,3,6,1,4]
    print("Before sorting: ")
    print(arr)
    bubleSort(arr)
    print("After sorting: ")
    print(arr)

def bubleSort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp


if __name__ == "__main__":
    main()