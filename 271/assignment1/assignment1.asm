TITLE Assignment 1     (assignment1.asm)

; Author(s): James Hinson
; Course Number: CS 271
; Date: 1/19/2024
; Description: The first assignment for CS 271 - Computer Architecture and Assembly Language

INCLUDE Irvine32.inc

; (insert constant definitions here)
PLANK_LENGTH = 6

.data

; (insert variable definitions here)

	username	BYTE		50 DUP(0)
	inputLength	WORD		?
	inputWidth	WORD		?
	inputPlank	DWORD		?
	intro1		BYTE		'This program finds the area, perimeter, and number of 1"x6" planks needed ', 0
	intro2		BYTE		'to make a fence around a pasture of a given length.', 0
	promptName	BYTE		"What is your name? Press enter when done: ", 0
	promptLen	BYTE		"Enter the length of your pasture (in feet) : ", 0
	promptWid	BYTE		"Enter the width of your pasture (in feet) : ", 0
	promptPlank	BYTE		"Enter the linear feet of wood planks available : ", 0		

.code
	main PROC

; (insert executable instructions here)

; Introduce the program
	mov		edx, OFFSET intro1
	call	WriteString
	mov		edx, OFFSET intro2
	call	WriteString
	call	Crlf

; Ask for and save user's name
	mov		edx, OFFSET promptName
	call	WriteString
	mov		edx, OFFSET username
	mov		ecx, 50
	call	ReadString
	call	Crlf
	call	Crlf

; Ask for and save pasture length
	mov		edx, OFFSET promptLen
	call	WriteString
	call	ReadInt
	mov		inputLength, eax
	call	Crlf
	
; Ask for and save pasture width
	mov		edx, OFFSET promptWid
	call	WriteString
	call	ReadInt
	mov		inputWidth, eax
	call	Crlf

; Ask for and save the number of available planks
	mov		edx, OFFSET promptPlank
	call	WriteString
	call	ReadInt
	mov		inputPlank, eax
	call	Crlf
	call	Crlf
	
	
	exit	; exit to operating system
main ENDP

; (insert additional procedures here)

END main
