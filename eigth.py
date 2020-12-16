import copy

def get_command(instruction):
    return instruction[0:3]


def get_parameters(instruction):
    return instruction[4:]


def eval_variable(var, arith_operation):
    if arith_operation[0] == '+':
        return add(var, int(arith_operation[1:]))
    elif arith_operation[0] == '-':
        return sub(var, int(arith_operation[1:]))

def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def run_machine(inputs):
    acc = ip = 0
    current = inputs[ip]
    while not current[1]:
        command = get_command(current[0])
        params = get_parameters(current[0])

        if command == 'acc':
            acc = eval_variable(acc, params)
        elif command == 'jmp':
            ip = eval_variable(ip, params) - 1

        current[1] = True
        ip += 1
        if ip > len(inputs) - 1:
            return acc
        current = inputs[ip]
    return None


f = open("inputs/eigth.txt",  "r")
inputs = []

for k in f.read().splitlines():
    inputs.append([k, False])

acc = None
i = 0
while acc is None:

    command = get_command(inputs[i][0])

    if command == 'nop':
        new_input = copy.deepcopy(inputs)
        new_input[i][0] = 'jmp' + inputs[i][0][3:]
        acc = run_machine(new_input)
    elif command == 'jmp':
        new_input = copy.deepcopy(inputs)
        new_input[i][0] = 'nop' + inputs[i][0][3:]
        acc = run_machine(new_input)

    i += 1

print(acc)
