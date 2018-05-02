import sys
import operator

def exp_eval(ops, op_exp):
    op_exp = op_exp.split()
    stack = [op_exp[0]]
    for i in range(1,len(op_exp)):
        if stack[-1] not in ['+','-'] and op_exp[i] not in ['+','-']:
            value_1 = stack.pop()
            op = stack.pop()
            temp_calc = str(ops[op](int(value_1),int(op_exp[i])))
            stack.append(temp_calc)
        else:
            stack.append(op_exp[i])
    if len(stack) < 3:
        return int(stack[-1])
    elif len(stack) == 3:
        return ops[stack[0]](int(stack[1]),int(stack[2]))
    else:
    	while len(stack) > 3:
    		value_2 = stack.pop()
    		value_1 = stack.pop()
    		op = stack.pop()
    		temp_calc = str(ops[op](int(value_1),int(value_2)))
    		stack.append(temp_calc)
	return ops[stack[0]](int(stack[1]),int(stack[2]))

if __name__ == '__main__':
	s = sys.argv[1]
	ops = { "+": operator.add, "-": operator.sub }

	print(exp_eval(ops,s))