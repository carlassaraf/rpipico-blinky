;@ Copyright (c) 2023 CarlosFTM
;@ Modificaciones por Fabrizio Carlassara

	.cpu cortex-m0plus
	.thumb

;@ Tabla de vectores
	.section .vectors, "ax"
	.align 2
	.global _vectors

_vectors:
	.word 0x20001000
	.word _reset

;@ Reset handler, el programa viene aca
	.thumb_func
	.global _reset

_reset:
	ldr r0, =0x20001000     ;@ Stack Pointer (SRAM) ultimos 0x1000 words
	mov sp, r0              ;@ Copio r0 al stack pointer

	ldr  r3, =0x4000f000    ;@ Apunto al Resets.reset (Atomic bitmask clear)
	movs r2, #32            ;@ Bit que referencia el IO_BANK0
	str  r2, [r3, #0]       ;@ Reseteo el periferico

	ldr  r3, =0x400140cc    ;@ Apunto a IO_BANK0.GPIO25_CTRL
	movs r2, #5             ;@ Function 5 (SIO)
	str  r2, [r3, #0]       ;@ Cargo la funcion SIO para el GPIO25

	ldr  r3, =0xd0000020    ;@ Apunto al SIO_BASE.GPIO_OE
	movs r2, #1             ;@ Bit 0
	lsl  r2, r2, #25        ;@ Lo corro 25 lugares para apuntar al GPIO25
	str  r2, [r3, #0]       ;@ Habilito GPIO25 como salida

_blink:
	ldr  r3, =0xd000001c    ;@ Apunto al SIO_BASE.GPIO_XOR
	movs r2, #1             ;@ Bit 0
	lsl  r2, r2, #25        ;@ Lo corro 25 lugares para apuntar al GPIO25
	str  r2, [r3, #0]       ;@ Conmuto el valor del GPIO25

	ldr r0, =831250         ;@ Cargo numero para decrementar
	bl _delay               ;@ Salto al _delay

	b _blink                ;@ Vuelvo a _blink


;@ Funcion de delay

.thumb_func

_delay:
	mov r4, r0      ;@ Copio el valor de r0 en r4 [1]

_loop:
	sub r4, r4, #1  ;@ Decremento r4 [1]
	cmp r4, #0      ;@ Comparo con 0 [1]
	bne _loop       ;@ Si aun no llego a cero, vuelvo a _loop [2]
	bx lr           ;@ Sino, vuelvo a donde indique el LR [2]

.align 4
