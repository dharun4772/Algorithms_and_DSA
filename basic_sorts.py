def bubble_sort(arr):
    for i in range(len(arr)):
        j = 1
        flag = 0
        while j <= len(arr) - 1 - i:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                flag = 1
            j += 1
        if flag == 0:
            return


def selection_sort(arr):
    for i in range(len(arr)):
        small = arr[i]
        pos = i
        j = i + 1
        while j <= len(arr) - 1:
            if small > arr[j]:
                small = arr[j]
                pos = j
            j += 1
        arr[i], arr[pos] = arr[pos], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quick_sort_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot = quick_sort_partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def merge_sort(arr, low, high):
    if low < high:
        mid = len(arr) // 2
        arr1 = merge_sort(arr[low,mid], low, mid)
        arr2 = merge_sort(arr[low,mid], mid + 1, high)
        final = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                final.append(arr1[i])
                i += 1
            else:
                final.append(arr2[j])
                j += 1
        if i < len(arr1):
            final.append(arr1[i:])
        if j < len(arr2):
            final.append(arr2[j:])
        return final
    return arr


import time

arr = [10, 11, 1, 2, 99, 14, 10, 5]
st = time.perf_counter()
# bubble_sort(arr)
# selection_sort(arr)
# insertion_sort(arr)
# quick_sort(arr, 0, len(arr) - 1)
merge_sort(arr, 0, len(arr))
end = time.perf_counter()
print(arr, end - st)
