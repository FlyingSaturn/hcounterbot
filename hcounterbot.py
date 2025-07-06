from re import findall

subreddits = {
    "thelettera" : 'a',
    "theletterb" : 'b',
    "theletterc" : 'c',
    "theletterd" : 'd',
    "thelettere" : 'e',
    "theletterf" : 'f',
    "theletterg" : 'g',
    "theletterh" : 'h',
    "theletteri" : 'i',
    "theletterj" : 'j',
    "theletterk" : 'k',
    "theletterl" : 'l',
    "theletterm" : 'm',
    "thelettern" : 'n',
    "thelettero" : 'o',
    "theletterp" : 'p',
    "theletterq" : 'q',
    "theletterr" : 'r',
    "theletters" : 's',
    "thelettert" : 't',
    "theletteru" : 'u',
    "theletterv" : 'v',
    "theletterw" : 'w',
    "theletterx" : 'x',
    "thelettery" : 'y',
    "theletterz" : 'z'
 }

def main():
    S = 0
    text = ""
    print("Inputting text...")
    with open('abc.txt') as file:
        text = file.read()
    print("Inputted.\n")
    ind = counting_individual(text)
    stretch_arr = counting_series(text)
    total = stretch_arr[0]
    multiple = stretch_arr[1]
    max_stretch = stretch_arr[2]
    single = total - multiple
    occupancy = (ind/len(text)) * 100
    occupancy = round(occupancy * 100) / 100
    print("\nTotal number of Hs:", ind)
    print("Occupying", str(occupancy) + "% of the entire text.");
    print("\nTotal stretches of Hs:", total)
    print("No. of single Hs:", single)
    print("No. of multiple Hs at a stretch:", multiple)
    print("Length of the longest stretch of Hs:", max_stretch)
    #TODO: Loop through the comments and posts
    #TODO: For every text, find out the number of occurences
    #TODO: Add those occurences
    #TODO: Khat likho bhai
    #TODO: Bhejo khat.
    #TODO: average length of comments/posts, total length of all the comments/posts, length of a specific comment/post, average of number of individual Hs


# Main place to count stuff [matches, 1] or [matches, longest_length]
def counting(string, text, longest=False):
    arr = findall(string, text)
    out = []
    out.append(len(arr))
    if longest:
        out.append(len(max(arr, key=len)))
    else:
        out.append(1)
    return out


# Individual counts of the letter
def counting_individual(text, letter='h'):
    string = "[" + letter + letter.upper() + "]"
    return (counting(string, text))[0]


# How many stretches of the letter [total, multiple]
def counting_series(text, letter='h'):
    string = "[" + letter + letter.upper() + "]+"
    count = []
    count.append((counting(string, text))[0])
    string = "(?=[" + letter + letter.upper() + "]{2})[" + letter + letter.upper() + "]+"
    arr = counting(string, text, True)
    count.append(arr[0])
    count.append(arr[1])
    return count


main()
