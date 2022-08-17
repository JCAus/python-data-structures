def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for char in phrase:
        if char.isupper() is True and char == to_swap:
            char.lower()
        if char.isupper() is False and char == to_swap:
            char.upper()
    print(phrase)
flip_case('Hello how are you', 'h')