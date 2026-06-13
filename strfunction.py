str1 = "Divyarajsinh Puwar!"

#String end checking:-

print(str1.endswith("ar!") )
print(str1.endswith("Divya") )

str2 = "divyaraj puwar"

#capitalizing:-

print(str2.capitalize() ) # Do not capitalize real string
str3 = str2.capitalize() #would capitalize real string
print (str3)

#Replacing:-

print(str2.replace("divyaraj" , "Divyaraj"))
print(str2.replace("w" , "v"))

#Finding:-

print(str2.find("puwar"))
print(str2.find("Puwar"))

#counting:-

print(str2.find("a"))
print(str2.find("t"))