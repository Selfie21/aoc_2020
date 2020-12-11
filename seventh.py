import re


class InputParser:

    @staticmethod
    def get_main_rule(input_line):
        pattern = r' bags contain'
        main_rule = re.split(pattern, input_line)
        input_rule = InputParser.parse_bag(main_rule[0])
        output_rule = InputParser.get_output_rule(main_rule[1])
        return input_rule, output_rule

    @staticmethod
    def get_output_rule(input_line):
        pattern = r' bags?, '
        output_rule = re.split(pattern, input_line)
        output_rule[-1] = output_rule[-1][:-5]
        bags = []
        for bag in output_rule:
            bags.append(InputParser.parse_bag(bag))
        return bags

    @staticmethod
    def parse_bag(input_bag):
        input_bag = input_bag.replace(" ", "")
        colour = re.search(r'[a-zA-Z]+', input_bag).group(0)
        amount = re.search(r'\d+', input_bag)
        if amount is None:
            return Bag(1, colour)
        else:
            return Bag(int(amount.group(0)), colour)


class Bag:

    def __init__(self, amount, colour):
        self.amount = amount
        self.colour = colour


def check_rule_for_bag(output_bags, rule):
    for bag in output_bags:
        if bag.colour == rule:
            return True
    return False


def get_first_unchecked(queue):
    for val in queue:
        if queue[val]:
            queue[val] = False
            return val


def add_if_unchecked(queue, rule):
    if not(rule in queue):
        queue[rule] = True


f = open("inputs/seventh.txt", "r")
rules = {}

luggage = f.read().splitlines()
for bag in luggage:
    main_rule = InputParser.get_main_rule(bag)
    rules[main_rule[0].colour] = main_rule[1]

queue = {'shinygold': True}
currentSearch = 'shinygold'
while not(currentSearch is None):
    currentSearch = get_first_unchecked(queue)
    for rule in rules:
        if check_rule_for_bag(rules[rule], currentSearch):
            add_if_unchecked(queue, rule)


first = len(queue) - 1
print(first)
