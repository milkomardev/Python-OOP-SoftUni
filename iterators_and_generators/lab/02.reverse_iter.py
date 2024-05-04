class reverse_iter:
    def __init__(self, obj):
        self.obj = obj
        self.current_index = len(self.obj)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index < 0:
            raise StopIteration()

        return self.obj[self.current_index]


reversed_list = reverse_iter([1, 2, 3, 4])

for item in reversed_list:
    print(item)