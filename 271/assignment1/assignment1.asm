TITLE Assignment 1     (assignment1.asm)

; Author(s): James Hinson
; Course Number: CS 271
; Date: 1/24/2024
; Description:  The first assignment for CS 271 - Computer Architecture and Assembly Language
; 				Calculates the area, perimeter, and linear feet of wooden planks needed to
; 				fence a pasture of a size given by the user.

INCLUDE Irvine32.inc

; (insert constant definitions here)
PLANK_LENGTH = 6


.data

; (insert variable definitions here)

	userName	BYTE		50 DUP(0)
	intro1		BYTE		'This program finds the area, perimeter, and number of 1x6" planks needed ', 0
	intro2		BYTE		"to make a fence around a pasture of a given length.", 0
	promptName	BYTE		"What is your name? Press enter when done: ", 0
	promptLen	BYTE		"Enter the length of your pasture (in feet) : ", 0
	promptWid	BYTE		"Enter the width of your pasture (in feet) : ", 0
	promptPlank	BYTE		"Enter the linear feet of wood planks available : ", 0
	areaOutput	BYTE		"The area of the pasture is : ", 0
	permOutput	BYTE		"The perimeter of the pasture is : ", 0
	plankOut1	BYTE		"You have enough wood for ", 0
	plankOut2	BYTE		" and an extra ", 0
	plankOut3	BYTE		' linear feet of 1x6" planks', 0
	loopPrompt	BYTE		"Would you like to do another calculation? (0=NO 1=YES) : ", 0
	goodBye1	BYTE		"Goodbye ", 0
	goodBye2	BYTE		'!', 0

	inputLoop	DWORD		?
	inputLength	DWORD		?
	inputWidth	DWORD		?
	inputPlank	DWORD		?
	area		DWORD		?
	perimeter	DWORD		?
	numPlanks	DWORD		?
	remainder	DWORD		?


.code
	main PROC

; (insert executable instructions here)

	; Introduce the program
	mov 	edx, OFFSET intro1
	call	WriteString
	mov 	edx, OFFSET intro2
	call	WriteString
	call	Crlf

	; Ask for and save user's name
	mov 	edx, OFFSET promptName
	call	WriteString
	mov 	ecx, 50
	call	ReadString
	call	Crlf
	call	Crlf

	; Ask for and save pasture length
	mov 	edx, OFFSET promptLen
	call	WriteString
	call	ReadInt
	mov 	inputLength, eax
	call	Crlf
	
	; Ask for and save pasture width
	mov 	edx, OFFSET promptWid
	call	WriteString
	call	ReadInt
	mov 	inputWidth, eax
	call	Crlf

	; Ask for and save the linear feet of available planks
	mov 	edx, OFFSET promptPlank
	call	WriteString
	call	ReadInt
	mov 	inputPlank, eax
	call	Crlf
	call	Crlf
	
	; Calculate the area
	mov 	eax, inputLength
	mul 	inputWidth  ; Multiply eax (inputLength) by inputWidth
	mov 	area, eax   ; Store the result in the area variable

	; Calculate the perimeter
	mov 	eax, inputLength
	add		eax, inputWidth
	mov 	ebx, 2      ; Set the multiplier to 2
	mul 	ebx         ; Multiply the sum by 2 to get perimeter
	mov 	perimeter, eax

	; Calculate the number of planks
	mov 	eax, perimeter
	mov 	ebx, PLANK_LENGTH
	div 	ebx          	; Divide EDX:EAX by EBX, result in EAX (quotient), EDX (remainder)
	mov 	numPlanks, eax  ; Store the number of planks in numPlanks
	mov 	remainder, edx	; Store the remainder in a separate variable

	; Display the area
	mov 	edx, OFFSET areaOutput
	call	WriteString
	call	Crlf

	; Display the perimeter
	mov 	edx, OFFSET permOutput
	call	WriteString
	call	Crlf

	; Display the number of possible rails
	mov 	edx, OFFSET plankOut1
	call	WriteString
	mov 	edx, numPlanks
	call	WriteInt
	mov 	edx, OFFSET plankOut2
	call	WriteString
	mov 	edx, remainder
	call	WriteInt
	call	Crlf
	call	Crlf

	; Ask if user wants to do another calculation
	mov 	edx, OFFSET loopPrompt
	call	WriteString
	call	ReadInt
	mov 	inputLoop, eax
	call	Crlf

	; Loop if user wants to do another calculation
	cmp		inputLoop, 1
	je		main

	; Say goodbye to user
	mov 	edx, OFFSET goodBye1
	call	WriteString
	mov 	edx, OFFSET userName
	call	WriteString
	mov 	edx, OFFSET goodBye2
	call	WriteString

	; exit to operating system
	exit

main ENDP

; (insert additional procedures here

END main
