def main():
  number = int(input('Enter your number: '))
  print(addDigits(number))

def addDigits(number):
  sum_digits = 0
  arr = list(str(number))
  for number in arr:
    sum_digits += int(number)
  
  while sum_digits > 10:
    arr = list(str(sum_digits))
    sum_digits = 0
    for number in arr:
      sum_digits += int(number)

  return sum_digits

if __name__ == '__main__':
  main()