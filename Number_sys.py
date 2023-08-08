print('******** NUMBER SYSTEM CONVERTER ********')


def Decimal_to_Binary(Decimal):
    output=""

    for i in range (int(Decimal)):
        reminder= int(Decimal)%2

        if int(Decimal)==1:
            # print('1')
            output= output+'1'
            break
            
        else:
            Decimal=int(Decimal)/2
            # print(reminder)
            output=output+str(reminder)
    # print("The Binary Value is : ",output[::-1])
    # return ("The Binary Value is : ",output[::-1])
    return output[::-1]



def Decimal_to_Hexadecimal(Decimal):
        # Decimal=input("Enter Decimal Number : ")
    output=""


    for i in range (int(Decimal)):

        reminder= int(Decimal)%16

        if int(Decimal)==0:
            # print('1')
            output=output+ '0'
            break

        if int(Decimal)==1:
            # print('1')
            output=output+ '1'
            break
        
        elif reminder==10:
            # print("A")
            output=output+"A"
            
        elif reminder==11:
            # print("B")
            output=output+"B"
            
        elif reminder==12:
            # print("C")
            output=output+"C"
            
        elif reminder==13:
            # print("D")
            output=output+"D"
            
        elif reminder==14:
            # print("E")
            output=output+"E"
            
        elif reminder==15:
            # print("F")  
            output=output+"F"
        
        else:
            output=output+str(reminder)
        
        Decimal=int(Decimal)/16
    # print("The Hexadecimal value is : ",output[::-1])
    return output[::-1]


def Binary_to_Decimal(Binary):

    # Binary = int(input("Enter Binary Number : "))
    Binary_str=str(Binary)[::-1]
    # print(len(Binary_str))
    Decimal =0

    for i in range (len(Binary_str)):
        var= ((2**i) * int(Binary_str[i]))
        Decimal= Decimal + var
    # print ("The Decimal value is : ",Decimal)
    return Decimal

def Decimal_to_Octal(Decimal):
    # Decimal=input("Enter Decimal Number : ")
    output=""

    for i in range (int(Decimal)):

        reminder= int(Decimal)%8

        if int(Decimal)==1:
            # print('1')
            output=output+ '1'
            break

        elif int(Decimal)<8:
            # print('0')
            output=output+str(reminder)
            break
            
        else:
            Decimal=int(Decimal)/8
            output=output+str(reminder)

    # print("The Octal Value is : ",output[::-1])
    return output[::-1]




def Octal_to_Decimal(Octal):
    # Octal = int(input("Enter Octal Number : "))
    Octal_str=str(Octal)[::-1]

    var1 =0

    for i in range (len(Octal_str)):
        var= ((8**i) * int(Octal_str[i]))
        var1= var1 + var

    # print("The decimal value is : ",var1)
    return var1





def Hexadecimal_to_Decimal(Hexadecimal):
    # Hexa = input("Enter Hexadecimal Number : ")
    Hex_str = str(Hexadecimal)[::-1]
    # print(Hex_str)
    var1 =0
    varx=0

    for i in range (len(Hex_str)):
        if Hex_str[i] == 'A':
            hexnew=Hex_str[i].replace('A',"10")
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue
        if Hex_str[i] == "B" :
            hexnew=Hex_str[i].replace('B','11')
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue
        
        if Hex_str[i]=="C":
            hexnew=Hex_str[i].replace('C','12')
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue
        if Hex_str[i]=="D":
            hexnew=Hex_str[i].replace('D','13')
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue
        if Hex_str[i]=="E":
            hexnew=Hex_str[i].replace('E','14')
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue
        if Hex_str[i]=="F":
            hexnew = Hex_str[i].replace('F','15') 
            varx= ((16**i)* int(hexnew))
            var1= int(varx)+int(var1)
            continue

        var= ((16**i) * int(Hex_str[i]))
        var1= var1 + var 

    # print("The Decimal value is : ",var1)
    return var1


def Binary_to_Octal(Binary):
    decimal=Binary_to_Decimal(Binary)
    return Decimal_to_Octal(decimal)

def Binary_to_Hexadecimal(Binary):
    
    Decimal=Binary_to_Decimal(Binary)
    return Decimal_to_Hexadecimal(Decimal)


def Octal_to_Binary(Octal):
    Decimal=Octal_to_Decimal(Octal)
    return Decimal_to_Binary(Decimal)

def Octal_to_Hexadecimal(Octal):
    
    Decimal=Octal_to_Decimal(Octal)
    return Decimal_to_Hexadecimal(Decimal)


def Hexadecimal_to_Binary(Hexadecimal):
    Decimal=Hexadecimal_to_Decimal(Hexadecimal)
    return Decimal_to_Binary(Decimal)

def Hexadecimal_to_Octal(Hexadecimal):
    Decimal=Hexadecimal_to_Decimal(Hexadecimal)
    return Decimal_to_Octal(Decimal)






while True:
    question= int(input("""Enter your choice :
    1. Decimal to Binary
    2. Decimal to Octal
    3. Decimal to Hexadecimal
    4. Binary to Decimal 
    5. Binary to Octal
    6. Binary to Hexadecimal
    7. Octal to Decimal 
    8. Octal to Binary 
    9. Octal to Hexadecimal 
    10. Hexadecimal to Decimal
    11. Hexadecimal to Binary
    12. Hexadecimal to Octal
    13. Exit\n"""))


    if question==1:
        Decimal = int(input('Enter the Decimal value : '))
        a=Decimal_to_Binary(Decimal)
        print("The Binary Value is : ",a)
    elif question==2:
        Decimal = int(input('Enter the Decimal value : '))
        b=Decimal_to_Octal(Decimal)
        print("The Octal Value is : ",b)
    elif question==3:
        Decimal = int(input('Enter the Decimal value : '))
        c=Decimal_to_Hexadecimal(Decimal)
        print("The Hexadecimal Value is : ",c)

    elif question==4:
        Binary = int(input('Enter the Binary value : '))
        d=Binary_to_Decimal(Binary)
        print("The Decimal Value is : ",d)
    elif question==5:
        Binary = int(input('Enter the Binary value : '))
        e=Binary_to_Octal(Binary)
        print("The Octal Value is : ",e)
    elif question==6:
        Binary = int(input('Enter the Binary value : '))
        f=Binary_to_Hexadecimal(Binary)
        print("The Hexadecimal Value is : ",f)

    elif question==7:
        Octal = int(input('Enter the Octal value : '))
        g=Octal_to_Decimal(Octal)
        print("The Decimal Value is : ",g)
    elif question==8:
        Octal = int(input('Enter the Octal value : '))
        h=Octal_to_Binary(Octal)
        print("The Binary Value is : ",h)
    elif question==9:
        Octal = int(input('Enter the Octal value : '))
        i=Octal_to_Hexadecimal(Octal)
        print("The Hexadecimal Value is : ",i)

    elif question==10:
        Hexadecimal = str(input('Enter the Hexadecimal value : '))
        f=Hexadecimal_to_Decimal(Hexadecimal)
        print("The Decimal Value is : ",f)
    elif question==11:
        Hexadecimal = str(input('Enter the Hexadecimal value : '))
        f=Hexadecimal_to_Binary(Hexadecimal)
        print("The Binary Value is : ",f)
    elif question==12:
        Hexadecimal = str(input('Enter the Hexadecimal value : '))
        f=Hexadecimal_to_Octal(Hexadecimal)
        print("The Octal Value is : ",f)
    elif question==0:

        print("Thanks for using our app meet soon , Have a great Day")
        exit()
    else:
        print("welome back")
        exit()
        

