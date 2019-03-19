from mypackage import sorting
from mypackage import recursion

def test_merge():
    '''
    make sure bubble_sort works correctly
    '''
    assert sorting.merge([1,2,3],[3,5]) == [1, 2, 3, 3, 5], 'incorrect'
    assert sorting.merge([5],[3]) == [3, 5], 'incorrect'
    assert sorting.merge(['abc','k'],['dd','xyz']) == [
    'abc', 'dd', 'k', 'xyz'],'incorrect'

def test_merge_sort():
    '''
    make sure bubble_sort works correctly
    '''
    assert sorting.merge_sort([1,2,3,6,5,4]) == [
    1, 2, 3, 4, 5, 6], 'incorrect'
    assert sorting.merge_sort([10,6,6,8,4,23,82]) == [
    4, 6, 6, 8, 10, 23, 82], 'incorrect'
    assert sorting.merge_sort(['word','abc','xyz','something']) == [
    'abc', 'something', 'word', 'xyz'], 'incorrect'

def test_quick_sort():
    '''
    make sure bubble_sort works correctly
    '''
    assert sorting.quick_sort([1,2,3,8,7]) == [1, 2, 3, 7, 8], 'incorrect'
    assert sorting.quick_sort([9,25,25,3,7,1,1]) == [
    1, 1, 3, 7, 9, 25, 25], 'incorrect'
    assert sorting.quick_sort(['dee','avs','bee','eks']) == [
    'avs', 'bee', 'dee', 'eks'], 'incorrect'

def test_sum_array():
    '''
    make sure sum_array works correctly
    '''
    assert recursion.sum_array([1,2,3,4]) == 10, 'incorrect'
    assert recursion.sum_array([5.5, 3.9 ,10,17]) == 36.4, 'incorrect'
    assert recursion.sum_array(['eks','deeee']) == 'eksdeeee', 'incorrect'

def test_fibonacci():
    '''
    make sure fibonacci works correctly
    '''
    assert recursion.fibonacci(1) == 1, 'incorrect'
    assert recursion.fibonacci(7) == 13, 'incorrect'
    assert recursion.fibonacci(15) == 610, 'incorrect'

def test_factorial():
    '''
    make sure factorial works correctly
    '''
    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(1) == 1, 'incorrect'
    assert recursion.factorial(13) == 6227020800, 'incorrect'

def test_reverse():
    '''
    make sure reverse works correctly
    '''
    assert recursion.reverse('some') == 'emos', 'incorrect'
    assert recursion.reverse('Hanah') == 'hanaH', 'incorrect'
    assert recursion.reverse('words') =='sdrow', 'incorrect'
