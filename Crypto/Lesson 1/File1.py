def bubble_sort(arr, asc=True):
    n = len(arr)
    # Проходимо по всіх елементах масиву
    if asc:
        for i in range(n):
            # Останні i елементів вже відсортовані
            for j in range(0, n-i-1):
                # Якщо поточний елемент більший за наступний, міняємо їх місцями
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    elif not asc:
        for i in range(n):
            # Останні i елементів вже відсортовані
            for j in range(0, n-i-1):
                # Якщо поточний елемент більший за наступний, міняємо їх місцями
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    else:
        print("Помилка")

    # Приклад використання
arr = [64, 34, 25, 12, 22, 11, 90]
print("Невідсортований список:", arr)

bubble_sort(arr)
print("Відсортований список:", arr)
bubble_sort(arr, False)
print("Відсортований список зворотньо:", arr)