TITLE Assignment 4     (assignment4.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 3/4/2024
; Description: This program generates a random array of integers given lower & upper bounds,
;              taken as input by the user. The array length is also based on user input.


INCLUDE Irvine32.inc

MIN = 10
MAX = 200

.data
    authorInfo      BYTE    "Assignment 4: Sorting Random Integers by James Hinson", 0
    intro1          BYTE    "This program generates random numbers in the range 100-999.", 0
    intro2          BYTE    "It displays the unsorted list, calculates the median value,", 0
    intro3          BYTE    "and then sorts & displays the list in descending order.", 0
    inputPrompt     BYTE    "How many numbers should be generated? (10 - 200): ", 0
    inputLoPrompt   BYTE    "Enter lower bound (lo): ", 0
    inputHiPrompt   BYTE    "Enter upper bound (hi): ", 0
    arrayError      BYTE    "Upper bound must be >= lower bound. Please try again.", 0 
    rangeError      BYTE    "Please enter a number within the range provided."
    unsortedOutput  BYTE    "The unsorted random numbers: ", 0
    medianOutput    BYTE    "The median is ", 0
    sortedOutput    BYTE    "The sorted list: ", 0
    padding         BYTE    "   ", 0

    randomArray     DWORD   MAX DUP(?) ; The array can't be bigger than max
    arraySize       DWORD   ? ; Number of random numbers to generate
    lo              DWORD   ? ; Replaced with user input
    hi              DWORD   ? ; Replaced with user input
    totalPrinted    DWORD   0

.code

    ; Procedure: intro
    ; Description: Display author information and program description
    ; Inputs: None
    ; Outputs: None
    ; Registers modified: edx

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


    ; Procedure: getData
    ; Description: Obtains user input for the size of an array, validates it, and prompts for lower and upper bounds.
    ; Inputs: 
    ;   - [ebp+12]: Address of the string prompt for the array size
    ;   - [ebp+8]: Address of the variable storing the array size
    ; Outputs: None
    ; Registers modified: eax, ebx, edx, ebp, esp

    getData PROC
        push    ebp
        mov     ebp, esp

        mov     edx, [ebp+12]
        call    WriteString
        call    ReadInt
        mov     arraySize, eax
        call    validate
        mov     ebx, [ebp+8]    ; Address of arraySize moved into ebx
        mov     [ebx], eax      ; Data stored in a global variable

        ; Prompt for lower bound
        mov     edx, OFFSET inputLoPrompt
        call    WriteString
        call    ReadInt
        mov     lo, eax         ; Save lower bound

        ; Prompt for upper bound
        mov     edx, OFFSET inputHiPrompt
        call    WriteString
        call    ReadInt
        mov     hi, eax         ; Save upper bound
        
        pop     ebp
        ret     8

    getData ENDP


    ; Procedure: validate
    ; Description: Validates if the array size is within the specified range.
    ; Inputs: 
    ;   - arraySize: The size of the array to be validated
    ; Outputs: None
    ; Registers modified: ebx, edx

    validate PROC
        mov     ebx, arraySize
        cmp     ebx, MAX
        jg      outOfRange  ; Print rangeError and prompt again if input too big
        cmp     ebx, MIN
        jl      outOfRange  ; Print rangeError and prompt again if input too small
        ret

        outOfRange: ; Print rangeError and execute input loop again
            mov     edx, OFFSET rangeError
            call    WriteString
            call    CrLf
            call    getData

    validate ENDP


    ; Procedure: fillArray
    ; Description: Fills an array with random numbers within a specified range.
    ; Inputs:
    ;   - arraySize: The size of the array to be filled
    ;   - randomArray: The address of the array to be filled
    ;   - lo: The lower bound of the range for random numbers
    ;   - hi: The upper bound of the range for random numbers
    ; Outputs: None
    ; Registers modified: eax, ecx, esi, ebp

    fillArray PROC
        push    ebp
        mov     ebp, esp

        mov     ecx, [ebp+8]    ; Set the loop counter to arraySize
        mov     esi, [ebp+12]   ; Move address of randomArray to esi

        addNum:
            mov     eax, hi
            sub     eax, lo
            inc     eax
            call    RandomRange
            add     eax, lo
            mov     [esi], eax
            add     esi, 4
            loop    addNum
        pop     ebp
        ret     8

    fillArray ENDP


    ; Procedure: sortList
    ; Description: Sorts an array
    ; Inputs:
    ;   - arraySize: The size of the array to be sorted
    ;   - randomArray: The address of the array to be sorted
    ; Outputs: None
    ; Registers modified: eax, ecx, esi, ebp

    sortList PROC
        push    ebp
        mov     ebp, esp

        mov     ecx, [ebp+8]
        dec     ecx

        outerLoop:
            push    ecx
            mov     esi, [ebp+12]   ; Address of randomArray

        innerLoop:
            mov     eax, [esi]
            cmp     [esi+4], eax        
            jl      noSwap          ; Don't swap if unnecesarry
            xchg    eax, [esi+4]    ; Swap if the next value is greater than the current
            mov     [esi], eax

        noSwap:
            add     esi, 4          ; Check the next element
            loop    innerLoop

            pop     ecx
            loop    outerLoop
            pop     ebp
            ret     8

    sortList ENDP


    ; Procedure: displayMedian
    ; Description: Calculates and displays the median of an array of integers.
    ; Inputs:
    ;   - arraySize: The number of elements in the array
    ;   - randomArray: The address of the array containing the numbers
    ; Outputs: None
    ; Registers modified: eax, ebx, edx, esi, ebp, esp

    displayMedian PROC
        call    CrLf
        push    ebp
        mov     ebp, esp

        mov     edx, [ebp+16]   ; Print median string
        call    WriteString
        mov     edx, 0
        mov     eax, [ebp+8]    ; Value of arraySize
        mov     ebx, 2
        div     ebx             ; Divide arraySize by 2
        cmp     edx, 0
        jne     oddNum
        
        ; Calculate median if number of elements is even in an array
        dec     eax                     ; Decrementing so that 0-indexing is correct
        mov     ebx, 4                  ; Byte size of a DWORD
        mul     ebx
        mov     esi, [ebp+12]           ; The address of the array
        add     esi, eax                ; Add eax to get the address of the primary middle element
        mov     ebx, [esi]
        sub     esp, 20                 ; Reserve space for local variables
        mov     DWORD PTR[ebp-4], ebx   ; [ebp-4] is the primary middle element in a local variable
        add     esi, 4                  ; Point to the address of the second middle element
        mov     ebx, [esi]              ; Move the secondary middle element value into ebx
        mov     DWORD PTR[ebp-8], ebx   ; [ebp-8] is the secondary middle element in a local variable
        mov     edx, 0
        mov     eax, [ebp-4]
        add     eax, [ebp-8]            ; Add the two middle elements togeher
        mov     ebx, 2                  ; Calculate average
        div     ebx
        add     eax, edx                ; Round up if needed
        mov     [ebp-12], eax           ; ebp-12 is the quotient (average)
        mov     [ebp-16], edx           ; Remainder
        jmp     printMedian

        ; If the number of elements in an array is odd, then the median is the middle number
        oddNum:
            mov     ebx, 4              ; Byte size of a DWORD
            mul     ebx
            mov     esi, [ebp+12]       ; The address of the array
            add     esi, eax            ; Point to the middle element
            mov     eax, [esi]      

        printMedian:
            call    WriteDec
            call    CrLf
            mov     esp, ebp            ; Remove local variables from the stack
            pop     ebp
            ret     8

    displayMedian ENDP


    ; Procedure: displayList
    ; Description: Displays the elements of an array in a formatted list.
    ; Inputs:
    ;   - arraySize: The number of elements in the array
    ;   - randomArray: The address of the array containing the numbers
    ;   - totalPrinted: The total number of values that have been printed (starts at 0)
    ; Outputs: None
    ; Registers modified: eax, ebx, edx, esi, ecx, ebp

    displayList PROC
        call    CrLf
        push    ebp
        mov     ebp, esp

        mov     edx, [ebp+16]           ; Address of the array name (either unsorted or sorted)
        call    WriteString
        call    CrLf
        mov     ebx, 10                 ; Set the number of columns print in ebx
        mov     esi, [ebp+12]           ; The address of randomArray
        mov     ecx, [ebp+8]            ; arraySize is loop counter in ecx

        printNum:
            mov     eax, [esi]          ; Get the current element in the array
            call    WriteDec
            mov     edx, [ebp+20]       ; Print padding
            call    WriteString
            inc     totalPrinted        ; Keep track of the numbers printed so far in totalPrinted
            mov     edx, 0
            mov     eax, 0 ; Clear eax
            mov     eax, totalPrinted

        ; Check if a newline is needed
        div     ebx                     ; Divide the numbers printed so far by ten
        cmp     edx, 0                  ; If the remainder is zero, a new line is needed
        jne     noNewLine               ; If there aren't ten columns yet, don't print a new line
        call    CrLf                    ; Otherwise, print a new line

        noNewLine:
            add     esi, 4              ; Get the next element in the array
            loop    printNum
            call    CrLf

        pop     ebp
        ret     16

    displayList ENDP


    ; Procedure: main
    ; Description: Entry point of the program. Performs the following tasks:
    ;   1. Clears the screen
    ;   2. Initializes random number generation
    ;   3. Displays program introduction
    ;   4. Gets the array size, lower bound, and upper bound from the user
    ;   5. Populates the randomized array
    ;   6. Prints the unsorted list
    ;   7. Sorts the list
    ;   8. Calculates and prints the median
    ;   9. Prints the sorted list
    ;   10. Exits the program
    ; Inputs: None
    ; Outputs: None
    ; Registers modified: esp

    main PROC
        call    Clrscr
        call    Randomize

        call    intro

        ; Get the array size, lower bound, and upper bound from the user
        push    OFFSET inputPrompt
        push    OFFSET arraySize
        call    getData

        ; Populate the randomized array
        push    OFFSET randomArray
        push    arraySize
        call    fillArray

        ; Print the unsorted list
        push    OFFSET padding
        push    OFFSET unsortedOutput
        push    OFFSET randomArray  
        push    arraySize
        call    displayList

        ; Sort the list
        push    OFFSET randomArray
        push    arraySize
        call    sortList

        ; Calculate and print the median
        push    OFFSET medianOutput
        push    OFFSET randomArray
        push    arraySize
        call    displayMedian

        ; Print the sorted list
        push    OFFSET padding
        push    OFFSET sortedOutput
        push    OFFSET randomArray
        push    arraySize
        call    displayList

        exit

    main ENDP

END main