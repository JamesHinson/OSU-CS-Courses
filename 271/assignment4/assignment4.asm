TITLE Assignment 4     (assignment4.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 3/2/2024
; Description:

INCLUDE Irvine32.inc

; (insert constant definitions here)

.data
    unsortedTitle 	BYTE 	"The unsorted random numbers:", 0
    sortedTitle 	BYTE 	"The sorted list:", 0
    prompt1 		BYTE 	"How many numbers should be generated? [10 .. 200]: ", 0
    prompt2 		BYTE 	"Enter lower bound (lo): ", 0
    prompt3 		BYTE 	"Enter upper bound (hi): ", 0
    medianMsg 		BYTE 	"The median is: ", 0
    goAgainMsg 		BYTE 	"Would you like to go again (No=0/Yes=1): ", 0
    programIntro 	BYTE 	"Sorting Random Integers Programmed by James Hinson", 0

    array_size 		DWORD 	?
    lo 				DWORD 	?
    hi 				DWORD 	?
    array 			DWORD 	200 DUP(?)

.code

introduction PROC
    ; display program intro
    mov edx, OFFSET programIntro
    call WriteString
    call Crlf
    ret
introduction ENDP


getData PROC
    ; get array size from user
    ; validate array size
    ; get lo and hi from user
    ret
getData ENDP


fillArray PROC
    ; generate random integers and store in array
    ret
fillArray ENDP


sortList PROC
    ; sort the list in descending order
    ret
sortList ENDP


displayMedian PROC
    ; calculate and display the median
    ret
displayMedian ENDP


displayList PROC, title:PTR BYTE
    ; display the list
    ret
displayList ENDP


goAgain PROC
    ; prompt user to go again or quit
    ret
goAgain ENDP


main PROC

; (insert executable instructions here)
    call introduction
    call getData
    call fillArray
    call displayList, ADDR unsortedTitle
    call sortList
    call displayMedian
    call displayList, ADDR sortedTitle
    call goAgain
	exit	; exit to operating system
main ENDP

; (insert additional procedures here)

END main
