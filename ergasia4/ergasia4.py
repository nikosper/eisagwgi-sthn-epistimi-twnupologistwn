def letter_to_number(mylist):
    mylist[0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'sevem',8:'eight',9:'nine']

    return

firstnumber=input('you have to put the firt number')
choosepraxis=input('you have to choose the praxis')
secondnumber=input('you have to put the second number')




if firstnumber == 'zero':
    firstnumber = 0
if secondnumber == 'zero':
    secondnumber = 0
if firstnumber == 'one':
    firstnumber = 1
if secondnumber == 'one' :
    secondnumber = 1
if firstnumber == 'two':
 firstnumber = 2
if secondnumber == 'two':
    secondnumber = 2
if firstnumber == 'three':
    firstnumber = 3
if secondnumber == 'three' :
    secondnumber = 3
if firstnumber == 'four':
    firstnumber = 4
if secondnumber == 'four' :
    secondnumber = 4
if firstnumber == 'five':
 firstnumber = 5
if secondnumber == 'five':
    secondnumber = 5
if firstnumber == 'six':
    firstnumber = 6
if secondnumber == 'six' :
    secondnumber = 6
if firstnumber == 'seven':
    firstnumber = 7
if secondnumber == 'seven' :
    secondnumber = 7
if firstnumber == 'eight':
 firstnumber = 8
if secondnumber == 'eight':
    secondnumber = 8
if firstnumber == 'nine':
    firstnumber = 9
if secondnumber == 'nine' :
    secondnumber = 9



if firstnumber == '' and choosepraxis == '' and secondnumber =='':
    print("put number")
else:
    if choosepraxis == "plus":

        sum= int(firstnumber) + int(secondnumber)
        if firstnumber == 0:
            firstnumber = 'zero'
        if secondnumber == 0:
            secondnumber = 'zero'
        if firstnumber == 1:
            firstnumber = 'one'
        if secondnumber == 1:
            secondnumber = 'one'
        if firstnumber == 2:
            firstnumber = 'two'
        if secondnumber == 2:
            secondnumber = 'two'
        if firstnumber == 3:
            firstnumber = 'three'
        if secondnumber == 3:
            secondnumber = 'three'
        if firstnumber == 4:
            firstnumber = 'four'
        if secondnumber == 4:
            secondnumber = 'four'
        if firstnumber == 5:
            firstnumber = 'five'
        if secondnumber == 5:
            secondnumber = 'five'
        if firstnumber == 6:
            firstnumber = 'six'
        if secondnumber == 6:
            secondnumber = 'six'
        if firstnumber == 7:
            firstnumber = 'seven'
        if secondnumber == 7:
            secondnumber = 'seven'
        if firstnumber == 8:
            firstnumber = 'eight'
        if secondnumber == 8:
            secondnumber = 'eight'
        if firstnumber == 9:
            firstnumber = 'nine'
        if secondnumber == 9:
            secondnumber = 'nine'

        print (firstnumber,"(",choosepraxis,"(",secondnumber,"))","ΕΞΟΔΟΣ",sum)
    elif choosepraxis == "times":
       Multiplying = firstnumber * secondnumber
       if firstnumber == 0:
           firstnumber = 'zero'
       if secondnumber == 0:
           secondnumber = 'zero'
       if firstnumber == 1:
           firstnumber = 'one'
       if secondnumber == 1:
           secondnumber = 'one'
       if firstnumber == 2:
           firstnumber = 'two'
       if secondnumber == 2:
           secondnumber = 'two'
       if firstnumber == 3:
           firstnumber = 'three'
       if secondnumber == 3:
           secondnumber = 'three'
       if firstnumber == 4:
           firstnumber = 'four'
       if secondnumber == 4:
           secondnumber = 'four'
       if firstnumber == 5:
           firstnumber = 'five'
       if secondnumber == 5:
           secondnumber = 'five'
       if firstnumber == 6:
           firstnumber = 'six'
       if secondnumber == 6:
           secondnumber = 'six'
       if firstnumber == 7:
           firstnumber = 'seven'
       if secondnumber == 7:
           secondnumber = 'seven'
       if firstnumber == 8:
           firstnumber = 'eight'
       if secondnumber == 8:
           secondnumber = 'eight'
       if firstnumber == 9:
           firstnumber = 'nine'
       if secondnumber == 9:
           secondnumber = 'nine'
       print(firstnumber,"(",choosepraxis,"(",secondnumber,"))","ΕΞΟΔΟΣ",Multiplying)
    elif choosepraxis == "minus":
        plin = firstnumber - secondnumber
        if firstnumber == 0:
            firstnumber = 'zero'
        if secondnumber == 0:
            secondnumber = 'zero'
        if firstnumber == 1:
            firstnumber = 'one'
        if secondnumber == 1:
            secondnumber = 'one'
        if firstnumber == 2:
            firstnumber = 'two'
        if secondnumber == 2:
            secondnumber = 'two'
        if firstnumber == 3:
            firstnumber = 'three'
        if secondnumber == 3:
            secondnumber = 'three'
        if firstnumber == 4:
            firstnumber = 'four'
        if secondnumber == 4:
            secondnumber = 'four'
        if firstnumber == 5:
            firstnumber = 'five'
        if secondnumber == 5:
            secondnumber = 'five'
        if firstnumber == 6:
            firstnumber = 'six'
        if secondnumber == 6:
            secondnumber = 'six'
        if firstnumber == 7:
            firstnumber = 'seven'
        if secondnumber == 7:
            secondnumber = 'seven'
        if firstnumber == 8:
            firstnumber = 'eight'
        if secondnumber == 8:
            secondnumber = 'eight'
        if firstnumber == 9:
            firstnumber = 'nine'
        if secondnumber == 9:
            secondnumber = 'nine'
        print(firstnumber, "(", choosepraxis, "(", secondnumber, "))", "ΕΞΟΔΟΣ",plin)