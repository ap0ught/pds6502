# The PDS Z80 Manual

> **Auto-converted from:** `The_PDS_Z80_Manual.pdf`. Text extracted from the original PDF; OCR may contain recognition errors. Consult the PDF for exact diagrams and formatting.


---

<!-- Source PDF page 1; extraction: ocr -->




---

<!-- Source PDF page 2; extraction: ocr -->

- The assembler is the sole property and copyright
of P.D. Systems Ltd. Revisions to the specification
of the assembler may be made at the author’s discretion.
Users of the system, will of course be notified of these
revisions, and downward compatibility will be
maintained, where at all possible.

This manual is the copyright of P.D, Systems Ltd.
No copying, duplication or any other
such acts which may be interpreted as a breach of copyright
may be performed without the authors’ permission.

The contents of this document are copyright 1987.


---

<!-- Source PDF page 3; extraction: ocr -->

Contents

1 The Programmers Development System Z80 assembler

2. Expression evaluation

3.1
3.2

41
42
43

44

Sa
5.2
5.3

61
6.2
63
6.4
6.5

The assembler pseudo opcodes

Assembly listing related pseudo opcodes

Example programs
Errors during assembly
Example macros in the Z80 assembler

Different syntaxes allowed in Z80

The PDS download software
The PDS download software protocols

The control lines during PDS communication

The PDS Z80 Monitor

The PDS monitor commands

The options and configure system in the monitor
The trace system

The trace system options


---

<!-- Source PDF page 4; extraction: ocr -->

The PDS Z80 Manual 1

1 The Programmers Development System Z80 Assembler

‘The assembler is invoked from the editor at any position in the source code by pressing the [ASSEM]
function key. Assembly begins at the start of file 0 and will continue through the files until the end
of file 7, or an END is reached. If an error occurs during assembly the assembler will stop, display

. an error message and move the current cursor position to the start of the line containing the error.
Clear the error message by pressing any key, correct the error and reassemble again.

Each line is individually processed and assembled. The assembler is looking for a number of
possibilities the line could contain.

Labels in PDS must start on the first character of the line. Labels can be of any length, containing
any valid label characters for that particular assembler. The first character can be any valid label
character, except the numeric digits 0 to 9. The valid label characters that are allowed in the Z80
assembler are:

#$%.0-927A-Z_£

Note the assembler is not case sensitive, it converts everything into upper case, At the end of the
label PDS will ignore one non-label character. This means that if your source code has come from
an assembler that demands labels be followed with colons or hashes then PDS will ignore the extra
characters, For example, PDS accepts all these syntaxes as label definitions for FRED:

FRED NOP
FRED: NOP
FRED# NOP

This feature may cause a problems if you insert an extra character by mistake, as in the following
examples:

FRED + NOP
FRED- NOP
FRED* NOP
FRED; NOP

Notice the semicolon in the fourth example does not cause the rest of the line to be ignored, it is
treated as the label terminator. If you don’t want to define a label on a line you must enter at least
one space or tab. In between all the fields on a line, PDS will skip over any number of tabs and/or
spaces. After a label PDS will expect to find a pseudo opcode or mnemonic. If you have an isolated
label in a line, it is given the current value of program counter.

Comments may be included anywhere in the source code, they are preceded by semi colons. Note,
never use a semi colon for a comment immediately after a label as it will read as the label terminator
character, After a semi colon the rest of the line is ignored. At the very start of a line you may also
use an asterisk to make the assembler ignore the line. For example:

3 This is just a line of comment
coreereereererd

* Soisthis *

prereteecetertd

NOP } This is a comment


---

<!-- Source PDF page 5; extraction: ocr -->

2 The PDS 280 Manual

2 Expression Evaluation

When a label is at the start of the line, it is set to the current value of the program counter (the
program counter is the address where code is assembled to). You may have an number of labels,
each having the same value. For example:

FRED
JOHN
BILL NOP.

FRED, JOHN, BILL all have the same value, the memory address of the NOP instruction.

Local labels are a major part of PDS, any label that starts with a dollar sign ($) is considered a local
label. You may use local labels in the same way you'd use normal labels, although every time you
use a ‘normal’ label, all the local label definitions are cleared. We recommend that you use normal
labels at the start of main subroutines, and local labels within the subroutine. This way you will
never get re-defined label errors. Below is an example of local labels.

$1 NOP
NOP
JP $1 ;(Jumps to the first $1)
FRED... NOP
JP $1 i(Second)
NOP
$1 DJNZ $1 i(Second)
NOP
BILL NOP
NOP
$1 JP $41 i(Third)

You should try and use local labels as much as Possible. , For short jumps (over a few bytes) it is not
worth having to think up a valid label name. Local labels must be used in macros to prevent multiple
definitions, but they will not affect other local labels with the same name, either in the main program,
or in nested macros. Local labels also make it easy to copy large blocks of source code, because if
all the labels are local, they need not be altered. Just ensure that you insert a normal label in front
of the copied code.

Ifyou wish to know the current address of the program counter (PC) in an expression then you may
use '*" or'S', which will return the current PC, So the example below, FRED, BILL, JOE and JOHN
are given the same value:

FRED EQUS
BILL EQu*
JOE

JOHN NOP

Note: The $ stands for current PC only when it is followed by a non label character, otherwise it
would be treated as a'local label reference, It has been included in both these formats for
compatibility with other assembler packages,


---

<!-- Source PDF page 6; extraction: ocr -->

The PDS Z80 Manual 3

Numbers in PDS may be entered in HEX, DECIMAL, ASCII or BINARY,

To enter anumber in decimal just enter the number as normal. PDS will allow you to enter numbers
from -32768 to 65535, but remember that minus numbers are a duplication of the numbers 32768 to
65535. For example, if you entered -20/4 the expression would return 16379 instead of -5 28 you
might expect. This is because the -20 was treated as 65516 (the 2's complement value).

To enter a number in HEX, you may either enter it starting with a hash (#) eg: #1234 or #ABCD
oruse the more familiar duo where d is a digit 0-9 and xis a HEX digit O-F, eg: 1234h or ABCD

To enter a number in BINARY follow the string of ones and zeros with a’B’ eg: 1010B or 1001110b

Toenter ASCII values, just enclose them in double quotes, for example "a" returns 61h, or*ab" returns
6261h

Expressions in PDS can contain labels, numbers and any number of brackets and operators.
+ Expressions are evaluated from left to right using standard mathematical priorities, for example:
2+3°6 will return 20 not 30. The operators PDS allows are as follows:

- Negate, if a number or label, not an expression, is preceded by a minus sign then
its value will be negated. If you wish to negate an expression then you should use,
-1* (expression).

+7 Will add, subtract, multiply and divide the two operands. There are no error
checks on these operations, so you may have expressions such as 60000°S or
60000 + 60000 which will return the result MOD 65535, Remember that division
will round down, so 7/3 will be 2.

oe . Will.Jogical.AND the wwo:operands.
! Will logical OR the two operands.
7 Will logical XOR the two operands,
= Ifthe two operands afe equal, this will return one, else it will return zero. eg: S=4
returns 0 and 23 = 23 returns 1.
<> Is the reverse of the above.
> If the expression on left hand side, is greater than the right hand side expression,

then this will evaluate to one, otherwise zero is returned,
< Is the reverse of the above,

If’>’ or'<" is at the start of an expression, PDS will return either the low or high bytes only. For
example > #1234 will return #34 and < #1234 will return #12. This is the default setting, the arrow
Pointing at the byte returned. You may reverse this setting in the configuration system, so that
> #1234 would return #12. Note the greater or lesser than signs can only be used at the start of
expressions, eg: > 23°S2+FRED. If you want to use high or low bytes within an expression you will
have to surround the expression with brackets eg: 23 + 52*(< FRED).

The expressions are evaluated from left to right, except for operators with higher priorities.
Operators are evaluated in the following order:


---

<!-- Source PDF page 7; extraction: ocr -->

4 ‘The PDS Z80 Manual

(and)

< and > - when used to return LSB and MSB,
*and/

+ and-

=,<>,>,and< ~.when used as more than and less than.
&, land ~ .

So 2+78&3 will evaluate 2+7 then AND with 3, returning 1. Or 7&3 +2 would evaluate 3+2 then
AND with 7, returning 5. Brackets can be used to override these priorities, as they have the highest

priority.

A nice feature in PDS is the ability to check the range of expressions in the program code. If you
Want an expression to return a value only within a specific range, eg between 100 and 120, thea siniply
insert the range directly after the expression, enclosed in square brackets. For example:

FRED*2+3-BILL [100,120]

Will given an ‘expression out of range’ error if it evaluates to below 100, or above 120. The ranges
could even be expressions themselves, they don’t have be numeric, This does not affect the
expression in any way and is ignored by the assembler, unless the expression is out ofrange. Spaces
and/or tabs can be used after the expression and before the range check, and will be ignored, eg:

LD (IX+FRED +23 (58,70)),BILL*2 [2,6]

One common mistake is to.use expressions brackets in.the wrong place-and.foobthe assembler, for:
example:

LD A, (FRED +2)*3
Would give an extra characters on line error, as the expression in brackets would be treated as a
indirect memory reference, the *3 would be extra characters. If you wish to use this sort of expression

then you would have to enter it as below :

LO A,3*(FRED +2)
or
LD A.0+(FRED +2)+3

Which would load A with the immediate value of the expression.


---

<!-- Source PDF page 8; extraction: ocr -->

The PDS Z80 Manual 5

3.1 The assembler pseudo ops.

Most pseudo ops have a number of different syntax, this is to allow the programmer to use source
code directly from other assemblers without having to make too many changes. Any or all of them
can be used in your programs, all of which will perform exactly the same task.

‘There are two pseudo opcode lists, the first covers the usual code related pseudo ops, while the
second list is specifically for assembly listings related pseudo ops.


---

<!-- Source PDF page 9; extraction: ocr -->

6 The PDS 280 Manual

ASK - Will get a yes/no response from the user

ASK must be used on a line with a label. This pseudo opcode will stop assembly on pass 1, print the
message following the ask pseudo op, adding this prompt, '(Y/N)?”, automatically, ‘The user has to
now press either [Y] or [N], in response to the prompt. If [N] is pressed, then the label is given a
value of zero while depressing [Y] will assign a value of one to the label. Note: due to the way the
assembler works, any text following the command will be converted into upper case. To use lower
case as well puta single quote at the start of your message. For example:

CHEAT ASK "Cheat mode

Will stop assembly and display the following message in the command window:
Cheat mode (Y/N)?

Then wait for a ¥ or N response.

Similar pseudo opcode is QUERY.


---

<!-- Source PDF page 10; extraction: ocr -->

‘The PDS Z80 Manual 7

BANK. - Downloads code into different memory banks

Syntax: BANK <bank number 0-255 > {start address]

This is a very complex command in PDS, but it allows the user to program computers which either
have banked RAM, or a RAM capacity greater than 64K. If PDS finds a BANK command in your
program, the indicated bank number is sent to the target computer. This will then select the correct
bank configuration, download all the assembled code before the BANK pseudo opcode. Only the
code assembled from the last occurrence of a BANK pseudo opcode, or the start of the program,
will be downloaded. Ifa start address is specified, then the downloader will jump to the address, and
continue the assembly.

The bank numbers mean nothing to PDS, these are just passed directly to the target computer
download software, the programmer must add their own routines to the download software to
interpret them. Ona Spectrum 128, the user could simply OUT the number to the bank select port,
See the chapter on the download software for more information.

By allowing an optional start address the user can make the target computer jump to the routine just
downloaded, while PDS continues assembling. Here is one possible use for this powerful function,

If the download software is located at 8000h and the programmer wants to write code to this address,
to save having to make a new copy of the download software, simply download it somewhere else in
memory. The program would then look something like this:

ORG 7000h
oo ‘DOWNLOAD SOFTWARE'CODE(SPEC:DL1 foriexample) “*

BANK 0,7000H
ORG 8000H

** PROGRAM CODE **
END

What this will do is assemble anew copy of the download software at 7000h, jump to it, then download
the main program at 8000h, where the old download software used tobe, This is assuming that the
download software would take BANK 0 as being main memory. This is only one example of bank's
use. It can also be used to download code overlays (routines that run at a common address)
individually, then save them to disk, compress them, or move them about in memory.

Note: After a bank command, the assembler is ‘reset’, apart from the symbol table, which means the
user will have to insert anew ORG before code following the BANK pseudo op. The SKIP function
will also be disabled.

If required to write code for a computer with a number of banks the program would look something
like:


---

<!-- Source PDF page 11; extraction: ocr -->

8 The PDS Z80 Manual

ORG START

** PROGRAM FOR BANK NUMBER 1 **
BANK 1 .

** PROGRAM FOR BANK NUMBER 2 **
BANK 2

** PROGRAM FOR BANK NUMBER 3 **
BANK 3
END

Note that PDS will automatically download the code on pass 2, without prompting "Download
(Y/N)?’, otherwise downloading could become very tedious, particularly when using a number of
banks. Ifan error occurs in the second pass, while PDS is assembling the code for bank 2, you should
note the code for bank 1 will already have been assembled and downloaded. The target computer
will also still be setup for BANK 1.

To change bank, without downloading code, then simply insert the bank command before the ORG
pseuido opcode. This may have to be done in the last example, if START was actually in bank 1.
Under these conditions the program will not run correctly, because the last block of code was
downloaded to bank 3. So when the execution address is passed, it will execute code in bank 3. To
get around this situation, insert the setup of the correct bank for the execution label, in this case a
"BANK 1’ command directly before the 'END’ in the program,

After assembling the complete program, the prompt "Download (Y/N)’ appears as normal.

Rather than have bank numbers such as 0,1,2.... most software will have odd numbers such as 139
for main memory, 192 for bank 1 etc. The code will be more readable if you define equates such as:

MAIN EQU 139
ONE EQU 192

Then enter BANK ONE or BANK MAIN.

Note that when using the BANK command, skip is disabled, and you will see ‘no skip’ displayed in
the command line window after assembly has been completed.


---

<!-- Source PDF page 12; extraction: ocr -->

‘The PDS Z80 Manual 9

CBM - Commodore define message

‘This has the exactly the same syntax as DB, but any text in quotes will be given in the Commodore
64 screen codes rather than ASCII. For example:

CBM "CAT"
produces :3,1,14h

This command does not allow text to be used in expressions though eg: "C"+ 128 would not be
allowed.

Similar pseudo opcodes, see DB.


---

<!-- Source PDF page 13; extraction: ocr -->

10 The PDS Z80 Manual

DB + Defines bytes and messages.
DFB
DEFB

EQUB
«BYTE
ASCH
TEXT
ASC

STR

DEFM

DM
DFM

Following the command there can be any number of parameters, separated by commas, each of which
must be an expression within the range -128 to 255. Strings of text and text mixed with numerie
expressions can also be used. For example:

DB 23,45 + 52-FRED,"This is a test message", 13,10,"!"+ 128

Toinclude the quotes character inside strings, put two quotes one after the other eg: "Say""HELLO"™"
would produce : SAY “HELLO”, .

-BYTE is slightly different in that if there are no parameters it will default to .BYTE 0.

For similar commands see CBM, DC and STRING.
For a faster way of storing data see HEX.


---

<!-- Source PDF page 14; extraction: ocr -->

‘The PDS Z80 Manual uu

DC - Define message, ending in bit 7 set.

this pseudo opcode is very similar to DB, but any text strings will have bit 7 set on their last character,

Many programmers use this format for text, to indicate that the end of a string has been reached, for
example:

OC 2,"cat",13,"1"
would produce:
2,63b,61h,0F4h,13,0Aih

For similar command see DB, CBM and STRING.


---

<!-- Source PDF page 15; extraction: ocr -->

2 ‘The PDS Z80 Manual

DH + Define high bytes only
DHIGH

Is similar to DW, but adds a"<’ (gets high byte of expression only) in front of all the expressions. It
is mainly-used when you have tables of high and low bytes in programs. This is a common occurrence
in 6502 code. For example: :

DH 65500,23,500
will produce: OFFh,0,1

For similar commands see DL,


---

<!-- Source PDF page 16; extraction: ocr -->

‘The PDS Z80 Manual B

DL - Define low bytes only
DLOW :

This functions in a similar way to DW, but a ">" (symbol to get low byte of expression) is added in
front of all expressions. ‘This is mainly used when you have tables of high and low bytes in programs,
‘This is a common occurrence in 6502 code. For example:

DH 65500,23,500
will produce: 0DCH,23,0F4h

For similar commands see DH.


---

<!-- Source PDF page 17; extraction: ocr -->

The PDS 280 Manual
DO

+ Used in DO...LOOP or DO...UNTIL expressions

" ‘There are two different syntaxes for the ‘DO’ command, both uses produce blocks of similar code.

DO expression

ooo program code xx000cx

LOOP

This will repeat the block of code be
of times. For example:

‘tween the DO and LOOP pseudo opcodes, expression number

Dos

LD A,(DE)
LD (HLA
INCH
INC DE

LOOP

Note that the expression after the DO is only evaluated once, when the DO is first assembled. When’
LOOP is executed the local labels are cleared, allowing local labels to be used in DO structures, ie:

DOs
ADD 20
JR NC,S1

INCH
INC DE

$1
LOOP
‘The second syntax for the DO command, is as follows:
bo
yo0ex program code xe00x
UNTIL expression

This is similar to 'DO...LOOP’, but the expression is evaluated each time and will only exit when it
Teturns anon zero value, This could be used in the following way:


---

<!-- Source PDF page 18; extraction: ocr -->

‘The PDS Z80 Manual

DO

LD A,(HL)
LD (DE)A
INC H
INC DE

UNTIL $> 1000

fills memory with the code until the PC

just in case the code stepped ‘over’ that
to wrap round at 65535.

15

Goes above address 1000, Note that $= 1000 was not used,
address, in which instance it would keep looping until it tried


---

<!-- Source PDF page 19; extraction: ocr -->

16” ‘The PDS Z80 Manual

DS - Define a space of memory
DFS -

DEFS

-BLOCK

Syntax : DS length of block {filler byte}

Isused for either leaving or filling areas of memory. By entering :

DS 20
the PC will be moved on 20 memory locations, Note when downloading the code the 20 locations
will be filled with random data, you cannot assume anything. If you wish to fill the 20 bytes with

zeros then you should use

DS 20,0


---

<!-- Source PDF page 20; extraction: ocr -->

‘The PDS Z80 Manual 7

DW + Define words
DFW

DEFW

.WORD

‘This is similar function to DB, but defines word rather than byte values. There may be any number
of parameters following the command, all separated by commas, but will only accept strings one or
two characters long. The expressions should range from -32768 to 65535. As with.BYTE,.WORD
is different in that if you don’t have a parameter following the command, it will default to the
equivalent of DW 0.

Example:
DW 0,23,23*5,FRED +45,"ab"

For a faster way of storing data see HEX.


---

<!-- Source PDF page 21; extraction: ocr -->

8 . The PDS Z80 Manual

END - End of your program
.-END

Normally the PDS assembler will stop at the end of file even while assembling a program. By
inserting an END statement in the code, the assembler will stop at that point, Specify the execution
address of your program by placing it after the end, for example:

END START

or

END 8000h

Once the program is assembled an execution address is given. If it is downloaded, the target
computer will automatically jump to this address. If an execution address isn’t included and you
download code after assembiy, the target computer will continue executing the download software.
You may also specify the execution address with other commands (see EXEC), you may only specify
the start address once though.


---

<!-- Source PDF page 22; extraction: ocr -->

‘The PDS Z80 Manual . 19

ERROR - Stop the assembly with a user error.

Syntax: ERROR message

‘When the assembler encounters this line, it will terminate assembly and print the specified message
in the command line window. Once a key is pressed, you are returned to the editor with the cursor
on the ERROR line, Normally this is used in an ‘IF...ELSE...ENDIF’ structure when something
has gone wrong, or a condition has not been met. As with ASK and QUERY, the assembler will
convert the message into uppercase unless a single quote is placed at the start of the message. A
terminating quote is not required, and if used, will be printed as part of the message.

Examples: .

ERROR "Tao many aliens! .
ERROR "Coordinates were off the screen


---

<!-- Source PDF page 23; extraction: ocr -->

F 0 : ‘The PDS 280 Manual

EQU OE - Equate a value to a label
EQ’

-EQU ¢

DEFL

The line with the EQU must have a label at the beginning. The label will be given the value of the
expression following the EQU, The expression must return the same value on pass 1 and pass 2. No
undefined labels can be used in the expression. Therefore, a forward reference to a label would not
be allowed in the expression.

DEFL and = are slightly different in that because they allow the label on that line to be used again,
theyare called re-definable, You can redefine these labels as often as you wish, for example:

FRED =2 iFRED is set to 2
FRED = FRED+1 ;FRED is now equals 3

This could be used in a loop. To fill 20 bytes with the numbers 0) to 20 you could do the following:

TEMP =0
DO 20
DB.FRED.,
FRED = FRED+1
Loop

Normal equates cannot be re-defined, a ’multiply defined label’ error will occur ifyou try. Equates
help to make programs more readable by giving names to arbitrary figures.


---

<!-- Source PDF page 24; extraction: ocr -->

‘The PDS Z80 Manual a

EXEC - Define your programs start address
START
Syntax: EXEC expression .

‘This will define the execution address of the program. By using an execution address, after code is
download, the target computer will jump to it. Ifan execution address is not specified then the code
will still be downloaded but the target computer will continue running the download software. You
may also define the start address by having it as an expression after the END command, If you wish
to trace programs, or use the monitor, don’t puta start address for your programs.


---

<!-- Source PDF page 25; extraction: ocr -->

2 The PDS Z80 Manual

FREE - Adds up free space in your programs
g)

Syntax: FREE expression

Atthe beginning of assembly, the assembler clears the free memory variable, and every time a FREE
command is issued, the expression following the command is added to the free variable. At the end
of assembly the free memory is displayed in the command line window. This need not be used for
free memory, it could be used to tell you the value of a symbol, or one particular address. To use
free to add up all free memory, insert a FREE pseudo opcode before each ORG, ie:

FREE 8000h-$
. ORG 8000h

If the PC was on 7FF2h before the ORG then FREE will tell you there are 14 bytes of free RAM.
Normally a FREE pseudo opcode is inserted before all ORGs, and a free at the end of the program
with RAMTOP-S as the expression. You will then know the exact number of bytes available as free
memory. Ifyou don’t want to use FREE to add up free memory, then the function has other uses,
ie:

i) Finding the length of routines by having a FREE END-START inyour code. As
you change the routine you don't need to have list on to find out the routine’s
exact length.

Displaying the value of labels, whose values can then be used in the monitor by
having FREE DATAAREA. The value of DATAAREA is printed after
assembly.


---

<!-- Source PDF page 26; extraction: ocr -->

‘The PDS 280 Manual B

HEX ~ Define hex bytes

Syntax: HEX x,

PDS often uses HEX statements, because they are very fast, compact and easy to read. HEX is
followed by 2 digit HEX bytes, which may be separated with spaces or tabs. You can fit up to 57
HEX bytes on one 120 character line. We recommended that you put all your data in this format,
simply because it’s easy to use. If you have many DEFB's, assemble and download them, then upload
them into HEX bytes using the monitor.


---

<!-- Source PDF page 27; extraction: ocr -->

4 ‘The PDS Z80 Manual

IF - Conditional assembly

Also covered in this section

ENDIF
ELSE
IFS
IFF

When assembling something depending on a condition, use the "IF command. If the expression
after the IF returns a non zero value, then the code after the IF will be assembled. If the expression
is equal to zero, the code will be ignored until an ENDIF is found. You may nest IF statements to
adepth of 10. For example:

IF FRED =23
This code will only be assembled if FRED = 23
ENDIF

You may also use ELSE to allow the assembler to assemble an alternate piece of code, if the
expression is equal to zero, eg:

IF FRED

This code will be assembled if FRED < >0
ELSE

This code will be assembled if FRED =0
ENDIF

IFF is similar to IF, but will only assemble the following code if the expression after the IFF contains
aforward reference. This is necessary because normal IF statements cannot have forward references
in their expression as the assembler needs to know the route of action on both pass 1 and 2, An
error will be given if it cannot evaluate the expression completely. For an example of IFF see the
example macros chapter.

IFS is similar to IF, but is used for string comparisons. The code following will only be assembled if
the two strings contained in square brackets are equal. For example:

\FS [FRED] [BILL]
this will not be assembled
ENDIF

IFS [FRED] [FRED]
this will be assembled
ENDIF

IFS is mainly used in macros, with parameters such as:

1FS [@1] [SCREEN]


---

<!-- Source PDF page 28; extraction: ocr -->

‘The PDS Z80 Manual 2

You inay use it to see if a macro parameter exists eg:

IFS (@1) 0)

You may compare the first string against a number of different strings. If any one of them is equal,
the following code will be assembled. For example:

IFS [FRED] [BILL] [JOHN] [TONY] [FRED]

This will be assembled
ENDIF

Note: Due to the way the assembler works, all the parameters will be converted into upper case.


---

<!-- Source PDF page 29; extraction: ocr -->

6 The PDS Z80 Manual

INCLUDE - Reads source code from the disk. file
-INCLUDE :

FILE

Syntax: INCLUDE filename

When PDS finds an INCLUDE pseudo opcode in the source, it will try and open the specified file
and start reading source code from that file. When the end of the disk file is reached PDS will go
back to the line directly after the INCLUDE in memory, The filename may contain drive speci-
fiers and path names, for example:

: INCLUDE A:\PDS\GAMES\EMPIRE\ GRAPHICS
INCLUDE FRED
INCLUDE BILL.TXT

‘You may not nest include files, but you can have as many as you like in your main program. If there
are large amounts of data in the program, preferably with no forward references (graphics data is a
perfect example), store them in include files, As data in include files is only read in on pass 1 (with
skip working), on a hard disk INCLUDE's are very fast, so assembly is hardly slowed down. This
means the largest program that PDS can assemble is determined by the size of the disk drives attached
tothe-host systenrand the size-of'source in RAM:

— en


---

<!-- Source PDF page 30; extraction: ocr -->

rr

‘The PDS Z80 Manual . . . 27

MACRO ~ Define a new command in the assembler

.MACRO

Also covered in this section:

ENDM
.ENDM
EXITM

This pseudo op is used to generate new instructions for the assembler. To define a new instruction
called FRED, which will insert four NOPs into the object code, the following code would be used:

+ FRED MACRO
NOP
NOP
NOP
NOP
ENDM

This should be placed near the start of the program, before the macro is invoked. Whenever
assembling FRED as a normal instruction, four nops will be inserted into the code instead. You
may have up to 250 different macros. You may not have macros with the same name as pseudo ops
or instructions already in the assembler.

“Parameters may also be passed macros. ‘Parameters should be separated by commas and are referred
to in the macro definition by @1 to @9. So if you invoked the above macro by using:

FRED bill,23,"hello*

Then @1is set to’bill’, @2is set to '23' and @3 is set to “hello”. Note that macro parameters need
not be expressions, They are text strings that are inserted into the code in the macro in place of the
equivalent @ number (@1 to @9). For example: .

SUM MACRO
@1A,@2
ENDM

SUM ADD,3
SUM XOR,23

You-may also define labels eg:

VAR MACRO '

@1
VARS = VARS+@2

ENDM


---

<!-- Source PDF page 31; extraction: ocr -->

Bs ‘The PDS Z80 Manual

VARS = 8000H
VAR FRED,2
VAR BILL,1
VAR JOHN,3
VAR JANE,1

The above macro is used to define variables in a data area, when each variable has adifferent length.
This is useful as variables need not be tied to absolute memory addresses. [tis possible to insert or
delete variables as they will never overlap. Also you can define labels within your program, when
you need them - you do not need to define them together at the start. In the above example the
labels would have been defined in the following way:

FRED : 8000H
BILL : 8002H
JOHN + 8003H.
JANE : 8006H

If macro’s parameters are all expressions, then you can refer to them as labels within the macro:

FRED MACRO JOHN, BILL, JANE
LD AJOHN
ADD BILL
XOR JANE
ENDM

‘This has been included for: compatibility. Assembling the macro with list on and list macro produces
code for FRED 2,3,4°as follows:' ~

JOHN =2

BILL =3

JANE =4
LD AJOHN
ADD BILL
XOR JANE

Macros can be nested to a depth of four, but may not be recursive, Labels can be used in macros,
although it would be best not to define any, as using the macro more than once will give a multiple
definition error. To define labels in macros, use local labels. This will not affect other local labels
of the same name in the source code, or in other nested macros, See the following example:

BILL MACRO
$t NOP
JP $4
ENDM
FRED MACRO
$1 BILL
JR $1
ENDM
St FRED
JP $4

‘The code produced is quite useless, but you can see that the local labels really are local. Note that


---

<!-- Source PDF page 32; extraction: ocr -->

‘The PDS Z80 Manual »

because local labels are local to macros, you cannot reference a local label outside the macro
definition. For example, using a macro parameter of $1 means that the assembler would only search
the macro definition for the $1, It would not use the $1 from the source code that called the macro.

Macro parameters are separated by commas, leading and trailing spaces are not passed to the macro,
Ifyou wish to pass the comma character then enclose the parameter in Square brackets, for example:

FRED 23,[45,56,67],98

@ = 23
@2 = 45,56,87
@3 = 98

EXITM isused with IF, IFF or IFS statements inside a macro. When EXITM is executed, the macro
definition halts and returns to the main program - basically it is the same as an ENDM, except that
uncompleted conditional structures are cleared. For example:

FRED MACRO
IFS (@1) ]
EXITM

ENDIF
ADO @1
ENDOM

This example will produce no code if no parameter is given, else it will add the parameter to A. See
the example macros chapter for more useful examples.


---

<!-- Source PDF page 33; extraction: ocr -->

30 : . ‘The PDS 280 Manual
ORG + Setup the current PC.

.ORG.

Syntax: ORG new PC [,true PC]

The ORG pseudo opcode defines a new assembly address, and updates the program counter
accordingly. You may have up to 100 orgs in your program. The new PC must not be a forward
reference, itshows where the code will be assembled to in memory. If you have a true PC parameter,
then all assembled code would use this value of the PC when the code references the PC, but will
actually insert the code at the memory pointed to by the new PC, When downloading the code to
the target computer, PDS will download the code in blocks, from the start of an org, to the end of a
block of code, then from the next org, and so on. If the program comprises two small sections of
code, one in low memory, the other in high memory, then PDS’s download software would only
download the two sections of code, not all the memory in between.

For example:
ORG 8000h,100h

Would place the code in memory at address 8000h, but the code would only run properly when moved
toaddress 100h. This is useful for producing disk overlays, or routine modules that move in memory.
To remove the ’PC offset” justuse-anotherorg; without atrvepc: parameter. If you.wanted:the code.
to continue after the relocatable routine at 8000h you would have to use something like:

ORG $-100h +8000h
Now the rest of the code would follow on in memory, and could be run where it was.

Ifemploying a number of ORGs in programs, there is always the risk that at some point you will have
code that overlaps other pieces of code already written. PDS will not trap this as some people need
to use memory dynamically. The only way you can tell if you have overlapping code is when you
have skip on. Instead of giving you a skip value, the display will read 'no skip’. If this ever happens,
then go through all the ORGs in the code and find the one that overlaps other code.

You may ORG anywhere in memory, from 0 to OFFFFh. ORGs do not have to be sequential, they
can be above or below one another.


---

<!-- Source PDF page 34; extraction: ocr -->

‘The PDS 280 Manual aL

QUERY - Will get an expression from the user

QUERY must be used on a line with a label. It will temporarily stop assembly on pass 1, display
any message after the QUERY pseudo opcode, followed by a flashing cursor. ‘The user may then
enter an expression or number, press enter and assembly will continue. The label on the QUERY
line will then be assigned the value of the expression. Note that due to the way the assembler works
any text following the command will be converted into upper case. To use lower case, put a single
quote at the start of your message, for example:

LIVES QUERY "How many lives do you want :

Labels may be entered as part of the expression, so you can enter string responses to your questions
by defining a few equates as below:

AMSTRAD EQU1
SPECTRUM EQUO
FRED QUERY “Which machine is it for :

If the user enters AMSTRAD, FRED will equal 1, or SPECTRUM and FRED will equal 0.

A similar command is ASK.


---

<!-- Source PDF page 35; extraction: ocr -->

32 . The PDS Z80 Manual

RADIX - Setup the default radix for the expression evaluator.
-RADIX
Syntax: RADIX expression

The radix pseudo opcode defines the default base for the expression evaluator. Any value, from 2
to 16, can be used with the RADIX statement. The default base is 10. If using a large amount of

binary data, rather than putting B after all the data, you could insert a RADIX 2 command before
the data, and a RADIX 10 command after it.

For example:
RADIX 2
DB 10101101,10101010

DB 00101010,10101010
RADIX 10

Note: The expression following the RADIX pseudo op is ALWAYS in base 10 (the default).


---

<!-- Source PDF page 36; extraction: ocr -->

* The PDS Z80 Manual B
REPEAT + Repeats the following line a number of times.
Syntax: REPEAT expression

Repeat is used for repeating one instruction or any line a number of times. For example:

REPEAT 4
RRCA

This is equivalent of inserting the following in your code:

RRCA
RRCA
RRCA
RRCA


---

<!-- Source PDF page 37; extraction: ocr -->

4 ‘The PDS Z80 Manual

SEND + Tells PDS where to send the program once assembled.
DLOAD .

DOWNLOAD °

Syntax: SEND destination

The SEND pseudo opcode is used to determine the destination of the object code, once a program
has been assembled. The destination can be one of the following:

SERIAL - Via the serial port at 9600 baud
SERIAL1 ~ Serial, 19200 Baud

- SERIAL2 + Serial, 1200 Baud
SERIAL3 - Serial, 300 Baud
COMPUTERO + Computer 1 port, ‘nibble’ protocol
COMPUTER1 - Computer 1 port
COMPUTER2 - Computer 2 port

If employing this command in your program, when assembly is completed you will be prompted
"Download (Y/N)?". If you hit any key other than {N] then your code will be downloaded to the
specified destination. Once the code has been downloaded, the prompt remains.onthe screen: You
may resume'editing by-hitting any key other than [YJ. Pressing [Y] will download your code once
again. While code is downloading the cursor will flash. If it seems to be taking too long, then there
is probably a fault in either the download software on the target or the interface connections. You
may press (FINISH) at any time, to break out of downloading. In all other areas of PDS there is an
automatic time-out while downloading, but the assembler does not do this to allow you to get the
target computer ready to receive the code.

‘The interface card inside your machine has two Ports onit. You can download to different computers
attached to these by specifying COMPUTERI or COMPUTER?. Some computers such as the BBC
Micro need a special form of download software, which sends and receives 4 bits at a time rather
than whole bytes. To send in this format, use "SEND COMPUTERDO’, with the target computer
plugged into port 1. The send using the serial ports only needs to be used with computers that do
not have PDS interface available for them, but the protocols remain identical. The data is sent with
8 bits, 1 stop bit and no parity, You should go at the fastest reliable speed. Some machines are
capable of 9600 baud, most are better at 1200. Not many can keep up with 19,200 baud. If you
cannot get any results, even at 300 baud, then you must either have a faulty RS232 cable, or you have
not setup the target computer properly.


---

<!-- Source PDF page 38; extraction: ocr -->

‘The PDS Z80 Manual 35
SKIP. - Used to speed up assembly time
Syntax : SKIP expression

This command is specific to PDS, and enables your programs to assemble at nearly twice the speed
with no drawbacks. The command makes a note on pass one, of any large sections of program that
doesn't need to be reassembled again on pass 2, these are then SKIPped over on pass 2. As alarge
amount of information has to be stored for every skip, there is a limit to how many ‘skipping’ points
PDS canremember. Therefore, after assembly, the percentage of skip table used is displayed in the
command line window. If the skip percentage returned is 100%, then the skip table has been filled
up early on in the program and has probably missed some blocks towards the end of the program.
The best skip table usage is about 80% to 95%. There is an expression after the skip command, for
average length programs this will range from about 15 to 30. ‘This expression tells the assembler the
minimum size of a block which contains no forward references that can inserted into the skip table.
So the lower the number, the larger the number of blocks that are added to table. If the number is
too high, very few or maybe no blocks will be found. If you have to use include files, try to have just
data in them (no forward references), that way they will only be read in once on pass 1, on pass 2
they will be skipped. If PDS ever displays 'no skip’ after assembly, then there is an ORG overlapping
with a block of code previously coded, or you are using the BANK command which disables skip.
Skip must be placed at the start of programs, before any ORGs.


---

<!-- Source PDF page 39; extraction: ocr -->

36 ‘The PDS 280 Manual

STRING - For defining strings ending in zero.

This has the same syntax as DB, but any text strings will have azero byte added after the last character.
This is similar to the DC pseudo op. Many programmers use a zero to define the end of a message
stored in memory.

Examples:
STRING 13,"Cat","dog*

produces :

13,43h,61h,74h,0,64h,6Fh,67h,0


---

<!-- Source PDF page 40; extraction: ocr -->

The PDS Z80 Manual 3

3.2___ Assembly listing related pseudo opcodes

There are a number of pseudo opcodes specifically designed for listing assembled text. These have
been separated from the main pseudo opcode list, as we felt they needed to be explained together.

LIST
«LIST
LST

All the above commands have one of three parameters, ON, OFF or MACRO. LIST ON and LIST
OFF control the listing output to the screen. When 'LIST ON’ is selected, you will see the source
code displayed in the current window, while it is assembled on the second pass. ‘The listing produced
is similar to the sample listing below:

ORG 10
NOP
NOP
END

‘The first HEX number at the start of each line shows the current address of the program counter,
and any code on that line will be assembled to this memory address. The character directly following

“the HEX number shows the action taken*by-the assembler for that‘particular:line. A-colon (:)
signifies that the line has been assembled, A’+’ means that the line has been ignored, this would
occur if an ’IF” structure had failed at that point. The only other alternative is a” character, this

* means that a macro definition was decoded at that particular line. The next list of HEX bytes
represent the value of the bytes that were assembled for that line, a maximum of 5 bytes can be
displayed at that position. If an IF’ or EQU’ statement was assembled on the line, then the result
of expression is displayed instead, this allows you to see what the expression was evaluated to in the
listing. An example of this is shown below :

QO0Eh: 0017= FRED EQU 23
In this case fred was assigned the value 23, so at the start of the line 0017 = was printed,
When listing to the screen any character going off the edge of the screen will be lost.

Normally when you list a macro call, the assembler will print something like this:

Q00Fh> 00 CAT

This is a macro called cat, which produces a single zero byte. If you wanted to see exactly what the
assembler was assembling in the macro, you could turn LIST MACRO on. The default is off, by
using the instruction LIST MACRO, you toggle the option on and off. With LIST MACRO on, the
above example could look like this:


---

<!-- Source PDF page 41; extraction: ocr -->

38 The PDS Z80 Manual

O00Fh > CAT
O00Fh> 00 NOP
o010h> ENDM . :

This macro is very simple, in fact all it does is insert a NOP, but you can now see the assembler’s
action.

Listings to the screen do not use most of the list options (see LSTOPT), but are paged, so that once
@ page is printed, a key has to be depressed before the next page is displayed.. For a very fast
continuous listing, just hold down a key.

LLIST
LLST

Are the same as LIST, except they output the listing to the printer, You may print to either screen
or printer, or both if you wish, Note that LIST MACRO applies to both printer and screen, for
example, LLIST MACRO will not be accepted. There are many commands for configuring the
printer, while printing listings. These are:

PRINTER

This works in the same way as define byte (DB ), but all the parameters are sent to the printer, This
allows you to setup the printer with specialized control sequences, for example:

PRINTER 27,"@",12

Would initialize and do a form feed on Epson compatible printers.

SKP

This pseudo opcode needs just one parameter, and sends the specified number of line feeds to the
printer, ie:

SKP 5

This would send five line feeds to the printer, and would leave five blank lines in your listing.

PAGE


---

<!-- Source PDF page 42; extraction: ocr -->

‘The PDS 280 Manual . 39

This command has a number of different syntaxes, these are:

PAGE (no parameters)

Will issue a form feed to the printer, moving the paper to the next start of form.

PAGE expression (parameter 15 to 255)

Will define form length for the printer, ie the number of lines per page.

PAGE expression , expression

‘The first expression defines the maximum line width, and the second expression defines the form
length,

PAGE “nnnnn

‘This will issue a form feed to the printer, then define the current title for the code listing, This is
equivalent to an EJECT and TITLE used together. Note that you need an initial quote in front of
the text expression, otherwise the rest of the text will be converted into upper case.

EJECT

Will issue a form feed to the printer, ie move the Paper to the top of form. This performs exactly
the same task as a PAGE instruction by itself.

TITLE "nnnn
TTL

This defines the current title, which will be printed at the top of each page (centered) from this point
on. This can also be achieved by using a PAGE "nnnn instruction. Note that the title will be
converted into upper case unless a single leading quote is included in the string expression,

SUBTITLE "nnnn
STITLE
SUBTTL


---

<!-- Source PDF page 43; extraction: ocr -->

“0 : ‘The PDS Z80 Manual

This will define the current sub-title that will be printed at the top left of each page. Note that the

title will be converted into upper case unless a single leading quote is included in the string
expression.

WIDTH expression

This will define the maximum line length. Any line longer than this value will either be split or
truncated, depending on the current list options (see LISTOPT).


---

<!-- Source PDF page 44; extraction: ocr -->

‘The PDS Z80 Manual 4a

LISTOPT
LSTOPT

Syntax: LISTOPT expression

This will set and reset the list option flags. ‘The specified expression will be XORed with the current
option flags. So LSTOPT'S followed by LSTOPT 1 is exactly the same as using LSTOPT 4. There
are 16 different list options, each bit ina 16 bit number performs a single task. “Therefore, most
people define list options in the following way:

LSTOPT 1024+5124+4+2+4

This is easier to understand, and use, than working out the exact 16 bit number manually, as each
used can be easily distinguished. The full range of list options follow:

Br EUNCTION

1 Line numbers printed at the start of the line

2 Add time and date to the top of pages

4 Add version number to top of pages

8 Add a page number in the top right

16 Add a page number in the bottom left

32 Print file headers from the RAM source

64 When include files are started print a small header
128 Print printer pseudo ops (eg: PAGE, TITLE...)
256 Print symbol table in PC order (else alphabetically)
512 Remove h from the end of the PC value

1024 Don’t do pages, just continuous listing

2048 Truncate text at the end of line

4096 Same as LIST MACRO when enabled

8192 Add a file number in the top right corner

16384 ‘When text wraps, print 3 tabs, (else just a ;)

32768 Global ignore all list pseudo ops

When a particular bit is set, then that function is selected. LISTOPT defaults to a value of 0.

Most functions are quite obvious and change the format of the pages being printed, ‘The following
require a little explanation:

Option 1 ‘These are line numbers that can be referenced using editor functions, This also
means that line numbers re-start from 1, at the beginning of any file, either a
memory file or a disk include file.

Option 32 Will issue a form feed then print the PDS start of file header when the start of a
file is printed. Otherwise there will be no break in the source code as the
assembler moves from file to file. .

Option 64 Allows you to see which file is being included.

Option 128 Will make PDS print all the printer pseudo ops to the printer - these are normally
Not sent to the printer, as list pseudo ops only change printer formats and do not
generate any code.

Option 32768 When bit 15, or 32768 is set, all following printer commands (including LSTOPTs)
will be ignored, until another LSTOPT is executed that flips bit 15 (32768). So
if you globally wanted to ignore all printer commands you could do:


---

<!-- Source PDF page 45; extraction: ocr -->

42 : ‘The PDS Z80 Manual

UST OFF
LSTOPT 32768

Now, whatever you try, even LIST ON, will be ignored, When requiring to ignore all the printer
commands and just get a listing use:

LIST ON
LSTOPT 32768


---

<!-- Source PDF page 46; extraction: ocr -->

The PDS Z80 Manual 8

41 Example programs

PDS is very flexible in allowing many different syntaxes for most pseudo opcodes. Although there
are one or two commands that you will find in every program, below is an example ‘shell’ of a PDS
program :

SKIP 20 ;Turn skip on for speed
ORG 8000H iMust be after skip

** program source code **

SEND COMPUTER1 Download after assembly
END start ;End source and give program execution address

‘The minimum source you need in a your source code is an ORG, otherwise PDS will not know where
to assemble the source code. Without the SKIP function, assembly time will increase, without the
SEND pseudo opcode no download prompt will be given after assembly, without the END pseudo
opcode, assembly will only terminate at the end of file 7.

Below is an example program for flashing the screen on the Amstrad or Spectrum.

‘ ORG'‘8000H
SEND COMPUTER1

AMSTRAD EQU1
SPECTRUM QUO

COMPUTER QUERY ‘Enter computer for (SPECTRUM,AMSTRAD) :

START IF COMPUTER
LO HL,OCOOOH
LD BC, 16384

ELSE :Work out screen
yaddress and size

LD HL,4000H

LD BC,6144

ENDIF


---

<!-- Source PDF page 47; extraction: ocr -->

“ The PSD Z80 manual

LD D,H

LOE

INC (HL) > :Keep flashing 256 times

RET Z ;Return to downloader

LOIR Fill screen

JP START

END START iJump to START after downloading

When assembling this program, you are prompted to enter either SPECTRUM or AMSTRAD. You
will then, almost instantly, be asked if you wish to download, if you press any key other than ’N’ then
it will be downloaded and run the program on the target computer. The screen should flash for a
few seconds, then return to the download software with the screen totally filled.


---

<!-- Source PDF page 48; extraction: ocr -->

‘The PDS Z80 Manual 45

4.2 Errors during assembly +

Ifyou get an error during assembly, PDS will stop assembling and display the error message in the
commandline window, Once a key is depressed the cursor will move to the line containing the error,
and the error is then cleared. PDS will only report one error at a time, making error corrections
much simpler, and a single error will normally cause a number of other errors. You will also find
that PDS error messages are a lot more descriptive than other assembler error messages. For
example, if a relative jump was out of range, the error message produced will read like this:

Relative destination too far behind, remove 23 (16h) bytes.

This is much more useful, than the normal ‘out of range’ error message. Nearly all PDS error
messages (there are over 100) are very straight forward, You will probably find most errors are just
typing mistakes, these will often return an ’Extra characters on line’ error. This generally happens
when a character PDS is not expecting is found on a line, ie a comment that is not preceded by a semi
colon will generate this error.

Ifyou get an error while executing a macro, the cursor is not moved to the corresponding line in the
macro, but is moved to the macro call. The error message will be preceded by ’M:’, to signify it is a
macro error, Press a key, and PDS will then print the macro line that caused the error. PDS will
replace any TABs in the line, with spaces, so that you can see a greater portion of the line, When
you press another key, PDS will move your cursor to the start of the line where the macro call was
made. Normally errors are caused by parameters being incorrectly passed.

Ifyou get an error while in an include file, PDS will use the same process to show the error as that
used when macro errors are displayed, but will display 'I:’ in front of the error, instead of 'M:’.


---

<!-- Source PDF page 49; extraction: ocr -->

6 . ‘The PDS 280 Manual

43 Example macros in the PDS Z80 assembler

Macros are very useful, they can save typing, memory, and improve source code readability. Here
are a few sample macros that you can try to understand, or even use.

JS MACRO
IF (@2-$ < 128) | ($-@2< 128)
IFF @2
ELSE
JR @1,@2
EXITM
ENDIF
JP @1,@2
ENDIF
ENDM

This macro expands the Z80 instruction set. Instead of entering "JR condition.address’ or ‘JP
cond,addr’, it allows you to enter "JS condaddr’. If the address can be reached with a relative
instruction it will use JR’, else it will use a normal jump, ‘JP’. Note that this will always use a jump
if you have.a forward reference.to-a-label, simply. because:it cannot know how. far-away. the:label:
might be. For example:

FRED NOP
JS NC,FRED

Will generate aJR NC,FRED, and

FRED DS 300
JS NZ,FRED

Will generate a JP NZ,FRED.

IX MACRO

P@1 EQU PIX

@1 EQU @2-OPIX

PIX = PIX+@2
ENDM

‘This macro defines two variables, the first allows you to reference the specified variable directly to
memory, while the other references the memory address as the offset to the IX register. Many 280
Programmers point to the main data area with 1X, and use relative references to access the data, ie:


---

<!-- Source PDF page 50; extraction: ocr -->

‘The PDS 280 Manual a
OPIX EQU OFFOOH ‘Setup two variables pointing at
PIX = OPIX . ithe start of the IX data area

LD IX,OPIX iSetup the IX register

IX FRED,2 iDefine a two by variable FRED

IX BILL,1 31 byte variable, BILL

LD A,(PBILL) jLoads A with the byte at BILL

ADD (IX+FRED) jadds it to the variable at FRED

These types of macros are useful, because you never need to allocate memory addresses yourself,
which means they can change automatically. This also prevents you from having overlapping
variables, which is a common programming error.

- Ifusing many ORGs in programs, you find that they often overlap, ie ’no skip’ is displayed at the end
of assembly. You can use a macro to perform all the program ORG’s, and trap any overlapping, ie:

CORG MACRO
IF $@1
ERROR "Overlapping code at address @1
ENDIF
ORG @1
ENDM

Now instead of ORG, use CORG address and your code will be checked for overlapping sections
automatically, This macro is also useful when using banked RAM, as SKIP is then disabled and will
not indicate overlapping code, :


---

<!-- Source PDF page 51; extraction: ocr -->

a ‘The PDS Z80 Manual

44 Different syntaxes allowed in Z80

All the standard Z80 instructions are allowed. The ‘extra’ Z80 instructions that access the high and
tow bytes of IX and TY, or the extra shift instructions are not supported by the assembler, because
older Z80's may not always accommodate them, and syntaxes vary greatly. If you do want to use
them, then simply define your own macros, using whichever syntax you are accuvoned va

PDS has a number of ’shorthand’ versions of popular Z80 instructions. These have been included
to aid development, and are really only logical changes, and do not stop you using conventional
syntaxes. The added syntaxes, with their original counter parts are shown below:

EX AF,AF’ may be coded as EXAF (like 8080)

EX HLDE may be coded EX DE,HL

JRNZ,nonn may be coded JNZ nnnn (like 8088)

JR Z,nnnn may be coded JZ nnnn

JR Canna may be coded JC nnan

JRNGanan may be coded NC nana

RST may have an expression following RST

IX+ and IY + may also be coded as IX-nn or IY-nn

PUSH and POP may have a list of registers, separated by commas

All'accumulator Telared'instructions'may havethe’A” omitted! eg: ADC'A‘S or ADC: ‘5, SUBA,S or
SUBS.

Remember that all the normal syntaxes are Supported, but we feel these changes make programming
less tedious, and make the code more readable. For example, PUSH HL,DE,BC,AF is very
compact, and generally more logical. Note that the opposite to this is POP AF,BC,DE,HL.


---

<!-- Source PDF page 52; extraction: ocr -->

‘The PDS Z80 Manual ”

5.1 __ The PDS Download Software

‘The download software has been written over a period of time, and has been heavily optimised for
speed and size. All the different types of download software are supplied on the master disk, with
all the PDS software. There are three main types of download software:

Short ’dumb’ download software (*.DL0)

This is the shortest possible software that allows you to download and execute code. This should be
used when free memory on the target machine is restricted. It will not operate correctly with most

* monitor commands, such as modify, although commands such as fill, that only download data, will
still operate, This version is also useful when writing new download software, or the software has
to be typed, in an emergency.

Long ’clever’ download software (*.DL1)

When you purchase a target computer interface, this version of software is supplied on tape or disk.
It will allow you to use all the monitor's features (except analyze which requires the DL2 version
download software), while still allowing you download and execute a program from the assembler.

Interrupt driven software (*.DL2)

This is the download software that runs under the interrupts and allows you to use most monitor
commands while your program is running on the target computer. This allows you to watch areas
of memory change, stacks building down, or modify variables while a program is running. You may
not alter registers or trace from the monitor, as this would cause data areas to clash and not be of
much benefit. It is useful to insert the source code of the downloader within your own program
while it is being developed - this make debugging faster and easier.

All the download software can be positioned anywhere in memory, and run completely
independently, with all data areas self contained. You are free to rewrite them if you wish, and
mould them to suit your own requirements. They can be made substantially faster by removing the
CALLS to the GETBYTE and SENDBYTE routines in the upload and download loops, and
replacing them with an exact copy of the actual routines.

DLOand DL1 both have the interrupts disabled, this allows you to download programs over operating
system workspace, or over interrupt vectors, without crashing the target machine.

Make sure you keep track of the stack’s position in memory, the DLO and DLI software will both
use two bytes of stack space. Situations have occurred where a user downloaded a program over
the stack, thus corrupting the program as it was being downloaded. This caused great confusion,
and was simply remedied by moving the stack to the top of memory. To alter the stack starts position
on a Spectrum, enter:

ee


---

<!-- Source PDF page 53; extraction: ocr -->

50 ‘The PDS Z80 Manual
CLEAR.nnnn

on the Amstrad,

MEMORY nan

Where nnan is an address that is slightly above the required stack address allow at least 64 bytes for
the system stack.

If you don’t want the downloader to use any stack Space you could change the download software
‘jump to program’ routine, at the moment this does a call, which is where the two bytes of stack space
get used. If you replaced this with a jump then it would not affect anything, although you could not
return to the download software by doing a ‘return’,

When downloading programs, ensure that you do not download over the downloader itself. This
applies even when you are downloading the download software itself, as self modifying code is used
in all versions of the software. Although this sounds obvious, you will be surprised the number of
times this will happen to you, and could leave you with mystifying crashes.

Most users load their download software of tape or disk, into a completely free area of memory.
This will then allow them to return to the downloader at uny point, to download new code, so. speeding
up development greatly, and saves having to continually reload the download software. On the
Spectrum, SB00h is normally a good location for the download software, while 100h can be used on
the Amstrad.

‘When you first setup the PDS, it is normally best to make up your own version of thé download
software, and save it to tape or disk. To do this load the correct download software into PDS (either
SPECTRUM or AMSTRAD .DLOor DL1), change the ORG at the top of the source, to the required
address (remember, avoid overwriting the present download software, or the stack). Load the
supplied download software into the target computer and assemble and download the new download
software. You should now save it to disk or tape,


---

<!-- Source PDF page 54; extraction: ocr -->

‘The PDS Z80 Manual a

5.2 The PDS download software protocols.

‘There now follows a complete description of the Z80 communication protocols used by PDS
software. The software is designed to be machine independent, so the same protocols can be used,
regardless of the target machines processor or make. All the communication is basically the same,
there are four major routines, SEND BYTE, GET BYTE and two direction swapping routines.
These have been optimised as much as possible and all the data formats are as compact as possible.
For example, ifyou had a small piece of code in low memory and a small piece of code in high memory,
then PDS would automatically download two small blocks, instead of downloading the memory in
between as well. There now follows a description of the main parts of the downloading system on
the target computers.

The interface hardware

‘The target machine interfaces are quite straight-forward. They have eight bi-directional data lines,
which are buffered, one input flag and one output flag, which are also buffered.

Initialization of the download software

‘The first thing the software must do is to setup the direction of the eight data lines, these should start
inputting from the main computer. The output flag line must be set to 1, when the machine is first
turned on, this line should not be toggled on initialization.

The main loop of the download software

Atthe start of the main loop, you must continually read in bytes from the interface, until a command
byte is received (from 180 to 187). The correct routine must then be entered, to perform the
required function. PDS may sometimes send a 179 padding byte, this should be ignored by the
downloader, and is only used to make sure that all blocks of data are an even number of bytes long.
‘This ensures that the handshaking lines are always in the same state at the start of each function.
Each command byte is now explained:


---

<!-- Source PDF page 55; extraction: ocr -->

52 ‘The PDS Z80 Manual

Command 180 - Download code

‘This will download an area of memory from the main computer into the target computer. This
command is present in all download software and is used by the assembler for downloading programs,
Note that programs will be downloaded in blocks, from the start of one ORG, to the beginning of
the next or the end of the program. Monitor commands such as fill, use this command, After the
180 command byte, the start and length addresses of the code are downloaded, in that order. All
addresses are downloaded high byte first, followed by the low byte. A length of zero, is actually a
length of 65536, Once the length is sent, the block itself is then downloaded into the specified
memory addresses. The downloader now re-enters the main loop. For example, to download four

bytes (255,65,23,45) into address 8000h, the following command block would be sent to the target
computer:

179 - Padding byte

180 - Command, download
80h ~ Start address, high

0 - Start address, low

0 - Length, high

4 + Length, low

255 + Ist data byte

65 - 2nd data byte

23 - 3rd data byte

45 ~ 4th data byte


---

<!-- Source PDF page 56; extraction: ocr -->

The PDS Z80 Manual 53

Command 181 - Jump to an address

This command will download an address from the main computer and CALL’ it. Ifa RETurn is
executed, then control will return to the main loop. This command is also found in all versions of
download software and is used by the assembler if you specify a start or exec address for the program.
The main computer will always send a padding 179.byte, as there are only three bytes in the main
command. For example, to execute a routine at address 1234h the following list of bytes would be
sent:

179 - Padding byte
181 - Command, Jump
12h + Start address, high

34h - Start address, low


---

<!-- Source PDF page 57; extraction: ocr -->

a ‘The PDS 280 Manual

Command 182 - Upload memory

The DLO software does not support this command, It is similar to the download (180) command in
format, except that after the length is sent, the ports are reversed and the requested block is sent up
to the main computer. Once the data block has been sent, the ports are once more reversed, and
the main loop is entered. For example, to upload three bytes from the target computer, starting at
address 1234h, the following would occur:

179 - Padding byte
182 - Command, upload
12h = Start address, high
34h - Start address, low
0 ~ Length, high

3 - Length, low

Reverse ports (flags act as if half a byte has been sent)

2 - Ist upload byte
= 2nd upload byte
- 3rd Upload byte

Reverse ports (Like half a byte again)

Note that the two reverses of ports act as if one byte has been sent, hence the need for the padding
byte.


---

<!-- Source PDF page 58; extraction: ocr -->

‘The PDS Z80 Manual cy

Command 183 + Select bank

All version of the download software have this command. The assembler uses this feature in the
BANK command, the monitor uses it in the Z command. The main computer just sends the byte
givenin the command, unaltered and expects the target computer to act onit accordingly, in whatever
way you wish the command to be used. You will have to write the code to support this command if
you have a special use for it. This is a simple two byte command, 183 followed by the bank number.

183 - Command, select bank
292 + Bank number


---

<!-- Source PDF page 59; extraction: ocr -->

56 The PDS 280 Manual

Command 184 - Send all registers to the main computer

This is only in the DLI version of the software. It isused in the tracing and register related functions
of the monitor. A block of 26 bytes are sent to the main computer. This block contains all the Z80
registers, and is uploaded using the Upload command (182). The registers are setup for 26 bytes
and the start of address of the upload is setup by the downloader itself. Bytes are sent as follows:

184 - Send registers command
Reverse ports (same as sending half a byte)

26 data bytes are sent

Reverse ports back (same as sending half a byte)

There is no padding byte, because the length will always be an even length. ‘The register block is
stored in the following order:

DE
BC

HL

DE’

BC’

Ix

ly

AF

IR - and R registers

AP

HL

PC -The'address on the stack
SP - - The Z80 stack pointer

The register block is updated when the download software is first entered, when you jump out of the
download software. All the registers are loaded with values from this table.


---

<!-- Source PDF page 60; extraction: ocr -->

—_——_

‘The PDS 280 Manual 7

Command 185 - Get registers from the main computer

This command downloads a 26 byte register block from the main computer. The registers of the
target computer will be loaded with these values when the download software is jumped out of. The
register block is in the same format as above. A padding 179 is always sent first, as there are an odd
number of bytes in the command, (a 185 command byte and 26 data bytes). This command is only
found in DL1.


---

<!-- Source PDF page 61; extraction: ocr -->

58 ‘The PDS Z80 Manual

Command 186 - Trace code buffer

This is the main command used by the tracer, and is only found in DLI, Four bytes are downloaded
after the command and are stored ina buffer, The registers are loaded from the register block, and
the four byte buffer is executed. The registers are then saved back into the register block and the
main loopentered. Note that the code executed in the buffer has to be carefully chosen - if you were
to execute jumps then the download software would lose control, and function incorrectly. If the
instruction you wish to execute is shorter than four bytes then the rest of the buffer must be padded.
with NOPS. The tracer handles this all automatically, so you need not worry, but it is important that
you are aware how the system works. The tracer will emulate some instructions itself, such as jumps
or load register from register instructions and just move pointers. When the tracer comes actoss an
instruction such as ‘ADD 23’, then it will download ADD 23’, NOP’, "NOP" into the instruction
buffer. The buffer is then executed and the register block is uploaded, to see what was altered,
Most instructions are executed in the instruction buffer, because in Z80 some of the flags in the flag
register cannot be simulated.


---

<!-- Source PDF page 62; extraction: ocr -->

‘The PDS Z80 Manual 9

Command 187 - Return Analyze address

This command is only used in DL2 software. It will send two bytes up to the main computer,
containing the address of the PC, when the interrupt occurred. ‘The analyze commandin the monitor
ses this command, to work out where the program is spending most of its time.


---

<!-- Source PDF page 63; extraction: ocr -->

0 The PDS Z80 Manual

53 The control lines during PDS communication

‘There now follows a description of the four low level routines in PDS’s communication software.
Note that the protocol does not set the control lines directly, but toggles the lines to communicate.
‘All the protocols are designed so one computer can never get ahead of the other, even if there is a.
big speed difference. There are no error checking protocols, as the interfaces are very reliable, and
error checking will slow down processes, and no real action can be taken, even if an error was
detecte

SENDING A BYTE TO THE TARGET COMPUTER

i) The main computer puts the byte on the data lines, then flips its output line. The
. main computer now waits for the input line to change state.
ii) The target computer waits for the control input to flip, the byte on the data lines
is then read in and its output control line is toggled.
iii) The main computer initiates this process first, and the target computer should

finish the process first.

GETTING A BYTE FROM THE TARGET COMPUTER

i) Tlie main computer waits for its control input to flip, then reads the byte from the
data bus, and flips its control output.

ii) The target computer puts the byte on the data lines, then flips its output line. It
then waits for it’s input control line to flip.

iii) The target computer starts this process first, the main computer finishes first.

SWAPPING PORTS, FROM Main--> Target TO Target --> Main

i) ‘The main computer flips its data lines direction and then its control line.

ii) ‘The target computer waits until the control input flips and then reverses the
direction of its data lines.

iii) The main computer starts this process first, and is finished first.

SWAPPING PORTS, FROM Target--> Main TO Main--> Target

i) The main computer waits for its control input to flip, then changes the direction
of its data lines.
ii) The target computer changes the direction of its data lines, then flips its control
: output. ,

iii) ‘The target computer starts this process first, and is finished first.


---

<!-- Source PDF page 64; extraction: ocr -->

‘The PDS Z80 Manual 61

6.1 The PDS Z80 Monitor system

You many enter the monitor at any time from the main PDS editor by pressing the [MONITOR]
function key. In the monitor the screen is divided into two areas, The top two lines of the screen show
the Z80 registers and their values. The main area on the screen is the command area.

‘You may use the cursor keys to move around the command area, [HOME] will move you to the top
left of the screen

(HOME) will clear the screen and move you to the top left oo.
Ifyou press cursor left at the beginning of a line, the cursor will move to the end of the previous line.
Commands may be entered in upper or lower case and must start in the left hand column of the
screen.

‘You may return to the editor from the monitor by pressing the (FINISH] function key. The monitor
screen will be saved, this allows you to flip between the monitor and editor without loosing any work.

To execute a command, place the cursor anywhere on the line with the command and press [return].
PDS will then execute the command, ignoring any extra characters after the command.

You do not need a target computer attached to your system to enter the monitor. If you are using
the 'Clever’ PDS software then all the monitor commands will function as normal. If you are using
the Dumb’ download software then only a few monitor commands will work. The others may give
unusual responses or error Messages,

When a.monitor command fails or contains an error, PDS will put a question mark at the end of the
‘line and beep. You may then correct the error and press enter on the line to execute it again. If there
is something wrong with either the download software or the link between the computers you will
get an error message such as :

Error, other computer not receiving

When you get an error like this first make sure that the target computer is running the download
software. Then check the connection between the main computer and target is secure. If the error
persists then you must assume that there is something wrong with the download software, or it has
been overwritten,


---

<!-- Source PDF page 65; extraction: ocr -->

2 ‘The PDS 280 Manual

6.2___The PDS monitor commands.

On the following pages the PDS monitor commands are listed, their syntax explained, why they may
not work and examples on their use.

In all commands the expressions that you use are evaluated using the assemblers expression
evaluator. This means that if you have just assembled a piece of code then you may use the labels in
your expressions, for example, DSTART would disassemble from the label START. The evaluator
has been expanded to allow you to access memory locations, you do this by putting curly brackets
around the expression. The value within the brackets will be evaluated and used as an address. The
byte at this memory location in the target computer will be returned. For example, B
FRED,{FRED} + 1, Would increment the byte at location FRED. You may also return a word ata
memory address by using square brackets, for example, M[FRED] would modify memory pointed
to by the word at location FRED. Quite complex expressions may be built up using these sets of
brackets. In both cases there is no limit on the number of times the brackets may be nested.

Some monitor commands don’t require any target computer attached, they are : L,O,P,Q,V,X.

Most commands need some sort of target computer attached and running the appropriate download
software. There are three types of download software we supply :

DLO - This is the shortest and can only download and run programs. [tis meant to be
used with the assembler whensspace onthe target computer is at a premium, Some
monitor commands will operate with this download software. They are : B (modify
only), E, F, G (although it will perform a Jump), W (modify only), Z.

DLI ~ This is the longest download software, about 400 bytes. It will work with all the
commands, except Analyze, which requires the download software under the
interrupts. This should be used if possible, else DLO.

DL2 + This is designed to be called from your interrupt routine, it will work will all the
commands except R,T, as it cannot trace or alter registers. Its main use is to
examine your variable area during the running of your programs, or to analyze the
Programs execution, or to modify data while the program is still running.

Ifyou have the incorrect download software in the target computer, then you may get unpredictable
errors, of commands may not work at all.


---

<!-- Source PDF page 66; extraction: ocr -->

—_——$i WM quem. ._____....

‘The PDS Z80 Manual 63

A - Analyze a programs execution

‘This can be used in three different ways:

Y A

This will repeat the last Analyze command, or A0,65535,1 if not used before.
2) Astart address , end address

This will analyze between the two adresses, the whole of memory is 0,65535.
3} Astart address , end address , count value

This is the same as 2] , but sets up the count value as well. The count value remains set until it is
changed again. It starts being set to one.

‘This will give an error if:
‘There is a fault in the link to the target computer
The DL2 type of software is not running under the interrupts

Analyze is designed to allow you to see where your program is spending most of its time. Install DL2

download software in the target computer, running under the interrupts of your program, When your

program is running type A0,65535,1 - This will display a bar graph, each bar covering about 4K of
“memory.’PDS will print one star on a row when an interrupt occurs in that address range:'To'make 3

it more accurate you may set the count value higher, this tells PDS how many times an address must

occur before astar is printed. Once a bar reaches the other side of the display, that shows where your

Program is spending most of its time, now narrow the address Tange eg:

A 1000,2000

Keep doing this until you have an address range of about 100 bytes, this will be the most used routine
in your program, optimise this one section of code and you will see significant improvements in the
speed of your code. The minimum address range-is 15 bytes. It will take slightly longer to produce a
bar graph as you narrow the address range because it will not interrupt as often in that area of
memory. The analyze command will not work properly if your program contains VSYNCS, or
HALTS, as interrupts will then ALWAYS occur in the same place in you code. Most programs in
Z80 generally only have one HALT or VSYNC somewhere in the main loop if at all, Remove this
and the command will be invaluable.


---

<!-- Source PDF page 67; extraction: ocr -->

——————LL LEE

Lad The PDS 280 Manual

B + Change or display a byte at a memory location

There are two ways to use this command:

1 Baddress
Tals wil display the byte at the address given, The value will be displayed in hex, decimal, binary and
ascii,

2 Baddress , byte value

This will move the byte value into the address given,

address
This is the address of the byte to be changed

byte value
This is a byte value, from -128 to +255

This will give an error if:
The byte value is novinthe Tange'-128 to +255"
‘There is a fault in the link to the other computer

1] Needs the clever PDS download software
2] Only needs the dumb download software

NOTES:

The W command has the same function, but works on words instead of bytes.

‘This command is mainly used for altering values in your program, to quickly see the effect of small
changes,

EXAMPLES:

B4000h,23
‘This will load the location 4000h with the value 23

B FRED, {FRED}*2
This will double the byte value at location FRED


---

<!-- Source PDF page 68; extraction: ocr -->

——

‘The PDS Z80 Manual 6s

Cc + Copy block of memory

Cstart address , end address , new start address

start address
This is the first address used by the block to be moved

end address
‘This is the address of the last byte in the block

new start address
‘This is the position that the new block will start from

‘This will give an error if:

‘The end address is lower than the start address.

‘The new block goes above OFFFFh or 65535.

‘The ‘clever’ PDS download software is not being used.
‘There is a fault in the link to the target computer.
NOTE:

. The new block can overwrite part or all of the old block. PDS uploads the whole block into the main
~ computer, then downloads it at the new location. This requires the download software that can send i
and receive blocks of memory. .

EXAMPLES

CO,3FFH,4000H

‘This will move the first 4K of memory to memory location 4000H
C VARS, VARE , NEWVARS

‘This will move the memory from VARS to VARE and place it at NEWVARS onwards.


---

<!-- Source PDF page 69; extraction: ocr -->

6 ‘The PDS Z80 Manual

D - Disassemble memory

This command can be used in three ways:
y D

‘This will disassemble a block of. memory starting from where the last disassembly finished,

qj D start address

This will disassemble a block of memory starting from start address

3) D start address , end address

This will disassemble a block of memory starting from start address and ending with end address

This will given an error if:
‘The target computeris nor running’clever’ download software
The end address is less than the start address

NOTE:

‘The disassembler uses standard Z80 Pesudo ops. When it comes across an instruction that it cannot
disassemble it will print DB followed by the bytes it did not understand. If it can guess at the
instruction it will do so after a; for example:

8000: FD AF DB OFDH,OAFH i XORA

If type 3] (D start address,end address) is used then PDS will disassemble very quickly, it will stop
when any key is pressed, and wait until any other key is pressed before continuing, pressing [FINISH]
or [ESC] will stop the disassembly. .


---

<!-- Source PDF page 70; extraction: ocr -->

‘The PDS Z80 Manual . 67

E - Enter a program

Esstart address
start address
Is the address of the first byte of the program

This will give and error if:

‘There is a fault in the link to the target computer.

Only the dumb download software is needed.

NOTE:

This command is used for entering programs when you are given the program in hex or decimal. As
you enter the program, PDS will disassemble it when you enter whole instructions. For example if
you had the program 23,21,00,05,C9 to go at 8000h then you would enter:

E8000h

Then type 23210005C9, while you are typing, PDS will print on the display:

8000: 23 INC HL
8001: 210005 LD HL,OSOOH:
8004: C9 RET

_ 8005: *
This is very useful as it allows you to check the program you are entering for mistakes.
To stop entering a program, press [FINISH]

Note that PDS only sends the bytes down to the target computer when a whole instruction has been
entered,

When you are entering hex, PDS will allow you to delete characters entered wrongly. If you press
delete when the cursor is next to the address then the address will be decremented by one.

When you enter programs in decimal, press enter or comma after each byte entered.

Hex or decimal program entry and the format of disassembly may be changed using the config system
or ’Q' options command,


---

<!-- Source PDF page 71; extraction: ocr -->

8 ‘The PDS Z80 Manual

F - Fill memory with data

F start address , length , data byte(s)

start address
‘This is the address that the fill will start from

length
‘This is the number of bytes that will be filled

data byte(s)
This can be any number of bytes. The memory area will be filled with this pattern of bytes

‘This will give an error if:

‘The length is zero.

‘There is a fault in the link to the target computer.
Only the dumb download software is needed.

NOTE?

Memory can be filled with either a single value, or a pattern. For example to fill the first 4K of memory
with 0 you would use:

F0,4096,0 ©

To fill the first 4K of memory with the repeating pattern 1,2,3,1,2,3,1,2,3.... enter:

F 0,4096,1,2,3


---

<!-- Source PDF page 72; extraction: ocr -->

‘The PDS Z80 Manual cc)

G - Calla routine and return

G start address

start address
Is the address that will be called

‘This will give an error if:
‘There is a fault in the link to the target computer,

NOTE: .

This will use the download software to call the routine. This means there will be a return address on
the stack. If a return is executed then it will 80 back into the download software. If you don’t want a
return address on the stack and you don’t need to go back into the download routine then use the ’J’
command,

This command is mainly used for testing routines. If you first use the R command to setup register
values, then Groutine address then use the R command again to see how the registers have changed.
For example:

RHL=23,A=2
vnG MULTIPLY
R

If you only have the DLO type download software in the target computer, then the routine will be
JUMPED to, not called. .


---

<!-- Source PDF page 73; extraction: ocr -->

70 ‘The PDS Z80 Manual

J - Jump to an address

J start address

start address
Is the address that will be jumped to

This will give an error if
The 'CLEVER' PDS download software is not being used.
‘There is a fault in the link to the target computer.

NOTE:

This is similar to the G command, but executes a jump to the routine. This means that a return will
Rot return you to the download software, your program will have to jump back into the download
software itself. This is mainly used for jumping into the middle of a routine after setting up all the
registers,


---

<!-- Source PDF page 74; extraction: ocr -->

‘The PDS Z30 Manual a

L - Loop and execute commands quickly

This command is used to execute a string of monitor commands one after the other very quickly.
What you dois type all the commands starting in the top left of the screen, and place an Lat the end
of them. When you press enter on the line with the L, PDS will do a" HOME’ and keep doing returns,
executing any commands it comes across. For example, clear the screen using control home and press
M (return) then L (return). You will see a block of memory rapidly changing. PDS is executing the
Mcommand, then looping and executing the M command again, over and over. To stop PDS, press
any key. When PDS reaches the L command it will stop looping. If any of the commands give an
error, then the loop command will also be stopped.

A common use for this command is for download software running under the interrupts, while a
game is playing for example. To have the command M DATAAREA looping. This will show you the
data area changing as the game is being played. You could also modify the stack and see it build up
and down, or the keyboard buffer.

You may build up very complex loops such as :

RHL=23,A= {BILL}
G MULTIPLY

W [STORE],[RESULT]
W STORE, [STORE] +2
B BILL, {BILL} +1

L

If MULTIPLY is a routine that multiplies HL by A and returns the result in a location called
RESULT, then the above string of commands will build up a table of results from the address in
STORE onwards. Note if you wanted to stop the above loop when a certain address in STORE was
reached then you could add the following commund to the loop:

X 1/([STORE]-ENDADDR)

Which would stop and give a division by zero error when the contents of STORE was the same as
ENDADDR.

Loop is a command that may not be immediately useful, but becomes invaluable after a while.


---

<!-- Source PDF page 75; extraction: ocr -->

n The PDS Z30 Manual

M Modify a block of memory

‘This command can be used in two different ways:

1) M

his will modify a block of memory starting from where the last modify command finished.
2) M start address

This will modify a block of memory starting from start address

This will give an error if:
‘The target computer is not running the clever download software
There is a fault in the link to the target computer

NOTE:

‘This willshowa block of memory on the display, showing the hex and ascii, You may:move: the,cursor
up the screen and alter the hex bytes, pressing enter on the line will then download it, changing the
bytes altered. The line will then be uploaded again and reprinted. This is so ifyou were to alter ROM,
it would not change when you pressed enter on the line.


---

<!-- Source PDF page 76; extraction: ocr -->

‘The PDS 280 Manual B

N ~ Send a command down to the download software

N byte value {, byte value,, byte value, byte value ..}

byte value
Is avalue that is sent to the target computer

‘This command is included to allow you to expand the uses of the PDS monitor yourself. It will send
this byte down to the download software. The download software protocols in PDS use, or will use
the bytes in the range 170 - 200 to specify certain functions, so try and avoid these unless you have
changed the target computers download software. The cu: rrent version of the DL1 software only uses
bytes in the range 179 to 187 to specify commands, although the others will be used for future
expansion. This command is very powerful, although you will have to write the software yourself,
Basically, add a say, CP 5, JP Z,MINE to the main loop of the target computer download software,
then in your MINE routine do something clever. To initiate this clever routine from the monitor,
Just type NS. You could for instance have NO to freeze the program when used with DL2, under the
interrupts software, and N1 to restart the Program again. Or you could have NO to exchange screens
ina two screen game. Remember that multiple bytes can be sent, so that complicated commands
can be sent to the target computer. You will need to become familiar with the download software
to use this command fully.


---

<!-- Source PDF page 77; extraction: ocr -->

4 The PDS Z80 Manual

(2) - Set'an offset for all addresses

‘There are two ways to use this command:
1) . °

This will show the current offset being added to all addresses

2 O offset

This will set the new offset to offset

All memory addresses sent to and from the target computer will have this offset added to them first.

For example, if Ihad a program loaded in the target computer at 8000h and it was supposed to be at
9000h, then if I entered:

© 8000h-8000h

From then on it would be as if the Program really was at 9000h, for example D 9000h would
disassemble the start of the Program.


---

<!-- Source PDF page 78; extraction: ocr -->

The PDS Z80 Manval 15

Pp - Work out screen coordinates or addresses

‘There are three ways to use this command:

y] Paddress .
‘This will return the x and y coordinates of the screen address.

2] Pxy

‘This will return the screen address of the.x andy coordinates.

3) P@ address

This will set the start of the screen to address

NOTE:

‘These commands do not require a target computer connected. The computer must be setup in the
config system or using the 'Q’ command before this command is used. There are six different screen
formats supported by this command:

0. ZX-SPECTRUM. ~ Hires screen at 4000h, 256 by 192 pixels
“lCOMMODORE 64 ~‘Hires screen at‘0;'300 by 200 pixels

2. AMSTRAD MODE 0 _ - Hires screen at CO00h, 160 by 200 pixels

3. AMSTRAD MODE 1 _ - Hires screen at COUOh, 320 by 200 pixels

4. AMSTRAD MODE 2 ___- Hires screen at CO00h, 640 by 200 pixels

5. SPECIAL AMSTRAD | - Mimic spectrum mode’ at CO0Oh, 256 by 192

Ifyou are using a second screen , or you have moved the screen from the defaults listed above, use
the P@ address command to specify the new start address.

When you use the P address command, the coordinates return will be for the left most pixel in that
byte.

EXAMPLES:

(All these assume that the current computer is 0, ZX-SPECTRUM)

PO,0 Will print: Addr=4000h, Bit =80h

P103,48 WiIIl prin Addr=40CCh, Bit=01h

PS5234h Will print: X= 160, ¥=138
P3829h Will print That address is not on the screen!


---

<!-- Source PDF page 79; extraction: ocr -->

16 The PDS 280 Manual

Q + Read or set options

This command can be used in two ways:

Hy Qoption

Will print the current value of the option.

2 Qoption , value
Will set the option to the value given,
NOTE:

‘This command does not require a target computer connected, All the options can also be found in
the config system, see the editor manual for more details. For a list of all the options and their
Parameters see the chapter on options. .

EXAMPLES:

‘The sequence of commands below will take a screen address on the Spectrum and return the
equivalent address on the Amstrad screen.

Q1,0 ~ Select Spectrum as default computer
P4567h + Find the coordinates of a screen address
Qi ~ Select Amstrad as default computer
P56,29 - Find the screen address given coordinates

‘The sequence of commands below will take an area of memory from the Spectrum and transfer it to
an Amstrad. The Spectrum is connected in port 1, the Amstrad in port 2.

Q0,1 ~ Select port 1 (The Spectrum)
U>DEMO,4000h,1000 = Upload 1000 bytes from 4000h

0,2 ~ Select port 2 (The Amstrad)
U<DEMO,0C000h - Download the bytes to address OCOOUh

Instead of entering values using the assembler expression evaluator, you may enter them in hex only,
for example:

MOA987h + Will modify memory address 0A987h
Q3,1 = Set "HEX expressions’
MA987 = Now all numbers are treated as hex


---

<!-- Source PDF page 80; extraction: ocr -->

‘The PDS Z80 Manual n

R - Set or update the register values

The two formats for this command are:
y R

This will update all the registers at the top of the screen

2} R register = value
This will set the register to the value specified

register
Is any Z80 register, word or byte, for example HLDE,D,F’ or SP

This will given an error if:
The clever download software is not being used,

‘There is a fault in the link to the target computer.
The value is too big for the register specified.

_ NOTE:
You may set more than one register at a time, for example:

RHL=23,A=2,PC =4000h

The registers at the top of the screen are only updated after tracing has finished, or an R command
has been executed. If you wish to update them yourself, enter R on its own. PDS could not keep them
updated all the time because you may not have a target computer connected, or it may not be running
clever download software.


---

<!-- Source PDF page 81; extraction: ocr -->

—

B ‘The PDS 280 Manual
s - Search memory for data

S start address, end address , data
start address

Is the first byte that will be scanned in the search

end address
Is the last byte that will be examined

data
Is the data the is being searched for

This will give an error if:

The clever download software is not being used.
There is a fault in the link to the target computer,
‘The end address is lower than the start address,

NOTE:

Thie'data may be any number of bytes, for example:

$0,100,23 + Will search the first 100 bytes for 23s
$0,100, 1,2,3 ~ Will search for the Pattern 1,2,3
S0,100,"PDS" - Will search for the string PDS’

PDS will search the memory by uploading the block and searching through it in the main computers
memory. If it finds a match then it will Print the address of the first byte of the match. It will the carry

on the search from the byte following this address,


---

<!-- Source PDF page 82; extraction: ocr -->

‘The PDS Z80 Manual oe

T = Trace

This command takes two formats:
y T

This start tracing from the current PC

2 T address
This will start tracing from address
This will give an error if:

The clever download software is not being used.
‘There is a fault in the link to the target computer.

NOTE:

Thisis one of the most complex features in the whole of the development system. For full information
see the chapter on tracing.


---

<!-- Source PDF page 83; extraction: ocr -->

8 ‘The PDS Z80 Manual

u = Upload/Download memory from/to the target computer.

This command has three different formats:
y U start address , length {,bytes per line]

Tis will upload an area of memory and place it at the current editor cursor position in the form of
HEX statements, each line will have 16 bytes, if bytes per line is not specified.

2 U> filename , start address , length

‘This will upload an area of memory from the target computer into a disk file called filename, Note
the U

3] Usfilename , start address, length

This will download a disk file into the target computer at the start address, if length is not specified
then the whole file is transferred. Note the U

This will give.an error if.

The clever download software is not being used.
There is a fault in the link to the target computer.
3] length is longer than the file on the disk,

3] filename does not exist.

1] Too much memory is uploaded, not enough space in the file.

NOTE:

The file name in versions 2] and 3] may contain drives and path names, In version 1] you may have
1 to 55 bytes per line in the HEX statements.

EXAMPLES:

To upload a screen from the spectrum into a file in the current directory called SCREEN.ZX use:
U>SCREEN.ZX,4000h,6144

To download it again to the Spectrum screen use:

U<SCREEN.ZX,4000h


---

<!-- Source PDF page 84; extraction: ocr -->

The PDS 280 Manual 81

Vv - Show nearest label

Vexpression

expression
‘This can be any number or normal expression,

Once entered, this will display the nearest label before, after and at that address, A message will be,
displayed if no match was found. This is very useful when you are trying to trace or disassemble your
‘code, as you can then reference addresses with labels in your code. Make sure that you assemble
your program before hand, as a symbol table is required if this function is to work.

EXAMPLE:

If BILL =3E8h, TOM =514h, and DICK = 11B4h. Then entering the following command :
2000

Will return:

TOM (0514h), 028C bytes below that address

No labels at that address
“DICK'(11B4h), D9E4 bytes above that address


---

<!-- Source PDF page 85; extraction: ocr -->

& ‘The PDS Z80 Manual

WwW ~ Change or display a word at a memory location

This command can be used in two ways:
q Waddress

This will display the word at the address given. The value will be displayed in hex, decimal, binary
and ascii.

2 Waddress , value

‘This will move the value into the address given.

address
‘This is the address of the word to be changed

value
‘This is a value, from -32768 to 65535

This will give an error if:
There is a fault in the link to the other computer
1) Needs the clever PDS download software
2] Only needs the dumb download software

NOTES:

The Bcommand has the same function, but works on bytes instead of words. This command is mainly
used for altering values in your program, to quickly see the effect of small changes.

EXAMPLES:
W4000h,23

This will load the location 4000h with the value 23, and location 4001h with 0
W FRED, {FRED}*2

‘This will double the word value at locations FRED and FRED +1


---

<!-- Source PDF page 86; extraction: ocr -->

‘The PDS Z0 Manual B

x - Evaluate an expression

X expression

expression
Is a valid expression that will be evaluated using the assemblers expression evaluator. If you have
just assembled something then you may use label names,

NOTE:

This does not require a target computer attached,
The value of the expression will be printed in hex, decimal, binary and if within the range 32 to 127,
in ascii.

EXAMPLE:

X23 +45*2
HEX =0071 , DEC =00113 , BIN =00000000-01110001 , "?


---

<!-- Source PDF page 87; extraction: ocr -->

& The PDS Z80 Manual

Zz - Change the bank selected in the target computer

Zbank number

bank number is a value sent down to the target computer.

This will give an error if:
‘There is a fault in the link to the target computer

. This command varies on all computers, in the download software you will find a small section you
have to write yourself. This is a section that gets the bank number 0-255 and sets up the computers
memory depending on that value. If you wish you could ‘OUT? it straight to a ‘bank select’ port, on
a spectrum 128 for instance. Or you could have a more complex routine, with different setups for
each value of BANK. This command has been written like this as all banked ram computers are
different and most programmers have different systems, or values for each different bank
configuration,


---

<!-- Source PDF page 88; extraction: ocr -->

The PDS Z80 Manual

63

The options and configure system in the monitor

The monitor can be changed or altered by a number of options, which can be set or examined either
in the config system from the editor, or by using the Q command in the monitor. Below are all the
Q options and what they can change.

Option

0

G5,ANS

— 0-255

Range
lor2

OtoS

0,2-16

~ 0-255

po

o:

— 128 (7).
64 (6)
— 32(5)
~ 16 (4)
8 (3)

ABS

128 (7)

128 (7)
64 (6)

Alters

Which PDS port the monitor works from, the default is *

port 1.

Which computer PDS thinks it is attached to, this is only
really used in the P command so that PDS knows how the
screen is addressed.

This sets the radix of all the monitor commands, the
default is 10. If it was set to 2 then D1010 would
disassemble from location 10 (decimal) onwards. If this
is set to 0 then the commands only accept hex numbers.
No expressions are allowed, you could then use
commands such as DABCD or MC9.

This sets the number of lines displayed in the M
command. The default is 8, If it is set to 0 then memory
will displayed one screen at a time, and key will move
onto the next screen, the up arrow will move backwards
one screen, Escape or finish will quit this command.
This sets the number of lines displayed in the D

‘command. The Yefaultis 8.'If itisisetto;0.then code will

be disassembled one screen at atime, any key will go onto
the next screen. Finish or escape will quit this command.
Disassembler flags, each bit in this byte controls a
function in the disassembler.

1=All expressions in decimal, else in Hex.-.

1 = Expressions in ascii if in range.

‘ab after the instruction, else a space.

ial address in decimal, else in Hex.

1=1X+nn and IY +nn always in decimal, else current
radix is used.

Trace system flags. Each bit controls a function :

1 = When executing in "FAST mode, do a VSYNC after
each instruction, This makes the bar visible all the time
on the screen, although it slows the tracer down to 50
instructions a second.

General monitor commands flags

1=The E command accepts decimal input, else hex.

1 = Analyze doesn’t stop when one bar reaches the end,
it will keep going until a key is pressed.


---

<!-- Source PDF page 89; extraction: ocr -->

$$$
86 ‘The PDS Z80 Monitor

### 6.4 The trace system

You gan start to trace a program by entering T address as a command in the monitor. If the PC
displayed at the top of the screen is already pointing at the start of your program, you may press just
T to start tracing,

enter the tracer you will see 15 lines of source code disassembled along with their addresses and hex,
There will be an inverted bar on the first line of this disassembly, this shows the current instruction,
(huike bottom of the sereen there is a small box, this is for memory displays. Above this there are all
the options, with their first letters highlighted,

in the clever download software. It restores all the registers, executes the instruction, saves all the
registers, sends them back up to the main computer and then carries on with the next instruction, It
has to do this with most instructions it executes to get the flags altered correctly, Even doing all this
work, on anIBM,PC itcan.execute. ‘about one.thousand. instructions, a-second... .

If PDS comes across an unknown instruction, it will place the inverted bar on top of it and beep, it
will not continue until the value of the PC is altered to either another part of your program, or just
Past that instruction. You could put illegal instructions around your program to halt the tracer, OFDh,
OFDh for instance.

Note that the Programs you trace should not do OUTS to the ports used by the PDS interface, this
will almost certainly stop the (racer, and probably crash the target computer. You should also notice
that while the clever download software is used, the interrupts are always disabled. The tracer will
show when interrupts are enabled or disabled, although they never really alter. If you trace a HALT,
it will be treated just like a NOP by the tracer (unless the interrupts are disabled), If the interrupt
routine is important (say reading keyboards) then cal! them now and again from the tracer.


---

<!-- Source PDF page 90; extraction: ocr -->

‘The PDS Z80 Manual 87

### 6.5 The tracer options

‘There are 11 different options you may choose in the tracer main menu they are:

Any key
Will execute the next instruction and show and registers changed.

G +'Go full speed’
Will execute a jump into your program at the current PC. This will leave the download software and
run your program full speed.

F + ‘Fast trace’
‘This will execute code fast, as if you kept a key held down. It will stop when you press any key.

Q + ‘Quick trace’

‘This will execute code quickly, it will only update the PCin the register display, it will not disassemble
the current instruction on the screen and will not update any other register values. This speeds up
the tracer a lot and is used to keep an eye on where it is without slowing it down too much. It will
stop when you press any key.

s = 'Stack display’

This will open or close a box on the right hand side of the disassembly, This box shows the contents

of the last ten items pushed on the stack. When a PUSH HL is executed you will see the value of HL

and the letters HL on the bottom of the stack. If you execute a call then ’--’ is shown where the HL
~was. Thisis'so-you can see’iftthe correct registers are beirig pulled offthe stack in‘order. Toturn:this

stack off, press S again.

R + "Register values’
Allows you to change register values, it will prompt you for the register and value in the form
reg=value, value can be any expression as long as it is within range. <reg> can be any eight or
sixteen bit register,

M -'Memory display’

This will allow you to see a block of 32 bytes in hex and ascii, the block can be at a fixed address, or
Pointed to by a register. To switch off the memory display, select M again. The memory display is
updated after every instruction,

L + "Execution limits’
Allows you to specify a range of addresses that can be traced, if the program goes out of these limits
then it will stop and beep. The upper and lower limits are default set to 0 and OFFFFh.

N + ’Execute the next instruction’

‘The tracer will execute the next instruction at full speed. This is mainly used for executing routines
at full speed. Say the tracer was about to execute CALL CLS, you don’t really want to trace this
routine so just press N. If the routine is very long and takes over a second to execute then the tracer
may think the target computer has bung. If this occurs you will just have to wait until the routine has
finished and the enter T for trace continue.


---

<!-- Source PDF page 91; extraction: ocr -->

88 The PDS Z80 Manual

I = "Ignore this instruction’
‘This will make the tracer skip over the current instruction. It is mainly used for skipping out of loops,
or avoiding calling routines,

T + Trace very quickly until condition’
Will trace as fast as it can, with no display updating, until a condition is met. Once T is pressed, a
second menu is displayed containing the conditions,

Key- ’K’
Will trace until any key is pressed. This is the fastest trace available.

Halt. "H?
Will trace until a HALT is executed (many programs have a HALT at the start of
the main loop).

: Djnz- 'D’
Will trace until a DINZ finished (doesn’t loop),

Return - 'R’
Will trace until a RET or RET cc is executed.

Stack- 'S’
Will trace until the stack is altered in any way.

Fail- °F)
Will trace until a conditional instruction fails, or does not jump.

Pass- 'P?

Will trace until a certain point is passed a certain number of times. This can be
used as a breakpoint. It can also display the number of times the point has been
passed as a countdown.

Compare - ’C’ .
Will trace until a register or memory address either goes outside set limits or until
a particular bit pattern occurs.
