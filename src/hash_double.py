import math


class DoubleHash:
    def __init__(self, prime):
        self.num = prime
        self.get_prime()  # changing num
        self.table = [[], ] * self.num
        self.k = 0.0  # fill factor
        self.const = (math.sqrt(2) - 1) % 2  # const offset for hashing

    def check_prime(self):  # check if num is prime
        if self.num == 1 or self.num == 0:
            return 0
        for i in range(2, int(math.sqrt(self.num))):
            if self.num % i == 0:
                return 0
        return 1

    def get_prime(self):  # getting prime num from the inputting one
        if self.num % 2 == 0:
            self.num += 1
        while not self.check_prime():
            self.num += 2
        return self.num

    def hash_function(self, key):
        capacity = self.get_prime()
        return key % capacity

    def off_hash_function(self, key):
        temp = int(self.num * ((self.const * key) - int(self.const * key)))
        return temp

    def insert_data(self, key, data, i=0):
        if i < self.num and self.k < 2 / 3:
            index = (self.hash_function(key) + i * self.off_hash_function(key)) % self.num
            if self.table[index] and self.table[index] != ["delete"]:  # if cell is not empty
                if self.table[index][0] == key:  # if key is exist in table
                    self.table[index] = [key, data]  # update data
                else:  # in case of collision
                    i += 1
                    self.insert_data(key, data, i)
            else:
                self.table[index] = [key, data]
                self.k += 1 / self.num
        else:  # resize to increase empty cells amount
            saved_num = self.num
            saved_table = self.table
            self.num = self.num * 2
            self.get_prime()
            self.table = [[], ] * self.num
            self.k = 0
            for i in range(saved_num):
                if saved_table[i]:
                    self.insert_data(saved_table[i][0], saved_table[i][1], 0)
            self.insert_data(key, data, 0)

    def remove_data(self, key, i=0):
        if i < self.num:
            index = (self.hash_function(key) + i * self.off_hash_function(key)) % self.num
            if self.table[index]:
                if self.table[index][0] == key:
                    self.table[index] = ["delete"]
                else:
                    i += 1
                    self.remove_data(key, i)

    def search_elem(self, key, i=0):
        if i < self.num:
            index = (self.hash_function(key) + i * self.off_hash_function(key)) % self.num
            if self.table[index]:
                if self.table[index][0] == key:
                    return self.table[index][1]
                else:
                    i += 1
                    return self.search_elem(key, i)
            else:
                return "didn't find"
        else:
            return "did't find"
