def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phraseLen = len(phrase) - 1
    forward = phrase[0:phraseLen:1]
    backward = phrase[phraseLen:0:-1]

    if forward == backward:
        print('True')
    else:
        print('False')

is_palindrome('wow')