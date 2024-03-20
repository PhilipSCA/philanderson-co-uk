# Computer Science
# Paper 1 - Computer Systems

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
1) Device drivers - 'translators' between OS to hardware - software to communicate with internal hardware/peripherals 
- every piece of hardware has a driver
- When computer booted up, OS chooses correct drivers for the hardware
- If new hardware is connected, system will install the new, matching driver
- Device manufacturers can release updates to drivers to fix bugs, add features or improve performance of hardware.
2) User interface - allows user to interact with computer system 
    - GUI - Graphical UI - visual, interactive, intuitive - optimised for specific input methods - WIMP (Windows, Icons, Menus, Pointers) or touchscreen - Android, iOS - use finger gestures like swiping, pinching 
    - Command-line interface - text based - user enters specific commands for tasks - less resource heavy than GUIs - for advanced users, far more efficient and powerful than GUIs - can automate processes using scripts
3&4) OS helps CPU carry out multi-tasking by efficiently managing memory and CPU processing time: (app = application)
   - When an app is opened, OS moves necessary parts of app to memory, followed by additional parts when they are required. OS decides if apps or features have been used recently - if not, they may be removed from memory
   - To run multiple apps, OS needs to make sure apps dont overwrite or interfere with each other. A memory manager allocates certain apps certain memory addresses, so their processes are placed in separate locations
   - Only one process is processed by CPU at a time - OS divides CPU time between open apps and may prioritise other processes in order for instructions to be executed in the most efficient order
   - When required, OS organises movement of data to and from virtual memory
5) File & disk management - organisation of data in a useable hierarchical structure - movement, editing, deletion of data.
   - file extensions (.jpg, .mp3, .mpeg) tell computer which software used to open file
   - hard disk managed by OS - splits physical disk into storage sectors, decides which sectors to write data to, keeps track of free space of disk.
   - Utility software - helps maintain or configure a computer.
      - file compression software - reduces size of files
      - encryption software - securs contents of files
      - Defragmentation software - helps organise and maintain hard disk by collecting all free space together
6) User accounts - OS can be single-user or multi-user:
  - Single user OS - allow only one user to use computer at once. (Windows 10, OS X). Even if computer has multiple user accounts or is connected to a network, still single-user.
  - Multi user OS - allow several users to use computer at once. Often used on mainframes and give many users simultaneous access. e.g ATMs allow thousands of people access to a bank's mainframe at same time (eg. UNIX server)
User account control - allows different users to be granted access to specific resources on a computer.
 - On most desktop OS, each user has their own personal data and desktop, but cant access other users' data
 - OS may have anti-theft measures to prevent other users from accessing locked devices/accounts to steal info. Accounts may be password, PIN, fingerprint, specific patterns or face ID protected
Defragmenting - reorganising storage on HDD to put fragmented files back together, & collects all free space to prevent further fragmentation. | Fragmented files makes reading & writing much slower as R/W head has to move back and forth.
 - An SSD uses flash storage(no moving parts) - cant be fragmented - can access data quickly no matter how arranged. SSDs have a limited number of read/writes, defragmenting shortens lifespan
Backup - copy of files and settings stored externally. Data can be recovered in event of data loss
Backup utility - software wtih facilities like scheduling regular backups, rescue disks, disk images, options of full or incremental backups.
Full backup - copy is taken of every file on system. Use a lot of storage space - take a long time to create, but faster to restore from
Incremental backup - only files created or edited since last backup copied. Use Less storage space, much quicker to create. A full system restore is slow as last full backup must be restored, and every incremental backup since then.
Compression software - reduces size of files to take up less disk space. Used loads on internet. (.zip, .rar). Compressed files need to be extracted before used.
Encryption software - encrypts data to stop third-parties from accessing it. Can be decrypted using a special 'key'
Open Source Software - software where source code is freely available. Users can legally modify source code to create own spin-off software, that can be shared under same license and terms as original. (Examples: Apache HTTP server, GIMP, Firefox, VLC, Linux)
  - Linux is hugely successful open source OS released in 1991 - most popular linux based OSs are: UBUNTU, Debian & Android
  - Popular open source software is always supported by a strong community - users actively help improve software
Advantages:
1) Usually free
2) Made for greater good - not profit - benefits everyone, encourages collaboration, sharing of ideas
3) Software can be adapted by users to fit needs
4) Wide pool of collaborators can be more creative and innovative than original programmers.
5) Popular software - very reliable and secure - any problems quickly solved by community.
Disadvantages:
1) Small projects may not be regularly updated - can be buggy/have unpatched security holes
2) Limited user documentation
3) No warranties
4) No official customer support
5) Companies using open-source custom code may not want competitors to see their code, but have no choice
Proprietary software - closed source - paid for - only compiled code is released & source code is closely-guarded secret. Licenses restrict modification, copying, redistribution of software.
 - Businesses often use proprietary as it tends to have better customer support options. 
 - Examples include: Microsoft(Office, Windows, Outlook) and Adobe(Photoshop, Illustrator)
Advantages:
1) Comes with warranties, documentation, customer support
2) Well-tested and reliable as company's reputation depends on it. Fixes & updates more regularly or scheduled
3) Usually cheaper for business - dont need to develop custom software
Disadvantages:
1) Expensive
2) May not exactly fit users needs
3) Software companies may not maintain older software after warranties expire - want people to buy latest product


### Memory
Main Memory - where all data, files, programs are stored when being used
Primary storage - Memory CPU can access very quickly: (Registers, Cache, RAM, ROM, flash memory)
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
1) SSD - no moving parts - most use flash memory - internal storage 
- significantly faster read/write times than HDD - fastest secondary storage
- dont need defragmenting
- more shock-proof
- silent
- shorter R/W life
- hybrid drives exist, using SSD to boot up computer and HDD for data
- limited number of read/writes - defragmenting shortens lifespan
1) Optical discs - CD, DVD, Blu-ray - CD = 700 MB of data, DVD = 4.7GB, Blu-ray = 25GB,
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

# Paper 2 - Computational Thinking, Algorithms and Programming

Casting - changing a data type


ASCII - 7-bit character set - (128 characters) - uses less memory space
ASCII extended - 8-bit - 256 characters
Unicode - 16-bit - 65,000+ characters - every possible character in every language


Module - external python file which often contains functions
Structured (modular) programming - decomposing the program that you want to write into manageable modules
Input validation - checking if data meets certain criteria before passing it into the program

Trace table - table to test that a program is working

Binary shift - method to multiply/divide binary numbers by moving all values to left/right (Left = multiply, Right = divide)
Character set - collection of characters that a computer can recognise from their binary number
Colour depth - number of bits used per pixel - 2^(number of bits)
Resolution - the concentration of pixels in an area - given as WidthxHeight

## Algorithms
### Computational Thinking
Decomposition - breaking a complex problem into smaller problems to solve individually
Abstraction - filtering unnecessary information, simplifying to important information in a problem
Algorithmic thinking - logical way of solving problems, step by step solution

Algorithm - ordered set of instructions to complete a task
Pseudo-code - universal - follows similar structure of every coding language - easily readable - can be converted into any programming language - used to figure out structure of program
Flowcharts - diagram showing algorithms, using different symbols, arrows.
 - Start/End - oval
 - Decision - Diamond
 - Input/Output - parallelogram
 - Process - rectangle

Binary search - start in middle, slice - Adv: More efficient than linear, Dis: complex to program, only ordered lists
Linear search - start from beginning, check each item - Adv: any list, Dis: not efficient - long time with long lists

Bubble sort - compares first two values, swaps, moves to next value - biggest value to right - Adv: Simple, Dis: long time
Merge sort - decomposition method - find middle, split, sort, merge back - Adv: (Most) Efficient, Dis: Slow
Insertion sort - compares each value to first value, swaps - biggest value to left - Quick for small lists, slow for long

### Programming
Data type - String, Integer, Boolean, Real, Character
Variable - identifier with name that stores value - can be changed in run-time
Constant - variable that **cant** be changed whilst program is running
Local variable - can only be used in the structure they're declared in (subroutine)
Global variable - variable that can be used anywhere in code, after declared
Exponentation - powers - e.g 2**3 or 2^3 
Quotient DIV - DIV - integer division
Modulo division -  MOD - Remainder
Array - data structure - can store  group of values, of one same type, under one name
1D-Arrays - list 
2D-Array - table - lists within a list
Sequence - order of instructions carried out chronologically in program
Selection - when program **interacts** with user - decisions
Iteration - when the program uses repitition/loops (For, Repeat(do)-until, while)
- Indefinite iteration - (Condition-contolled) when the loop repeats until a condition is met - WHILE, DO-UNTIL
- Definite iteration - (Count-controlled) when loop repeats exact number of times instructed. - FOR
- Nested iteration - loop inside another loop
CASE statement - performs different actions for different values of same variable
#### String manipulation
x.length - Outputs length of string (Starts at 1)
x.upper - changes string to all upper case
x.lower - string all lower case
x(i) - Outputs character in position of integer(i) (Starts from 0)
x.substring(a,b) - Gives characters from a with length b. (e.g x=word, x.substring(2,2) = "rd")
#### File handling
openRead("myfile.txt") - Opens file in read mode
openWrite("myfile.txt") - Opens in write mode
.writeLine("Hello") - Writes line to file
Line1 = myfile.readLine() - Reads 1 line of file
.close - closes files
endOfFile() - determines end of file

Sub-program - set of instructions stored under a name, which can be called to run whole set
Function - Sub-program that returns a value
Procedure - doesnt return a value
Parameter - variables  passed as a value into subroutine
Argument - the values that you assign to the parameters
Record - data structure - can store different data types - single row in a data table
Field - each data items within a record - columns in the data table

### Defensive Design
Defensive design - programmers test their code to: reduce number of errors, prevent misuses, for well-maintained code
Input sanitisation - removes any unwanted characters entered into program
Input validation - Checks if data meets certain criteria before passing it through program. Following checks can be used:
 - Presence check - data has been entered
 - Length check - data is correct length
 - Range check - data within set range
 - Format check - in correct format (e.g dd/mm/yy)
 - Check digit - numerical data entered correctly
 - Look-up table - checks against a table of accepted values
Authentication - program confirms identity of user before giving access to full program. - user accounts, passwords
Maintainability - well-maintained code = easy to edit without causing errors:
 - Comments - other programmers understand code, easier to read
 - Indentation - easy for programmers to see flow of diagram - easier to read, can convert to other languages easier
 - related variable/subprogram names
#### Testing
Final testing - program tested once at end of development - all in one go
Iterative testing - tested & changes made throughout development cycle - may go through process few times
Test plan - test to see if a program input is working by testing its boundaries
Normal data - valid data that user would input into program
Boundary data - data on boundary of what program should accept
Erroneous data - data the program shouldn't accept
Syntax error - doesn't follow rules or grammar of the language(SPaG error) - computer doesnt understand - program doesnt run
Logic error - unexpected output - program does run but returns an unexpected output (human error)
### Logic gates
NOT gate - output is opposite of input (0, 1)
AND gate - if both inputs are 1, then output is 1. Otherwise 0. (0, 0, 0, 1)
OR gate - if one or more inputs is 1, output is 1. The output is only 0 if all inputs are 0 (0, 1, 1, 1)
XOR gate(not needed) - exclusive OR - if exactly one input is 1, output is 1. Otherwise output is 0. (0,1,1,0)
A and B - A ^ B
A OR B - A v B
NOT A - ¬A
Truth table - show all possible combinations of inputs and outputs in circuit
- Computers use binary to represent flow of electricity in circuits. 1=on, 0=off
Bit - single binary digit
Nibble - 4 bits
Byte - 8 bits
KiloByte(KB) - 1000 bytes
Megabyte(MB) - 1000 Kilobytes
Gigabyte(GB) - 1000 Megabytes
Terabyte(TB) - 1000 GB
Petabyte(PB - 1000 TB)

### Languages
High level language - need to be translated into machine code - cannot be understood by computer (Python, java)
 - Each instruction is many machine code instructions
 - Code transferable to many different computers and processors
 - Data stored in structures (lists, arrays)
 - Easy to read, understand
 - Dis: Less memory efficient - no control over CPU
Low level language - Machine code(binary) & Assembly:
 - written for one particular machine/processor
 - programmer needs to understand how CPU manages memory
 - Difficult to read, understand
 - Machine code can be executed without translators
 - More memory efficient - control what CPU does

Assemblers - turn assembly language to machine code
Compilers - Translate all code in one - creates executeable file. (Source code --> assembly --> machine)
 - can take a long time, but final code runs quickly
 - gives list of errors for entire program
 - Adv: Execution faster, no need for translation software at run-time, code optimised
 - Dis: Source code easier to write in high-level, but program wont run with syntax errors - more difficult
   - code needs to be recompiled when changed
   - Designed for specific type of processor
Interpreters - translates source code one line at a time.
Adv: - Easy to write source code - program always runs, stops when finds syntax error
     - does not need to be recompiled when changed - easy to try out commands when program finds error
     - easy for beginner programmers to learn to write code
Dis: - Translation software needed at run-time
     - Slower
     - code not optimised
     - source code is needed
