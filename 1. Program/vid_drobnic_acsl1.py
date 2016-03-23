# Vid Drobnič
# Gimnazija Vič, 3.b
# Intermediate 3
# Language: Python 3.5

stringRepresentation = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]

def octal(input):
    input = input.split(" ")
    binary = ""
    string = ""
    for i in input:
        binaryNumber = bin(int(i, 8))[2:]
        zerosToAdd = 3 - len(binaryNumber)
        binaryNumber = zerosToAdd * "0" + binaryNumber
        binary += binaryNumber + " "
        string += stringRepresentation[int(i, 8)] + " "
    output = binary + "and " + string[:-1]
    print(output)

def binary(input):
    input = input.split(" ")
    octal = ""
    string = ""
    for i in input:
        decimal = int(i, 2)
        string += stringRepresentation[decimal] + " "
        octal += str(decimal)
    output = octal + " and " + string[:-1]
    print(output)

def string(input):
    input = input.split(" ")
    octal = ""
    binary = ""
    for i in input:
        decimal = stringRepresentation.index(i)
        octal += str(decimal)

        binaryNumber = bin(decimal)[2:]
        zerosToAdd = 3 - len(binaryNumber)
        binaryNumber = zerosToAdd * "0" + binaryNumber
        binary += binaryNumber + " "
    output = octal + " and " + binary[:-1]
    print(output)

for i in range(0, 2): octal(input())
for i in range(0, 2): binary(input())
string(input())
