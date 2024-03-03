TITLE Assignment 4     (assignment4.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 3/2/2024
; Description:

INCLUDE Irvine32.inc

; (insert constant definitions here)

.data
    array_size DWORD ?
    lo DWORD ?
    hi DWORD ?
    array DWORD 200 DUP(?)
    unsortedTitle BYTE "The unsorted random numbers:", 0
    sortedTitle BYTE "The sorted list:", 0
    prompt1 BYTE "How many numbers should be generated? [10 .. 200]: ", 0
    prompt2 BYTE "Enter lower bound (lo): ", 0
    prompt3 BYTE "Enter upper bound (hi): ", 0
    medianMsg BYTE "The median is: ", 0
    goAgainMsg BYTE "Would you like to go again (No=0 Yes=1): ", 0
    programIntro BYTE "Sorting Random Integers Programmed by James Hinson", 0

.code
main PROC

	call Randomize
    ; Call introduction
    call introduction
    ; Get data from the user
    call getData
    ; Fill array with random integers
    call fillArray
    ; Display unsorted list
    call displayList, ADDR unsortedTitle
    ; Sort the list
    call sortList
    ; Display the median
    call displayMedian
    ; Display the sorted list
    call displayList, ADDR sortedTitle
    ; Prompt the user to go again
    call goAgain
    ; Exit the program
    exit
main ENDP

introduction PROC
    ; Display program intro
    mov edx, OFFSET programIntro
    call WriteString
    call Crlf
    ret
introduction ENDP

getData PROC
    ; Get array size from user
    mov edx, OFFSET prompt1
    call WriteString
    call ReadInt
    mov array_size, eax

    ; Validate array size
    cmp array_size, 10
    jl getData ; If array_size < 10, get data again
    cmp array_size, 200
    jg getData ; If array_size > 200, get data again

    ; Get lo and hi from user
    mov edx, OFFSET prompt2
    call WriteString
    call ReadInt
    mov lo, eax

    mov edx, OFFSET prompt3
    call WriteString
    call ReadInt
    mov hi, eax

    ret
getData ENDP

fillArray PROC
    ; Generate random integers and store in array
    mov ecx, array_size ; Counter for loop
    mov esi, OFFSET array ; Pointer to array
    fillLoop:
        call RandomRange
        add eax, lo ; Adjust random number to range [lo..hi]
        mov [esi], eax ; Store random number in array
        add esi, TYPE array ; Move to next element in array
        loop fillLoop ; Repeat for array_size times
        ret
fillArray ENDP

sortList PROC
    ; Sort the list in descending order
    ; Using Selection Sort algorithm
    mov ecx, array_size ; Outer loop counter
    mov esi, OFFSET array ; Pointer to array
    outerLoop:
        mov edi, esi ; Inner loop counter
        add edi, TYPE array ; Move to next element
        mov edx, [esi] ; Current max value
        innerLoop:
            cmp edi, OFFSET array + array_size * TYPE array ; Check end of array
            je outerLoop ; If end of array reached, exit inner loop
            mov eax, [edi] ; Next element in array
            cmp eax, edx ; Compare with current max value
            jle nextElement ; If less than or equal, skip swap
            mov edx, eax ; Update max value
        nextElement:
            add edi, TYPE array ; Move to next element in array
            jmp innerLoop ; Repeat inner loop
        swapElements:
            mov eax, [esi] ; Current element
            mov ebx, edx ; Max element
            mov [esi], ebx ; Swap
            mov [edi], eax ; Swap
            jmp outerLoop ; Repeat outer loop
            ret
sortList ENDP

displayMedian PROC
    ; Calculate and display the median
    mov edx, OFFSET medianMsg
    call WriteString
    ; Check if array_size is even
    mov eax, array_size
    test eax, 1 ; Check if array_size is odd or even
    jz evenSize ; If even, find average of two middle elements
    ; If odd, find middle element
    mov eax, array_size
    shr eax, 1 ; Divide array_size by 2
    mov esi, OFFSET array
    add esi, eax * TYPE array ; Move to middle element
    mov eax, [esi] ; Median
    call WriteInt ; Display median
    call Crlf
    ret
    evenSize:
        mov eax, array_size
        shr eax, 1 ; Divide array_size by 2
        mov esi, OFFSET array
        add esi, eax * TYPE array ; Move to first middle element
        mov edx, [esi] ; First middle element
        sub esi, TYPE array ; Move to second middle element
        add edx, [esi] ; Add first and second middle elements
        shr edx, 1 ; Divide sum by 2 to find average
        mov eax, edx ; Median
        call WriteInt ; Display median
        call Crlf
        ret
displayMedian ENDP

displayList PROC
    ; Retrieve parameters from the stack
    mov eax, [esp + 4] ; Get title pointer
    ; Display the list
    mov edx, eax
    call WriteString
    call Crlf
    mov ecx, array_size ; Counter for loop
    mov esi, OFFSET array ; Pointer to array
    mov edx, 0 ; Counter for numbers per line
    printLoop:
        mov eax, [esi] ; Current number
        call WriteInt ; Display number
        add edx, 1 ; Increment numbers per line counter
        cmp edx, 10 ; Check if reached 10 numbers per line
        jne continuePrint ; If not, continue printing on same line
        call Crlf ; If yes, move to next line
        mov edx, 0 ; Reset numbers per line counter
    continuePrint:
        add esi, TYPE array ; Move to next element in array
        loop printLoop ; Repeat for array_size times
        call Crlf ; Move to next line after printing list
        ret 4 ; Clean up the stack and return, assuming title parameter takes 4 bytes
displayList ENDP

goAgain PROC
    ; Retrieve parameters from the stack
    mov eax, [esp + 4] ; Get response pointer
    ; Prompt user to go again or quit
    mov edx, eax
    call WriteString
    call ReadInt
    cmp eax, 1 ; Check if user wants to go again
    jne exitProgram ; If not, exit program
    ret 4 ; Clean up the stack and return, assuming response parameter takes 4 bytes
    exitProgram:
        ret 4 ; Clean up the stack and return, assuming response parameter takes 4 bytes
goAgain ENDP

END main