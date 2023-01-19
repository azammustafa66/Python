height = input("Enter the heights separated by space: ")
heights = height.split()

for i in range(len(heights)):
    heights[i] = int(heights[i])

print(f"The average height is {(round(sum(heights) / len(heights)))}")
