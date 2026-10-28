# PDS guide early version

> **Auto-converted from:** `PDS_guide_early_version.pdf`. Text extracted from the original PDF; OCR may contain recognition errors. Consult the PDF for exact diagrams and formatting.


---

<!-- Source PDF page 1; extraction: ocr -->

There now follows a short guide to all the key functions of PDS

It was written by myself over a few hours so it is not ment to be complete,
it is just a short quide, as soon as better manuals are available we will
let you have them. Any problems Please ring myself Andrew Glaister

on Crawley, @293 883819 or ‘Foo’ on @1 959 60908 with questions about the
manual or opperations.

Keyboard overlays will be sent soon, (as soon as I feel happy with the layout!)
The keyboard layout for the IBM PC Programmers development system.

Fi (CAssembled F2 [Save/Load]
FS (CGraphics] F4 [CMonitor3
FS (Configure] F& [Print]

F7 CHelp] Fe (CRepeatl
F9 [Disk] F1i@ [Finish]
Fi - Assemble — Will assemble the program in RAM, starting from file @, line 1.
F2 = When you first run PDS, will be LOAD, press this and the files in the curr

ent directory will

be loaded into memory, from then on this key will be SAVE, press it and all
windows

will be saved inte the current directory. This saves you having to geo into

the disk system and allows you to make regular saves to disk without interu
pting

your work.

FS = Will enter the graphics editor, this is not implemented on the PC's at the
moment due to the fact I have to cater for colour graphics and CGA and EGA
formats.

F4 - Enters the PDS monitor.

FS - Allows you to configure areas of the PDS system, note this is being

implemented slowly due to the large number of hardware differences
in the IBM and Apricot.

Fe -~ Print -— this will allow printing of files, windows or all files, on the
PC this is not implemented yet due to hardware differences in the
print spooler program.

F7 = Loads the PDS help file into the ‘other’ window and find help on the

topic the cursor was sitting on, swap to the other window and back again
to get rid of it. Note you may change it.

FS —- Repeat, for use with finds and replaces, prompts for type of repeating.
Fo = Disk enters the disk system
F1@ - Finish ~ will escape from most commands in PDS, also used to exit PDS.

IIIT TEETER REE FETE ETE FTE TEETER EEE EEE FE ERIE HERRERO EEE EE

Shift and keys F1-FS allows you to swap between files @-7 (Eventually the
numbering system may be changed on the PC’s to 90 from 1-8!)

STEUER EE IOI TEETER TIE ETE IETHER IERIE EHGEHEIHE IEEE

Alternate and keys F1-F1@ allows you to set markers 1-@, note setting a marker
deletes any other markers of the same number any where in your program

Control and keys F1-F@ moves the cursor to the marker 1-@, or beeps if the
marker has not been set

FUSE ITERATE EITHER EEE HEF
Escape - Is used to enter the escape mode, when ‘TECO’ type commands may be

executed, Press escape twite on an empty line to escape this mode.
Control or Alternate Escape - will Prompt tor deleting the whole current file.

SETI EE EEE EEG HHEIEIIGEIHEHHEEHRE ROHR IIEH


---

<!-- Source PDF page 2; extraction: ocr -->

Control or Alternate and keys 1-@ across the top of the keyboard are the PDS

function keys, which default to Fi-F@ and can be set for each file in the
configure system.

TEETER HEAGEEI HEHE EIE EGER EERE HE

Del --> will remove the character the cursor is sitting on

Shift Del --> will remove the character behind the cursor (same as normal delete
d

<—— Del will remove the character behind the cursor
Shift <-- Del will remove the character the curser is sitting on

Alternate and either delete key will remove the line the cursor is on

Control Del --> will delete all characters to the end of the line

Control <-~ Del will delete all characters to the start of the line
ihe heehee LCL LLL LE LLL TT TELE T Te Te ere Cree
Shift, control or alternate and PRTSC will enter the ‘PRINT’ menu (like F4)
OCI IEICE EEE IGE EAE IE EIEIO IE HEIE I EHR AEIE EE a
Alternate or control and c/r will enter a c/r, leaving the cursor where it was
FORTE TENE IE SIE TFET TE TEE TEE ETE ETE TEE TEE EEE EEE ETE IEEE ILI IEICE REIL ERIE aE
Caps lock — will change letters ‘a’ to ‘z‘ into ‘A’ to ‘Zz’ when lit up.

note that at the moment the ‘auto caps lock’ in PDS works, but

cannot change the status of the LED on the key! - I'm thinking
about this.

TEETER TE FETTER TEETER IE TEETER TEE TEE ETE ETE TERETE IEICE EIR HRHEIHEJE IERIE CII ee
Num lock ~- When lit up, the keys on the keypad return numbers, when they are

shifted they return the cursor keys, also when control and alternate
are used they return their special functions

FETE IE TET ETE FETE TEE TET EE ITE TEETER TEE TEE TEE HE ETE TE EERIE IERIE TEI TEETER IERIE EERIE

Scroll lock/Break —- Swaps between the two windows if they are open on the displa
y

Control CSerik] - Sets the window divison to the middie of the display.

Alternate (Scrik] - Changes windows and enlarges the new window to take up the
(or shift) whole display

FEIT TET TE TEETER IEEE ETE EE ETE EERE UE EERIE EECA EE FETTER IEEE EEE EER IIE EE IE EEE
Alternate or control — on keypad, is the same as “T, repeat last find or replace

Alternate or control + on keypad, evaluate the expresson the cursor is at the
start of.

Alternate or control Enter on keypad, enter time and date at cursor position

Alternate or control .Cdel] on keypad, Swaps the case of the character under the
cursor and moves one character right.

Alternate or control @fins] on keypad, does a “G and displays the results in the
other window, leaving the cureent window untouched,

TERETE IRIE IE TE TE FETE PETE ETE AE HEE HE TERETE TE TE FETE FETE TE TEE TEE JE HE JE FETE HE TE FE JETER E EE HEHEHE JE EE JE HE EE EHR IEICE OEE EE

The following keys are accessed by having NUM LOCK off (not lit up) or by
pressing shift first.


---

<!-- Source PDF page 3; extraction: ocr -->

~ Goto the end of the current file

- Move down a line

Move down 20 lines (one page)

~ move one character left

~ UNDO, goes back to where you were before the last opperation eg: “G or find
or home. Note cursor keys don’t count, so you could “G, curser around

the routine and the press UNDO to go back to where you were before
the “G6

- Move one character right

~ Go to the top of the current file
Move one line up

- Move up 28 lines (one page)

OkrwW Ne
1 t

wonea
1

FEET TEETER ETI EAHEIHE HIE ERIE

The following is a list of the numeric keys when Control is pressed at the
same time (The state of NUM LOCK doesn't matter)

1 — Will scroll down to the end of the file quickly, it will stop when any
key 1S pressed.

- Move to the end of the file
- Will move down one page

- Will move to the start of the current line (Chr @@1)
UNDO

~ Will move to the end of the current line

- Will HOME all the files and place you at the top of file @
- Move to the top of the current file

- Will meve up one page

SCOnOUWUSWN
i

FREI IE IE TIE THE TEETER HEE HE SE TEE SEITE JE HE FETE FEE HEE FEE FEE SEC EHR EE J HEE FEE FEE FEE BETES HE JERE HEHE EE IEEE IE HE HEHE EEE

The following is a list of the numeric keys when Alternate is pressed at the
same time (The state of NUM LOCK doesn't matter)

1 —- Will seroll down to the end of the file quickly, it will stop when any
key iS pressed.

~ Move to the end of the file

— Will move down one page

— Will move the window partition one character to the left

— UNDO

Will move the window partition one character to the right
— Will HOME all the files and place you at the top of file @
— Move to the top of the current file

~ Will move up one page

CONGO UMSUW
'

(Note only 4 and 6 are different from Control)
FETE TEE TERE AE IEEE IE ETE ETE EE HEE SEE FEE FTE FTE ETE BE JE SEE SEE 96 98 9 FE EJ EE EE EE EE JJ ECE Ce

Alternate or control the letters A-Z

“A - Auto label A, if cursor at CHR @@1, the label will be incremented first

“R ~ Block start ( note more popular key is °< )

“C - Block copy

“D ~ Block delete — prompts yes/no first

“E — Execute escape mode macro

°F — Find @ string, note the c/r and tabs characters can be searched for, end
the string with escape, or FINISH to exit.

“G — This is the most popular command in the whole of PDS, it will move the
cursor to the start of the routine that is called by the label that
the cursor is sitting on, eg: if the cursor was sitting anywhere on the
‘FRED’ in CALL FRED, and you presed “G, the cursor would move to where
the routine FRED is in your program, or beep if not present

“H - Moves the cursor to the start of block marker

“I = Inserts a comment bo»


---

<!-- Source PDF page 4; extraction: ocr -->

vo o— Jumps to a prompted for line number

“K = End of block ( note more popular is *> )

“L - Load current file, you are prompted where from
“M - Move block

“No - Move the cursor to the end of block marker

“O ~ Assemble (same as F1)

°P - Print block

“@ —- Moves the cursor te after the next quote character on the current line
“R ~ Read a block from disk

“S - Save the current file, you are prompted where from

“T - Repeat the last find or replace

“U — UNDO

“VY — Enlarge the current window to take up the whole display

“Wo- Write block to disk

“X — Find and replace (Xchange)

“Y — Moves cursor to last assembler error line and reports error again
“Z - Same as “A but enters LZ labels

The best way to learn these keys is to use them, some you may never use,
I never use °B,°K,*1,°A,°Z,°Q and a few others.

All other keys and shift keys should do what is written on the key.

If you have an AT keyboard, with seperate cursor keys etc... PDS will still work
with it.

FETE TEER TE TEETER TE HEE IE TE IE FETE TEE JE HEE HEE EF FEI FE HE ETE TE HEHE IE SE E EE IE EIEIO IE IE aE HE EEE RR

The disk system is in a bit of a mess, it was written with an Apricot micro
screen in mind, it is being re written at the moment, but if you just use it
for loading and saving MSDOS files it is ok. Note: the keys are a bit of a
muddle because I have not tried te order them yet.

When you enter the disk system you are in the MSDOS format mode (although
without a microscreen you cannot tell (at the mo.!)) Fi is load, either

@ single file or ALL files. F3 is save, either all or Single files.
F2 will change the current directory.

NOTE : Please only use the hard disk, the floppy will be implemented soon
but I have to make it compatable with all possible formats yet.

This really limits the disk system at the moment, and does not allow you to
use any MSDOS commands, formatting, XMSDOS mode (much faster load/save), or
PDS mode (fast for floppies). I will redo the disk system very very soon
(days....) F1@ to exit back to the editor by the way.

HEEFT FETE RTECS HEE IE FEE FE EE EE EE JE ESE SE SE J EEE EEE IE EE EE EE IE EE EE OE EE EE ed

The files PDS writes to disk in MSDOS mode have no ‘nasty’ characters, they
have c/r and 1/¢# at the end of line (13,1@) and tabs are just CHRS(9).

Note when you alter tab settings in PDS, or file titles, or author, or function
keys they will be lost when saved to MSDOS (XMSDOS gets round this...). At

the end of file there is no ‘end of file character’ you will have a c/r l/#
then the file just stops.

If you are getting files from another assebler or computer, when PDS reads
in MSDOS files it will ignore silly characters, ignore 1/fs or lack of them.

Also any lines over 12@ charcters it will mark, insert a carridge return
and inform you it has done so.

The same as above applies for block read/write in the editor (SR, OW)

TETRIS FETE FETE ITE TEE EE EE EE EE EEE EEF TE EEE SHEE IEE EIR IIHR IOI
