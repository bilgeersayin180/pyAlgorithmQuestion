Letter_list = {}
timesUsed = 0
#print(letters["n"])
string = str(input("Enter a word: "))
for letters_in_string in string:
    if (letters_in_string == ' '):
        #string.split(letters_in_string)
        continue
    """
    elif (Letter_list.get(letters_in_string, 'Not Found') == "Not Found"):
        timesUsed = 1
        Letter_list[letters_in_string] = timesUsed
    else:
        timesUsed += 1
        Letter_list.update({letters_in_string: timesUsed})
    """
    if ((letters_in_string in Letter_list) == True):
        Letter_list[letters_in_string] += 1
    else:
        Letter_list[letters_in_string] = 1
        
    
print(Letter_list)
