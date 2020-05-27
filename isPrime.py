

def inputNumber(answer):
  while True:
    try:
       userInput = int(input(answer))       
    except ValueError:
       print("Not an integer! Try again :)")
       continue
    else:
       return userInput 
       break 
     

toCheck = inputNumber("Tell me an integer to check: ")
alreadyFound = set()

def isPrime(toCheck):
    if toCheck < 2:
        print("Only integers greater than 1 can be primes")
    else: 
        divisor = 2
        if toCheck not in alreadyFound:
            while divisor <= toCheck/2:
                if toCheck % divisor == 0:
                    print("{} is not prime! It can be divided by {}".format(toCheck, divisor))
                    alreadyFound.add(toCheck)
                    break
                else:
                    divisor = divisor + 1
            else: print("It seems that {} is perfectly prime!".format(toCheck))
        else:
            print("It seems that {} is perfectly prime and you've already checked it :)".format(toCheck))
    
isPrime(toCheck)