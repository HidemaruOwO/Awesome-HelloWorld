import ctypes
import platform

if platform.system() == 'Windows':
    write_call = ctypes.cdll.msvcrt._write
else:
    libc = ctypes.CDLL('libc.so')
    write_call = libc.write

message = b'Hello World!\n'

write_call(1, message, len(message))
