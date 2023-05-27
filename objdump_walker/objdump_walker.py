#!/usr/bin/python3



# Sources used: 
# https://www.cs.virginia.edu/~evans/cs216/guides/x86.html 
# https://docs.oracle.com/cd/E19455091/806-3773/instructionset-70/index.html 
# https://c9x.me/x86/html/file_module_x86_id_217.html 
# https://www.cs.uaf.edu/2017/fall/cs301/lecture/09_11_registers.html 



# Notes 
# |-------------------------------------------------------------------------------------------------------------------|
# | Registers                                                                                                         | 
# |-------------------------------------------------------------------------------------------------------------------|
# | Name | 64-bit Long | 32-bit int | 16-bit short | 8-bit char | Notes                                               |
# |------|-------------|------------|--------------|------------|-----------------------------------------------------|
# | rax  | rax         | eax        | ax           | ah, al     | Values are returned from functions in this register |
# |-------------------------------------------------------------------------------------------------------------------|
# | rcx  | rcx         | ecx        | cx           | ch, cl     | Some instructions use this as a counter             |
# |-------------------------------------------------------------------------------------------------------------------|
# | rdx  | rdx         | edx        | dx           | dh, dl     |                                                     | 
# |-------------------------------------------------------------------------------------------------------------------|
# | rbx  | rbx         | ebx        | bx           | bh, bl     | PRESERVED REGISTER, don't use it without saving it  |
# |-------------------------------------------------------------------------------------------------------------------|
# | rsp  | rsp         | esp        | sp           | spl        | Stack Pointer, points to the top of the stack       |
# |-------------------------------------------------------------------------------------------------------------------|
# | rbp  | rbp         | ebp        | bp           | bpl        | PRESERVED REGISTER, sometimes used to store the old | 
# |      |             |            |              |            | value of the stack pointer, or the "base"           |
# |-------------------------------------------------------------------------------------------------------------------|
# | rsi  | rsi         | edi        | si           | sil        | Used to pass function argument#2 in 64-bit linux    |
# |-------------------------------------------------------------------------------------------------------------------|
# | rdi  | rdi         | edi        | di           | dil        | Used to pass function argument#1 in 64-bit linux    | 
# |-------------------------------------------------------------------------------------------------------------------|
# |      | Full 64-bit | Lower 32-  | Lower 16-bit | Lower half of the 16-bit value, first is the value of the upper  |
# |      | value       | Value      | Value        | 8-bits, second is the value of the lower 8-bits                  |
# |-------------------------------------------------------------------------------------------------------------------|



# TODO 
# 1.) Instead of taking text input, take in the binary to run objdump on and run objdump on it When implementing this, 
#     take in argument for objdump arguments 
#
# 2.) Implement a curses type interface instead of current implementation



import sys
import getopt
import os
import re 



#Global Variables
g_aRegisterStatesHistorical = [] # Holds registers listed above but also machine status word register
g_aStackStatesHistorical    = [] 
g_aMemoryStatesHistorical   = [] 

g_dictRegistersStateNow = {} # Holds registers listed above but also machine status word register
g_lStackStateNow = [] 
g_dictMemoryStateNow = {}



def objdumpwalker_exit(intExitValue): 
    
    if not intExitValue: 

        intExitValue = 0 #Default to a successful exit if no exit code given 

    sys.exit(intExitValue)


 
def print_objdumpwalker_help(): 
    strHelp = "objdumpwalker.py                                                           \n" \
              "                                                                           \n" \
              "Required Arguments:                                                        \n" \
              "                                                                           \n" \
              "\t-f <input file>, --file=<input file>                                     \n" \
              "\t\t Specifies the file to walk. The file should be a section of           \n" \
              "\t\t objdump that only contains instructions.                              \n" \
              "\t\t Example contents of file:                                             \n" \
              "\t\t 0000000000001135 <main>:                                   <- Exclude \n" \
              "\t\t     1135:  55                       push   rbp             <- Include \n" \
              "\t\t     1136:  48 89 e5                 mov    rbp,rsp         <- Include \n" \
              "\t\t     1139:  48 83 ec                 sub    rsp, 0x10       <- Include \n" 
              
    print(strHelp) 



def loadFile(strFilename): 
    
    astrFileContents = None 

    # Does the file exist? 
    if os.path.isfile(strFilename): 
        
        #Yes, load the lines of the file into astrFileContents
        with open(strFilename) as objFile: 

            astrFileContents = objFile.readlines()

    return astrFileContents 



def massageFileIntoInstructions (astrFileContents): 
   
    adictInstructions = [] 

    for strLine in astrFileContents: 
        
        astrLineElements = strLine.split("\t")
        
        dictOperands = { 
            "left"   : "",
            "right"  : "",
            "single" : ""
        } 
            
        dictInstruction = {
            "address"    : "",
            "hex"        : "",
            "opcode"     : "",
            "operands"   : dictOperands, 
            "objdumphelp": ""
        } 
            
        for intIndex, strElement in enumerate(astrLineElements): 
        
            # Clean the elements and assign to the dictionary
            if intIndex == 0: 

                # Remove colon from instruction address
                strElement = re.sub(r':','', strElement)
                dictInstruction ["address"] = strElement.lstrip().rstrip()
                
            if intIndex == 1: 
                
                # Clean up spaces on either side and assign to dictionary
                dictInstruction["hex"] = strElement.lstrip().rstrip()
            
            if intIndex == 2: 
                 
                # First, split the element into opcode, parameters, and additional information dictInstruction
                dictInstruction["opcode"]= re.search(r'\A[a-zA-Z]*', strElement).group(0) 

                # Next, remove the opcode from the element and spaces on either side
                strElement = re.sub(dictInstruction ["opcode"], '', strElement).lstrip().rstrip() 

                # Next, remove the objdumphelp and extra spaces on either side and store in the dictionary
                strOperands = re.sub (r'(#.*$)|(<.*>)', '', strElement).lstrip().rstrip() 

                # Next, parse the operands (left operand, right operand, etc)
                if len(strOperands) == 0: 
                    
                    # No operands 
                    dictInstruction ["operands"] = None
                
                else:
                    
                    astrOperands = strOperands.split(",")
                
                    if len(astrOperands) == 1:
                    
                        dictInstruction["operands"]["single"] = astrOperands[0]
                    
                    elif len(astrOperands) == 2:
                        
                        dictInstruction["operands"]["left"]  = astrOperands[0].lstrip().rstrip()
                        dictInstruction["operands"]["right"] = astrOperands[1].lstrip().rstrip()

                # Next, see if there is objdump help
                if re.search(r'(#.*$)|(<.*>)', strElement):
                    
                    dictInstruction ["objdumphelp"] = re.search(r'(#.*$)|(<.*>)', strElement).group(0)
                
        adictInstructions.append(dictInstruction) 
    
    return adictInstructions
    


def determineOperandType(stroperand): 
    
    stroperandType = None
 
    astrRegisters = ["rax", "eax", "ax", "ah ", "al", "rcx", "ecx", "cx", "ch", "cl", "rdx", "edx", "dx", 
                     "dh ", "d1", "rbx", "ebx", "bx", "bh", "bl", "rsp", "esp", "sp", "spl", "rbp", "ebp",
                     "bp", "bpl", "rsi", "edi", "si", "sil", "rdi", "edi", "di", "dil"]

    for strRegister in astrRegisters: 
        
        if strRegister in stroperand:

            stroperandType = "Register" 
            break 
        
        if not stroperandType: 
            
            stroperandType = "Memory"
            
        stroperandType = "Memory" 
    
    return stroperandType 


def handle_PUSH(dictInstruction):

    strValueToPush = None
    strOperandType = determineOperandType(dictInstruction["operands"]["single"])
    
    if strOperandType == "Register":
    
        strValueToPush = readRegister(dictInstruction["operands"]["single"])
    
    elif strOperandType == "Memory":
        
        strValueToPush = readFromMemory(dictInstruction["operands"]["single"])
        
    stackPush(strValueToPush)
    
    print("Push + str(strValueToPush) + onto the stack")



def handle_POP (dictInstruction):

    strPoppedValue = None
    strPoppedValue = stackPop()
    
    strOperandType = determineOperandType(dictInstruction ["operands"]["single"])
    
    if strOperandType == "Register":
        
        writeRegister(dictInstruction["operands"]["single"], strPoppedValue)
 
    elif strOperandType == "Memory":
        
        writeToMemory(dictInstruction["operands"]["single"], strPoppedValue)
        
    print("Popped " + str(strPoppedValue) + " from the stack into " + dictInstruction["operands"]["single"]) 



def handle_MOV(dictInstruction): 
    
    print("Handle MOV: " + dictInstruction["opcode"]) 



def handle_SUB(dictInstruction): 
    
    print("Handle SUB: " + dictInstruction["opcode"])



def handle_JMP(dictInstruction):
    
    print("Handle JMP: " + dictInstruction[ "opcode"])



def handle_ADD(dictInstruction): 
    
    print("Handle ADD: " + dictInstruction["opcode"])



def handle_CMP(dictInstruction):
    
    print("Handle CMP: " + dictInstruction["opcode"])



def handle_JLE(dictInstruction): 

    print("Handle JLE: " + dictInstruction["opcode"]) 



def handle_LEA(dictInstruction):
    
    print("Handle LEA: " + dictInstruction["opcode"]) 



def handle_CALL(dictInstruction):
    
    print("Handle CALL: " + dictInstruction["opcode"]) 



def handle_RET(dictInstruction):
    
    print("Handle RET: " + dictInstruction["opcode"]) 
 
 

def handle_LEAVE(dictInstruction):

    print("Handle LEAVE: " + dictInstruction["opcode"]) 



def handle_NOP(dictInstruction): 
    
    print("Handle NOP: " + dictInstruction["opcode"]) 



def handle_NOT_IMPLEMENTED (dictInstruction): 
 
    print("NOT_IMPLEMENTED")
    


def writeRegister(strRegister, strValueToWrite): 

    # Needed due to how we are tracking register states 
    print("writeRegister")



def readRegister(strRegister): 

    # Needed due to how we are tracking register states
    strRegisterValue = "register_value"

    return strRegisterValue
    


def writeToMemory(strMemoryAddress, starValueToWrite):
    
    # Needed due to how we are tracking memory
    print("writeToMemory")
    


def readFromMemory(strMemoryAddress): 
    
    # Needed due to how we are tracking memory
    strMemoryValue = "memory_value"
    
    return strMemoryValue



def initializeRegisters():
    
    global g_dictRegistersStateNow
    g_dictRegistersStateNow = {
        "registers" : { 
            "rax" : { 
                "rax" : "0000000000000000000000000000000000000000000000000000000000000000", 
                "eax" : "00000000000000000000000000000000", 
                "ax"  : "0000000000000000",
                "ah"  : "00000000",
                "al"  : "00000000"
            },
            "rcx" : { 
                "rcx" : "0000000000000000000000000000000000000000000000000000000000000000",
                "ecx" : "00000000000000000000000000000000",
                "cx"  : "0000000000000000",
                "ch"  : "00000000",
                "cl"  : "00000000" 
            }, 
            "rdx" : { 
                "rdx" : "0000000000000000000000000000000000000000000000000000000000000000",
                "edx" : "00000000000000000000000000000000",
                "dx"  : "0000000000000000",
                "dh " : "00000000",
                "dl " : "00000000"
            }, 
            "rbx" : {
                "rbx" : "0000000000000000000000000000000000000000000000000000000000000000",
                "ebx" : "00000000000000000000000000000000 ",
                "bx"  : "0000000000000000",
                "bh"  : "00000000", 
                "bl"  : "00000000" 
            }, 
            "rsp" : {
                "rsp" : "0000000000000000000000000000000000000000000000000000000000000000",
                "esp" : "00000000000000000000000000000000",
                "sp"  : "0000000000000000",
                "spl" : "00000000"
            }, 
            "rbp" : {
                "rbp" : "0000000000000000000000000000000000000000000000000000000000000000 ",
                "ebp" : "00000000000000000000000000000000",
                "bp"  : "0000000000000000",
                "bpl" : "00000000"
            },
            "rsi" : {
                "rsi" : "0000000000000000000000000000000000000000000000000000000000000000",
                "edi" : "00000000000000000000000000000000",
                "si"  : "0000000000000000", 
                "sil" : "00000000"
            },
            "rdi" : {
                "rdi" : "0000000000000000000000000000000000000000000000000000000000000000",
                "edi" : "00000000000000000000000000000000",
                "di"  :"0000000000000000",
                "dil" : "00000000"
            }
        }, 
        "machinestatus" : {} 
    }



def initializeStack():

    global g_lStackStateNow
    
    g_lStackStateNow.append(None)



def initializeMemory():

    global g_dictMemoryStateNow 

    #"allocate" 128 "bytes" of memory 
    #TODO find a better way to do this
    
    for i in range(0, 1024):

        strkey = "0x" + str(i)
        g_dictMemoryStateNow[strkey] = "0"



def storeStates():

    global g_aRegisterStatesHistorical
    global g_aStackStatesHistorical
    global g_aMemoryStatesHistorical
    
    global g_dictRegistersStateNow
    global g_lStackStateNow
    global g_dictMemoryStateNow
    
    g_aRegisterStatesHistorical.append(g_dictRegistersStateNow)
    g_aStackStatesHistorical.append(g_lStackStateNow)
    g_aMemoryStatesHistorical.append(g_dictMemoryStateNow)



def stackPush(strValue):
    
    global g_lStackStateNow
    
    intIndex = len(g_lStackStateNow)
    g_lStackStateNow.append("")
    
    while intIndex > 0:

        g_lStackStateNow[intIndex] = g_lStackStateNow[intIndex - 1]
        intIndex = intIndex - 1
    
    g_lStackStateNow[0] = strValue
    
def stackpop():

    global g_lStackStateNow
    strPoppedValue = g_lStackStateNow[0]

    for intIndex in range(0, len (g_lStackStateNow)):

        if intIndex < len(g_lStackStateNow) - 1:

            g_lStackStateNow[intIndex] = g_lStackStateNow[intIndex + 1]

        else:

            g_lStackStateNow[len(g_lStackStateNow) - 1] = None

    return strPoppedValue


def walkInstructions(adictInstructions):

    initializeRegisters()
    initializeStack()
    initializeMemory()

    storeStates()

    for intInstructionIndex, dictInstruction in enumerate(adictInstructions):
        
        if dictInstruction["opcode"].lower() == "push":

            handle_PUSH(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "pop":
 
            handle_POP(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "mov":
 
            handle_MOV(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "sub": 
 
            handle_SUB(dictInstruction)
 
        elif dictInstruction ["opcode"].lower() == "jmp":
 
            handle_JMP(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "add":
 
            handle_ADD(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "cmp":
 
            handle_CMP(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "jle": 
 
            handle_JLE(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "lea":
 
            handle_LEA(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "call":
 
            handle_CALL(dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "leave":
 
            handle_LEAVE (dictInstruction)
 
        elif dictInstruction["opcode"].lower() == "ret":
 
            handle_RET (dictInstruction)
 
        elif dictInstruction ["opcode"].lower() == "nop":
 
            handle_NOP (dictInstruction)
 
        else:
 
            handle_NOT_IMPLEMENTED(dictInstruction)
        
        storeStates()



def objdumpwalker_main(objArguments):

    strFilename = None
    
    try: 

        astrOptions, astrArguments = getopt.getopt(objArguments, "hf:", ["file="])

    except getopt.GetoptError:

        print_objdumpwalker_help()
        objdumpwalker_exit(2)

    for strOption, strArgument in astrOptions:

        if strOption == '-h':

            print_objdumpwalker_help()
            objdumpwalker_exit(0)

        elif strOption in ("-f", "--file"):

            strFilename = strArgument
    
    if not strFilename:
        print_objdumpwalker_help()
        objdumpwalker_exit(2)
        
    astrFileContents = loadFile(strFilename)
    adictInstructions = massageFileIntoInstructions(astrFileContents)

    walkInstructions(adictInstructions)
 


# TODO Need a way to output the historical states in a somewhat comprehensible way



if __name__ == "__main__":
    objdumpwalker_main(sys.argv[1:])
    objdumpwalker_exit(0)