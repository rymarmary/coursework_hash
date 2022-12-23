import hash_open_addressing

hash_table = hash_open_addressing.OpenHash(5)

hash_table.insert_data(1, "one")  # testing insert function
hash_table.insert_data(34, "thirty-four")
hash_table.insert_data(17, "seventeen")

print("insert: ", hash_table.table, "\n")

hash_table.insert_data(90, "ninety")   # testing resize
hash_table.insert_data(73, "seventy-three")

print("resize: ", hash_table.table, "\n")

hash_table.insert_data(55, "fifty")

print("insert in resized table: ", hash_table.table, "\n")

print("searching: ")

print(hash_table.search_elem(34))  # searching existing element
print(hash_table.search_elem(101))  # searching not existing element
print(hash_table.search_elem(34 % 10))   # searching not existing element with existing hash

hash_table.remove_data(34)  # trying to remove existing element
hash_table.remove_data(101)  # trying to remove not existing element
hash_table.remove_data(34 % 10)  # trying to remove not existing element with existing hash

print()
print("removing: ", hash_table.table, "\n")

hash_table.remove_data(34)  # trying to remove already removed element

print("removing already removed element: ", hash_table.table)
