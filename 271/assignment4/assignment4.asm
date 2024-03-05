TITLE Assignment 4     (assignment4.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 3/3/2024
; Description:

INCLUDE Irvine32.inc

; TODO:
;   ---Make or modify process to ask for and save lower and upper bounds (remember parameter passing!)---
;   ---Make a process or modify current to validate lower and upper bounds---
;   Use edx instead of [ebx + _] when possible (in getData, etc)
;   Fix all areas indicated (e.g. ; comment out when trying to add the below line)
;   Change all comments, headers, spacing, and any extra names to match your style of coding



; (insert constant definitions here)
MIN_ARRAY_SIZE = 10
MAX_ARRAY_SIZE = 200

.data
    authorInfo      BYTE    "Assignment 4: Sorting Random Integers by James Hinson", 0
    intro1          BYTE    "This program generates random numbers in the range 100-999.", 0
    intro2          BYTE    "It displays the unsorted list, calculates the median value,", 0
    intro3          BYTE    "and then sorts & displays the list in descending order.", 0
    inputPrompt     BYTE    "How many numbers should be generated? (10 - 200): ", 0
    inputLoPrompt   BYTE    "Enter lower bound (lo): ", 0
    inputHiPrompt   BYTE    "Enter upper bound (hi): ", 0
    rangeError      BYTE    "Upper bound must be >= lower bound. Please try again.", 0 
    unsortedOutput  BYTE    "The unsorted random numbers: ", 0
    medianOutput    BYTE    "The median is ", 0
    sortedOutput    BYTE    "The sorted list: ", 0
    padding         BYTE    "   ", 0

    arraySize       DWORD   ?
    lo              DWORD   ?
    hi              DWORD   ?
    randomArr       DWORD   MAX_ARRAY_SIZE DUP(?)
    totalPrinted    DWORD   0

.code

    ; Introduction procedure to display program information
    intro PROC
        ; Display author information
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    CrLf
        call    CrLf

        ; Display program description
        mov     edx, OFFSET intro1
        call    WriteString
        call    CrLf
        mov     edx, OFFSET intro2
        call    WriteString
        call    CrLf
        mov     edx, OFFSET intro3
        call    WriteString
        call    CrLf
        call    CrLf

        ret
    intro ENDP

    getData PROC
        ; Parameters: none
        ; Returns: arraySize, lo, hi
        push    ebp
        mov     ebp, esp

        ; Display prompt to get input
        mov     edx, OFFSET inputPrompt
        call    WriteString
        call    ReadInt
        mov     arraySize, eax            ; Save user input

        ; Prompt for lower bound
        mov     edx, OFFSET inputLoPrompt
        call    WriteString
        call    ReadInt
        mov     lo, eax

        ; Prompt for upper bound
        mov     edx, OFFSET inputHiPrompt
        call    WriteString
        call    ReadInt
        mov     hi, eax

        ; Return values
        mov     eax, arraySize
        mov     ebx, lo
        mov     ecx, hi
        pop     ebp
        ret
    getData ENDP



    ; Procedure to validate input range
    validate PROC
        ; Parameters: arraySize
        ; Returns: none
        cmp     ebx, MAX_ARRAY_SIZE
        jg      outOfRange
        cmp     ebx, MIN_ARRAY_SIZE
        jl      outOfRange
        ret

    outOfRange:
        mov     edx, OFFSET rangeError
        call    WriteString
        call    CrLf
        call    getData
        ret
    validate ENDP

    ; Procedure to fill the array with random numbers
    fillArray PROC
        ; Parameters: arraySize
        ; Returns: randomArr
        push    ebp
        mov     ebp, esp

        ; Parameters: none
        call    Randomize

        ; Parameters: none
        mov     esi, OFFSET randomArr

        ; Parameters: none
        mov     ecx, ebx            ; arraySize is loop counter in ecx

    fillLoop:
        ; Parameters: none
        call    RandomRange         ; Generate random number
        add     eax, lo             ; Adjust random number to range [lo..hi]
        mov     [esi], eax          ; Store random number in array
        add     esi, 4              ; Move to next element in array (assuming DWORD elements)
        loop    fillLoop            ; Repeat for arraySize times

        pop     ebp
        ret
    fillArray ENDP

    ; Procedure to sort the list in descending order
    sortList PROC
        ; Parameters: arraySize
        ; Returns: randomArr
        push    ebp
        mov     ebp, esp

        mov     ecx, ebx            ; arraySize is loop counter in ecx
        dec     ecx

    outerLoop:
        push    ecx
        mov     esi, OFFSET randomArr

    innerLoop:
        mov     eax, [esi]
        cmp     [esi+4], eax        
        jge     noSwap               ; If next element is greater or equal, no need to swap
        xchg    eax, [esi+4]         ; Swap values
        mov     [esi], eax
    noSwap:
        add     esi, 4                ; Move to next element
        loop    innerLoop

        pop     ecx
        loop    outerLoop

        pop     ebp
        ret
    sortList ENDP

    ; Procedure to calculate and display the median of the unsorted list
    displayMedian PROC
        ; Parameters: arraySize
        ; Returns: none
        push    ebp
        mov     ebp, esp

        ; Print median message
        mov     edx, OFFSET medianOutput
        call    WriteString

        ; Calculate median
        mov     eax, ebx            ; arraySize
        mov     ecx, 2
        div     ecx                 ; Divide arraySize by 2

        ; If the number of elements is even
        cmp     edx, 0
        jne     oddNum

        dec     eax                 ; Adjust for 0-indexing
        mov     ecx, 4              ; Sizeof DWORD
        mul     ecx
        mov     esi, OFFSET randomArr   ; Address of the array
        add     esi, eax            ; Address of first middle element
        mov     ebx, [esi]          ; Value of first middle element
        sub     esp, 20             ; Reserve space for local variables
        mov     DWORD PTR [ebp-4], ebx
        add     esi, 4              ; Address of the next middle element
        mov     ebx, [esi]          ; Value of the next middle element
        mov     DWORD PTR [ebp-8], ebx
        mov     edx, 0
        mov     eax, [ebp-4]
        add     eax, [ebp-8]        ; Sum of two middle elements
        mov     ebx, 2              ; Number of elements for average
        div     ebx
        add     eax, edx            ; Round up if necessary
        mov     [ebp-12], eax       ; Quotient (average)
        mov     [ebp-16], edx       ; Remainder
        jmp     printMedian

        ; If the number of elements is odd
    oddNum:
        mov     ecx, 4              ; Sizeof DWORD
        mul     ecx
        mov     esi, OFFSET randomArr   ; Address of array
        add     esi, eax            ; Address of the middle element
        mov     eax, [esi]          ; Value of the middle element

    printMedian:
        call    WriteDec
        call    CrLf

        mov     esp, ebp            ; Remove locals from stack
        pop     ebp
        ret
    displayMedian ENDP

    ; Procedure to print a list of numbers
    displayList PROC
        ; Parameters: arraySize
        ; Returns: none
        push    ebp
        mov     ebp, esp

        call    CrLf

        ; Print title
        mov     edx, [ebp + 16]
        call    WriteString
        call    CrLf

        ; Print numbers
        mov     ebx, 5              ; Number of columns
        mov     esi, OFFSET randomArr   ; Address of randomArr
        mov     ecx, ebx            ; arraySize

    printNum:
        mov     eax, [esi]          ; Get current element in array
        call    WriteDec
        mov     edx, [ebp + 20] ; Print spaces to separate numbers
        call    WriteString
        inc     totalPrinted        ; Keep track of numbers printed so far
        mov     edx, 0
        mov     eax, 0              ; Clear eax
        mov     eax, totalPrinted
        div     ebx                 ; Divide numbers printed so far by five
        cmp     edx, 0              ; If remainder is zero, print a new line
        jne     noNewLine           ; If there aren't five columns yet, don't print new line
        call    CrLf                ; Otherwise, print new line
    noNewLine:
        add     esi, 4              ; Get next element in array
        loop    printNum

        call    CrLf

        pop     ebp
        ret
    displayList ENDP

    main PROC
        ; Clear the screen
        call    Clrscr

        ; Ensure set of random numbers is unique, based on system clock
        call    Randomize

        ; Print introduction
        call    intro

        ; Get the user input for number of random numbers to generate
        call    getData

        ; Fill the array with random numbers
        push    arraySize
        push    OFFSET randomArr
        push    lo
        push    hi
        call    fillArray

        ; Print unsorted list
        push    OFFSET padding
        push    OFFSET unsortedOutput
        push    OFFSET randomArr
        push    arraySize
        call    displayList

        ; Calculate and print median
        push    OFFSET medianOutput
        push    OFFSET randomArr
        push    arraySize
        call    displayMedian

        ; Sort the list
        push    OFFSET randomArr
        push    arraySize
        call    sortList

        ; Print sorted list
        push    OFFSET padding
        push    OFFSET sortedOutput
        push    OFFSET randomArr
        push    arraySize
        call    displayList

        ; Exit
        exit
    main ENDP

END main
