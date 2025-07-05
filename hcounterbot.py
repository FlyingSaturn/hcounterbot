from re import findall

subreddits = {
    "r/thelettera" : 'a',
    "r/theletterb" : 'b',
    "r/theletterc" : 'c',
    "r/theletterd" : 'd',
    "r/thelettere" : 'e',
    "r/theletterf" : 'f',
    "r/theletterg" : 'g',
    "r/theletterh" : 'h',
    "r/theletteri" : 'i',
    "r/theletterj" : 'j',
    "r/theletterk" : 'k',
    "r/theletterl" : 'l',
    "r/theletterm" : 'm',
    "r/thelettern" : 'n',
    "r/thelettero" : 'o',
    "r/theletterp" : 'p',
    "r/theletterq" : 'q',
    "r/theletterr" : 'r',
    "r/theletters" : 's',
    "r/thelettert" : 't',
    "r/theletteru" : 'u',
    "r/theletterv" : 'v',
    "r/theletterw" : 'w',
    "r/theletterx" : 'x',
    "r/thelettery" : 'y',
    "r/theletterz" : 'z'
    }

def main():
    S = 0
    text = ""
    print("Inputting text...")
    with open('abc.txt') as file:
        text = file.read()
    print("Inputted.\n")
    ind = counting_individual(text)
    stretch = counting_series(text)
    occupancy = (ind/len(text)) * 100
    occupancy = round(occupancy * 100) / 100
    print("Total number of Hs:", ind)
    print("Total stretches of Hs:", stretch)
    print("Occupying", str(occupancy) + "% of the entire text.");
    #TODO: Loop through the comments and posts
    #TODO: For every text, find out the number of occurences
    #TODO: Add those occurences
    #TODO: Khat likho bhai
    #TODO: Bhejo khat.
    #TODO: average length of comments/posts, total length of all the comments/posts, length of a specific comment/post, average of number of individual Hs


# Main place to count stuff
def counting(string, text):
    matches = len(findall(string, text))
    return matches


# Individual counts of the letter
def counting_individual(text, letter='h'):
   string = "[" + letter + letter.upper() + "]"
   return counting(string, text)


# How many stretches of the letter
def counting_series(text, letter='h'):
   string = "[" + letter + letter.upper() + "]+"
   return counting(string, text)


main()
