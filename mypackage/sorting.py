def top_n(items, n):
    """
    Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """

    for i in range(n):  # keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # if this item is bigger than next item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # get last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]

def bubble_sort(items):

    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): list or array-like object containing numerical or
        string values .

    Returns:
        array: returns array sorted in ascending by bubbling items.

    Examples:
        >>> bubble_sort([5, 1 ,4, 2 ,8 ])
        [1, 2, 4, 5, 8]

    '''

    bubbled_list = items.copy()
    for i in range(len(bubbled_list)):
        for x in range(len(bubbled_list)-1-i):
            if bubbled_list[x] > bubbled_list[x+1]:
                bubbled_list[x],bubbled_list[x+1] = bubbled_list[x+1],bubbled_list[x]
    return bubbled_list

def merge(list1, list2):

    '''
    Given an ordered 2 list ,Returns 1 array of items, sorted in ascending order

    Args:
        list1,list2 (array): list or array-like object containing numerical or
        string or values.

    Returns:
        array: returns

    Examples:
        >>> merge_sort([1,2,3].[3,5])
        [1, 2, 3, 4, 5]
        >>> merge_sort([5] ,[3])
        [4, 6, 6, 8, 10, 23, 82]
    '''

    merge_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            merge_list.append(list1.pop(0))

        else:
            merge_list.append(list2.pop(0))

    if len(list1) == 0:
        merge_list.extend(list2)
    else:
        merge_list.extend(list1)

    return merge_list

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): list or array-like object containing numerical or string
        or values.

    Returns:
        array: returns array sorted in ascending order by recusively splitting
        the array in half and passing it to the merge function that returns a merged
        sorted list.

    Examples:
        >>> merge_sort([1,2,3,6,5,4])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sort([10,6,6,8,4,23,82])
        [4, 6, 6, 8, 10, 23, 82]

  '''

    list_len = len(items)

    if list_len == 1:
        return items

    mid_point = int(list_len / 2)
    half1 = merge_sort(items[:mid_point])
    half2 = merge_sort(items[mid_point:])

    return merge(half1, half2)
