TITLE Assignment 4  (assignment4.asm)
; Lucy Wyman    wymanl@onid.oregonstate.edu
; CS 271 400
; Assignment 4
; Description: Generate a list of x random numbers, where x is a number between 10 and 200 chosen by the user.
; Print the unsorted list, the median of the unsorted list, and the sorted list

INCLUDE Irvine32.inc

STACK_FRAME macro ; A macro for setting up stackframe
    push    ebp
    mov     ebp, esp
ENDM

MIN = 10
MAX = 200
; LO = 100
; Hi = 999

.data
    introduction        BYTE    "Sorting Random Number by Lucy Wyman", 0
    instructions        BYTE    "This program generates random numbers in the range (100, 999), ", \
                                    "displays the original list, sorts the list, and calculates the median value.", \
                                    " Finally, it displays the list sorted in descending order", 10, 13, 0
    prompt              BYTE    "How many numbers should be generated? (10 - 200): ", 10, 13, 0
    error               BYTE    "Oops! Your number is out of range.", 0 
    unsortedMessage     BYTE    "Unsorted random numbers: ",0
    medianMessage       BYTE    "The median is ", 0
    sortedMessage       BYTE    "The sorted list: ", 0
    spaces              BYTE    "   ", 0

    numToGenerate       DWORD   ? ; Number of random numbers to generate
    randomArray         DWORD   MAX DUP(?) ; The array can't be bigger than this, so we just make the largest possible array
    numPrinted          DWORD   0 ; Number printed so far
    lo                  DWORD   100
    hi                  DWORD   999

.code

    ; Introduce the programmer and program
    ; ***************************************************************
    ; Procedure to introduce the program and display instructions
    ; receives: Introduction, instructions
    ; returns: none
    ; preconditions: none
    ; registers changed: edx
    ; ***************************************************************
    intro   PROC
        STACK_FRAME
        mov     edx, [ebp+12]
        call    WriteString
        call    CrLf
        call    CrLf
    ; Print instructions
        mov     edx, [ebp+8]
        call    WriteString
        call    CrLf
        pop     ebp
        ret     8

    intro   ENDP

    ; ***************************************************************
    ; Get the number of random numbers to generate from the user
    ; receives: Address of the variable numToGenerate
    ; returns: numToGenerate
    ; preconditions: none
    ; registers changed: edx, ebx, eax, ebp, esp
    ; ***************************************************************
    getData PROC
        STACK_FRAME
        mov     edx, [ebp+12]
        call    WriteString
        call    ReadInt
        mov     numToGenerate, eax
        call    validate
        mov     ebx, [ebp+8] ; address of numToGenerate into ebx
        mov     [ebx], eax  ; Store in a global variable
        pop     ebp
        ret     8

    getData ENDP

    ; ***************************************************************
    ; Procedure to validate that the user's input is between 10 and 200
    ; receives: Number to Generate
    ; returns: none
    ; preconditions: none
    ; registers changed: ebx, edx
    ; ***************************************************************
    validate    PROC
            mov     ebx, numToGenerate
            cmp     ebx, MAX
            jg      outOfRange  ; If the number of iterations is larger than or equal to 401, then print error and prompt again
            cmp     ebx, MIN
            jl      outOfRange  ; If the number of iterations is less than or equal to 0, then print error and prompt again
            ret

            outOfRange: ; Print error and execute input loop again
                mov     edx, OFFSET error
                call    WriteString
                call    CrLf
                call    getData

    validate    ENDP

    ; ***************************************************************
    ; Fill the array with x many random numbers, where x is numToGenerate
    ; receives: numToGenerate, address of the array to populate
    ; returns: Array of random numbers
    ; preconditions: none
    ; registers changed: eax, ebx, ecx, edx, esi, ebp, esp
    ; ***************************************************************
    fillArray   PROC
        STACK_FRAME
        mov     ecx, [ebp+8] ; Set loop counter to user input number
        mov     esi, [ebp+12] ; Move address of array to esi

        addNum:
            mov     eax, HI
            sub     eax, LO
            inc     eax
            call    RandomRange ; eax is [0, .., 900]
            add     eax, LO ; eax is [100, 999]
            mov     [esi], eax  ; Add it to the list
            add     esi, 4 ; Move to next element
            loop    addNum
        pop     ebp
        ret     8

    fillArray   ENDP

    ; ***************************************************************
    ; Procedure to sort the list in descending order
    ; receives: Array of random numbers (randomArray), and numToGenerate
    ; returns: randomArray, now sorted.
    ; preconditions: Array has been populated
    ; registers changed: eax, ecx, esi, ebp, esp
    ; ***************************************************************
    sortList    PROC
        STACK_FRAME
        mov     ecx, [ebp+8]            ; numToGenerate is loop counter in ecx
        dec     ecx

        outerLoop:
            push    ecx
            mov     esi, [ebp+12]           ; address of randomArray

        innerLoop:
            mov     eax, [esi]
            cmp     [esi+4], eax        
            jl      noSwap                  ; descending order so if next element is less than current element, OK
            xchg    eax, [esi+4]            ; if next element is larger than current element, then swap values
            mov     [esi], eax

        noSwap:
            add     esi, 4                  ; check next element
            loop    innerLoop

            pop     ecx
            loop    outerLoop
            pop     ebp
            ret     8

    sortList    ENDP

    ; ***************************************************************
    ; Calculate and display the median of the unsorted list
    ; receives: Median message, numToGenerate, randomArray, unsorted
    ; returns: the median of the list
    ; preconditions: none
    ; registers changed: eax, ebx, edx, esi, esp, ebp
    ; ***************************************************************
    displayMedian   PROC
        call    CrLf
        STACK_FRAME
        mov     edx, [ebp+16] ; Print median message
        call    WriteString
        mov     edx, 0 ; Clear edx
        mov     eax, [ebp+8] ; Value of numToGenerate
        mov     ebx, 2
        div     ebx     ; Divide numToGenerate by 2
        cmp     edx, 0
        jne     oddNum
        
        ; If the number of elements is even then the median is the average of the middle two numbers
        ; This is where that's calculated
        dec     eax ; So that 0-indexing is correct
        mov     ebx, 4 ; Sizeof DWORD
        mul     ebx
        mov     esi, [ebp+12] ; Address of the array
        add     esi, eax ; Add eax to get address of first middle element
        mov     ebx, [esi]  ; Addres of array again
        sub     esp, 20 ; Reserve space for local variables
        mov     DWORD PTR[ebp-4], ebx ; [ebp-4] is num1
        add     esi, 4      ; Get the address of the next middle element
        mov     ebx, [esi]  ; Move that element value into ebx
        mov     DWORD PTR[ebp-8], ebx ; Move that into local variable num 2
        mov     edx, 0  ; Clear edx
        mov     eax, [ebp-4]
        add     eax, [ebp-8]    ; Add the two middle elements togeher
        mov     ebx, 2      ; Number of elements to divide by for average
        div     ebx
        add     eax, edx        ; If the remainder is 0, leave be, otherwise round up
        mov     [ebp-12], eax       ; ebp-12 is quotient (average)
        mov     [ebp-16], edx       ; Remainder
        jmp     printMedian

        ; If the number of elements is odd, then the median is the middle number
        oddNum:
            mov     ebx, 4  ; Sizeof DWORD
            mul     ebx
            mov     esi, [ebp+12] ; Address of array
            add     esi, eax        ; Get the middle element
            mov     eax, [esi]      

        printMedian:
            call    WriteDec
            call    CrLf
            mov     esp, ebp ; Remove locals from stack
            pop     ebp
            ret     8

    displayMedian   ENDP

    ; ***************************************************************
    ; Procedure to print a list of numbers
    ; receives: numToGenerate (length of the list), 
    ; returns: none
    ; preconditions: none
    ; registers changed: eax, ecx, edx, ebp, esi, ebp, esp
    ; ***************************************************************
    displayList PROC
        call    CrLf
        STACK_FRAME
        mov     edx, [ebp+16]       ; address of title (either unsorted or sorted)
        call    WriteString
        call    CrLf
        mov     ebx, 10  ; Set number of columns to ebx
        mov     esi, [ebp+12]       ; address of randomArray
        mov     ecx, [ebp+8]        ; numToGenerate is loop counter in ecx

        printNum:
            mov     eax, [esi]          ; get current element in array
            call    WriteDec
            mov     edx, [ebp+20]   ; print spaces to separate numbers
            call    WriteString
            inc     numPrinted          ; keep track of numbers printed so far in numPrinted
            mov     edx, 0
            mov     eax, 0 ; Clear eax
            mov     eax, numPrinted

        ; check if we need to print a newline
        div     ebx         ; divide numbers printed so far by five
        cmp     edx, 0              ; if remainder is zero, then we need a new line
        jne     noNewLine           ; If there aren't five columns yet, don't print new line
        call    CrLf                ; Otherwise, do.

        noNewLine:
            add     esi, 4              ; Get next element in array
            loop    printNum
            call    CrLf

        pop     ebp
        ret     16

    displayList ENDP

    main PROC
        call    Clrscr ; Clear the screen
        call    Randomize   ; Ensure set of random numbers is unique, based on system clock

        ; Push strings to the stack
        push    OFFSET introduction
        push    OFFSET instructions
        call    intro   ; Print introduction

        ; Get the user input for number of random numbers to generate
        push    OFFSET prompt
        push    OFFSET numToGenerate    ; Push the variable onto the stack
        call    getData ; Populate numToGenerate

        ; Fill an array with x many random numbers
        push    OFFSET randomArray ; Push array address
        push    numToGenerate
        call    fillArray

        ; Print unsorted list
        push    OFFSET spaces
        push    OFFSET unsortedMessage
        push    OFFSET randomArray  
        push    numToGenerate
        call    displayList

        ; Calculate and print median
        push    OFFSET medianMessage
        push    OFFSET randomArray
        push    numToGenerate
        call    displayMedian

        ; Sort the list
        push    OFFSET randomArray
        push    numToGenerate
        call    sortList

        ; Print sorted list
        push    OFFSET spaces
        push    OFFSET sortedMessage
        push    OFFSET randomArray
        push    numToGenerate
        call    displayList

        exit ; Exit

    main ENDP
END main