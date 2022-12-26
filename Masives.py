from collections import Counter


def Convert(string):
    li = list(string.split(" "))
    return li

tocontinueorfinish = 'y'
result = None
while tocontinueorfinish == 'y':
    text = input('Enter your text: ')
    puncoff = text.replace(', ', ' ').replace('. ', ' ').replace('"', ' ')
    words = puncoff.lower().split()
    operation = input('Enter a opetation you want to make with text(a/b/c): ')

    if operation == 'a':
        counter = Counter(words)
        common_element = counter.most_common(5)
        print(common_element)

    if operation == 'b':
        words.sort()
        words = list(dict.fromkeys(words))
        print(words)

    if operation == 'c':
        q = ""
        for i in sorted(words, key=lambda b: len(b), reverse=True):
            q = q + " " + i
        k = (Convert(q))
        print(k[1:6])

    else:
        tocontinueorfinish = input("Press 'y' to continue or 'n' to finish: ")

if tocontinueorfinish == 'n':
    print("See you later")
