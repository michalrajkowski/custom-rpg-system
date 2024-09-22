import random

# files paths
subclassess_file = 'data/text data/subclassess.txt'
names_file = 'data/text data/names.txt'
subclass_skills_file = 'data/text data/skills_subclass.txt'
all_skills_file = 'data/text data/skills_all.txt'

# files dicts/lists
subclasses_list = []
subclasses_names = {}
subclass_skills = {}
all_skills = []

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

def load_subclass_skills():
    current_subclass = None
    with open(subclass_skills_file, 'r') as infile:
        for line in infile:
            if line.strip():
                # check if it is subclass
                if line.strip() in subclasses_list:
                    current_subclass = line.strip()
                    subclass_skills[line.strip()] = []
                    continue
                # if not it is name
                subclass_skills[current_subclass].append(line.strip())    

def load_all_skills(all_skills_file=all_skills_file):
    with open(all_skills_file, 'r') as infile:
        for line in infile:
            all_skills.append(line.strip())

load_subclassess()
load_names()
load_subclass_skills()
load_all_skills()

# Generater character:
# random subclass, then random name
this_subclass = random.choice(subclasses_list)
this_name = random.choice(subclasses_names[this_subclass])
# 3 skills from subclass and 2 random ones
this_skills = []
this_skills.extend(random.sample(subclass_skills[this_subclass],3))
# remove those skills from all skills
not_used_skills = list(filter(lambda item: item not in this_skills, all_skills))
this_skills.extend(random.sample(not_used_skills,2))



print(f"{this_subclass}\n" + f"{this_name}\n")
print(f"{this_skills}")
