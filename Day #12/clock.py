from math import floor, fabs

def main():
    first = str(input('Enter the first clock position in format hh:mm : '))
    second = str(input('Enter the second clock position in format hh:mm : '))

    first_arr = first.split(':')
    second_arr = second.split(':')

    ## if first is smaller oduzeti drugi od prvog pa oduzeti jedan pa obraditi minute
    ## ako je prvi veci onda oduzeti 24 od prvog pa isto za prvi

    first_hour = int(first_arr[0])
    second_hour = int(second_arr[0])
    first_minute = int(first_arr[1])
    second_minute = int(second_arr[1])

    if first_hour > second_hour:
        first_hour -= 24
    
    result = second_hour - first_hour - 1
    
    first_minute_position = floor(first_minute / 5)
    second_minute_position = floor(second_minute / 5)

    if fabs(first_hour) < first_minute_position:
        result += 1
    elif fabs(second_hour) < second_minute_position:
        result += 1
    
    print(result)
    
if __name__ == '__main__':
    main()