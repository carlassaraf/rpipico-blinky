NAME    = asm-blink
CPU     = cortex-m0plus
ARMGNU  = arm-none-eabi
AFLAGS  = --warn --fatal-warnings -mcpu=$(CPU) -g
LDFLAGS = -nostdlib
PICOSDK = ${PICO_SDK_PATH}
BUILD_DIR = build

all: ${BUILD_DIR}/$(NAME).bin

${BUILD_DIR}/$(NAME).o: $(NAME).s
	mkdir ${BUILD_DIR}
	$(ARMGNU)-as $(AFLAGS) $(NAME).s -o ${BUILD_DIR}/$(NAME).o

${BUILD_DIR}/$(NAME).bin: boot_stage.ld $(NAME).s ${BUILD_DIR}/$(NAME).o
	$(ARMGNU)-ld $(LDFLAGS) --entry 0x20040001 -T boot_stage.ld ${BUILD_DIR}/$(NAME).o -o ${BUILD_DIR}/$(NAME).elf
	$(ARMGNU)-objdump -D ${BUILD_DIR}/$(NAME).elf > ${BUILD_DIR}/$(NAME).list
	$(ARMGNU)-objcopy -O binary ${BUILD_DIR}/$(NAME).elf ${BUILD_DIR}/$(NAME).bin
	$(PICOSDK)/tools/elf2uf2/elf2uf2 ${BUILD_DIR}/$(NAME).elf ${BUILD_DIR}/$(NAME).uf2

clean:
	rm -rf ${BUILD_DIR}
