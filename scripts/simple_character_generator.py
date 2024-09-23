import random

# files paths
subclassess_file = 'data/text data/subclassess.txt'
names_file = 'data/text data/names.txt'
subclass_skills_file = 'data/text data/skills_subclass.txt'
all_skills_file = 'data/text data/skills_all.txt'
goals_neutral_small_file = 'data/text data/goals_neutral_small.txt'
goals_neutral_big_file = 'data/text data/goals_neutral_big.txt'
class_goals_small_file = 'data/text data/goals_class_small.txt'
class_goals_big_file = 'data/text data/goals_class_big.txt'

# files dicts/lists
subclasses_list = []
subclasses_names = {}
subclass_skills = {}
all_skills = []
goals_neutral_small = []
goals_neutral_big = []
class_goals_small = {}
class_goals_big = {}

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

def load_goals_neutral_small():
    with open(goals_neutral_small_file, 'r') as infile:
        goal_name = None
        for line in infile:
            if line.strip():
                if goal_name == None:
                    goal_name = line.strip()
                    continue
                goals_neutral_small.append((goal_name, line.strip()))
                goal_name = None

def load_goals_neutral_big():
    with open(goals_neutral_big_file, 'r') as infile:
        goal_name = None
        for line in infile:
            if line.strip():
                if goal_name == None:
                    goal_name = line.strip()
                    continue
                goals_neutral_big.append((goal_name, line.strip()))
                goal_name = None

def load_goals_class_small():
    current_subclass = None
    with open(class_goals_small_file, 'r') as infile:
        goal_name = None
        for line in infile:
            if line.strip():
                if line.strip() in subclasses_list:
                    current_subclass = line.strip()
                    class_goals_small[current_subclass] = []
                    continue
                if goal_name == None:
                    goal_name = line.strip()
                    continue
                class_goals_small[current_subclass].append((goal_name, line.strip()))
                goal_name = None

def load_goals_class_big():
    current_subclass = None
    with open(class_goals_big_file, 'r') as infile:
        goal_name = None
        for line in infile:
            if line.strip():
                if line.strip() in subclasses_list:
                    current_subclass = line.strip()
                    class_goals_big[current_subclass] = []
                    continue
                if goal_name == None:
                    goal_name = line.strip()
                    continue
                class_goals_big[current_subclass].append((goal_name, line.strip()))
                goal_name = None

load_subclassess()
load_names()
load_subclass_skills()
load_all_skills()
load_goals_neutral_small()
load_goals_neutral_big()
load_goals_class_small()
load_goals_class_big()

# random subclass, then random name
this_subclass = random.choice(subclasses_list)
this_name = random.choice(subclasses_names[this_subclass])
print(f"{this_subclass}\n" + f"{this_name}\n")
# 3 skills from subclass and 2 random ones
this_skills = []
this_skills.extend(random.sample(subclass_skills[this_subclass],3))
# remove those skills from all skills
not_used_skills = list(filter(lambda item: item not in this_skills, all_skills))
this_skills.extend(random.sample(not_used_skills,2))

this_small_goals = random.sample(goals_neutral_small, 1)
this_small_goals.extend(random.sample(class_goals_small[this_subclass], 1))
chance = random.random()
print(chance)
if chance < 0.5:
    this_big_goals = random.sample(goals_neutral_big, 1)
else:
    this_big_goals = random.sample(class_goals_big[this_subclass], 1)

print(f"{this_skills}")
print(f"{this_small_goals}")
print(f"{this_big_goals}")