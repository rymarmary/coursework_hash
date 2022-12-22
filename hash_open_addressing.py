import math

class OpenHash:
    def __init__(self, prime):
        self.num = prime
        self.get_prime()  # changing num
        self.table = [[],] * self.num

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

    def insert_data(self, key, data):
        index = self.hash_function(key)
        self.table[index] = [key, data]

    def remove_data(self, key):
        index = self.table(key)
        self.table[index] = 0


