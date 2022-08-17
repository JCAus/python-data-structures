def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lc_phrase = phrase.lower()
    vowel_count = {char: lc_phrase.count(char) for char in lc_phrase if char in 'aeiou'}
    print(vowel_count)

vowel_count('HOW ARE YOU? i am great!')
vowel_count('rithm school')