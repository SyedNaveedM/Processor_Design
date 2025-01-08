import numpy as np
def binToDec(st):           #This is a function that is used for conversion from binary string to integers
    i = len(st)-1
    n = 0
    while(i>0):
        n = n+int(st[i])*2**(len(st)-i-1)
        i -= 1
    if(int(st[i])):
        n -= 2**(len(st)-1)
    return n
def DecToBin(N, k):         #This function is for converting from integers to binary string
    n = int(N)
    st = ""
    while(n>0):
        st = str(n%2)+st
        n = n//2
    st = "0"*(k-len(st)) + st
    if(n== -1):
        return "1"*k
    return st
#Processor Class Implementation
class Processor:
    Memory = np.full(1000, "0"*40)      #Memory is an attribute of the processor class(not just the instance but the whole class)
    def __init__(self):                 #Defining various registers
        self.ac = "0"*40
        self.mq = "0"*40
        self.mbr = "0"*40
        self.ibr = "0"*20
        self.pc = "0"*12
        self.ir = "0"*8
        self.mar = "0"*12
        self.lir = True                 #This is not a register but a control variable to determine whether the left instruction is required or not at every fetch cycle
        self.jumpr = False              #This is another control variable used for jump to the right so that ibr gets the right opcode and address
    def Mem_LOAD(self):                 #Method to load the binary strings into memory
        with open('binary.txt', 'r') as binary:
            for line in binary:
                Processor.Memory[int(line.split()[0])]=line.split()[1]
        binary.close()
    def fetch(self):                    #Method to execute the fetch cycle
        #1.
        if(self.lir):                   
            print("Fetch Cycle:")
            print("MAR gets PC:")
            self.mar = self.pc          #MAR gets the address from PC
            self.reveal()
            print("MBR gets Memory[MAR]:")
            self.mbr = Processor.Memory[binToDec(self.mar)]       #MBR gets the value in Memory[MAR]
            self.reveal()
            print("IR, MAR, IBR get their contents from MBR:")
            self.ir = self.mbr[0:8]                     #IR, MAR, IBR get their values from MBR
            self.mar = binToDec(self.mbr[8:20])
            self.mar=DecToBin(self.mar,12)
            self.ibr = self.mbr[20:]
            self.reveal()
            self.lir = False
        #2.
        else:
            if(self.jumpr):
                print("Jump Right: Left Instruction Not Required")                             #If the fetch is right after a jump right condition, mbr gets updated to the new value at memory location of pc
                self.mar = self.pc
                self.mbr = Processor.Memory[binToDec(self.mar)]
                self.ir = self.mbr[20:28]
                self.mar = self.mbr[28:]
                self.pc = DecToBin(binToDec(self.pc)+1, 12)
                self.reveal()
                self.jumpr = False
            else:
                print("MAR and IBR get their contents from IBR; PC increments by 1:")
                self.mar=binToDec(self.mar)
                self.mar = binToDec(self.ibr[8:20])
                self.mar=DecToBin(self.mar,12)
                self.ir = self.ibr[0:8]
                self.pc=binToDec(self.pc)
                self.pc += 1
                self.pc=DecToBin(self.pc,12)
                self.reveal()
            self.lir=True
    def decode(self):                                   #Decode cycle multiplexes the functions to be implemented by differentiating their opcodes
        if self.ir=="00001010":
            return self.LOAD_MQ
        elif self.ir=="00100001":
            return  self.STOR_M
        elif self.ir=="00000001":
            return self.LOAD_M
        elif self.ir=="00001101":
            return self.JUMP_ML
        elif self.ir=="00001110":
            return self.JUMP_MR
        elif self.ir=="00001111":
            return  self.JUMP_Con_L_M
        elif self.ir=="00010000":
            return  self.JUMP_Con_R_M
        elif self.ir=="00000101":
            return  self.ADD_M
        elif self.ir=="00000110":
            return  self.SUB_M
        elif self.ir=="00001100":
            return  self.DIV_M
        elif self.ir=="00001011":
            return  self.MUL_M
        elif self.ir=="00010101":
            return  self.RSH
        elif self.ir=="00010010":
            return  self.STOR_ML
        elif self.ir=="00010011":
            return  self.STOR_MR
        elif self.ir=="01000000":
            return  self.GT_M
        elif self.ir=="01000001":
            return  self.LT_M
        elif self.ir=="01000010":
            return  self.LTE_M
        elif self.ir=="01000011":
            return  self.EQ_M
        elif self.ir=="01000100":
            return self.SEND_M
        elif self.ir=="0"*8:
            return self.NOP
    def execute(self, f_name):                  #Execute cycle calls the function returned from the decode cycle and executes it.
        f_name(binToDec(self.mar))
        return

    #These are the various instructions from the ISA implemented using functions/methods

    def LOAD_MQ(self, X):
        self.ac=self.mq
        print("AC <-- MQ")
        self.reveal()
    def ADD_M(self,X):
        self.ac=binToDec(self.ac)
        self.mbr = self.Memory[X]
        self.ac+=binToDec(self.mbr)
        print(f'ADD M(X): AC <-- AC+M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    def DIV_M(self,X):
        self.ac=binToDec(self.ac)
        self.mq=binToDec(self.mq)
        self.mbr = self.Memory[X]
        self.ac=binToDec(self.mbr)
        self.mq=self.ac//(self.Memory[X])
        self.ac=self.ac%(self.Memory[X])
        print(f'DIV M(X): MQ <-- AC/M({X})')
        self.ac=DecToBin(self.ac,40)
        self.mq=DecToBin(self.mq,40)
        self.reveal()
    def LOAD_M(self,X):
        self.mbr=self.Memory[X]
        self.ac=self.mbr
        print(f'LOAD M(X): AC <-- M({X})')
        self.reveal()
    def STOR_M(self,X):
        self.mbr=self.ac
        self.Memory[X] = self.mbr
        print(f'STOR M(X): M({X}) <-- AC')
        self.reveal()
    def GT_M(self,X):  #This is a self-made instruction which compares if the value in AC is greater than M(X) and stores the answer(-1 or 1) in AC
        self.ac=binToDec(self.ac)
        self.mbr=self.Memory[X]
        if(self.ac>binToDec(self.mbr)):
            self.ac=1
        else:
            self.ac=-1
        print(f'GT M(X): AC <-- AC > M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    #This method works as JUMP+ M(X,0:19)
    def JUMP_Con_L_M(self,X):
        self.ac=binToDec(self.ac)
        self.pc=binToDec(self.pc)
        if(self.ac>=0):
            self.pc=X
            self.lir = True
        print(f'JUMP+ M(X,0:19): PC <-- {X}, Left instruction required, if AC is non-negative')
        self.ac=DecToBin(self.ac,40)
        self.pc=DecToBin(self.pc,12)
        self.reveal()
    #This method works as JUMP+ M(X,20:29)
    def JUMP_Con_R_M(self, X):
        self.ac=binToDec(self.ac)
        self.pc=binToDec(self.pc)
        if(self.ac>=0):
            self.pc=X
            self.lir=False
            self.jumpr=True
        print(f'JUMP+ M(X,20:39): PC <-- {X}, Left instruction not required, if AC is non-negative')
        self.ac=DecToBin(self.ac,40)
        self.pc=DecToBin(self.pc,12)
        self.ibr = "0"*20
        self.reveal()
    def NOP(self, X):
        print("NOP")
    #This function works as STOR M(X,8:19)
    def STOR_ML(self,X):
        st=self.Memory[X][0:8]
        st+=self.ac[-12:]
        st += self.Memory[X][20:]
        self.Memory[X]=st
        print(f'STOR M(X,8:19): M({X})[8:19] <-- AC[28:39]')
        self.reveal()
    def LT_M(self,X):           #Another self-made function(Lesser than) similar to GT
        self.ac=binToDec(self.ac)
        self.mbr = self.Memory[X]
        if(self.ac<binToDec(self.mbr)):
            self.ac=1
        else:
            self.ac=-1
        print(f'LT M(X): AC <-- AC < M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    def EQ_M(self,X):           #Self-made function: Equal to operator
        self.ac=binToDec(self.ac)
        self.mbr = self.Memory[X]
        if(self.ac==binToDec(self.mbr)):
            self.ac=1
        else:
            self.ac=-1
        print(f'EQ M(X): AC <-- AC == M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    def SUB_M(self,X):
        self.ac=binToDec(self.ac)
        self.ac=self.ac-binToDec(self.Memory[X])
        print(f'SUB M(X): AC <-- AC-M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    def SEND_M(self,X):         #This self-made instruction is for both printing the value and terminating the loop by pointing pc to location 1000
        print(f"Answer={binToDec(self.Memory[X])}")
        self.pc=binToDec(self.pc)
        self.pc = 1000
        self.pc=DecToBin(self.pc,12)
    def LTE_M(self,X):          #Self-made instruction: Less than or equal to
        self.ac=binToDec(self.ac)
        self.mbr=self.Memory[X]
        if(self.ac<=binToDec(self.mbr)):
            self.ac=1
        else:
            self.ac=-1
        print(f'LTE M(X): AC <-- AC <= M({X})')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    #Works as STOR M(X,28:39)
    def STOR_MR(self,X):
        st=self.Memory[X][0:28]
        st+=self.ac[-12:]
        self.Memory[X]=st
        print(f'STOR M(X,28:39): M({X})[28:39] <-- AC[28:39]')
        self.reveal()
    def RSH(self,X):
        self.ac=binToDec(self.ac)
        self.ac=self.ac//2
        print(f'RSH: Right Shift')
        self.ac=DecToBin(self.ac,40)
        self.reveal()
    #Unconditional JUMPs
    def JUMP_ML(self,X):
        self.pc=binToDec(self.pc)
        self.pc=X
        self.lir=True
        print(f'JUMP M(X,0:19): PC <-- {X}, Left Instruction Required')
        self.pc=DecToBin(self.pc,12)
        self.reveal()
    def JUMP_MR(self, X):
        self.pc=binToDec(self.pc)
        self.pc=X
        self.lir=False
        self.jumpr=True
        print(f'JUMP M(X,20:39): PC <-- {X}, Left Instruction Not Required')
        self.pc=DecToBin(self.pc,12)
        self.ibr="0"*20
        self.reveal()
    def reveal(self):           #This method is called at every step to reveal the contents of all the registers and variables for the program
        print("PC=>", self.pc, binToDec(self.pc))
        print("MAR=>", self.mar, binToDec(self.mar))
        print("MBR=>", self.mbr)
        print("IBR=>", self.ibr)
        print("IR=>", self.ir)
        print("AC=>", self.ac, binToDec(self.ac))
        print("MQ=>", self.mq, binToDec(self.mq))
        print("mid=", self.Memory[513], binToDec(self.Memory[513]))
        print("low=", self.Memory[511], binToDec(self.Memory[511]))
        print("high=", self.Memory[512], binToDec(self.Memory[512]))
        print("iterator=", self.Memory[502], binToDec(self.Memory[502]))
        print("Count=", self.Memory[500], binToDec(self.Memory[500]))
        print()

ias = Processor()       #Creating an object instance ias of Processor class
ias.Mem_LOAD()          #Loading binary file into the memory
ias.pc = "000001100100"
inp = 0
while(binToDec(ias.pc) < 1000):       #Running the processor till pc reaches 1000
    ias.fetch()
    f = ias.decode()
    ias.execute(f)
    inp += 1
    if(inp == 10):
        input("Press Enter to Continue:")
        inp=0
