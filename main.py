from cgitb import text

#Max of Three Numbers 
def max_num(a,b,c):
    return max ([a,b,c])

print(max_num(1,2,3)) #3
print(max_num(25,30,50)) #50
    
#Multiply numbers in a list
def mult_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(mult_list([4,10,15,2])) #1200

#Reverse a string
def rev_string(my_s):
    return my_s[::-1]

text = rev_string("I have class tonight")

print(text) #thginot ssalc evah I
print(rev_string("happy")) #yppah

#Find if a number falls within a range
def num_within(num1, num2, num3):
    return num1 in range(num2, num3+1)

print(num_within(10,2,5)) #false
print(num_within(10,1,200)) #true

#Pascal's triangle

def pascal(n):
    for i in range(n):
       row = [1]*(i+1)
       for j in range(1, i):
        prev_row = row
        row[j] = prev_row[j-1] + prev_row[j]
        print(row)

pascal(5)
