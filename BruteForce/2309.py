from sys import stdin

heights = [int(stdin.readline()) for _ in range(9)]
heights.sort()

sum_heights = sum(heights)

for i in range(8):
    for j in range(i+1, 9):
        if sum_heights - (heights[i] + heights[j]) == 100:
            del heights[j], heights[i]
            for c in heights:
                print(c, sep='\n')
            exit()
