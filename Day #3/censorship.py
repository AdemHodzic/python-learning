import re

def main():
    words = []
    word = str(input("Enter a word to censor (empty input will will end input process): "))
    while not word == "":
        words.append(word)
        word = str(input("Enter a word to censor (empty input will will end input process): "))
    message = str(input("Enter your message empty input will will end input process): "))
    newMessage = []
    for mess in list(message.split(' ')):
        for word in words:
            turn = '*' * len(word)
            mess = re.sub(word, turn, mess)
        newMessage.append(mess)
    print(' '.join(newMessage))    


if __name__ == "__main__":
    main()