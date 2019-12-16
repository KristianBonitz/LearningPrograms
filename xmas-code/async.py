## the engine does something based on the inital setup
## it awaits input
## it produces output

async def engine(operation):
    s = 0
    if operation == 1:
        s += await engine(2)

    if operation == 2:
        s += 3
        return s

    await print(s)

class Engine(object):
    """docstring for Engine"""
    def __init__(self, op_code):
        super(Engine, self).__init__()
        self.op_code = op_code
        self.input = 0 #random 10

    def get_input():
        pass

    def run_engine():
        pass

print(engine(1))


        