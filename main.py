class CPU:
    def __init__(self, cache_enabled=True):
        self.registers = [0]*8
        self.program_counter = 0
        self.cache_enabled = cache_enabled
        self.instructions = []
        self.data_memory = []
        self.cache = [
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
            {'tag': None, 'data': ''},
        ]
        
    def fetch(self):
        return self.instructions[self.program_counter]
    
    def decode(self, instruction_string):
        pass
    
    def execute(self, opcode, operand_list):
        pass
    
    def updatePC(self, opcode, operand_list):
        pass
    
    def readMemory(self, address):
        pass
    
    def writeMemory(self, address, value):
        pass
    
    

#MAIN PROGRAM

if __name__ == "__main__":
    new_cpu = CPU()
    
    