def vowel_filter(function):
    def wrapper():
        all_vowels = 'aeiou'
        result = function()
        return [l for l in result if l in all_vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())