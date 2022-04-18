def listSortAscending (listToSort):
    """Sorts the contents of a list in ascending order.

    :param list listToSort: The items to be sorted.
    :raise TypeError:
        listToSort must be like items; cannot compare strings to
        ints/floats
    :rtype: None
    """
    # this index...
    for targetIndex in range (0, len (listToSort) - 1):
        # ...compared to this index
        for comparisonIndex in range (targetIndex + 1, len (listToSort)):
            if listToSort[targetIndex] > listToSort[comparisonIndex]:
                # target character
                temp = listToSort[comparisonIndex]
                # character moved into unsorted series
                listToSort[comparisonIndex] = listToSort[targetIndex]
                # target character moved into sorted position
                listToSort[targetIndex] = temp