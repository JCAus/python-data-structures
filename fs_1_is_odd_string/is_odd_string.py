def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    ltr_val_total = 0
    for char in word:
        big_char = char.upper()
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ltr_val_total += abc.index(big_char) + 1

        print(ltr_val_total)
    
    if ltr_val_total % 2 == 1:
        print('True')
    if ltr_val_total % 2 == 0:
        print('False')

is_odd_string('AAaa') 
is_odd_string('amazing')  

