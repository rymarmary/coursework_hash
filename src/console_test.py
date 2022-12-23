import hash_double
import hash_open_addressing


table = hash_double.DoubleHash(5)
# table = hash_open_addressing.OpenHash(5)
data = ' '

while data:
    data = input().split(" ")
    if data[0] == "insert":
        table.insert_data(int(data[1]), data[2])
    elif data[0] == "search":
        print(table.search_elem(int(data[1])))
    elif data[0] == "remove":
        table.remove_data(int(data[1]))
    else:
        break

print(table.table)