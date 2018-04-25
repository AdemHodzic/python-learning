def decor(func):
    def wrap():
        print("==========================")
        func()
        print("==========================")
    return wrap

@decor
def greeting():
    print("Hello World")

def main():
    greeting()


if __name__ == "__main__":
    main()