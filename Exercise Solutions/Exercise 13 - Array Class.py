class Array:
    def __init__(self, list: list):
        self.__array = list

    def get(self, index: int):
        return self.__array[index]

    def append(self, value):
        self.__array.append(value)

    def pop(self, index=-1):
        return self.__array.pop(index)

    def extend(self, list):
        self.__array.extend(list)

    def insert(self, index, value):
        self.__array.insert(index, value)

    def index(self, value):
        return self.__array.index(value)

    def length(self) -> int:
        return len(self.__array)

    def __str__(self):
        return str(self.__array)


arr = Array(["zero", "one", "two", "three", "four"])

print(arr.get(0))  # Output: zero
arr.append("five")  # arr should be ["zero", "one", "two", "three", "four", "five"]
print(arr)
arr.pop()  # arr should be ["zero", "one", "two", "three", "four"]
print(arr)
arr.extend(["five", "six", "seven"])  # arr should be ["zero", "one", "two", "three", "four", "five", "six", "seven"]
print(arr)
arr.insert(8, "eight")  # arr should be ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
print(arr)
print(arr.index("zero"))  # Output: 0
print(arr.length())  # Output: 9
print(arr)
