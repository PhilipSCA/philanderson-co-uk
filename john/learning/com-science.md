# Computer Science
## Paper 1 - Computer Systems
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
Indefinite iteration - (Condition-contolled) when the loop repeats until a condition is met
Definite iteration - (Count-controlled) when loop repeats exact number of times instructed.
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
NOT gate - output is opposite of input (0, 1)
AND gate - if both inputs are 1, then output is 1. Otherwise its not the same and its 0. (0, 0, 0, 1)
OR gate - if one or more inputs is 1, output is 1. The output is only 0 if all inputs are 0 (0, 1, 1, 1)
XOR gate(not needed) - exclusive OR - if exactly one input is 1, output is 1. Otherwise output is 0. (0,1,1,0)
Binary shift - method to multiply/divide binary numbers by moving all values to left/right (Left = multiply, Right = divide)
Character set - collection of characters that a computer can recognise from their binary number
Colour depth - number of bits used per pixel - 2^(number of bits)
Resolution - the concentration of pixels in an area - given as WidthxHeight
 
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

### System Software
Operating System - OS - complex piece of software - manages hardware and runs software. Main functions:
   1) Communicate with hardware(internal & external) by device drivers
   2) Provide user interface
   3) Provide a platform for different applications to run
   4) Controls memory resources and CPU - allows computer to multi-task 
   5) File management, disk management
   6) Manage security of system - through user accounts
Multi-tasking OS - can run multiple applications at once
Device drivers - 'translators' between OS to hardware - software to communicate with internal hardware/peripherals 
- every piece of hardware has a driver
- When computer booted up, OS chooses correct drivers for the hardware
- If new hardware is connected, system will install the new, matching driver
- Device manufacturers can release updates to drivers to fix bugs, add features or improve performance of hardware.
User interface - allows user to interact with computer system 
  - GUI - Graphical UI - visual, interactive, intuitive - optimised for specific input methods - WIMP (Windows, Icons, Menus, Pointers) or touchscreen - Android, iOS - use finger gestures like swiping, pinching 
  - Command-line interface - text based - user enters specific commands for tasks - less resource heavy than GUIs - for advanced users, far more efficient and powerful than GUIs - can automate processes using scripts



### Memory
Main Memory - where all data, files, programs are stored when being used
Primary storage - Memory areas that the CPU can access very quickly: (Registers, Cache, RAM, ROM, flash memory)
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


## Networks
LAN - Local Area Network - small geographical area located on a single site - all hardware owned by organisation - wired or wireless - in homes, businesses, schools, universities etc.
Advantages:
- Sharing files is easier - network users can access same files, work at same time and copy files between machines
- Can share same hardware (eg printers)
- Internet connection shared to every device
- Can install and update software on all computers at once
- cheap, easy communication with other members - instant messaging
- User accounts stored centrally - users can log in from any device
### Network Threats - Malware
Malware - malicious software - installed on a device without person's knowledge or consent
Types of Malware (3 main ones):
1) Virus - copy themselves & attach to certain files (.exe, autorun scripts) - users spread them by copying them - activate them when file is opened
2) Worms - viruses that self-replicate without user help - spread very quickly - exploit weaknesses in network security
3) Trojans - malware disguised as real software - don't replicate, users install them through links
Actions of malware:
1) Scareware - tells user their computer is infected - scare them into malicious links or paying to fix problems
2) Ransomware - encrypts all files on computer - demands money in exchange for decryption key
3) Spyware - secretly monitor users actions (key presses), sends info to the hacker
4) Rootkits - alter permissions - give malware and hackers administrator-level access to devices
5) Backdoors - holes in security used for future attacks
##### Attacks:
Passive attack - monitors data travelling on a network and intercepts any sensitive information - network-monitoring ware like packet sniffers - hard to detect - best defence: encryption
Active attack - someone attacks a network with malware/ planned attacks - more easily detected - best defence: firewall
  - Brute force attack - type of active attack - gain information by cracking passwords through trial and error - automated software to produce hundreds of likely combinations - defences: account lock after number of failed attempts, strong passwords
Insider attack - person within organisation exploiting network access to steal information
Denial-of-service (DoS) attack - hacker stops users from accessing a part of network or website - involve flooding network with useless traffic - make network extremely slow or inaccessible

Social engineering - gaining sensitive information|illegal access to networks through influencing people, usually employees
Phishing - sending emails/texts to people pretending to be from well-known business - contains links to spoof websites - enter personal information - hackers access their genuine account (Vishing, smishing, whaling, angler, pharming)
 - Vishing - voice phishing - phishing over voice calls - asks them for personal info
 - Smishing - SMS(text) phishing - phishing with mobile texts
 - Whaling - phishing directed at high-level executives - pretends to be a known, trusted person
 - Angler - social media phishing - e.g pretending to be customer support to get details
 - Pharming - redirecting people to fake malicious websites - enter personal info - harder to identify
 - Ways to tell its fake: poor grammar/spelling, check the email @ is correct, suspicious links, sense of urgency 
SQL injections - used for weak validation, insecure SQL databases - pieces of SQL typed in a websites input box that reveal sensitive information - "1=1" is always true in SQL 
##### Network policies:
Penetration testing - organisation employ specialists to try to attack their network - identify weaknesses
Network forensics - investigations undertaken to find cause of an attack - system to analyse data packets entering network - discover how & prevent future attacks
Passwords - prevent unauthorised access - strong passwords - 10+ characters long, upper and lowercase, numbers and symbols, changed regularly
User access levels - different users can access more parts of network - help limit number of people with access to important data - prevents insider attacks, harder to scam network
Anti-malware - software designed to find and stop malware from damaging network - e.g antivirus programs
- firewalls - block unauthorised access - examine all data entering and leaving network, block any potential threats
Encryption - data(plain text) translated into unreadable cipher text - only person with decryption key can access - essential for sending data over network securely - prevents passive attacks etc.
