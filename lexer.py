import ply.lex as lex

tokens = (
    'NUMBER',
    'VARIABLE',
    'SETTO',
    'NEWLINE',
    'SUM',
    'OVER',
    'TIMES',
)


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    print("Accepted: ", t.value, t)
    return t


def t_SETTO(t):
    r'='
    print("Accepted: ", t.value, t)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value, t)
t_ignore = ' \t'


def t_SUM(t):
    r'\+'
    print("Accepted: ", t.value, t)
    return t


def t_OVER(t):
    r'\/'
    print("Accepted: ", t.value, t)
    return t


def t_TIMES(t):
    # this function is used to match the * character  
    r'\*'
    print("Accepted: ", t.value)
    return t


def t_error(t):
    print("Illegal character: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def print_result(result):
    print("Result:", result)
    
def parse(data):
    lexer.input(data)
    stack = []
    op_stack = []
    expecting_operator = True
    
    for tok in lexer:
        if tok.type == 'NUMBER':
            stack.append(tok.value)
            expecting_operator = True
        elif(tok.type == 'SUM' or tok.type == 'OVER' or tok.type == 'TIMES') and expecting_operator == True:
            op_stack.append(tok.type)
            expecting_operator = False
        elif tok.type == 'NEWLINE':
            break


    # for i in range(len(op_stack)):
    #     if op_stack[i] == 'SUM':
    #         result = stack[0] + stack[1]
    #     elif op_stack[i] == 'OVER':
    #         result = stack[0] / stack[1]
    #     elif op_stack[i] == 'TIMES':
    #         result = stack[0] * stack[1]
    #     stack.pop(0)
    #     stack[0] = result
    #     print_result(result)
    #     print(op_stack)
        
    # if stack:
    #     print_result(stack[0])

    while(len(op_stack) > 0):
        if op_stack[0] == 'SUM':
            result = stack[0] + stack[1]
        elif op_stack[0] == 'OVER':
            result = stack[0] / stack[1]
        elif op_stack[0] == 'TIMES':
            result = stack[0] * stack[1]
        op_stack.pop(0)
        stack.pop(0)
        stack[0] = result
        print_result(result)
        print(op_stack)
            
        if stack:
            print_result(stack[0])


while True:
    try:
        data = input(">")
        if data == 'exit':
            break
        parse(data)
    except EOFError:
        break
    
print("Done")