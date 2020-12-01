
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


def radix_sort(lst):

    # Find the maximum number to know number of digits
    max1 = max(lst)

    exp = 1
    while max1 / exp > 0:

        # count_sort
        max_element = int(max(lst))

        k = max_element + 1
        count = [0] * k
        output = [0] * len(lst)

        for i in range(0, len(lst)):
            index = (lst[i]/exp)
            count[int((index) % 10)] += 1

        for i in range(1, k):
            count[i] += count[i-1]

        for i in range(len(lst) - 1, -1, -1):
            index = (lst[i]/exp)
            output[count[(int(index) % 10)] - 1] = lst[i]
            count[(int(index) % 10)] -= 1

        lst = output.copy()

        exp *= 10

    return lst


def plot_graph(N, start_time):
    lst = []
    x_lst = []
    c_time = []
    r_time = []
    # b_time = []
    for i in range(N):
        lst = [random.randint(-10, 10) for x in range(N)]
        x_lst.append(i)
        count_sort(lst)
        c_time.append(round(time.time() - start_time, 2))
        radix_sort(lst)
        r_time.append(round(time.time() - start_time, 2))

    plt.plot(x_lst, c_time, label="O(n+k)")
    plt.plot(x_lst, r_time, label="O(d(n+k))")
    # plt.plot(x_lst, y_lst, label = "O(n+k)")
    plt.xlabel("n")
    plt.ylabel("Time")
    plt.show()


N = 1000

plot_graph(N, start_time)

lst = [-7, -12, -3, 5, 1, 5, -3, 5]
print("Sorted list = ", count_sort(lst))
lst = [2, 44, 98, 121, 0, 0, 3, 2]
print("Sorted list = ", radix_sort(lst))
