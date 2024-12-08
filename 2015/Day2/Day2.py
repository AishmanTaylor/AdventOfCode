import re

def find_area(dimensions):
    measurementsString = re.split(r'x', dimensions)
    measurementsInt = [int(i) for i in measurementsString]
    lw2 = measurementsInt[0] * measurementsInt[1] * 2
    hw2 = measurementsInt[1] * measurementsInt[2] * 2
    hl2 = measurementsInt[2] * measurementsInt[0] * 2
    extra = 0
    if lw2 <= hw2 and lw2 <= hl2:
        extra = lw2
    elif hw2 <= lw2 and hw2 <= hl2:
        extra = hw2
    elif hl2 <= lw2 and hl2 <= hw2:
        extra = hl2
    total = lw2 + hw2 + hl2 + extra
    return total 

paper_needed = 0

file = open('input.txt', 'r')
lines = file.readlines();

for line in lines:
    paper_needed += find_area(line)

print(f"Paper needed {paper_needed}")