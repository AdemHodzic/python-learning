def my_func(func, arg):
    return func(arg)

def main():
    print(my_func(lambda x: 2*x*x, 5))


if __name__ == "__main__":
    main()