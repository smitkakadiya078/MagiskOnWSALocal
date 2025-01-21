#BY SMIT KAKADIYA 24BCP262
#Remove one string from other
def remove_substring(string1, string2):
    return string1.replace(string2, '')
string1 = input("Enter parent string: ")
string2 = input("Enter string to remove: ")
finalstring = remove_substring(string1, string2)
print(finalstring)
#BY MAHIR SHAH
