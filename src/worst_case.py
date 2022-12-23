import hash_double
import hash_open_addressing
import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(20000)

#table = hash_double.DoubleHash(2003)
table = hash_open_addressing.OpenHash(2003)

num1 = [i for i in range(1000)]
num2 = [1000 - i for i in range(1000)]
func_search = []
func_remove = []
func_insert = []

for i in num1:
    time1 = time.time_ns()
    table.insert_data(table.num*i, "smth")
    time2 = time.time_ns()
    func_insert.append(time2 - time1)

for i in num1:
    time1 = time.time_ns()
    table.search_elem(table.num*i)
    time2 = time.time_ns()
    func_search.append(time2 - time1)

for i in num2:
    time1 = time.time_ns()
    table.remove_data(table.num*i)
    time2 = time.time_ns()
    func_remove.append(time2 - time1)
func_remove.reverse()

func1 = plt.subplot(3, 1, 1)
plt.title("Research complexity in the worst case")
func2 = plt.subplot(3, 1, 2)
func3 = plt.subplot(3, 1, 3)

func3.set_xlabel("Number of elements")
func1.set_ylabel("Time")
func2.set_ylabel("Time")
func3.set_ylabel("Time")

func1.grid()
func2.grid()
func3.grid()

func1.scatter(num2, func_search, s = 5, color = ["red"])
func2.scatter(num2, func_remove, s = 5, color = ["green"])
func3.scatter(num2, func_insert, s = 5, color = ["blue"])

func1.legend([" Search worst case"])
func2.legend([" Remove worst case"])
func3.legend([" Insert worst case"])

plt.show()
