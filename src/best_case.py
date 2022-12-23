import hash_double
import hash_open_addressing
import matplotlib.pyplot as plt
import time
from random import randint

#table = hash_double.DoubleHash(2000)
table = hash_open_addressing.OpenHash(2000)

num1 = [i for i in range(2000)]
func_search = []
func_remove = []
func_insert = []

for i in num1:
    time1 = time.time_ns()
    table.insert_data(i, "smth")
    time2 = time.time_ns()
    func_insert.append(time2 - time2)

for i in num1:
    time1 = time.time_ns()
    table.search_elem(i)
    time2 = time.time_ns()
    func_search.append(time2 - time1)

for i in num1:
    time1 = time.time_ns()
    table.remove_data(i)
    time2 = time.time_ns()
    func_remove.append(time2 - time1)
func_remove.reverse()

func1 = plt.subplot(3, 1, 1)
plt.title("Research complexity in the best case")
func2 = plt.subplot(3, 1, 2)
func3 = plt.subplot(3, 1, 3)

func3.set_xlabel("Number of elements")
func1.set_ylabel("Time")
func2.set_ylabel("Time")
func3.set_ylabel("Time")

func1.grid()
func2.grid()
func3.grid()

func1.scatter(num1, func_search, s = 5, color = ["red"])
func2.scatter(num1, func_remove, s = 5, color = ["green"])
func3.scatter(num1, func_remove, s = 5, color = ["blue"])

func1.legend([" Search best case"])
func2.legend([" Remove best case"])
func3.legend([" Insert best case"])

plt.show()
