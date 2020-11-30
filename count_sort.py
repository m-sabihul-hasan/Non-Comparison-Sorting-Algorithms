
import time
import random
import matplotlib.pyplot as plt
start_time = time.time()


def count_sort(lst):
    max_element = int(max(lst))
    min_element = int(min(lst))

    # compute range of elements
    k = max_element - min_element + 1

    # list to storre count of each value
    count = [0] * k

    # output list
    output = [0] * len(lst)

    # Store count of each character
    for i in range(len(lst)):
        count[lst[i] - min_element] += 1

    # Storing cumulative count
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Placing elements into the output array
    for i in range(len(lst) - 1, -1, -1):
        output[count[lst[i] - min_element] - 1] = lst[i]
        count[lst[i] - min_element] -= 1

    lst = output.copy()

    return lst


def plot_graph(N, start_time):
    lst = []
    x_lst = []
    y_lst = []
    for i in range(N):
        lst = [random.randint(-10, 10) for x in range(N)]
        count_sort(lst)
        x_lst.append(i)
        y_lst.append(round(time.time() - start_time, 2))

    plt.plot(x_lst, y_lst)
    plt.xlabel("N")
    plt.ylabel("Time")
    plt.show()


N = 5000

plot_graph(N, start_time)

lst = [-7, -12, -3, 5, 1, 5, -3, 5]
print("Sorted list = ", count_sort(lst))
