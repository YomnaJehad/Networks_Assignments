def xor(a, b): #XOR between 2 binary numbers-> output is 0 if they are equal and 1 if they are not equal
    output = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            output.append('0')
        else:
            output.append('1')
    return ''.join(output)
def division(data, gen): #divide the message with the generator using XOR and return the remainder
    stopmark = len(gen)
    tmp = data[0 : stopmark]
    while stopmark < len(data):
        if tmp[0] == '1':
            tmp = xor(gen, tmp) + data[stopmark]
        else:
            tmp = xor('0'*stopmark, tmp) + data[stopmark]
        stopmark += 1
    if tmp[0] == '1':
        tmp = xor(gen, tmp)
    else:
        tmp = xor('0'*stopmark, tmp)
    result = tmp
    return result #remainder of the division

import numpy as np
def generator(input_file): #takes the message and generator then calculates the transmitted data
    m,g=np.loadtxt(input_file, delimiter=" ")
    m=str(int(m))
    g=str(int(g))

    r=len(g)-1
    for l in range(r):
        m=m+"0"

    # print("gowa generator zawedt r zeros", m)


    remainder=division(m,g)
    # print("ana gowa generator abl ma",remainder)
    #remainder=format(remainder,"b")
    r=len(g)-1
    bits_left= r-len(remainder)
    zeros=""
    if bits_left>0:

        for l in range(bits_left):
            zeros=zeros+"0"


    m=m[:len(m)-r]
    message= m+zeros+remainder #concatenate the message with some zeros and the remainder for the transmitted data 
    # print("ana gowa generator de el message",message,"w kaman rem",remainder)
    return message,g

def verifier(message,g): #it takes the message and generator then print correct if the remainder is zero, esle wrong output
    # print("ana gowa ver w de el mes",message)
    rem=division(message,g)

    if int(rem)==0 :
        print("Correct output")
    else:
        print("Wrong output")
    return



def alter(message,index): #it changes the bit of number = index in message
    message=list(message)
    if message[index] == "0" :
        message[index]="1"
    else:
        message[index]="0"
    message = ''.join(message)
    #print("ana gowa alter",message)
    return message
#-----------------------------------------------
#console presentation
print("Welcome to YMYM Assignment1")
print("if you want generator <file | verifier")
print("Press 1")
print("if you want generator <file | alter arg | verifier")
print("Press 2")

required=input()
#print(required)
if required=="1":#if you want generator <file | verifier
    message,g=generator("ymym.txt")
    verifier(message,g)

if required=="2":#if you want generator <file | alter arg | verifier
    index=input("Enter alter index: ")
    message,g=generator("ymym.txt")
    if int(index) > (len(message)-len(g)):
        print("invalid alter value")
            pass
        else :    
            message=alter(message,int(index))
            verifier(message,g)
    print("\n\n")
    print("Try again if you want !")





