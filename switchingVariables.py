# # There are two variables, a and b from input
# a = input()
# b = input()
# # 🚨 Don't change the code above ☝️
# ####################################
# # Write your code below this line 👇
# Example Input 1
# 29
# 41
# Example Output 1
# a: 41
# b: 29

# # 🚨 Don't change the code below 👇
# print("a: " + a)
# print("b: " + b)

# create a temp variable to manipulate data

a = input()
b = input()

temp = a
a = b
b = temp

print("a: " + a)
print("b: " + b)