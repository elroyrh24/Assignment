def discount(ogPrice):
    ogPrice -= ogPrice * 0.05
    return ogPrice

def limitCheck(Salary):
    if type(Salary) == int :
        if ( 9000000 - discount(Salary) ) <= 0:
            return True
        else:
            return False
    else:
        return
    

DirtyListGaji = list(
    input("\nEnter the salaries : ").strip().split())

toberemoved = '.'

def cleaning(Number):
    cleanedNum = ''
    for n in Number:
        if n not in toberemoved:
            cleanedNum += n
    return cleanedNum

    
def TrueClean(Pay):
    calcPay = int(cleaning(Pay))
    if limitCheck(calcPay) == True:
        return Pay
    else:
        return 



print(str(list(filter(TrueClean, DirtyListGaji))))
