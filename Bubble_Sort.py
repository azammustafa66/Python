def main():
    mark = input("Enter marks separated by space: ")
    marks = mark.split()

    for i in range(len(marks)):
        marks[i] = int(marks[i])

    print(bubble(marks))


def bubble(marks):
    for i in range(0, len(marks)):
        swap = False
        for j in range(1, len(marks) - i):
            if marks[j - 1] > marks[j]:
                marks[j - 1], marks[j] = marks[j], marks[j - 1]
                swap = True
        if not swap:
            break
    return marks[len(marks) - 1]


main()
