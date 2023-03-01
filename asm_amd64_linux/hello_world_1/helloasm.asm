section .data
    msg db      "Hello, World!", 0x0a

section .text
    global _start
_start:
    ; ssize_t write(int fd, const void *buf, size_t count);
    mov     rax, 1 ; write systemcall
    mov     rdi, 1 ; int fd
    mov     rsi, msg ; const void *buf
    mov     rdx, 14 ; size_t count
    syscall
    ; void exit_group(int status);
    mov    rax, 0xe7 ; exit_group systemcall
    mov    rdi, 0 ; int status
    syscall
