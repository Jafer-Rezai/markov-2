"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    the_file = open(file_path).read()
    return the_file

print(open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt"))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.


    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    split_tx = text_string.split()

    for i in range(len(split_tx) - 2):
        line = (split_tx[i], split_tx[i+1])
        if line not in chains:
            chains[line] = [split_tx[i+2]]
    return chains



#iterate over the list
#get the item 1 and item 2 and store as tuple, 
#check if the tuple is NOT already a key of the chain
#then make the tupel key of the chain and the value to be item 3



print(make_chains(open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt")))


def make_text(chains):
    """Return text from chains."""

    dictionary_chain = make_chains(open_and_read_file("green-eggs.txt"))

    words = []
    all_keys = []
 
    for key, value in dictionary_chain.items():

        all_keys.append(key)
        #print(all_keys)
        
    random_key = choice(all_keys)
    words.append(random_key)
  

    for key, value in dictionary_chain.items():
        if random_key == key:
            random_value = choice(value)
            words.append(random_value)

    #[(would, you), rather]
    #(you, rather): 

    additional_key = (words[0][1], words[1])
    
    for key, value in dictionary_chain.items():
        if key not in  dictionary_chain:
            chains[additional_key] = choice(value)
        else:
            pass

    

        print(f"{key[0]} {key[1]} {value[0]}")
    
    
print(make_text(make_chains(open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt"))))

input_path = 'green-eggs.txt'
#
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
