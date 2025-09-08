numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
freq_dict = {}
for num in numbers:
    freq_dict[num] = freq_dict.get(num, 0) + 1
print("Frequency dictionary:", freq_dict)


