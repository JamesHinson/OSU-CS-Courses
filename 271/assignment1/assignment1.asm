TITLE Assignment1     (assignment1.asm)

; Author(s): James Hinson
; Course Number: CS 271, Section 001
; Date: 1/24/2024
; Description:  The first assignment for CS 271 - Computer Architecture and Assembly Language.
;               Calculates the area, perimeter, and number of wooden rails in linear feet needed
;               to fence a pasture of a size given by the user. Also contains integer input
;               validation for extra credit on the length, width, and linear feet inputs.


INCLUDE Irvine32.inc

; (insert constant definitions here)

.data

    ; (insert variable definitions here)

    authorInfo  BYTE        "Assignment 1: Fencing a Pasture by James Hinson", 0
    exCredit    BYTE        "***This assignment incorporates input ranges & validation for extra credit***", 0
    userName    BYTE        50 DUP(0)
    intro1      BYTE        'This program finds the area, perimeter, and number of possible rails ', 0
    intro2      BYTE        "that can be used to make a fence around a pasture of a given length.", 0
    promptName  BYTE        "What is your name? Press enter when done : ", 0
    promptLen   BYTE        "Enter the length of your pasture (in feet, from 1 to 1000) : ", 0
    promptWid   BYTE        "Enter the width of your pasture (in feet, from 1 to 1000) : ", 0
    promptPlank BYTE        "Enter the linear feet of wood planks available (from 1 to 500,000) : ", 0
    areaOutput  BYTE        "The area of the pasture is : ", 0
    permOutput  BYTE        "The perimeter of the pasture is : ", 0
    plankOut1   BYTE        "You have enough wood for ", 0
    plankOut2   BYTE        " rails and an extra ", 0
    plankOut3   BYTE        ' linear feet of 1x6" planks', 0
    loopPrompt  BYTE        "Would you like to do another calculation? (0=NO 1=YES) : ", 0
    goodBye1    BYTE        "Goodbye ", 0
    goodBye2    BYTE        '!', 0

    inputLoop   DWORD       ?
    inputLength DWORD       ?
    inputWidth  DWORD       ?
    inputPlank  DWORD       ?
    area        DWORD       ?
    perimeter   DWORD       ?
    numRails    DWORD       ?
    remainder   DWORD       ?


.code

    ; Ask for and save pasture length with integer input validation
    lengthPrompt PROC

        call    Crlf
        mov     edx, OFFSET promptLen
        call    WriteString
        call    ReadInt
        cmp     eax, 1          ; Check if length is at least 1
        jl      lengthPrompt    ; If not, prompt again
        cmp     eax, 1000       ; Check if length is at most 1000
        jg      lengthPrompt    ; If not, prompt again
        mov     inputLength, eax
        call    Crlf
        ret

    lengthPrompt ENDP


    ; Ask for and save pasture width with integer input validation
    widthPrompt PROC

        mov     edx, OFFSET promptWid
        call    WriteString
        call    ReadInt
        cmp     eax, 1         ; Check if length is at least 1
        jl      widthPrompt    ; If not, prompt again
        cmp     eax, 1000      ; Check if length is at most 1000
        jg      widthPrompt    ; If not, prompt again
        mov     inputWidth, eax
        call    Crlf
        ret

    widthPrompt ENDP


    ; Ask for and save linear feet with integer input validation
    plankPrompt PROC

        mov     edx, OFFSET promptPlank
        call    WriteString
        call    ReadInt
        cmp     eax, 1          ; Check if linear feet is at least 1
        jl      plankPrompt     ; If not, prompt again
        cmp     eax, 500000     ; Check if linear feet is at most 500,000
        jg      plankPrompt     ; If not, prompt again
        mov     inputPlank, eax
        call    Crlf
        ret

    plankPrompt ENDP


    main PROC

        ; (insert executable instructions here)

        ; 1: Introduce the program:
        ;       Author information
        ;       Extra credit notification
        ;       Introduction/description paragraph

        call    Crlf
        mov     edx, OFFSET authorInfo
        call    WriteString
        call    Crlf
        call    Crlf
        mov     edx, OFFSET exCredit
        call    WriteString
        call    Crlf
        call    Crlf
        mov     edx, OFFSET intro1
        call    WriteString
        mov     edx, OFFSET intro2
        call    WriteString
        call    Crlf


        ; 2: Ask for and save user's name
        mov     edx, OFFSET promptName
        call    WriteString
        mov     edx, OFFSET userName
        mov     ecx, 50
        call    ReadString

        ; Jump to loopStart to save the user from repeatedly
        ; seeing the introduction and entering their name
        jmp     loopStart

        loopStart:

            ; 3.1: Ask for and save pasture length
            call    lengthPrompt
            
            ; 3.2: Ask for and save pasture width
            call    widthPrompt

            ; 3.3: Ask for and save the linear feet of available planks
            call    plankPrompt
            

            ; 4.1: Calculate the area
            mov     eax, inputLength
            mul     inputWidth      ; Multiply eax (inputLength) by inputWidth
            mov     area, eax       ; Store the result in the area variable

            ; 4.2: Calculate the perimeter
            mov     eax, inputLength
            add     eax, inputWidth ; Add eax (inputLength) and inputWidth
            mov     ebx, 2          ; Set the multiplier to 2
            mul     ebx             ; Multiply the sum by 2 to get perimeter
            mov     perimeter, eax

            ; 4.3: Calculate the number of rails
            mov     eax, inputPlank
            mov     ebx, perimeter
            div     ebx            ; Divide eax (promptPlank) by ebx (perimeter)
            mov     numRails, eax  ; Store the number of rails in numRails
            mov     remainder, edx ; Store the remainder of planks in remainder


            ; 5.1: Display the area
            mov     edx, OFFSET areaOutput
            call    WriteString
            mov     eax, area
            call    WriteInt
            call    Crlf

            ; 5.2: Display the perimeter
            mov     edx, OFFSET permOutput
            call    WriteString
            mov     eax, perimeter
            call    WriteInt
            call    Crlf

            ; 5.3: Display the number of rails
            mov     edx, OFFSET plankOut1
            call    WriteString
            mov     eax, numRails
            call    WriteInt
            mov     edx, OFFSET plankOut2
            call    WriteString

            ; 5.4: Display the amount of extra planks
            mov     eax, remainder
            call    WriteInt
            mov     edx, OFFSET plankOut3
            call    WriteString
            call    Crlf
            call    Crlf


        ; 6.1: Ask if user wants to do another calculation
        mov     edx, OFFSET loopPrompt
        call    WriteString
        call    ReadInt
        mov     inputLoop, eax

        ; 6.2: Loop (jump back to loopStart) if user wants to do another calculation
        cmp     inputLoop, 1
        je      loopStart

        ; 6.3: Say goodbye to the user if not looping
        call    Crlf
        mov     edx, OFFSET goodBye1
        call    WriteString
        mov     edx, OFFSET userName
        call    WriteString
        mov     edx, OFFSET goodBye2
        call    WriteString

        ; exit to operating system
        exit

    main ENDP

; (insert additional procedures here

END main
