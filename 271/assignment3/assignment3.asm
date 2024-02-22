TITLE Assignment 3     (assignment3.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 2/21/2024
; Description:

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
    loopPrompt      BYTE    "Would you like to go again (Yes=1/No=0): ", 0
    goodBye         BYTE    "Goodbye!", 0

    inputNum        DWORD   ?
    value           DWORD   4
    loopCounter     DWORD   0
    displayCounter  DWORD   0
    divisorCount    DWORD   0
    currentDivisor  DWORD   1
    remainder       DWORD   0

.code
    ; Introduction procedure
    introduction PROC
        ; Print title and introductory messages
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    Crlf
        call    Crlf
        mov     edx, OFFSET intro1
        call    WriteString
        mov     edx, OFFSET intro2
        call    WriteString
        call    Crlf
        ret

    introduction ENDP


    ; Get user input procedure
    getUserData PROC
        mov     edx, OFFSET inputPrompt
        call    WriteString
        call    ReadInt
        mov     inputNum, eax
        mov     eax, inputNum
        call    validate
        ret

    getUserData ENDP


    ; Validate user input procedure
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
            call    getUserData
        valid:
            ret

    validate ENDP


    ; Show composite numbers procedure
    showComposites PROC
        ; Loop to check and display composite numbers
        checkValues:
            ; Call the isComposite function to check if the current value is composite
            call    isComposite

            ; Compare the result with 2
            cmp     eax, 2
            jle     notComposite     ; If less than or equal to 2, not composite

            ; Display the composite number
            mov     eax, value
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
            ; Increment value and check loop condition
            inc     value
            mov     eax, inputNum
            cmp     eax, loopCounter   ; Compare input and loopCounter
            jg      checkValues        ; If greater, continue checking
        ret

    showComposites ENDP


    ; Check if a number is composite
    isComposite PROC
        check:
            mov     eax, value
            cdq
            mov     ebx, currentDivisor
            div     ebx
            mov     remainder, edx
            mov     eax, remainder
            cmp     eax, 0
            jg      continueCheck   ; Continue if there's no divisor
            inc     divisorCount    ; Increment divisor count if divisor is found

        continueCheck:
            mov     eax, value
            cmp     eax, currentDivisor
            je      finish              ; If divisor equals value, finish checking
            inc     currentDivisor      ; Otherwise, increment current divisor
            jmp     check               ; Jump back to check for more divisors

        finish:
            mov     eax, divisorCount   ; Move divisor count to eax
        ret

    isComposite ENDP


    isLooping PROC
        call    Crlf
        mov     edx, OFFSET loopPrompt
        call    WriteString

        call    ReadInt
        cmp     eax, 1          ; Check if user wants to go again
        je      restartProgram  ; If yes, jump to restartProgram
        ret                     ; If no, return

        restartProgram:
            ; Clear screen and restart the program
            call    Clrscr
            call    main            ; Jump to the beginning of the program
            ret

    isLooping ENDP


    ; Farewell message
    farewell PROC
        call    Crlf
        mov     edx, OFFSET goodBye
        call    WriteString
        call    Crlf
        ret

    farewell ENDP


    main PROC
        call    Clrscr
        call    introduction
        call    getUserData
        call    showComposites
        call    isLooping
        call    farewell

        exit    ; Exit to operating system
    main ENDP

END main