# Computer Science
Decomposition - breaking a complex problem into smaller problems to solve individually
Abstraction - filtering unnecessary information out of a problem and focusing on what is important.
Algorithmic thinking - logical way of solving problems, step by step

Pseudo-code - follows a similar structure of every coding language - easily readable - can be converted into any programming language
Flowcharts - diagram showing algorithms, using different symbols, arrows.
Casting - changing a data type
Variable -  an identifier with a name that stores a(n adjustable) value - can be changed
Constant - variable that cant be changed
CASE statement - performs different actions for different values of same variable
Selection - when program **interacts** with user
Sequence - an order of instructions in a program
Iteration - when the program uses loops (For, Repeat-until, while, do-while)
Indefinite iteration - when the loop repeats until a condition is met
Definite iteration - when loop repeats exact number of times instructed.
Nested iteration - loop inside another loop
Subroutines - set of instructions stored under one name, function or procedure
procedure - function that doesnt return a value
Local variable - can only be used in the structure they're declared in (subroutine)
Global variable - variable that can be used anywhere in code, after the declaration
ASCII - 7-bit character set - (128 characters)
ASCII extended - 8-bit - 256 characters
Unicode - 16-bit - 65,000+ characters - every possible character in every language
Syntax error - code doesn't follow rules or grammar of the language(SPaG error) - computer doesnt understand - program doesnt run
Logic error - unexpected output - program does run (Human error)
Bit - single binary digit
Nibble - 4 bits
Byte - 8 bits
KiloByte(KB) - 1000 bytes
Megabyte(MB) - 1000 Kilobytes
Gigabyte(GB) - 1000 Megabytes
Terabyte(TB) - 1000 GB

Binary search - ordered lists - start in middle, slice etc
Linear search - works in any list - start from beginning, check each item

Bubble sort - sorts unordered lists - compares first values and swaps - biggest value to right
Merge sort - decomposition method for sorting unordered lists - split, sort, merge back
Insertion sort - sorts unordered lists - compares each value to first value, swaps - biggest value to left

## Components of a Computer System
Hardware - physical items in a computer system - you can see them
Software - programs or applications that computer system runs (e.g Operating System)
General purpose computer - designed to perform many tasks
Dedicated systems - designed for one particular function
Embedded system - systems, usually dedicated, built into another larger device. (E.g: Calculator, washing machine, car navigations, ATMs.)

CPU - Central Processing Unit - processes all data & instructions - fetch-decode-execute cycle - executes instructions
Control Unit(CU) - decodes, executes program instructions in cycle - controls flow of data in (to registers) and out (main memory, input/output devices) of CPU, controls hardware
Arithmetic Logic Unit(ALU) - performs all calculations, logic operations and binary shifts needed - stores result in accumulator
Cache - very fast primary memory - stores frequently used data for quicker access by CPU - more expensive, lower capacity than RAM, slower than registers, faster than RAM.
Level 1 Cache - quickest, lowest capacity - closest to CPU
Level 2 - slower, bigger capacity
Level 3 - slowest, highest capacity

### Memory

Main Memory - where all data, files, programs are stored when being used
Primary storage - Memory areas that the CPU can access very quickly: (Registers, Cache, RAM, ROM)
- fastest read/write times 
- mostly volatile
RAM - main memory in computer - can be read & written to - volatile - slower than CPU cache
ROM - Read Only Memory - can only be read - non-volatile - built into the motherboard. 
- Contains BIOS(Basic Input/Output System) - all instructions needed for a computer to boot up. 
- Copies OS into RAM.

Secondary storage - non-volatile - where all data is stored when not in use: Magnetic HDDs, SSD, CD, Magnetic tapes, SDs
- read/write times are alot slower than primary storage
1) HDD - internal storage in PC/laptops - made up of stack of magnetised metal disks spinning at a rate of 5400-15000rpm - data stored magnetically in sectors within circular tracks, read/write heads access sectors on disk 
- long lasting, reliable, cheap, high capacity
2) SSD - no moving parts - most use flash memory - internal storage 
- significantly faster read/write times than HDD - fastest secondary storage
- dont need defragmenting
- more shock-proof
- silent
- shorter R/W life
- hybrid drives exist, using SSD to boot up computer and HDD for data
3) Optical discs - CD, DVD, Blu-ray - CD = 700 MB of data, DVD = 4.7GB, Blu-ray = 25GB,
  Read-only (CD-ROM, DVD-ROM, BD-ROM) - Write-once(CD-R, DVD-R, BD-R) - rewriteable(CD-RW, DVD-RW, BD-RW)
- cheap, portable, durable from water or shocks
- use is declining, low capacity
- very slow R/W times
- poor reliability
1) Magnetic tapes:
- greater capacity than HDDs (very high)
- extremely low cost per GB (cheapest S.Storage)
- very slow when finding specific data, but fast R/W speeds when data in correct place.
- Often used by large businesses in archive libraries to store huge amounts of data

Array - data structure that can store a group of values, of one same type, under one name
Record - data structure that can store different data types - single row in a data table
Field - individual data items within a record - columns in the data table
Parameter - variables that are passed as a value into a subroutine
Argument - the values that you assign to the parameters
Module - external python file which often contains functions
Structured (modular) programming - decomposing the program that you want to write into manageable modules
Input validation - checking if data meets certain criteria before passing it into the program
Test plan - test to see if a program input is working by testing its boundaries
Normal data - valid data that a user should input into a program
Boundary data - data on the boundary of what the program should accept
Erroneous data - invalid data the program shouldn't accept
Trace table - table to test that a program is working
NOT gate - output is opposite of input
AND gate - if both inputs are 1, then output is 1. Otherwise its not the same and its 0.
OR gate - if one or more inputs is 1, output is 1. The output is only 0 if all inputs are 0