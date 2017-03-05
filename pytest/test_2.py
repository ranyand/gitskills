import string
text = open('mess.txt').read()

def my_solution(text):
    """select rare num in text"""

    s = filter(lambda x: x in string.letters, text)
    print s


if __name__ == '__main__':
    my_solution(text)
