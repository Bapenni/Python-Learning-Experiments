
my_list = [307, 215, 1923, 294, 111, 439, 5960, 6599, 4932, 293, 502, 950]
unsorted = my_list.copy()


def bubbly_sort(numbers):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                placeholder = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = placeholder


bubbly_sort(my_list)

print(unsorted)
print(my_list)
