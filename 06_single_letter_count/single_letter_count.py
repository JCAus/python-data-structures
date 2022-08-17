def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    letter_count = 0

    word = word.lower()

    for char in word:
        if char in letter:
            letter_count += 1
    
    print(letter_count)

single_letter_count('How are you today', 'o')