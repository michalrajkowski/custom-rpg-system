import random

# files paths
subclassess_file = 'data/text data/subclassess.txt'
names_file = 'data/text data/names.txt'

# files dicts/lists
subclasses_list = []
subclasses_names = {}


def load_subclassess(subclassess_file=subclassess_file):
    with open(subclassess_file, 'r') as infile:
        for line in infile:
            subclasses_list.append(line.strip())

def load_names():
    current_subclass = None
    with open(names_file, 'r') as infile:
        for line in infile:
            if line.strip():
                # check if it is subclass
                if line.strip() in subclasses_list:
                    current_subclass = line.strip()
                    subclasses_names[line.strip()] = []
                    continue
                # if not it is name
                subclasses_names[current_subclass].append(line.strip())    

load_subclassess()
load_names()

# Generater character:
# random subclass, then random name
this_subclass = random.choice(subclasses_list)
this_name = random.choice(subclasses_names[this_subclass])
print(f"{this_subclass}" + f"{this_name}")
