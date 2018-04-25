def main():
    with open("newFile.txt", "a") as f:
        userInput = str(input("What's on your mind ?"))
        f.write(userInput)
        f.write("\n") 


if __name__ == "__main__":
    main()