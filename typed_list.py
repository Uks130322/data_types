class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must be a list")

        for element in initial_list:
            self.__check(element)

        self.elements = initial_list[:]

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a typed list.")

    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element

    def __getitem__(self, i):
        return self.elements[i]

    def __len__(self):
        return len(self.elements)

    def __delitem__(self, key):
        del(self.elements[key])

    def append(self, new_element):
        self.__check(new_element)
        self.elements.append(new_element)


x = TypedList("", 5*[""])
x[2] = "Hello"
x[3] = "There"
print(x[:])
print(x[2] + " " + x[3])
a, b, c, d, e = x
print(a, c, d, e)
del(x[2])
print(x[:])
x.append("New")
print(x[:])
print(len(x))
x.append(2)
