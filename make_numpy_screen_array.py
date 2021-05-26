import numpy as np

#width_ = np.array(range(1,1921), dtype=int)

array = np.empty((1080,1920), dtype=object) #세로 / 가로 __ height / width
for height_index, line in enumerate(array): #
    for width_index, element in enumerate(line): #width
        width_start = 0
        height_start = 0
        width_end = 1920
        height_end = 1080
        count = 1
        hash_string = ""
        while count <= 5:
            width_center = (width_start + width_end)/2
            height_center = (height_start + height_end)/2
            if height_index <= height_center and width_index <= width_center:
                hash_string = hash_string + "0"
                width_end = width_center
                height_end = height_center
            elif height_index <= height_center and width_index > width_center:
                hash_string = hash_string + "1"
                width_start = width_center
                height_end = height_center
            elif height_index > height_center and width_index <= width_center:
                hash_string = hash_string + "2"
                width_end = width_center
                height_start = height_center
            elif height_index > height_center and width_index > width_center:
                hash_string = hash_string + "3"
                width_start = width_center
                height_start = height_center
            count += 1
        array[height_index][width_index] = hash_string

for line in array:
    for element in line:
        print(element, end=' ')
    print()
np.save("screen_array",array)