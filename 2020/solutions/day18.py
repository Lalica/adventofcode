with open("../inputs/18.txt") as f:
    data = [line.strip().replace(' ', '') for line in f]


def evaluate(expr, i):
    tmp = ''
    while i < len(expr):
        if expr[i] in '0123456789':
            tmp += expr[i]
        elif expr[i] in '+*':
            tmp = str(eval(tmp)) + expr[i]
        elif expr[i] == '(':
            res, j = evaluate(expr, i+1)
            tmp += res
            i = j
        elif expr[i] == ')':
            return [str(eval(tmp)), i]
        i += 1
    return eval(tmp)


def evaluate2(expr, i):
    tmp = ''
    tmpb, flag = '', False
    while i < len(expr):
        if expr[i] in '0123456789':
            if flag:
                tmpb += expr[i]
            else:
                tmp += expr[i]
        elif expr[i] == '+':
            if flag:
                tmpb = str(eval(tmpb)) + expr[i]
            else:
                tmp = str(eval(tmp)) + expr[i]
        elif expr[i] == '*':
            if flag:
                tmp += '*' + str(eval(tmpb))
            else:
                flag = True
            tmp = str(eval(tmp))
            tmpb = ''
        elif expr[i] == '(':
            res, j = evaluate2(expr, i+1)
            if flag:
                tmpb += res
            else:
                tmp += res
            i = j
        elif expr[i] == ')':
            return [str(eval((tmp + '*' + str(eval(tmpb))) if flag else tmp)), i]
        i += 1
    return eval((tmp + '*' + str(eval(tmpb))) if flag else tmp)


print(f'Day 19 part 1: {sum(evaluate(d, 0) for d in data)}')
print(f'Day 19 part 2: {sum(evaluate2(d, 0) for d in data)}')
