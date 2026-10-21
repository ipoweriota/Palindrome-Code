import sys
from pathlib import Path

def load(file):
    """Open a text file and return a list of lowercase words."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)

here = Path(__file__).parent
word_list = load(here / '2of4brif.txt')

for word in word_list:
    if word == word[::-1]:
        print(word)