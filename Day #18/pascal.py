def main():
  rows = int(input('Enter the number of rows: '))
  for row in pascal(rows):
    print(row)


def pascal(rows):
  if rows == 1:
    return [[1]]
  triangle = [[1], [1, 1]]
  row = [1, 1]

  for i in range(2, rows):
    row = [1] + [sum(column)for column in zip(row[1:], row)] + [1]
    triangle.append(row)

  print
  return triangle


if __name__ == '__main__':
  main()
