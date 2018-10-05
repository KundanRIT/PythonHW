def findMinIndex(start, itemList):
    minItem = itemList[start-1]
    minIndex = start-1
    for index in range(start, len(itemList)):
        if minItem > itemList[index]:
            minItem = itemList[index]
            minIndex = index
    return minIndex


def ssort(itemList):
    """
    Perform Selection Sort
    :param itemList:
    :return:
    """
    for index, item in enumerate(itemList):
        if index == (len(itemList) - 1):
            break
        minIndex = findMinIndex(index + 1, itemList)
        itemList[index], itemList[minIndex] = \
            itemList[minIndex], itemList[index]
    return itemList


def divide(itemList):
    mid = len(itemList) // 2
    return itemList[:mid], itemList[mid:]


def merge(left, right):
    mergedList = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            mergedList.append(left[leftIndex])
            leftIndex += 1
        else:
            mergedList.append(right[rightIndex])
            rightIndex += 1
    if leftIndex < len(left):
        mergedList.extend(left[leftIndex:])
    if rightIndex < len(right):
        mergedList.extend(right[rightIndex:])
    return mergedList


def msort(itemList):
    """
    Perform Merge Sort (Divide and Conquer Algorithm )
    :param itemList:
    :return:
    """
    if len(itemList) < 2:
        return itemList
    else:
        left, right = divide(itemList)
        return merge(msort(left), msort(right))


def isort(itemList):
    """
    Perform Insertion Sort
    :param itemList:
    :return:
    """
    for indexI in range(len(itemList)-1):
        if itemList[indexI] > itemList[indexI+1]:
            for indexJ in range(indexI,-1,-1):
                if itemList[indexJ] > itemList[indexJ+1]:
                    itemList[indexJ], itemList[indexJ+1] = \
                        itemList[indexJ+1], itemList[indexJ]
                else:
                    break
    return itemList


def partition(itemList, low, high):
    pivot = itemList[high]
    swapIndex = low
    for traverseIndex in range(low, high):
        if itemList[traverseIndex] <= pivot:
            itemList[swapIndex], itemList[traverseIndex] = itemList[traverseIndex], itemList[swapIndex]
            swapIndex += 1
    itemList[swapIndex], itemList[high] = itemList[high], itemList[swapIndex]
    return swapIndex


def quicksort(itemList, low, high):
    if low < high:
        partitionIndex = partition(itemList, low, high)
        quicksort(itemList, low, partitionIndex-1)
        quicksort(itemList, partitionIndex+1, high)
        return itemList


def qsort(itemList):
    """
    Perform Quick Sort (Divide and Conquer Algorithm)
    :param itemList:
    :return:
    """
    return quicksort(itemList, 0, len(itemList)-1)


if __name__ == '__main__':
    print(ssort([6,5,4,3,2,1]))
    print(msort([6,5,4,3,2,1]))
    print(isort([6,5,4,3,2,1]))
    print(qsort([6,5,4,3,2,1]))