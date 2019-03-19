def sum_array(array):
    '''
    Return sum of all items in array

    Args:
         items (array): list or array-like object containing numerical values
         or string not both.


    Returns:
         int or float or string (depending if all items is the same type): sum of all
         items in array.

    Examples:
         >>> sum_array([1,2,3,4])
         10
         >>> sum_array('a','bb')
         'abb'
    '''
    if len(array) == 1:
        return array[0]
    return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''
    Return nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(7)
        13
    '''

    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''
    Return n!

    Args:
        n (int): interger number to calculate the factorial of.

    Returns:
        int: n! is the number we get when we multiply every number from 1 to 𝑛.

    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        120
    '''

    if n == 0 or n == 1:
        return n
    return n * factorial(n-1)

def reverse(word):

    '''
    Return word in reverse

    Args:
        word (str): string that will be returned where the order is reversed.

    Returns:
        str: reversed string order of word.

    Examples:
        >>> reverse('some')
        'emos'
        >>> reverse('words')
        'sdrow'
    '''

    if len(word) == 1:
        return word
    return word[-1] + reverse(word[:-1])
