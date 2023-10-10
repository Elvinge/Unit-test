import pytest
from main import ListComparator

def test_compare_averages():
    # Test case 1: First list has a greater average
    lc = ListComparator([1, 2, 3], [4, 5, 6])
    assert lc.compare_averages() == "Первый список имеет большее среднее значение"

    # Test case 2: Second list has a greater average
    lc = ListComparator([4, 5, 6], [1, 2, 3])
    assert lc.compare_averages() == "Второй список имеет большее среднее значение"

    # Test case 3: Both lists have equal averages
    lc = ListComparator([1, 2, 3], [4, 5, 6])
    assert lc.compare_averages() == "Средние значения равны"

    # Test case 4: Empty lists, should return "Средние значения равны"
    lc = ListComparator([], [])
    assert lc.compare_averages() == "Средние значения равны"

    # Test case 5: One list is empty, should return "Второй список имеет большее среднее значение"
    lc = ListComparator([1, 2, 3], [])
    assert lc.compare_averages() == "Второй список имеет большее среднее значение"

def test_calculate_average():
    # Test case 1: Non-empty list
    lc = ListComparator([1, 2, 3], [])
    assert lc.calculate_average([1, 2, 3]) == 2

    # Test case 2: Empty list
    lc = ListComparator([], [])
    assert lc.calculate_average([]) == 0
