import re


class BagGraph:

    def __init__(self, root):
        self.root = root

    def add_node_above(self):


class Node:

    def __init__(self, content, childNodes):
        self.content = content
        self.childNodes = childNodes

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


f = open("inputs/seventh.txt", "r")
rules = {}

luggage =  f.read().splitlines()
testline = luggage[0]
ttt = InputParser.get_main_rule(testline)



print("")
