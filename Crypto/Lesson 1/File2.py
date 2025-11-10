def insertion_sort(arr):
    # Проходимо по кожному елементу масиву, починаючи з другого
    for i in range(1, len(arr)):
        key = arr[i] # Зберігаємо поточний елемент для порівняння
        j = i - 1
        # Переміщаємо елементи масиву, що більші за ключ, на одну позицію вперед
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            # Вставляємо ключ в правильну позицію
            arr[j + 1] = key
    return arr



# Приклад використання
arr = [12, 11, 13, 5, 6]
print("До сортування:", arr)
sorted_arr = insertion_sort(arr)
print("Після сортування:", sorted_arr)


