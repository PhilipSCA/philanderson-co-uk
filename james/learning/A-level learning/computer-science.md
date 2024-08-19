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
--------------------------------------------14/8/24-------------------------------------------------
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
Pen-type readers - Light source and photo diode scan. Diode for light intensity and light for waveform. Small size, durable and simple design. Must touch the barcodChe to read.
Laser scanners - Laser beam and photo diode. Used in supermarkets commonly. Reliable and cheap.
Camera-based readers - Camera and processing method to decode. Can read on any surface, even if poorly printed
Camera-based readers uses - Phones for QR code scanning, Age verification, Couponing, Event ticketing.
Digital cameras (CCD) - Sensor with millions of tiny light sensors in a grid. Binary data is recorded so image can be reproduced on a computer software. Higher quality images but high power consumption.
--------------------------------------------15/8/24--------------------------------------------------
Radio Frequent Identification (RFID) - Using I/O, a Microchip with antenna. Used for tracking and identifying
Active tags - Have a battery, physically larger. Used to track things further away like cars.
Passive tags - Cheaper, no battery. Use radio waves for power, used in tagging items like groceries or cards.
Output devices - Take data by the computer and turn it into a way humans can read. Screens, printers etc.
LCD monitors (Liquid crystal display) - RGD diodes for each pixel. Usually back-lit with LED's.
LCD monitors advantages - Max brightness fast, sharp image, thin, last indefinetely, low power consumption.
LCD disadvantages - Slow to refresh, OLED's up to 200x faster. Hard to see at an angle, goes dark from side.
Organic LED screen(OLED) - Plastic screen so flexible. Can be used on almost any display.
OLED advantages - Much thinner, Brighter, consume less power, refresh fast, Colours clear at tighter angles.
OLED drawbacks - Dont last as long, wear out about 4x faster than LCD's. Very sensitive to water.
Laser printers - Use powdered ink called toner. Have cyan, magenta, yellow and black (CMYB) for colour.
Laser printers advantages - High-quality, high-speed. Becoming more affordable and used. Can do colour.
Laser printer disadvantage - For jobs other than text is limited by print quality, about 1200 dpi.
Inkjet printers - Spray small ink dots onto paper for an image. If High quality will produce excellent images.
Resolution - Based on DPI (dots per inch), the more dots the better.
Inkjet printers advantages - Cheaper than laser, High quality images with good paper, colour and resolution.
Inkjet printers disadvantages - Much slower, ink has to be replaced frequently.
Dot matrix / Impact printers - Print head has a matrix of pins which strike the paper through an inked ribbon.
Dot matrix benefits - Useful for multi-part stationary, can be used in dirty or damp areas.
Dot matrix drawbacks - Noisy, slow and poor print quality
3D printers - Can be used to create spare parts like car or aeroplane parts, medical eqpmt and prototypes etc.
Multimedia projectors - Used in classrooms for schools. More consistent as teacher just has to do lesson once.
Multimedia projectors adv - Before students crowded round a "16 screen, Chalkboards were used, Videos and images can improve learning and make it more interesting.
Computer speakers - Used in PC's, smartphones and portable devices as an inbuilt speaker for music, calls etc.
Actuators - Motors used with sensors to control something. e.g: Opening a window, start/stopping a pump etc.
--------------------------------------------16/8/24--------------------------------------------------
Secondary storage - Slower Storage for when power is off.
Hard disk - High capacity, rotating platters that spin with a drive head on the disk.
Optical disk - etiher CD-ROM, CD-R or CD-RW. Laser to burn disk to make areas less reflective. ROM has lands.
SSD - Array of chips on a board. Millions of NAND flash memory cells and a controller.
Virtual memory - If the RAM doesnt have enough storage.
Operating system - Programs that manage operations of the computer.
Operating system functions - Memory management, service routines, processor scheduling, I/O management etc.
Memory management - Every application/program run has to be allocated in memory whilst being used.
Paging - Memory divided into fixed sizes of 4KB each.
Segmentation - Logical division of addresses into varying length segments depending on the program structure.
Interrupts - Signal from program, hardware or clock to CPU. Happens when requesting services from OS or timer.
Interrupt service routines - Suspends programs to deal with interrupt. Different routine for each interrupt.
Types of interrupts - Power-fail interrupt (high priority), Clock interrupt, I/O device request (low pri)
Processor scheduling - OS can queue up the next process required to make efficient use of processor.
Multi-tasking - Single processor carries out small parts of multiple larger tasks in turn.
Scheduler - Ensures processor time is as efficient as possible.
Scheduler objectives - Maximise throughput, be fair to all users, good response time and keep hardware busy.
Round robin - Each process has a time slice. Time interval is set and moves on continuously if not complete.
First come first served - Jobs processed in order that they came.
Shortest remaining time - Program with the smallest estimated time to complete is run next.
Shortest job first - Process with the smallest estimated running time is run next. Similar to (one above).
Multi-level feedback queues - Several job queues, jobs can move between queues depending on time. To maximise processor use
Backing store management - Apps transfer from backing storage to memory when loaded. OS knows where free space is and keeps directory of where files are stored
Peripheral management - Managing I/O devies through their operation. e.g: Printers
Buffer - Memory where data goes so CPU can continue with another task. Compensates for speed difference
Distributed OS - Form of parallel processing where load is spread over multiple servers. Job is split and each small task is run on separate computers
Multi-tasking OS - Runs on a standalone computer. Several apps/programs running at once. e.g Music and work.
--------------------------------------------19/8/24--------------------------------------------------
Real-time OS - Must respond quickly to inputs, have a 'fail-safe', handle many inputs at once and have backup.
BIOS - For start-up. Loads OS from hard disk into RAM and tests hardware.
Device drivers - Provides a software interface to hardware. Allows OS to access hardware without knowing details of it.
Systems software - Needed to run hardware and application programs, such as OS, utility programs etc.
Utility software - To optimise performance, responsible for backing up files, compression, a firewall etc.
Disk defragmentation - Reorganises a magnetic disk so files which are split up are recombined in a series of blocks. Makes reading files quicker.
Applications software - Can be general-purpose, special-purpose or custom-written software
General-purpose software - Used for several purposes. e.g: Word processors and graphics packages
Special-purpose software - Performs a single specfic task/set of tasks.
Freeware - Software free to use but the user doesn't get access to source code.
Bytecode - Combines compiling and interpreting creates this.
Aspects of software development - Analysis, Design, Programming, testing, implementation and evaluation
Analysis - Includes the data, procedures, future plans and problems
Design - Includes processing, data structures, I/O, user interface, security and hardware
Black box testing - Carried out independently of code. Looks at program specification, covering all I/O's.
White box testing - Depends on code logic, derives from program structure.
Alpha testing - Carried out by software developers testing team. Reveals errors and unincluded items.
Beta testing - Giving package to potential users to use and get feedback so it can be modified further.
Implementation - When all testing is done software installed and more testing is done as new problems arise.
Evaluation - Assessed on effectiveness, usability and maintainability. Waiting period beforehand for users.
Waterfall Model - Review method where each step is completed one at a time. Can go back stages but have to work down through following stages
Spiral model - Review method, develops software in iterative stages. 
Agile modeling - Feedback at each part, changes made as next part of system is built. Prototype at each stage.
Extreme programming - Frequent releases of software made in short development cycles. Improves quality.
Agile modeling drawback - Abscence of user involvement
Agile modeling benefit - Suitable for small projects.
Extreme programming and RAD benefit - Good for large projects.



### Section 2 - Systems software