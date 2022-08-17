def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    number1 = [int(a) for a in str(num1)]
    number2 = [int(b) for b in str(num2)]

    

    number1.sort()
    number2.sort()

    if number1 == number2:
        print('True')
    if number1 != number2:
        print('False')

same_frequency(551122, 221515) 
same_frequency(321142, 3212215)  
same_frequency(1212, 2211)