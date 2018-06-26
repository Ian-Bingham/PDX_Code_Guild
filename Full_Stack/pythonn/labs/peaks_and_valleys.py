# peaks_and_valleys.py 6/25/18

def peaks(num_list):
    peaks_indices = []
    for i in range(len(num_list) - 1):
        if i != 0 and i != (len(num_list) - 1):
            if num_list[i] > num_list[i - 1] and num_list[i] > num_list[i + 1]:
                peaks_indices.append(i)
    return peaks_indices

def valleys(num_list):
    valleys_indices = []
    for i in range(len(num_list) - 1):
        if i != 0 and i != (len(num_list) - 1):
            if num_list[i] < num_list[i - 1] and num_list[i] < num_list[i + 1]:
                valleys_indices.append(i)
    return valleys_indices

def peaks_and_valleys(num_list):
    pv_indices = peaks(num_list) + valleys(num_list)
    pv_indices.sort()
    return pv_indices

def draw_data(num_list):
    x_string_list = []
    for i in range(len(num_list)):
        print(str(num_list[i]) + (' X' * num_list[i]))

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print("Peak indices at: {}".format(peaks(data)))
print("Valley indices at: {}".format(valleys(data)))
print("Peak and Valley indices at: {}".format(peaks_and_valleys(data)))
draw_data(data)
