import time
import random
import matplotlib.pyplot as plt
start_time = time.time()


def radix_sort(lst):


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
print("Sorted list = ", radix_sort(lst))
