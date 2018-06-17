def main():
  number = int(input('Enter your number: '))
  print(sumOdds(number))

def sumOdds(number):
  sum = 0
  counter = 1
  while fibonacci(counter) <= number:
    if fibonacci(counter) % 2 == 1:
      sum += fibonacci(counter)
    counter += 1 
  return sum

def fibonacci(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fibonacci(num - 1) + fibonacci(num - 2)
if __name__ == '__main__':
  main()