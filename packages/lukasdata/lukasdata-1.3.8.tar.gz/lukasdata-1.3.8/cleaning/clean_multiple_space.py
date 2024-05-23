import regex as re


def clean_multiple_space(string):
    regex=re.compile("\s{2,}")
    search=regex.findall(string)
    for item in search:
        string=string.replace(item," ")
    return string