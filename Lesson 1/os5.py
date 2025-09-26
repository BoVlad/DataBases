import os

file_names = os.listdir()
file_full_name = []
file_full_size = []
file_sorted_dict = {}

for i in file_names:
    file_full_name.append(i)
    file_full_size.append(os.path.getsize(i))

for i in file_full_name:
    valmax = max(file_full_size)
    del file_full_size[file_full_size.index(valmax)]
    file_sorted_dict[i] = valmax

print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
for i in file_sorted_dict:
    print(f"{i}: {file_sorted_dict[i]}")
