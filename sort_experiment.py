import random
import sys
from time import time
from instrumented_sort import ssort, msort, isort, qsort
import matplotlib.pyplot as plt


def generateData(size):
    return random.sample(range(size), size)


def check_sorted(itemList):
    for index in range(len(itemList)-1):
        if itemList[index] > itemList[index+1]:
            return False
    return True


def main():
    # fetch size from commandline
    if len(sys.argv) > 1:
        size = int(sys.argv[1])
    else:
        size = 10000
    comparisions = 1234
    # generate data
    testData = generateData(size)
    selectionSortList = testData.copy()
    mergeSortList = testData.copy()
    insertionSortList = testData.copy()
    quickSortList = testData.copy()

    # test selection sort
    start_time = time()
    selectionSortList, ssort_comparisons = ssort(selectionSortList)
    end_time = time()
    ssort_time = end_time - start_time
    if check_sorted(selectionSortList):
        print("Selection Sort : Sorting Works !!!")
    else:
        print("Selection Sort : Sorting Did Not Work !!!")

    # test merge sort
    start_time = time()
    mergeSortList, msort_comparisons = msort(mergeSortList)
    end_time = time()
    msort_time = end_time - start_time
    if check_sorted(mergeSortList):
        print("Merge Sort : Sorting Works !!!")
    else:
        print("Merge Sort : Sorting Did Not Work !!!")

    # test insertion sort
    start_time = time()
    insertionSortList, isort_comparisons = isort(insertionSortList)
    end_time = time()
    isort_time = end_time - start_time
    if check_sorted(insertionSortList):
        print("Insertion Sort : Sorting Works !!!")
    else:
        print("Insertion Sort : Sorting Did Not Work !!!")

    # test quick sort
    start_time = time()
    quickSortList, qsort_comparisons = qsort(quickSortList)
    end_time = time()
    qsort_time = end_time - start_time
    if check_sorted(quickSortList):
        print("Quick Sort : Sorting Works !!!")
    else:
        print("Quick Sort : Sorting Did Not Work !!!")

    # log report
    with open("observations.txt", "a") as observation:
        print("ALGORITHM\t\tSIZE\tCOMPARISONS\tSECONDS")
        print("Selection Sort\t{}\t{}\t\t{}".format(size, ssort_comparisons,
                                                    ssort_time))
        print("Merge Sort\t\t{}\t{}\t\t{}".format(size, msort_comparisons,
                                                  msort_time))
        print("Insertion Sort\t{}\t{}\t\t{}".format(size, isort_comparisons,
                                                    isort_time))
        print("Quick Sort\t\t{}\t{}\t\t{}".format(size, qsort_comparisons,
                                                    qsort_time))
        observation.write("\nALGORITHM\t\tSIZE\tCOMPARISONS\tSECONDS\n")
        observation.write("Selection Sort\t{}\t{}\t\t{}\n"
                          .format(size, ssort_comparisons, ssort_time))
        observation.write("Merge Sort\t\t{}\t{}\t\t{}\n"
                          .format(size, msort_comparisons,msort_time))
        observation.write("Insertion Sort\t{}\t{}\t\t{}\n"
                          .format(size, isort_comparisons, isort_time))
        observation.write("Quick Sort\t\t{}\t{}\t\t{}\n\n"
                          .format(size, qsort_comparisons, qsort_time))

    # generate report
    x = ["Selection Sort","Merge Sort","Insertion Sort","Quick Sort"]
    y = [ssort_time, msort_time, isort_time, qsort_time]
    plt.bar(x, y, label="Time Chart", color="b")
    plt.xlabel("Sorting Techniques")
    plt.ylabel("Time Taken (Seconds)")
    plt.title("Sorting Time")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()