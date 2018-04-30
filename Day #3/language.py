import re

def main():
    text = str(input("Enter the text: "))
    text = re.sub('[^A-Za-z]', ' ', text)
    misspelled = []
    for word in text.split(' '):
        print(f"Checking {word}")
        if is_misspelled(word):
            misspelled.append(word)
    print(misspelled)

def is_misspelled(word:str) -> bool:
    #Define vowels
    vowels = ['a','e','i','o','u']
    #Check if word is empy string
    if len(word) == 0:
        return False
    #Check if word is only a vowel
    if len(word) == 1 and word in vowels:
        return False
    #Check if differnce in number of vowels and non-vowels is less or equal to 1
    vowels_list = list(filter(lambda x: x in vowels, list(word)))
    non_vowels_list = list(filter(lambda x: x not in vowels, list(word)))
    if abs(len(vowels_list) - len(non_vowels_list)) > 1:
        return True
    #Check if word starts with vowel and if it does it's len must be an odd number
    word_list = list(word)
    #If first char is vowel, the second one must be non vowel
    if word_list[0] in vowels: 
        if len(word_list) % 2 == 0:
            return True
        #In this case every odd index should be non vowel
        for i in range(0, len(word)): 
            if not i % 2 == 0:
                if word_list[i] in vowels:
                    return True
            elif i % 2 == 0:
                if not word_list[i] in vowels:
                    return True
    elif not word_list[0] in vowels:
        if not len(word_list) % 2 == 0:
            return True
        for i in range(0, len(word)): 
            if not i % 2 == 0:
                if not word_list[i] in vowels:
                    return True
            elif i % 2 == 0:
                if  word_list[i] in vowels:
                    return True
    return False
    
    


if __name__ == "__main__":
    main()