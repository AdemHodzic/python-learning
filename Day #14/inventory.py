def main():
  prev_arr = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]
  new_arr = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]
  final_arr = inventory(prev_arr, new_arr)
  print(final_arr)

def inventory(prev_arr, new_arr):
  prev_dict = makeDict(prev_arr)
  new_dict = makeDict(new_arr)

  for key, value in new_dict.items():
    if key in prev_dict:
      prev_dict[key] += value
    else:
      prev_dict.update({key:value})
    
  return makeArray(prev_dict)


def makeDict(arr):
  dictionary = {}
  for element in arr:
    key = element[1]
    value = element[0]
    dictionary[key] = value
  return dictionary

def makeArray(obj):
  arr = []
  key_list = sorted(obj.keys())
  for key in key_list:
    value = obj[key]
    arr.append([value, key])
  return arr

if __name__ == '__main__':
  main()