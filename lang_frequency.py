from collections import Counter
import re

def load_data(filepath):
    with open(filepath) as file_object:
        text = file_object.read()
        return text

def get_most_frequent_words(text):
    cnt = Counter(x for x in re.findall(r'[A-я\']{2,}', text))
    print(cnt.most_common(10))
        


if __name__ == '__main__':
    pass


get_most_frequent_words(load_data('123.txt'))
