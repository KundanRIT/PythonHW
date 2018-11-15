# instrumented_sort.py (Python HW 5)
# Author: Kundan Kumar (kk7272) & Deepam Shah (ds3689)

def findMinIndex(start, itemList):
    """
    Selection Sort Helper - Finds index of the smallest element in the list
    after starting index
    :param start:
    :param itemList:
    :return: index
    """
    minItem = itemList[start-1]
    minIndex = start-1
    comparisons = 0
    for index in range(start, len(itemList)):
        if minItem > itemList[index]:
            minItem = itemList[index]
            minIndex = index
        comparisons += 1
    return minIndex, comparisons


def ssort(itemList):
    """
    Perform Selection Sort
    :param itemList:
    :return:
    """
    all_comparisons = 0
    for index, item in enumerate(itemList):
        if index == (len(itemList) - 1):
            break
        minIndex, comparisons = findMinIndex(index + 1, itemList)
        itemList[index], itemList[minIndex] = \
            itemList[minIndex], itemList[index]
        all_comparisons += comparisons
    return itemList, all_comparisons


def divide(itemList):
    """
    Merge Sort Helper - Divides the list into two halves, left and right
    :param itemList:
    :return: tuple left half of list and right part of list
    """
    mid = len(itemList) // 2
    return itemList[:mid], itemList[mid:]


def merge(left, right):
    """
    Merge Sort Helper - Merge the left and right half of the list
    :param left: list
    :param right: list
    :return: merged and sorted list
    """
    mergedList = []
    leftIndex = 0
    rightIndex = 0
    comparisons = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            mergedList.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedList.append(right[rightIndex])
            rightIndex += 1
        comparisons += 1
    if leftIndex < len(left):
        mergedList.extend(left[leftIndex:])
    if rightIndex < len(right):
        mergedList.extend(right[rightIndex:])
    return mergedList, comparisons


def msort(itemList):
    """
    Perform Merge Sort (Divide and Conquer Algorithm )
    :param itemList:
    :return:
    """
    if len(itemList) < 2:
        return itemList, 0
    else:
        left, right = divide(itemList)
        left, left_comparison = msort(left)
        right, right_comparision = msort(right)
        mergedList, merge_comparison = merge(left, right)
        return mergedList, left_comparison+right_comparision+merge_comparison


def isort(itemList):
    """
    Perform Insertion Sort
    :param itemList:
    :return:
    """
    comparisons = 0
    for indexI in range(len(itemList)-1):
        if itemList[indexI] > itemList[indexI+1]:
            for indexJ in range(indexI,-1,-1):
                if itemList[indexJ] > itemList[indexJ+1]:
                    itemList[indexJ], itemList[indexJ+1] = \
                        itemList[indexJ+1], itemList[indexJ]
                else:
                    break
                comparisons += 1
        comparisons += 1
    return itemList, comparisons


def partition(itemList, low, high):
    """
    Quick Sort Helper - Partitions the list around the pivot with numbers
    smaller than pivot on pivots left side and numbers greater than pivot on
    pivots right side.
    pivot = last element in list
    :param itemList: list
    :param low: lower bound
    :param high: upper bound
    :return: partitioned list
    """
    pivot = itemList[high]
    swapIndex = low
    comparisons = 0
    for traverseIndex in range(low, high):
        if itemList[traverseIndex] <= pivot:
            itemList[swapIndex], itemList[traverseIndex] = \
                itemList[traverseIndex], itemList[swapIndex]
            swapIndex += 1
        comparisons += 1
    itemList[swapIndex], itemList[high] = itemList[high], itemList[swapIndex]
    return swapIndex, comparisons


def quicksort(itemList, low, high, allcomparisons):
    """
    Initiates Quick Sort Recursion
    :param itemList: given list
    :param low: lower bound
    :param high: upper bound
    :param allcomparisons: keeps track of comparisons made
    :return: sorted list
    """
    if low < high:
        partitionIndex, part_comparison = partition(itemList, low, high)
        allcomparisons += part_comparison
        itemList, low_comparison = quicksort(itemList, low, partitionIndex-1,
                                             allcomparisons)
        itemList, high_comparison = quicksort(itemList, partitionIndex+1, high,
                                              low_comparison)
        allcomparisons = high_comparison
    return itemList, allcomparisons


def qsort(itemList):
    """
    Perform Quick Sort (Divide and Conquer Algorithm)
    :param itemList:
    :return:
    """
    return quicksort(itemList, 0, len(itemList)-1, 0)


if __name__ == '__main__':
    print(ssort([6,5,4,3,2,1]))
    print(msort([6,5,4,3,2,1]))
    print(isort([6,5,4,3,2,1]))
    print(qsort([6,5,4,3,2,1]))