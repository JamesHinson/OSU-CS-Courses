TITLE Assignment 3     (assignment3.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 2/21/2024
; Description:

INCLUDE Irvine32.inc

; (insert constant definitions here)

.data
    authorInfo  BYTE    "Assignment 3: Finding Composite Numbers by James Hinson", 0
    intro1      BYTE    "Enter the number of composite numbers you would like to see.", 0
    intro2      BYTE    "I’ll accept orders for up to 400 composites.", 0
    inputPrompt BYTE    "Enter the number of composites to display [1 .. 400]: ", 0
    outOfRange  BYTE    "Out of range. Try again.", 0
    padding     BYTE    "   ", 0
    loopPrompt  BYTE    "Would you like to go again (Yes=1/No=0): ", 0
    goodBye     BYTE    "Goodbye!",0 

    inputNum    DWORD   ?


.code

    ; 1: Introduce the program:
    ;       Author information
    ;       Introduction/description paragraph
    introduction PROC
        call    Crlf
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    Crlf
        call    Crlf

        mov     edx, OFFSET intro1
        call    WriteString
        mov     edx, OFFSET intro2
        call    WriteString
        call    Crlf

    introduction ENDP

    ; Gets integer input from the user (range 1-400)
    getUserData PROC
        mov     edx, OFFSET inputPrompt
        call    WriteString
        call    ReadInt

        call    validate
        mov     inputNum, eax
        call    Crlf
        ret

    getUserData ENDP

    ; Validates user integer input (range 1-400)
    validate PROC
        cmp     eax, 1          ; Check if input is at least 1
        jl      outBounds       ; If not, prompt again
        cmp     eax, 400        ; Check if input is at most 400
        jg      outBounds       ; If not, prompt again

        outBounds:
            mov     edx, OFFSET outOfRange
            call    WriteString
            call    Crlf
            call    getUserData
            ret

    validate ENDP


    showComposites PROC

    showComposites ENDP


    isComposite PROC

    isComposite ENDP


    looping PROC

    looping ENDP

    ; 7. Say goodbye to the user if not looping

    farewell PROC
        call    Crlf
        mov     edx, OFFSET goodBye1
        call    WriteString
        mov     edx, OFFSET userName
        call    WriteString
        mov     edx, OFFSET goodBye2
        call    WriteString

    farewell ENDP


    main PROC

    ; (insert executable instructions here)

        exit    ; exit to operating system
    main ENDP

    ; (insert additional procedures here)

END main
