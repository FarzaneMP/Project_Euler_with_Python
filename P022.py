### Problem 20 from Project Euler
#https://projecteuler.net/archives
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
#over five-thousand first names, begin by sorting it into alphabetical order.
#Then working out the alphabetical value for each name,
#multiply this value by its alphabetical position in the list to obtain a name score.
#What is the total of all the name scores in the file?
df = open("p022_names.txt","r")
names = df.read().split('\",\"')

def list_of_names(names):
    """To make a list from the txt file"""
    i = -1
    for name in names:
        i += 1
        for char in name:
            if '\"' in char:
                names[i] = name.replace('\"', '')
    names_sort = sorted(names)
    return names_sort


def alpha_dict_upper():
    """Make a dict of alphabetical position for uppercase """
    import string
    alphabet_string = string.ascii_uppercase
    list = []
    d ={}
    for char in alphabet_string:
        list.append(char)
        d[char] = list.index(char)+1
    return d

def names_score(names_sort, d):
    """Finding the name score"""
    val_T = 0
    for name in names_sort:
        val = 0
        for char in name:
            val += d[char]
        val_T += val*(names_sort.index(name)+1)
    return val_T

names_score(list_of_names(names),alpha_dict_upper())

if __name__ =="__main__":
    print(names_score(list_of_names(names),alpha_dict_upper()))
