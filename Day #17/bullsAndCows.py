def main():
  secret = 1234
  user_input = int(input('Enter your guess: '))
  print(guess(secret, user_input))

def guess(secret, user_input):
  secret = list(str(secret))
  user_input = list(str(user_input))
  
  bulls = 0
  cows = 0

  for x in range(0, len(user_input)):
    if user_input[x] == secret[x]:
      bulls += 1
      user_input[x] = ''
      secret[x] = ''
  
  user_input = clean(user_input)
  secret = clean(secret)

  for i in range(0, len(user_input)):
    if user_input[i] in secret:
      secret[secret.index(user_input[i])] = ''
      user_input[i] = ''
      cows += 1
  
  solution = 'B'+str(bulls)+'C'+str(cows)

  return solution

def clean(arr):
  new_arr = []

  for char in arr:
    if not char == '':
      new_arr.append(char)

  return new_arr

if __name__ == '__main__':
  main()