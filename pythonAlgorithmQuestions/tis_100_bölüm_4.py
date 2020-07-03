IN = [2,1,2,0,-2,1,2,-2,-1,-2,1,-2,0,2,0,1,0,2,-1,0,-1,-1,-1,0,1,1,-2,-2,-2,2,-2,0,2,-1,1,2,0,-1,-1]
OUT_G = []
OUT_E = []
OUT_L = []
lenght = len(IN)
def JGZ(arr):
        for ACC in range(0, lenght):
            if (arr[ACC] > 0):
                OUT_G.append(1)
            else:
                OUT_G.append(0)
        return(OUT_G)

def JEZ(arr):
        for ACC in range(0, lenght):
            if (arr[ACC] == 0):
                OUT_E.append(1)
            else: 
                OUT_E.append(0)
        return(OUT_E)
def JLZ(arr):
        for ACC in range(0, lenght):
            if (arr[ACC] < 0):
                OUT_L.append(1)
            else:
                OUT_L.append(0)
        return(OUT_L)
        

print(JGZ(IN))
print(" ")
print(JEZ(IN))
print(" ")
print(JLZ(IN))
    
