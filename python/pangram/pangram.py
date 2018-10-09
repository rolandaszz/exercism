from collections import Counter
import string

def is_pangram(sentence):
    #https://stackoverflow.com/questions/3190122/python-how-to-print-range-a-z
    #a-z list
    az = list(string.ascii_lowercase)

    #zero
    Z = 0

    #letter count dict
    lc = dict()
    for azletter in az:
        lc[azletter] = lc.get(azletter, 0)

    #input
    raw = Counter(sentence.lower())

    for letter, count in raw.items():
        for azletter, azcount in lc.items():
            if letter == azletter:
                lc[azletter] = lc.get(azletter, azcount) + count

    if Z in lc.values():
        pangram_test = False
    else:
        pangram_test = True

    return pangram_test
