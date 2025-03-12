import sys

# MIPS operations
opcodes = {
    'add': 0x20,  # ADD
    'sub': 0x22,  # SUB
    'mul': 0x18,  # MULT
    'div': 0x1A,  # DIV
    'slt': 0x2A   # CMP replaced by SLT (Set Less Than)
}

# MIPS registers
registers = {
    '$t0': 8,
    '$t1': 9,
    '$t2': 10,
    '$t3': 11
}

# Load assembly file
with open(sys.argv[1], 'r') as f:
    code = f.readlines()

# Compile to MIPS instructions
with open('output_file.o', 'wb') as f:
    for line in code:
        parts = line.strip().split()

        op = parts[0]
        src = parts[1].strip(',')
        dest = parts[2]

        if op not in opcodes or src not in registers or dest not in registers:
            print(f"Error: Invalid opcode or register in line '{line.strip()}'")
            continue

        opcode = 0     # R-type opcode is 0
        rs = registers[src]
        rt = registers[dest]
        rd = registers[dest]  # Assuming dest is destination
        shamt = 0
        funct = opcodes[op]

        # R-format instruction encoding
        instruction = (opcode << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (shamt << 6) | funct

        # Write binary instruction
        f.write(instruction.to_bytes(4, byteorder='big'))
