# Computer Science

## contents
- [Computer Science](#computer-science)
  - [contents](#contents)
    - [Section 1 - Components of a computer](#section-1---components-of-a-computer)
    - [Section 2 - Systems software](#section-2---systems-software)


### Section 1 - Components of a computer

Control Unit - Controls and coordinates CPU activity. Decodes and executes and stores result in memory.
Buses - Parallel wires connecting computer components. Usually 8, 16, 32 or 64 lines. Transmission medium.
Address bus - For when CPU wants to access a specific memory location, gets the memory's address.
Data bus - Transmits data in memory between processor components and memory.
Control bus - Sends control signals. Bi-directional and ensures data and address bus dont conflict.
System bus - The three buses collectively connecting with a processor, I/O controller and memory.
Word - Fixed size of digits handled as a unit by a processor. Different processors have different word sizes.
Registers - Special memory cells operating at high speed. Store results of operations.
Accumulator(ACC) - Stores result of all calculations made by ALU.
Current Instruction register(CIR) -  Holds current instruction being executed, split into operand and opcode.
Memory Data Register (MDR) - Temporarily stores data read/written to memory.
Opcode - To determine the type of instruction and the hardware to execute it.
Operand - Holds either address of data, the actual data or the data to be operated on passed to ALU/ACC.
Clock - Switches between 1 and 0 millions of times per second generating signals.
Cache - Small, expensive, fast memory inside CPU. Instruction is copied to this.
Pipelining - Allows next instruction to be fetched whilst previous is being decoded to improve speed.
Von Neumann Architecture - Specifies basic components in a computer
Hardvard architecture - Physically separate held memories for instructions. Used extensively with DSP systems.
Digital Signal Processing (DSP) - Include audio/speech, sonar and radar, biomedical, seismic and digital image processing.
Complex Instruction Set Computers (CISC) - Large sets using few lines of assembly code. Loads data into a separate register to perform function then stores it back into the original memory.
CISC Disadvantages - Many specialised instructions had to be built into hardware but only 20% were used.
CISC Advantages - Compiler has little work. Very little RAM required to store instructions.
Reduced Instruction Set Computers (RISC) - Only simple instructions that take one clock cycle can be executed.
RISC Disadvantages - Compiler has to do more work. More RAM required to store instructions.
RISC Advantages - One clock cycle so pipelining is possible. Four instructions execute as fast as one CISC.
Co-processor - An extra processor to supplement the CPU. Limited range of functions.
GPU - Graphics and image processing, has thousands of smaller cores for handling several tasks.
Multi-core CPU's - Significantly higher performance. Distribute workload effectively. Supercomputers
Barcodes - 2 Types, linear and QR codes. QR can hold more info.
Barcode readers - 4 types, pen-type readers, laser scanners, CCD readers and camera-based readers.
Pen-type readers - Light source and photo diode scan. Diode for light intensity and light for waveform. Small size, durable and simple design. Must touch the barcode to read.
Laser scanners - Laser beam and photo diode. Used in supermarkets commonly. Reliable and cheap.
Camera-based readers - Camera and processing method to decode. Can read on any surface, even if poorly printed
Camera-based readers uses - Phones for QR code scanning, Age verification, Couponing, Event ticketing.
Digital cameras (CCD) - Sensor with millions of tiny light sensors in a grid. Binary data is recorded so image can be reproduced on a computer software. Higher quality images but high power consumption.








### Section 2 - Systems software