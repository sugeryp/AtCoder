li = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word: str):
    return word.capitalize()


change_words(li, sample_func)

print('############################################')
# lambda
li = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words2(words, func):
    for word in words:
        print(func(word))


samplie_func = lambda word: word.capitalize()

change_words2(li, sample_func)

print('############################################')
# lambda
li = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words3(words, func):
    for word in words:
        print(func(word))


change_words3(li, lambda word: word.capitalize())
