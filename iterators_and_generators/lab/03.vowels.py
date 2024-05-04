class vowels:
    def __init__(self, text: str):
        self.text = text
        self.end_idx = len(self.text) - 1
        self.current_idx = -1
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o']

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1

        if self.current_idx > self.end_idx:
            raise StopIteration

        if self.text[self.current_idx].lower() in self.vowels:
            return self.text[self.current_idx]

        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
