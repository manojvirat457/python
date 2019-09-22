



def outerFunction(message):
    
    def innerFunction():
        print(message)
    
    return innerFunction

result = outerFunction("Vetri")
result1 = outerFunction("Namadhe")

outerFunction("Hai Heelo")

result()
result1()