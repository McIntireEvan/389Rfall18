section .text                   ;declare this section to include executable instructions

global my_memset                ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp                ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp            ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, rdx            ;init rcx to rdx (strl)
my_memset_loop:                 ;loop tag
        mov byte [rdi], sil     ;load char into memory position
        add rdi, 1              ;move forward in memory
        loop my_memset_loop     ;loop

        leave                   ;moves down the stack pointer to the current base pointer,
                                ;and restores our saved base pointer, effectively
                                ;restoring our previous stack frame
        ret                     ;jumps to the top value on the stack, hopefully the return address!

global my_strncpy               ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:             
        push rbp                ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp            ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, rdx            ;init rcx to rdx (len)
my_strncpy_loop:                ;loop tag
        mov r8b, byte [rsi]     ;load src char into lower byte of r8
        mov byte [rdi], r8b     ;read lower byte of r8 into dest char
        add rsi, 1              ;move source forward
        add rdi, 1              ;move dest forward
        loop my_strncpy_loop    ;loop


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
