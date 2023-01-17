def main():
    arr = [4, 5, 3, 2, 1, 0]
    insertion_sort(arr)
    print(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


main()
