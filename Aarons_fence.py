# Calculations to build a fence in autocad coordinate format
import math 

# Inputs
lenght_fence_meters = 6 # int(input("Enter the lenght of the fence in m: "))
thickness_posts = 500 # int(input("Choose 3x3 or 4x4, as 300 or 400: "))
height_fence = 1000 # int(input("Choose a height of 500, 1000 or 1500: "))
lenght_fence = lenght_fence_meters * 1000

# Calculation number of posts
number_posts = math.ceil(lenght_fence / 2400)
print(f'Number of posts: {number_posts}')

# Calculation of the distance between posts
distance_between_posts = round(int((lenght_fence - (number_posts * thickness_posts)) / (number_posts - 1)))
print(f'The distance between posts is {distance_between_posts} mm')

# Calculating the coordinates for each post
coord_x = 0 - distance_between_posts
coord_x_y = []
coordinates_y = []
steps = number_posts * 4
for step in range(0, steps):
    if step % 4 == 0:
        coord_x += distance_between_posts
        coord_x_y.append(coord_x)
        coord_x_y.append(-500)
    if step % 4 == 1:
        coord_x_y.append(coord_x)
        coord_x_y.append(height_fence)
    if step % 4 == 2:
        coord_x += thickness_posts
        coord_x_y.append(coord_x)
        coord_x_y.append(height_fence)
    if step % 4 == 3:
        coord_x_y.append(coord_x)
        coord_x_y.append(-500)

# Combine into one     
# coord_x_y = [item for pair in zip(coordinates_x, coordinates_y) for item in pair]


for i in range(0, len(coord_x_y), 8):
    print("PLINE")
    for j in range(i, min(i + 8, len(coord_x_y)), 2):
        print(f"{coord_x_y[j]},{coord_x_y[j+1]}")
    print("""CLOSE
          """)