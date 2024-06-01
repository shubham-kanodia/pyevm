class EVM:
    def __init__(self):
        self.stack = []
        self.memory = bytearray()
        self.storage = {}

    def execute(self, bytecode):
        pc = 0
        if pc < len(bytecode):
            opcode = bytecode[pc]
            pc += 1
            self.execute_opcode(opcode)

    def execute_opcode(self, opcode):
        if opcode == 0x00:    # Opcode for stop
            return
        elif opcode == 0x01:
            self.add()
        else:
            raise Exception(f"Unsupported opcode: {opcode}")

    def add(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")

        a = self.stack.pop()
        b = self.stack.pop()

        self.stack.append(a + b)
