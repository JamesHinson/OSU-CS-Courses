TITLE Assignment 2     (assignment2.asm)

; Author(s): James Hinson
; Course / Project ID: CS 271 - Section 001
; Date: 2/1/2024
; Description: This program calculates and displays the factors of numbers from the
;              lower bound to the upper bound. It also indicates when a number is prime.

INCLUDE Irvine32.inc


UPPER_LIMIT = 1000  ; Constant for the upper limit


.data

    authorInfo  BYTE        "Assignment 2: Finding Prime Numbers by James Hinson", 0
    exCredit    BYTE        "***This assignment prints all prime numbers & perfect squares for extra credit***", 0
    userName    BYTE        50 DUP(0)
    intro1      BYTE        'This program finds all prime numbers in a range set by the user, ', 0
    intro2      BYTE        " from 1 to 1000. It also informs the user when a perfect square has been found.", 0
    promptName  BYTE        "What is your name? Press enter when done : ", 0
    isPrime     BYTE        "** Prime Number **", 0
    notPrime    BYTE        "Not Prime", 0
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

    main PROC

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


        mov     edx, OFFSET loPrompt
        call    WriteString
        call    ReadInt
        mov     lowerBound, eax
        mov     edx, OFFSET hiPrompt
        call    WriteString
        call    ReadInt
        mov     upperBound, eax

        ; Validate input
        cmp     lowerBound, 1
        jl      inputError
        cmp     upperBound, 1000
        jg      inputError
        jmp     calculateFactors


    inputError:

        ; Display error message and re-prompt
        mov     edx, OFFSET invalidMsg
        call    WriteString
        jmp     main


    calculateFactors:

        ; Loop through the range of numbers
        mov     ecx, lowerBound


    calculateLoop:

        ; Display the current number
        mov     eax, ecx
        call    WriteDec

        ; Calculate factors
        mov     ebx, 2
        mov     edx, 0
        div     ebx
        cmp     edx, 0
        je      notPrimeLabel

        ; Check if it's prime
        mov     edx, OFFSET isPrime
        jmp     displayPrime


    notPrimeLabel:

        mov     edx, OFFSET notPrime


    displayPrime:

        ; Display whether the number is prime or not
        call    WriteString
        call    Crlf

        ; Extra Credit: Keep track of prime numbers
        cmp     edx, OFFSET isPrime
        je      trackPrime

        ; Extra Credit: Check for perfect square
        mov     eax, ecx
        mov     edx, OFFSET perfSquare
        call    CheckPerfectSquare


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
        cmp     ebx, UPPER_LIMIT
        jl      displayLoop

        ret

    DisplayPrimeNums ENDP



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

        mov     edx, OFFSET perfSquare
        ret


    notPerfectSquare:

        ret

    CheckPerfectSquare ENDP


    main ENDP

END main
