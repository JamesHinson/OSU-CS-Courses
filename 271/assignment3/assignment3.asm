TITLE Assignment 3     (assignment3.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 2/21/2024
; Description: This program calculates and displays composite numbers from a set lower bound
;              to a user-provided upper bound, looping if the user wants to repeat the program.


INCLUDE Irvine32.inc

; (insert constant definitions here)
UPPER_LIMIT = 400
LOWER_LIMIT = 1

.data
    authorInfo      BYTE    "Assignment 3: Finding Composite Numbers by James Hinson", 0
    intro1          BYTE    "Enter the number of composite numbers you would like to see. ", 0
    intro2          BYTE    "I'll accept orders for up to 400 composites.", 0
    inputPrompt     BYTE    "Enter the number of composites to display [1 .. 400]: ", 0
    outOfRange      BYTE    "Out of range. Try again.", 0
    padding         BYTE    "   ", 0
    loopPrompt      BYTE    "Would you like to go again? (Yes=1/No=0): ", 0
    goodBye         BYTE    "Goodbye!", 0

    inputNum        DWORD   ?
    currentNum      DWORD   4
    currentDivisor  DWORD   1
    loopCounter     DWORD   0
    displayCounter  DWORD   0
    divisorCount    DWORD   0
    remainder       DWORD   0

.code
    
    ; Procedure Name: introduction
    ; Description: Displays introductions for the program and the author.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none
    ; Registers changed: edx

    introduction PROC
        ; Print title and introductory messages
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    Crlf
        call    Crlf
        mov     edx, OFFSET intro1
        call    WriteString
        call    Crlf
        mov     edx, OFFSET intro2
        call    WriteString
        call    Crlf
        call    Crlf
        ret

    introduction ENDP


    ; Procedure Name: getUserData
    ; Description: Gets user input as an integer.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none
    ; Registers changed: eax, edx

    getUserData PROC
        mov     edx, OFFSET inputPrompt
        call    WriteString
        call    ReadInt
        mov     inputNum, eax
        mov     eax, inputNum
        call    validate
        ret

    getUserData ENDP


    ; Procedure Name: validate
    ; Description: Validates user input with upper and lower limits, displaying an
    ;              error if the input isn't within the upper and lower bounds.
    ; Receives: none
    ; Returns: none
    ; Preconditions: User must have entered an integer as input
    ; Registers changed: eax, edx

    validate PROC
        validLoop:
            cmp     eax, LOWER_LIMIT
            jl      invalid
            cmp     eax, UPPER_LIMIT
            jg      invalid
            jmp     valid

        invalid:
            mov     edx, OFFSET outOfRange
            call    WriteString
            call    Crlf
            call    getUserData
        valid:
            ret

    validate ENDP


    ; Procedure Name: showComposites
    ; Description: Displays composite numbers after they are calculated.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none, but calls isComposite on a loop before taking any other actions.
    ; Registers changed: eax, edx

    showComposites PROC
        ; Loop to check and display composite numbers
        checkValues:
            ; Call the isComposite function to check if the current value is composite
            call    isComposite

            ; Compare the result with 2
            cmp     eax, 2
            jle     notComposite

            ; Display the composite number
            mov     eax, currentNum
            call    WriteDec
            inc     loopCounter
            inc     displayCounter

            ; Reset variables
            mov     eax, 0
            mov     divisorCount, eax   ; Reset divisorCount
            mov     eax, 1
            mov     currentDivisor, eax ; Reset currentDivisor
            mov     eax, displayCounter
            cmp     eax, 10             ; Check if 10 composites have been displayed
            jl      display             ; If less than 10, continue
            call    Crlf
            mov     eax, 0              ; Reset displayCounter
            mov     displayCounter, eax

        display:
            ; Print padding spaces between composite numbers
            mov     edx, OFFSET padding
            call    WriteString

        notComposite:
            ; Increment currentNum and check loop condition
            inc     currentNum
            mov     eax, inputNum
            cmp     eax, loopCounter   ; Compare input and loopCounter
            jg      checkValues        ; If greater, continue checking
        ret

    showComposites ENDP


    ; Procedure Name: isComposite
    ; Description: Checks if a number is composite.
    ; Receives: none
    ; Returns: none
    ; Preconditions: User must have entered a valid integer input.
    ; Registers changed: eax, ebx, edx

    isComposite PROC
        check:
            mov     eax, currentNum
            cdq
            mov     ebx, currentDivisor
            div     ebx
            mov     remainder, edx
            mov     eax, remainder
            cmp     eax, 0
            jg      continueCheck   ; Continue if there's no divisor
            inc     divisorCount    ; Increment divisor count if divisor is found

        continueCheck:
            mov     eax, currentNum
            cmp     eax, currentDivisor
            je      finish              ; If currentDivisor equals currentNum, finish checking
            inc     currentDivisor      ; Otherwise, increment current divisor
            jmp     check               ; Jump back to check for more divisors

        finish:
            mov     eax, divisorCount   ; Move divisor count to eax
        ret

    isComposite ENDP


    ; Procedure Name: isLooping
    ; Description: Asks the user if they want to restart the program, calling main if they
    ;              do and returning if they don't. Resets currentNum to 4 to avoid restarting
    ;              the program with the incorrect initial value.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none
    ; Registers changed: eax, edx

    isLooping PROC
        call    Crlf
        mov     edx, OFFSET loopPrompt
        call    WriteString

        call    ReadInt
        cmp     eax, 1          ; Check if user wants to go again
        je      restartProgram  ; If yes, jump to restartProgram
        ret                     ; If no, return

        restartProgram:
            ; Restart the program with default values
            call    Clrscr
            mov     currentNum, 4
            mov     currentDivisor, 1
            mov     loopCounter, 0
            mov     displayCounter, 0
            mov     divisorCount, 0
            mov     remainder, 0

            call    main            ; Jump to the beginning of the program
            ret

    isLooping ENDP


    ; Procedure Name: farewell
    ; Description: Displays a farewell message to the user and returns.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none
    ; Registers changed: edx
    farewell PROC
        call    Crlf
        mov     edx, OFFSET goodBye
        call    WriteString
        call    Crlf
        ret

    farewell ENDP


    ; Procedure Name: main
    ; Description: Main program entry point.
    ; Receives: none
    ; Returns: none
    ; Preconditions: none
    ; Registers changed: none

    main PROC
        call    introduction
        call    getUserData
        call    showComposites
        call    isLooping
        call    farewell

        exit    ; Exit to operating system
    main ENDP

END main