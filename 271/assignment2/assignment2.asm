TITLE Assignment 2     (assignment2.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 2/1/2024
; Description: This program calculates and displays the factors of numbers from the
;              lower bound to the upper bound. It also indicates when a number is prime.

; Note: At some point when hastily adding input validation and other functionality, something broke
;       and I am unable to figure out how to fix it at this moment, and I'm not sure the code will
;       run properly. If you see what the issue might be, I would greatly appreciate it if you could
;       let me know.

INCLUDE Irvine32.inc

.data
    authorInfo  BYTE        "Assignment 2: Finding Prime Numbers by James Hinson", 0
    exCredit    BYTE        "***This assignment prints all prime numbers & perfect squares for extra credit***", 0
    userName    BYTE        50 DUP(0)
    intro1      BYTE        'This program finds all prime numbers in a range set by the user, ', 0
    intro2      BYTE        "from 1 to 1000. It also informs the user when a perfect square has been found.", 0
    promptName  BYTE        "What is your name? Press enter when done: ", 0
    isPrime     BYTE        "  ** Prime Number **", 0
    loPrompt    BYTE        "Enter a number between 1 and 1000 for the lower bound: ", 0
    hiPrompt    BYTE        "Enter a number between 1 and 1000 for the upper bound: ", 0
    invalidMsg  BYTE        "Invalid input. Please enter a number between 1 and 1000.", 0
    perfSquare  BYTE        "[ Perfect Square! ]", 0
    loopPrompt  BYTE        "Would you like to do another calculation? (0=NO 1=YES) : ", 0
    goodBye1    BYTE        "Goodbye, ", 0
    goodBye2    BYTE        '!', 0

    lowerBound  DWORD       ?
    upperBound  DWORD       ?
    primeNums   DWORD       1000 DUP(?)   ; Assuming the range is up to 1000


.code

    CheckPrime PROC
        cmp     eax, 1           ; 1 is not prime
        jbe     IsNotPrime

        mov     ebx, 2           ; Start with divisor 2
        mov     ecx, eax         ; Copy the number to ecx for division

        checkLoop:
            mov     eax, ecx     ; Restore the original number
            div     ebx          ; Divide eax by ebx
            cmp     edx, 0       ; Check if there's a remainder
            je      IsNotPrime   ; If there's no remainder, it's not prime

            inc     ebx          ; Increment divisor
            cmp     ebx, ecx     ; Compare divisor with the original number
            jle     checkLoop    ; If less or equal, continue the loop

        ; If the loop completes, the number is prime
        mov     eax, 1           ; Set eax to 1 to indicate prime
        jmp     Done

        IsNotPrime:
            mov     eax, 0         ; Set eax to 0 to indicate not prime
            call    PrintFactors   ; Print factors if not prime

        Done:
            ret

    CheckPrime ENDP


    PrintFactors PROC
        ; Prints factors of the current number in ecx
        mov     ebx, 1
        mov     edx, OFFSET perfSquare  ; Use edx to check for a perfect square later
        mov     esi, 0  ; Counter for factors

    calculateFactorsLoop:
        ; Calculate factors
        mov     eax, ecx
        div     ebx
        cmp     edx, 0
        je      notFactor

        ; If there is no remainder, ebx is a factor of ecx
        mov     eax, ebx
        call    WriteInt  ; Use WriteInt to print the factor
        inc     esi  ; Increment the factor counter

    notFactor:
        inc     ebx
        cmp     ebx, ecx
        jle     calculateFactorsLoop

        ; Print a new line to separate factors from the next output
        call    Crlf

        ret

    PrintFactors ENDP


    CheckPerfectSquare PROC
        ; Check if a number is a perfect square
        mov     eax, ecx    ; Copy the number to eax
        mov     ebx, 0      ; Initialize the candidate integer square root to 0

        checkLoop:
            mov     edx, ebx    ; Move the candidate integer square root to edx
            imul    edx, ebx    ; Square the value

            cmp     edx, eax            ; Compare the squared value with the original number
            je      isPerfectSquare     ; Jump if equal

            inc     ebx                 ; Increment the candidate
            jmp     checkLoop           ; Repeat the loop

        isPerfectSquare:
            call    displayPerfectText
            ret

        notPerfectSquare:
            ret

    CheckPerfectSquare ENDP

    ; Ask for and save lower bounds with integer input validation
    lowerPrompt PROC

        call    Crlf
        mov     edx, OFFSET loPrompt
        call    WriteString
        call    ReadInt
        cmp     eax, 1         ; Check if input is at least 1
        jl      lowerPrompt    ; If not, prompt again
        cmp     eax, 1000      ; Check if input is at most 1000
        jg      lowerPrompt    ; If not, prompt again
        mov     lowerBound, eax
        call    Crlf
        ret

    lowerPrompt ENDP

    ; Ask for and save upper bounds with integer input validation
    upperPrompt PROC

        mov     edx, OFFSET hiPrompt
        call    WriteString
        call    ReadInt
        cmp     eax, 1         ; Check if input is at least 1
        jl      upperPrompt    ; If not, prompt again
        cmp     eax, 1000      ; Check if input is at most 1000
        jg      upperPrompt    ; If not, prompt again
        mov     upperBound, eax
        call    Crlf
        ret

    upperPrompt ENDP


    main PROC

        ; 1: Introduce the program:
        ;       Author information
        ;       Extra credit notification
        ;       Introduction/description paragraph
        call    Crlf
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
        call    Crlf


        ; Ask for and save user's name
        mov     edx, OFFSET promptName
        call    WriteString
        mov     edx, OFFSET userName
        mov     ecx, 50
        call    ReadString


        ; Get lower and upper bounds
        call    lowerPrompt
        call    Crlf
        call    upperPrompt

        ; Calculate the factors
        jmp     calculateFactors


        calculateFactors:

            ; Loop through the range of numbers
            mov     ecx, lowerBound
            mov     esi, 0  ; Counter for prime numbers


        calculateLoop:

            ; Display the current number
            mov     eax, ecx
            call    WriteDec
            call    WriteString  ; Add this line to print a colon after the number

            ; Calculate and display factors
            mov     ebx, 1
            mov     edx, OFFSET perfSquare  ; Use edx to check for a perfect square later
            mov     esi, 0  ; Counter for factors


        calculateFactorsLoop:

            ; Calculate factors
            mov     eax, ecx
            div     ebx
            cmp     edx, 0
            je      notFactor

            mov     eax, ebx
            call    WriteInt  ; Use WriteInt to print the factor
            inc     esi  ; Increment the factor counter


        notFactor:

            inc     ebx
            cmp     ebx, ecx
            jle     calculateFactorsLoop

            ; Check for prime number
            mov     eax, ecx
            call    CheckPrime
            cmp     eax, 1
            je      displayPrimeText

            ; Check for perfect square
            mov     eax, ecx
            call    CheckPerfectSquare
            cmp     eax, 1
            je      displayPerfectText

            jmp     continueLoop


        displayPrimeText:
            mov     edx, OFFSET isPrime
            call    WriteString
            jmp     continueLoop


        displayPerfectText:
            mov     edx, OFFSET perfSquare
            call    WriteString
            call    Crlf


        continueLoop:

            ; Ask if the user wants to repeat
            mov     edx, OFFSET loopPrompt
            call    WriteString
            call    ReadInt
            cmp     eax, 1
            je      calculateLoop
            jmp     endProgram


        trackPrime:

            ; Extra Credit: Store all prime numbers found
            mov     [primeNums + ecx * 4], ecx

            ; Ask if the user wants to repeat
            mov     edx, OFFSET loopPrompt
            call    WriteString
            call    ReadInt
            cmp     eax, 1
            je      calculateLoop
            jmp     endProgram


        endProgram:

            ; Extra Credit: Display prime numbers
            mov     ecx, OFFSET primeNums
            call    DisplayPrimeNums

            ; Say goodbye to the user if not looping
            call    Crlf
            mov     edx, OFFSET goodBye1
            call    WriteString
            mov     edx, OFFSET userName
            call    WriteString
            mov     edx, OFFSET goodBye2
            call    WriteString

            ; exit to operating system
            exit

        DisplayPrimeNums PROC

            ; Initialize index variables
            mov     ebx, 0
            mov     ecx, 0

            displayLoop:

                ; Display the prime number
                mov     eax, [primeNums + ebx * 4]
                call    WriteDec
                call    Crlf

                ; Move to the next prime number
                inc     ebx
                cmp     ebx, upperBound
                jl      displayLoop

                ret

        DisplayPrimeNums ENDP

    main ENDP

END main