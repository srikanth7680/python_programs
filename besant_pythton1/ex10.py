#Ascii
val = input("Enter the name")
for x in val:
    ord_val = ord(x)
    if ord_val>=65 and ord_val<=90:
        chr_val = ord_val+32
        print(chr(chr_val),end='')
    elif ord_val>=97 and ord_val<=122:
        chr_val = ord_val - 32
        print(chr(chr_val), end='')
    else:
        pass

#amar---> AMAR
'''val1 = "amar"
for y in val1:
    ord_val = ord(y)
    if ord_val>=97 and ord_val<=122:
        chr_val = ord_val - 32
        print(chr(chr_val),end='')
    else:
        pass'''