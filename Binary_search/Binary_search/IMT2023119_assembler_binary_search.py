import numpy as np

def binaryGen(N, k):
    n = int(N)
    st = ""
    while(n>0):
        st = str(n%2)+st
        n = n//2
    st = "0"*(k-len(st)) + st
    if(n== -1):
        return "1"*k
    return st
def DataGen(ls):
    return binaryGen(ls[1], 40);
def InsGen(ls):
    if ls[1] == "RSH":
        op1 = "00010101"
        add1 = "0000"*3
    elif ls[1] == "NOP":
        op1 = "00000000"
        add1 = "0000"*3
    elif ls[1] == "GT":
        op1 = "01000000"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LT":
        op1 = "01000001"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LTE":
        op1 = "01000010"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "GTE":
        op1 = "01000101"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "EQ":
        op1 = "01000011"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "SEND":
        op1 = "01000100"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LOAD":
        if ls[2]=="MQ":
            op1 = "00001010"
            add1 = "000000000000"
        else:
            op1 = "00000001"
            add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1]=="STOR":
        if ls[2][-3:-1]=="19":
            op1 = "00010010"
            add1 = binaryGen(ls[2][2:-6], 12)
        elif ls[2][-3:-1]=="39":
            op1 = "00010011"
            add1 = binaryGen(ls[2][2:-7], 12)
        else:
            op1 = "00100001"
            add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "ADD":
        op1 ="00000101"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "DIV":
        op1 = "00001100"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "SUB":
        op1 = "00000110"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "MUL":
        op1 = "00001011"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1]=="JUMP":
        if ls[2][-3:-1]=="19":
            op1 = "00001101"
            add1 = binaryGen(ls[2][2:-6], 12)
        else:
            op1 = "00001101"
            add1 = binaryGen(ls[2][2:-7], 12)
    elif ls[1]=="JUMP+":
        if ls[2][-3:-1]=="19":
            op1 = "00001111"
            add1 = binaryGen(ls[2][2:-6], 12)
        else:
            op1 = "00010000"
            add1 = binaryGen(ls[2][2:-7], 12)
    ret = op1+add1
    for i in range(len(ls)):
        if ls[i] == ";":
            arr = ['0']
            arr+=ls[i+1:]
            break
    ls = arr
    if ls[1] == "RSH":
        op1 = "00010101"
        add1 = "0000"*3
    elif ls[1] == "NOP":
        op1 = "00000000"
        add1 = "0000"*3
    elif ls[1] == "GT":
        op1 = "01000000"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LT":
        op1 = "01000001"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LTE":
        op1 = "01000010"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "GTE":
        op1 = "01000101"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "EQ":
        op1 = "01000011"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "SEND":
        op1 = "01000100"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "LOAD":
        if ls[2]=="MQ":
            op1 = "00001010"
            add1 = "000000000000"
        else:
            op1 = "00000001"
            add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1]=="STOR":
        if ls[2][-3:-1]=="19":
            op1 = "00010010"
            add1 = binaryGen(ls[2][2:-6], 12)
        elif ls[2][-3:-1]=="39":
            op1 = "00010011"
            add1 = binaryGen(ls[2][2:-7], 12)
        else:
            op1 = "00100001"
            add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "ADD":
        op1 ="00000101"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "DIV":
        op1 = "00001100"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "SUB":
        op1 = "00000110"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1] == "MUL":
        op1 = "00001011"
        add1 = binaryGen(ls[2][2:-1], 12)
    elif ls[1]=="JUMP":
        if ls[2][-3:-1]=="19":
            op1 = "00001101"
            add1 = binaryGen(ls[2][2:-6], 12)
        else:
            op1 = "00001110"
            add1 = binaryGen(ls[2][2:-7], 12)
    elif ls[1]=="JUMP+":
        if ls[2][-3:-1]=="19":
            op1 = "00001111"
            add1 = binaryGen(ls[2][2:-6], 12)
        else:
            op1 = "00010000"
            add1 = binaryGen(ls[2][2:-7], 12)
    return ret+op1+add1

binary = open('binary.txt', 'w')
with open('IMT2023119_assembly_binary_search.txt', 'r') as assembly:
    for line in assembly:
        cod = line.split()
        if (int(cod[0]) < 500):
            binary.write(cod[0]+' '+InsGen(cod)+'\n')
        else:
            binary.write(cod[0]+' '+DataGen(cod)+'\n')
binary.close()
assembly.close()
