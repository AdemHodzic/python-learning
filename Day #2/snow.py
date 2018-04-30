def main():
    heights = []
    cities = []
   
    while True:
        value = int(input("Enter height of snow (enter -1 for end of input): "))
        if value < 0:
            break
        heights.append(value)
        city = str(input("Enter the name of the city: "))
        cities.append(city)
    sort(heights, cities)
    for i in range(0, len(heights)):
        print(f"{cities[i]} {heights[i]}")

def sort(height, cities):
    for i in range(0, len(height)):
        for j in range(i+1, len(height)):
            if height[j] > height[i]:
                switch(i,j,height,cities)
            if height[i] == height[j]:
                index = 0
                while True:
                    i_city = cities[i][index]
                    j_city = cities[j][index]
                    if  i_city > j_city:
                        switch(i,j,height,cities)
                        break
                    elif i_city == j_city:
                        index+=1
                    else:
                        break
                        
def switch(i, j,height, cities):
    temp_h = height[i]
    height[i] = height[j]
    height[j] = temp_h
    temp_c = cities[i]
    cities[i] = cities[j]
    cities[j] = temp_c               


if __name__ == "__main__":
    main()