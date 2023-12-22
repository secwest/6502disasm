

import sys

opcode_mapping = {

    0x00: ("BRK", "Implied", 1), 0x01: ("ORA", "(Indirect,X)", 2), 0x05: ("ORA", "Zero Page", 2), 0x06: ("ASL", "Zero Page", 2), 0x08: ("PHP", "Implied", 1), 0x09: ("ORA", "Immediate", 2), 0x0A: ("ASL", "Accumulator", 1), 0x0D: ("ORA", "Absolute", 3), 0x0E: ("ASL", "Absolute", 3),
    0x10: ("BPL", "Relative", 2), 0x11: ("ORA", "(Indirect),Y", 2), 0x15: ("ORA", "Zero Page,X", 2), 0x16: ("ASL", "Zero Page,X", 2), 0x18: ("CLC", "Implied", 1), 0x19: ("ORA", "Absolute,Y", 3), 0x1D: ("ORA", "Absolute,X", 3), 0x1E: ("ASL", "Absolute,X", 3),
    0x20: ("JSR", "Absolute", 3), 0x21: ("AND", "(Indirect,X)", 2), 0x24: ("BIT", "Zero Page", 2), 0x25: ("AND", "Zero Page", 2), 0x26: ("ROL", "Zero Page", 2), 0x28: ("PLP", "Implied", 1), 0x29: ("AND", "Immediate", 2), 0x2A: ("ROL", "Accumulator", 1), 0x2C: ("BIT", "Absolute", 3), 0x2D: ("AND", "Absolute", 3), 0x2E: ("ROL", "Absolute", 3),
    0x30: ("BMI", "Relative", 2), 0x31: ("AND", "(Indirect),Y", 2), 0x35: ("AND", "Zero Page,X", 2), 0x36: ("ROL", "Zero Page,X", 2), 0x38: ("SEC", "Implied", 1), 0x39: ("AND", "Absolute,Y", 3), 0x3D: ("AND", "Absolute,X", 3), 0x3E: ("ROL", "Absolute,X", 3),
    0x40: ("RTI", "Implied", 1), 0x41: ("EOR", "(Indirect,X)", 2), 0x45: ("EOR", "Zero Page", 2), 0x46: ("LSR", "Zero Page", 2), 0x48: ("PHA", "Implied", 1), 0x49: ("EOR", "Immediate", 2), 0x4A: ("LSR", "Accumulator", 1), 0x4C: ("JMP", "Absolute", 3), 0x4D: ("EOR", "Absolute", 3), 0x4E: ("LSR", "Absolute", 3),
    0x50: ("BVC", "Relative", 2), 0x51: ("EOR", "(Indirect),Y", 2), 0x55: ("EOR", "Zero Page,X", 2), 0x56: ("LSR", "Zero Page,X", 2), 0x58: ("CLI", "Implied", 1), 0x59: ("EOR", "Absolute,Y", 3), 0x5D: ("EOR", "Absolute,X", 3), 0x5E: ("LSR", "Absolute,X", 3),
    0x60: ("RTS", "Implied", 1), 0x61: ("ADC", "(Indirect,X)", 2), 0x65: ("ADC", "Zero Page", 2), 0x66: ("ROR", "Zero Page", 2), 0x68: ("PLA", "Implied", 1), 0x69: ("ADC", "Immediate", 2), 0x6A: ("ROR", "Accumulator", 1), 0x6C: ("JMP", "(Indirect)", 3), 0x6D: ("ADC", "Absolute", 3), 0x6E: ("ROR", "Absolute", 3),
    0x70: ("BVS", "Relative", 2), 0x71: ("ADC", "(Indirect),Y", 2), 0x75: ("ADC", "Zero Page,X", 2), 0x76: ("ROR", "Zero Page,X", 2), 0x78: ("SEI", "Implied", 1), 0x79: ("ADC", "Absolute,Y", 3), 0x7D: ("ADC", "Absolute,X", 3), 0x7E: ("ROR", "Absolute,X", 3),
    0x81: ("STA", "(Indirect,X)", 2), 0x84: ("STY", "Zero Page", 2), 0x85: ("STA", "Zero Page", 2), 0x86: ("STX", "Zero Page", 2), 0x88: ("DEY", "Implied", 1), 0x8A: ("TXA", "Implied", 1), 0x8C: ("STY", "Absolute", 3), 0x8D: ("STA", "Absolute", 3), 0x8E: ("STX", "Absolute", 3),
    0x90: ("BCC", "Relative", 2), 0x91: ("STA", "(Indirect),Y", 2), 0x94: ("STY", "Zero Page,X", 2), 0x95: ("STA", "Zero Page,X", 2), 0x96: ("STX", "Zero Page,Y", 2), 0x98: ("TYA", "Implied", 1), 0x99: ("STA", "Absolute,Y", 3), 0x9A: ("TXS", "Implied", 1),
    0xA0: ("LDY", "Immediate", 2), 0xA1: ("LDA", "(Indirect,X)", 2), 0xA2: ("LDX", "Immediate", 2), 0xA4: ("LDY", "Zero Page", 2), 0xA5: ("LDA", "Zero Page", 2), 0xA6: ("LDX", "Zero Page", 2), 0xA8: ("TAY", "Implied", 1), 0xA9: ("LDA", "Immediate", 2), 0xAA: ("TAX", "Implied", 1), 0xAC: ("LDY", "Absolute", 3), 0xAD: ("LDA", "Absolute", 3), 0xAE: ("LDX", "Absolute", 3),
    0xB0: ("BCS", "Relative", 2), 0xB1: ("LDA", "(Indirect),Y", 2), 0xB4: ("LDY", "Zero Page,X", 2), 0xB5: ("LDA", "Zero Page,X", 2), 0xB6: ("LDX", "Zero Page,Y", 2), 0xB8: ("CLV", "Implied", 1), 0xB9: ("LDA", "Absolute,Y", 3), 0xBA: ("TSX", "Implied", 1) 0xBC: ("LDY", "Absolute,X", 3), 0xBD: ("LDA", "Absolute,X", 3), 0xBE: ("LDX", "Absolute,Y", 3),
    0xC0: ("CPY", "Immediate", 2), 0xC1: ("CMP", "(Indirect,X)", 2), 0xC4: ("CPY", "Zero Page", 2), 0xC5: ("CMP", "Zero Page", 2), 0xC6: ("DEC", "Zero Page", 2), 0xC8: ("INY", "Implied", 1), 0xC9: ("CMP", "Immediate", 2), 0xCA: ("DEX", "Implied", 1), 0xCC: ("CPY", "Absolute", 3), 0xCD: ("CMP", "Absolute", 3), 0xCE: ("DEC", "Absolute", 3),
    0xD0: ("BNE", "Relative", 2), 0xD1: ("CMP", "(Indirect),Y", 2), 0xD5: ("CMP", "Zero Page,X", 2), 0xD6: ("DEC", "Zero Page,X", 2), 0xD8: ("CLD", "Implied", 1), 0xD9: ("CMP", "Absolute,Y", 3), 0xDD: ("CMP", "Absolute,X", 3), 0xDE: ("DEC", "Absolute,X", 3),
    0xE0: ("CPX", "Immediate", 2), 0xE1: ("SBC", "(Indirect,X)", 2), 0xE4: ("CPX", "Zero Page", 2), 0xE5: ("SBC", "Zero Page", 2), 0xE6: ("INC", "Zero Page", 2), 0xE8: ("INX", "Implied", 1), 0xE9: ("SBC", "Immediate", 2), 0xEA: ("NOP", "Implied", 1), 0xEC: ("CPX", "Absolute", 3), 0xED: ("SBC", "Absolute", 3), 0xEE: ("INC", "Absolute", 3),
    0xF0: ("BEQ", "Relative", 2), 0xF1: ("SBC", "(Indirect),Y", 2), 0xF5: ("SBC", "Zero Page,X", 2), 0xF6: ("INC", "Zero Page,X", 2), 0xF8: ("SED", "Implied", 1), 0xF9: ("SBC", "Absolute,Y", 3), 0xFD: ("SBC", "Absolute,X", 3), 0xFE: ("INC", "Absolute,X", 3)
}

def decode_opcode(opcode):
    if opcode in opcode_mapping:
        instruction, mode, length = opcode_mapping[opcode]
        return instruction, mode, length
    else:
        return "Unknown", "Implied", 1

def disassemble_stream(byte_stream):
    address = 0
    while True:
        byte = byte_stream.read(1)
        if not byte:
            break
        opcode = ord(byte)
        instruction, mode, length = decode_opcode(opcode)

        # Read additional bytes for the current instruction, if any
        additional_bytes = byte_stream.read(length - 1)
        additional_data = ' '.join(f"{ord(b):02X}" for b in additional_bytes)

        print(f"Address: {address:04X}, Opcode: {opcode:02X}, Instruction: {instruction} {mode}, Data: {additional_data}")
        address += length

if __name__ == "__main__":
    disassemble_stream(sys.stdin.buffer)
