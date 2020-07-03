while(True):
    inputNum = int(input("Enter a positive integer: "))
    num_len = len(str(inputNum)) #lenght of the input number
    square_num = inputNum * inputNum #lenght of the square of the number
    str_square_num = str(square_num) #string type of the square of the number
    square_num_len = len(str_square_num) #lenght of the square of the number
    start = (square_num_len - num_len) #start of the for loop (to detect the input number in the square of the number)
    end = square_num_len #end of the for loop
    tries = 0
    for i in range(start, end): 
        if (str_square_num[i] == (str(inputNum))[i - start]):
            tries += 1
    if (tries == num_len):
        print(inputNum,"is an automorphic number.")
    else:
        print(inputNum,"is not an automorphic number.")
    
