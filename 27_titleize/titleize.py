def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    answer = []
    each_word = phrase.split(' ')
    for word in each_word:
        answer.append(word.capitalize())
    return ' '.join(answer)