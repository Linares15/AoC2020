entries = []
with open("Day_01/input.txt") as txt:
    for line in txt:
        entries.append(int(line))

#
# Specifically, they need you to find the two entries that sum to 2020 
# and then multiply those two numbers together.
# For example, suppose your expense report contained the following:
#
#   1721
#   979
#   366
#   299
#   675
#   1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299. 
# Multiplying them together produces 1721 * 299 = 514579, 
# so the correct answer is 514579.
# Of course, your expense report is much larger. 
# Find the two entries that sum to 2020; 
# what do you get if you multiply them together?
#

def solution1 ():
    for x in entries:
        for y in entries:
            if x + y == 2020:
                return(x * y)

print (solution1())

#
# They offer you a second one if you can find three numbers 
# in your expense report that meet the same criteria.
# Using the above example again, the three entries that
#
# sum to 2020 are 979, 366, and 675. 
# Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?
#

def solution2 ():
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    return(x * y * z)

print (solution2())
