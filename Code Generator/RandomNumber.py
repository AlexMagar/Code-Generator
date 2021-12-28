# Barcode generator 

import random
import string
from barcode import EAN13, EAN14

x = random.Random()
print(x)

# function that returns defined length of random alpha-numeric value
# length is the argument which is the length of the random code
# result is return (codeCollect) back that list of Barcode
def barCodeNumber(barCodeLength, numberOfBarcode):
    codeCollect = []
    for x in range(numberOfBarcode):  # + string.ascii_uppercase
        result = "".join((random.choice(string.digits + string.ascii_uppercase) for x in range(barCodeLength)))
        codeCollect.append(result)
    return codeCollect

# save code in file
def codeGenerator(barCodeNumber, loop):
    y=0
    #saving in file
    for x in range(loop):
        y+=1
        with open('Code.txt', 'a') as file:
            file.write(barCodeNumber[x])
            file.write(' ')
            if y%15==0:
                file.write('\n')
        

    

def main():
    # ask user lenght of Barcode and number of bar code
    # since the user input is a string so type cast into integer
    barCodeLength = int(input("Entre the length of Barcode: "))
    numberOfBarcode = int(input("Entre the number of Barcode you want: "))

    # get Barcode and store in object  
    rstl = barCodeNumber(barCodeLength, numberOfBarcode)

    #saving code in file
    codeGenerator(rstl, numberOfBarcode)

    # Store code in file
    with open('Barcode.txt', 'w') as file:
        for x in range(numberOfBarcode):
            file.write(rstl[x])
            file.write(", ")

    # print the result
    print(type(rstl))
    for x in range(numberOfBarcode):
        print(rstl[x])


# main function here
if __name__ =='__main__': main()