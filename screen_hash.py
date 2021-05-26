import numpy as np
import pickle

screen_array = np.load('screen_array.npy', allow_pickle=True)
'''print(screen_array.shape[0])
print(screen_array.shape[1])'''



#print(np.where(screen_array=="33333"))

screen_hash_5 = dict()
length_5_list = []
for line in screen_array:
    for data in line:
        if data not in length_5_list:
            length_5_list.append(data)

print(length_5_list) #1024개 박스
while len(length_5_list) != 0:
    for line in screen_array:
        for data in line:
            if data in length_5_list:
                length_5_list.remove(data)
                zoom_area_array = np.where(screen_array==data)
                y = zoom_area_array[0][0]
                h = zoom_area_array[0][-1] - zoom_area_array[0][0]
                x = zoom_area_array[1][0]
                w = zoom_area_array[1][-1] - zoom_area_array[1][0]
                screen_hash_5[int(data)] = [y, y+h, x, x+w] #y, y+h, x, x+w
                #print(screen_hash_5[data])

for line_index, line in enumerate(screen_array):
    for data_index, data in enumerate(line):
        screen_array[line_index][data_index] = data[:-1]

screen_hash_4 = dict()
length_4_list = []
for line in screen_array:
    for data in line:
        if data not in length_4_list:
            length_4_list.append(data)


print(length_4_list) #256개 박스
print(len(length_4_list))
while len(length_4_list) != 0:
    for line in screen_array:
        for data in line:
            if data in length_4_list:
                length_4_list.remove(data)
                zoom_area_array = np.where(screen_array==data)
                y = zoom_area_array[0][0]
                h = zoom_area_array[0][-1] - zoom_area_array[0][0]
                x = zoom_area_array[1][0]
                w = zoom_area_array[1][-1] - zoom_area_array[1][0]
                screen_hash_4[int(data)] = [y, y+h, x, x+w] #y, y+h, x, x+w
                #print(screen_hash_4[data])

for line_index, line in enumerate(screen_array):
    for data_index, data in enumerate(line):
        screen_array[line_index][data_index] = data[:-1]

screen_hash_3 = dict()
length_3_list = []
for line in screen_array:
    for data in line:
        if data not in length_3_list:
            length_3_list.append(data)


print(length_3_list) #256개 박스
print(len(length_3_list))
while len(length_3_list) != 0:
    for line in screen_array:
        for data in line:
            if data in length_3_list:
                length_3_list.remove(data)
                zoom_area_array = np.where(screen_array==data)
                y = zoom_area_array[0][0]
                h = zoom_area_array[0][-1] - zoom_area_array[0][0]
                x = zoom_area_array[1][0]
                w = zoom_area_array[1][-1] - zoom_area_array[1][0]
                screen_hash_3[int(data)] = [y, y+h, x, x+w] #y, y+h, x, x+w
                #print(screen_hash_4[data])

for line_index, line in enumerate(screen_array):
    for data_index, data in enumerate(line):
        screen_array[line_index][data_index] = data[:-1]

screen_hash_2 = dict()
length_2_list = []
for line in screen_array:
    for data in line:
        if data not in length_2_list:
            length_2_list.append(data)


print(length_2_list) #256개 박스
print(len(length_2_list))
while len(length_2_list) != 0:
    for line in screen_array:
        for data in line:
            if data in length_2_list:
                length_2_list.remove(data)
                zoom_area_array = np.where(screen_array==data)
                y = zoom_area_array[0][0]
                h = zoom_area_array[0][-1] - zoom_area_array[0][0]
                x = zoom_area_array[1][0]
                w = zoom_area_array[1][-1] - zoom_area_array[1][0]
                screen_hash_2[int(data)] = [y, y+h, x, x+w] #y, y+h, x, x+w
                #print(screen_hash_4[data])



screen_hash_2_pkl = open("screen_hash_2.pkl", "wb")
pickle.dump(screen_hash_2, screen_hash_2_pkl)
screen_hash_2_pkl.close()

screen_hash_3_pkl = open("screen_hash_3.pkl", "wb")
pickle.dump(screen_hash_3, screen_hash_3_pkl)
screen_hash_3_pkl.close()

screen_hash_4_pkl = open("screen_hash_4.pkl", "wb")
pickle.dump(screen_hash_4, screen_hash_4_pkl)
screen_hash_4_pkl.close()

screen_hash_5_pkl = open("screen_hash_5.pkl", "wb")
pickle.dump(screen_hash_5, screen_hash_5_pkl)
screen_hash_5_pkl.close()

