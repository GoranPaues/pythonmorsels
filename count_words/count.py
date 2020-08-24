import re
from collections import Counter

def count_words(input_string):
    return Counter(re.findall(r"\b[\w'-]+\b",input_string.lower()))