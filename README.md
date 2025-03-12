# EMUCOMP1.0
mips 
Overview

EMUCOMP1.0 is a lightweight compiler designed to translate simple assembly instructions into machine code suitable for basic emulator usage. It supports MIPS architecture and provides an easy-to-understand example for educational and development purposes.

Features

Supports basic MIPS instructions: ADD, SUB, MUL, DIV, SLT

Converts assembly code to binary machine code

Easy to extend with additional instructions and registers

Error checking for invalid instructions and registers

Usage

Requirements

Python 3.x

Running EMUCOMP1.0

python3 compiler.py <assembly_file>

Example

Assembly file (example.asm):

add $t0, $t1
sub $t2, $t3

Run the compiler:

python3 compiler.py example.asm

Machine code output will be saved to:

output_file.o

Project Structure

EMUCOMP1.0/
├── compiler.py     # Main compiler script
├── example.asm     # Example assembly input file
├── output_file.o   # Compiled binary output file
└── README.md

Contributing

Feel free to open issues or submit pull requests for enhancements and bug fixes.

License

This project is open source under the MIT License.

