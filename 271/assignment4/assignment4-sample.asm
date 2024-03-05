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
;
;   Access lo and hi by value (directly) to have something to submit, and don't validate input?
;   (Access directly during getData and during fillArray, unless you can work it out some other way;
;    the fewer functions that access it by value, the better)



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
    rangeError      BYTE    "Input must be in range, and upper bound must be >= lower bound. Please try again.", 0 
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

    ; Introduce the programmer and program
    ; ***************************************************************
    ; Procedure to introduce the program and display instructions
    ; receives: Introduction, instructions
    ; returns: none
    ; preconditions: none
    ; registers changed: edx
    ; ***************************************************************
    intro PROC
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    CrLf
        call    CrLf
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

    ; ***************************************************************
    ; Get the number of random numbers to generate from the user
    ; receives: Address of the variable arraySize
    ; returns: arraySize
    ; preconditions: none
    ; registers changed: edx, ebx, eax, ebp, esp
    ; ***************************************************************
    getData PROC
        push    ebp
        ; mov     ebp, esp ; comment out when trying to add the below line
        ; mov     edx, [ebp+12] ; comment out when trying to add the below line
        lea     edx, inputPrompt
        call    WriteString
        call    ReadInt
        mov     arraySize, eax
        call    validate
        mov     ebx, [ebp+8] ; address of arraySize into ebx
        mov     [ebx], eax  ; Store in a global variable
        
        ; Prompt for lower bound
        mov     edx, OFFSET inputLoPrompt  
        call    WriteString
        ; Read lower bound
        call    ReadInt              
        mov     eax, [ebp + 8]        ; Load the address of lo into eax
        mov     [eax], eax            ; Store the lower bound at the address pointed to by lo
        
        ; Prompt for upper bound
        mov     edx, OFFSET inputHiPrompt  
        call    WriteString

    validateUpperBound:
        ; Read upper bound
        call    ReadInt              
        cmp     eax, [ebp - 4]        ; Compare with lower bound
        ; ####################################
        ;   CHANGE jmp BACK TO jge WHEN FIXED
        ; ####################################
        jle     upperBoundIsValid     ; Jump if greater than or equal to lower bound
        jmp     invalidUpperBound     ; Jump if less than lower bound

    upperBoundIsValid:
        mov     [ebp], eax            ; Store upper bound on the stack
        jmp     done                  ; Jump to finish

    invalidUpperBound:
        mov     edx, OFFSET rangeError  ; Prompt for upper bound error
        call    WriteString
        call    Crlf
        mov     edx, OFFSET inputHiPrompt  ; Prompt again for upper bound
        call    WriteString
        jmp     validateUpperBound    ; Repeat until valid upper bound is entered

    done:
        mov     esp, ebp              ; Clean up the stack
        pop     ebp                   ; Restore the base pointer
        ret     8                     ; Return, popping arguments off the stack

    getData ENDP

    ; ***************************************************************
    ; Procedure to validate that the user's input is between 10 and 200
    ; receives: Number to Generate
    ; returns: none
    ; preconditions: none
    ; registers changed: ebx, edx
    ; ***************************************************************
    validate PROC
        mov     ebx, arraySize
        cmp     ebx, MAX_ARRAY_SIZE
        jg      outOfRange  ; If the number of iterations is larger than or equal to 401, then print error and prompt again
        cmp     ebx, MIN_ARRAY_SIZE
        jl      outOfRange  ; If the number of iterations is less than or equal to 0, then print error and prompt again
        ret

        outOfRange: ; Print rangeError and execute input loop again
            mov     edx, OFFSET rangeError
            call    WriteString
            call    CrLf
            call    getData

    validate ENDP


    ; ***************************************************************
    ; Fill the array with x many random numbers, where x is arraySize
    ; receives: arraySize, address of the array to populate
    ; returns: Array of random numbers
    ; preconditions: none
    ; registers changed: eax, ebx, ecx, edx, esi, ebp, esp
    ; ***************************************************************
    fillArray PROC
        ; Prologue
        push ebp
        mov ebp, esp

        ; Access parameters from the stack
        mov ecx, [ebp + 12]     ; Counter for loop (array_size)
        mov esi, [ebp + 8]      ; Pointer to array (randomArray)
        mov eax, [ebp + 16]     ; Upper bound (hi)
        sub eax, [ebp + 20]     ; Calculate the range (hi - lo)
        inc eax                 ; Increment to include the upper bound
        mov edx, [ebp + 20]     ; Lower bound (lo)

        ; Body of the procedure
        fillLoop:
            call RandomRange    ; Generate random number
            add eax, edx       ; Adjust random number to range [lo..hi]
            mov [esi], eax     ; Store random number in array
            add esi, 4         ; Move to next element in array (assuming DWORD elements)
            loop fillLoop      ; Repeat for array_size times

        ; Epilogue
        pop ebp
        ret 16                  ; Clean up parameters and return
    fillArray ENDP

    ; ***************************************************************
    ; Procedure to sort the list in descending order
    ; receives: Array of random numbers (randomArr), and arraySize
    ; returns: randomArr, now sorted.
    ; preconditions: Array has been populated
    ; registers changed: eax, ecx, esi, ebp, esp
    ; ***************************************************************
    sortList PROC
        push    ebp
        mov     ebp, esp
        mov     ecx, [ebp+8]            ; arraySize is loop counter in ecx
        dec     ecx
        outerLoop:
            push    ecx
            mov     esi, [ebp+12]           ; address of randomArr
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

    sortList ENDP

    ; ***************************************************************
    ; Calculate and display the median of the unsorted list
    ; receives: Median message, arraySize, randomArr, unsorted
    ; returns: the median of the list
    ; preconditions: none
    ; registers changed: eax, ebx, edx, esi, esp, ebp
    ; ***************************************************************
    displayMedian PROC
        push    ebp
        mov     ebp, esp        ; comment out whe trying to add the below line 
        mov     edx, [ebp + 16] ; comment out when trying to add the below line
        ; mov     edx, inputPrompt
        call    WriteString     ; Print median message
        mov     edx, 0 ; Clear edx
        mov     eax, [ebp + 8]  ; Value of arraySize
        mov     ebx, 2
        div     ebx             ; Divide arraySize by 2
        cmp     edx, 0
        jne     oddNum
        
        ; If the number of elements is even then the median is the average of the middle two numbers
        ; This is where that's calculated
        dec     eax ; So that 0-indexing is correct
        mov     ebx, 4 ; Sizeof DWORD
        mul     ebx
        mov     esi, [ebp + 12]       ; Address of the array
        add     esi, eax              ; Add eax to get address of first middle element
        mov     ebx, [esi]            ; Addres of array again
        sub     esp, 20               ; Reserve space for local variables
        mov     DWORD PTR[ebp-4], ebx ; [ebp-4] is num1
        add     esi, 4                ; Get the address of the next middle element
        mov     ebx, [esi]            ; Move that element value into ebx
        mov     DWORD PTR[ebp-8], ebx ; Move that into local variable num 2
        mov     edx, 0                ; Clear edx
        mov     eax, [ebp-4]
        add     eax, [ebp-8]          ; Add the two middle elements togeher
        mov     ebx, 2                ; Number of elements to divide by for average
        div     ebx
        add     eax, edx              ; If the remainder is 0, leave be, otherwise round up
        mov     [ebp-12], eax         ; ebp-12 is quotient (average)
        mov     [ebp-16], edx         ; Remainder
        jmp     printMedian

        ; If the number of elements is odd, then the median is the middle number
        oddNum:
            mov     ebx, 4        ; Sizeof DWORD
            mul     ebx
            mov     esi, [ebp+12] ; Address of array
            add     esi, eax      ; Get the middle element
            mov     eax, [esi]      

        printMedian:
            call    WriteDec
            call    CrLf
            mov     esp, ebp ; Remove locals from stack
            pop     ebp
            ret     8

    displayMedian ENDP

    ; ***************************************************************
    ; Procedure to print a list of numbers
    ; receives: arraySize (length of the list), 
    ; returns: none
    ; preconditions: none
    ; registers changed: eax, ecx, edx, ebp, esi, ebp, esp
    ; ***************************************************************
    displayList PROC
        call    CrLf
        push    ebp
        mov     ebp, esp
        mov     edx, [ebp + 16]
        call    WriteString             ; address of title (either unsorted or sorted)
        call    CrLf
        mov     ebx, 5                  ; Set number of columns to ebx
        mov     esi, [ebp + 12]         ; address of randomArr
        mov     ecx, [ebp + 8]          ; arraySize is loop counter in ecx
        printNum:
            mov     eax, [esi]          ; get current element in array
            call    WriteDec
            mov     edx, [ebp + 20]     ; print spaces to separate numbers
            call    WriteString
            inc     totalPrinted        ; keep track of numbers printed so far in totalPrinted
            mov     edx, 0
            mov     eax, 0              ; Clear eax
            mov     eax, totalPrinted
                                        ; check if we need to print a newline
            div     ebx                 ; divide numbers printed so far by five
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

        call    intro   ; Print introduction

        ; Get the user input for number of random numbers to generate
        push    OFFSET arraySize    ; Push the variable onto the stack
        call    getData ; Populate arraySize

        ; Fill an array with x many random numbers
        push    arraySize
        push    OFFSET randomArr ; Push array address
        push    lo          ; Push the lower bound
        push    hi          ; Push the upper bound
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

        exit ; Exit
    main ENDP

END main