str1 = "How are you John?"
name = "Yeghia"
str2 = str1[:12] + name + str1[-1:]
print(str2)
str2 = str1.replace("John",name)
print(str2)