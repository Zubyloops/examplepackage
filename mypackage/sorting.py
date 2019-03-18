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

            if items[j] > items[j+1]:  # if this item is bigger than next item.
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

    l_copy = items.copy() # in place protection on items
    for i in range(len(l_copy)): # iteratively sweeping through every item.
        for x in range(len(l_copy)-1-i):
            if l_copy[x] > l_copy[x+1]: # if this item is bigger than next item
                l_copy[x],l_copy[x+1] = l_copy[x+1],l_copy[x] # swop item places
    return l_copy

def merge(list1, list2):

    '''
    Given an 2 ordered lists ,Returns 1 array of lists merged, sorted in
    ascending order

    Args:
        list1,list2 (array): list or array-like object containing numerical or
        string or values.

    Returns:
        array: returns singular array of the two lists merged in ascending
        order

    Examples:
        >>> merge_sort([1,2,3],[3,5])
        [1, 2, 3, 4, 5]
        >>> merge_sort([5] ,[3])
        [3,5]
    '''

    # initializing empty list1
    merge_list = []
    # while loop to add items to empty list
    while len(list1) > 0 and len(list2) > 0: # both lists lenth cannot be zero
        if list1[0] < list2[0]: # if this item is smaller than other item
            merge_list.append(list1.pop(0)) # pop and append list1 1st item

        else:
            merge_list.append(list2.pop(0)) # else pop and append list2 2nd item

    # extends the remaining item to the merged list depending on length of list
    if len(list1) == 0:
        merge_list.extend(list2)
    if len(list2) == 0
        merge_list.extend(list1)

    # returns merged list in ascending order
    return merge_list

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order

    Args:
        items (array): list or array-like object containing numerical or string
        or values.

    Returns:
        array: returns array sorted in ascending order by recusively splitting
        the array in half and passing the halfs recursively to the merge
        function that returns a merged sorted list.

    Examples:
        >>> merge_sort([1,2,3,6,5,4])
        [1, 2, 3, 4, 5, 6]
        >>> merge_sort([10,6,6,8,4,23,82])
        [4, 6, 6, 8, 10, 23, 82]

  '''
    # length of array
    list_len = len(items)

    # returns array if list is 1 array
    if list_len == 1:
        return items

    mid_point = int(list_len / 2) # index of the mid point of array
    half1 = merge_sort(items[:mid_point]) # recusively halfs array to eventually
    half2 = merge_sort(items[mid_point:]) # get 2 sublists of 1 item

    # inputs the 2 sublists in the function to be merged in ascending order
    return merge(half1, half2)

def quick_sort(items):

    '''
    Takes in an unsorted list of numbers,returns a list in ascending order
    using quick sort algorithm.

    Args:
        items (array): list or array-like object containing numerical or string
        or values.

    Ruturns:
        items (array): list or array-like object containing numerical or string
        or values.

    Examples:
        >>> quick_sort([1,2,3,8,7])
        [1, 2, 3, 7, 8]
        >>> quick_sort([9,25,25,3,7,1,1])
        [1, 1, 3, 7, 9, 25, 25]
    '''
    len_i = len(items)

    if len_i <= 1:
        # Logic Error
        return items

    # initializing
    pivot = items[-1] # takes last item of array as pivot variable
    small = []
    large = []
    dup = [] # list of the pivots

    # sorting items to their respective list
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    #recusively breaking up the list into sublists around the pivot point
    small = quick_sort(small)
    large = quick_sort(large)

    # returns a joined list by adding the small, pivot and large list together
    # reppectively
    return small + dup + large
