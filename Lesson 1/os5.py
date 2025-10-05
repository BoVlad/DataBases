# import os
#
# file_names = os.listdir()
# file_full_name = []
# file_full_size = []
# file_sorted_dict = {}
#
# for i in file_names:
#     file_full_name.append(i)
#     file_full_size.append(os.path.getsize(i))
#
# for i in file_full_name:
#     valmax = max(file_full_size)
#     del file_full_size[file_full_size.index(valmax)]
#     file_sorted_dict[i] = valmax
#
# print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
# for i in file_sorted_dict:
#     print(f"{i}: {file_sorted_dict[i]}")
#


# import os
#
# file_names = os.listdir()
# file_dict = {}
# file_sorted_dict = {}
# file_size = list(map(lambda x: os.path.getsize(x), file_names))
#
# for i in range(0, len(file_names)):
#     file_dict[file_names[i]] = file_size[i]
#
# file_sorted_dict = sorted(file_dict, reverse=True)
# print(file_sorted_dict)
#
# print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
# for i in file_sorted_dict:
#     print(f"{i}: {file_sorted_dict[i]}")


# import os
#
# with os.scandir(".") as it:
#     files = sorted(
#         ((e.name, e.stat().st_size) for e in it if e.is_file()),
#         key=lambda x: x[1],
#         reverse=True,
#     )
#
# print("Файли у каталозі, відсортовані за розміром (від найбільшого до найменшого):")
# for name, size in files:
#     print(f"{name}: {size}")