# -*- coding: utf-8 -*-

print "Dobrodošli v kalkulator!"
operator = ""
rezultat = ""
zanka1=False
zanka2=False
while zanka1 == False:
    prvaSt= raw_input("Vnesi prvo število: ")
    try:
        prvaSt = float(prvaSt)
        zanka1 = True
    except ValueError:
        print "Napaka"


while operator == "":
    vnosOperatorja= raw_input("Vnesi operator ( + / - / * / / / % : ")
    if vnosOperatorja == "+" or vnosOperatorja == "-" or vnosOperatorja == "*" or vnosOperatorja == "/" or vnosOperatorja == "%" :
        operator = vnosOperatorja



while zanka2 == False:
    drugaSt= raw_input("Vnesi drugo število: ")
    try:
        drugaSt = float(drugaSt)
        zanka2 = True
    except ValueError:
        print "Napaka"


print eval(str(prvaSt)+operator+str(drugaSt))
