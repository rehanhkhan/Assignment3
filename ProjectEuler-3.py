def getPrimeNumbers(maxnumber=100):
    wholeNum = 2
    primeNums = []
    rem = 1
    while(wholeNum<maxnumber):
        #get half value of whole number to check existance in any other number
        Denominator = round(wholeNum/2)
        while(Denominator > 1 and rem > 0):
            rem = wholeNum % Denominator
            Denominator -=1
        if rem > 0:
            primeNums.append(wholeNum)
        rem = 1
        wholeNum += 1
    return primeNums


primeNumbers = getPrimeNumbers(10000)
factorial = 600851475143
factors = []
while(factorial>1):
    rem=1
    index = -1
    while(rem > 0):
        index+=1
        rem = factorial % primeNumbers[index]
        print(str(rem) + ' - ' + str(primeNumbers[index]) + ' - ' + str(factorial))

    factorial = factorial / primeNumbers[index]
    factors.append(primeNumbers[index])

print(factors)
print(max(factors))

