TARGET = helloasm
OBJS = helloasm.o

.PHONY: all
all: $(TARGET)

$(TARGET): $(OBJS) Makefile
	ld.lld $(LDFLAGS) -o $@ $(OBJS)

%.o: %.asm Makefile
	nasm -f elf64 -o $@ $<
