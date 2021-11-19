
"""
PROBLEM: how many people do you need in a
group in order for the probability of two
individuals to have the same birthday be
X%?
e.g., how many people need to be in a group
for there to be a 50% chance of two people
having the same birthdate...
conventionally, this number is expected
to be: 365/2
"""

from datetime import datetime
from random import randint

random_date = lambda: str(datetime.fromtimestamp(randint(1609419600,1640869200))).split(" ")[0]

# history, for given people
def history(people=2) -> int:
    def count(birthdays):
        counted = {}
        for bd in birthdays:
            if bd not in counted:
                counted[bd] = 0
            counted[bd] += 1
        return counted
    # desired_probability = desire / 100 # 0.5 if 50
    people = people # the # of people
    birthdates = [random_date() for _ in range(people)]
    values = [x for x in count(birthdates).values() if x > 1]
    return len(values) > 0

def correct_for(people, hists):
    histories = [history(people) for _ in range(hists)]
    return sum(histories)/hists

# compile results for # of people in group, alternate histories
results = []
for i in range(50): # the people
    if i == len(results):
        results.append([])
    for _ in range(75): # samples
        results[i].append(correct_for(i, 1000))

# compile tsv report
report = ""
for i, res in enumerate(results):
    report += str(i) + "\t" + "{:.2f}%".format(sum(res)/len(res)*100) + "\n" # avg
open("results/birthdays.tsv", "w").write(report)
