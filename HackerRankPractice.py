#Integer Division and Float Division
"""
a = 3
b= 5
print(a//b)
print(a/b)

# for loops for non negative integers
n = 6

for x in range(n):
    print(x)

"""
"""
#leap year function exercise
x= 1990
def leap_year(x):
    if x%400 ==0:
        print("is a leap year")
        return True
    elif x%100==0:
        print("is not a leap year")
        return False
    elif x%4 ==0:
        print("is a leap year")
        return True
    else:
        print("is not leap year")
        return False

leap_year(x)
"""
"""
#convert number list into single string
n = 6
num_list =[]
string = ''
for x in range(1,n):
    y = str(x)
    num_list.append(y)
    z = ''.join(num_list)


print(z)
"""

