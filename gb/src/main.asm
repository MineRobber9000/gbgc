INCLUDE "gbhw.inc"
; rst vectors
SECTION "rst00",ROM0[0]
	jp SendByte

SECTION "rst08",ROM0[8]
	ret

SECTION "rst10",ROM0[$10]
	ret

SECTION "rst18",ROM0[$18]
	ret

SECTION "rst20",ROM0[$20]
	ret

SECTION "rst30",ROM0[$30]
	ret

SECTION "rst38",ROM0[$38]
	ret

SECTION "vblank",ROM0[$40]
	jp VBlank
SECTION "lcdc",ROM0[$48]
	reti
SECTION "timer",ROM0[$50]
	reti
SECTION "serial",ROM0[$58]
	reti
SECTION "joypad",ROM0[$60]
	reti

SECTION "bank0",ROM0[$61]

SECTION "romheader",ROM0[$100]
	nop
	jp Start

Section "start",ROM0[$150]

Start::
	di
	cp $11
	jr nz,.notGBC
	ld a,$01
	jr .ok
.notGBC	xor a
.ok	ld [wGBC],a
	call DisableLCD
	ld hl,$8000
	ld bc,$1000
	xor a
	call FillMem
	ld a,[wGBC]
	push af
	ld hl,$c000
	ld bc,$2000
	xor a
	call FillMem
	pop af
	ld [wGBC],a
	call LoadFullFont
	ld a,$00
	rst $00
	jr nz,.good
	ld a,$58
	jr .skip
.good	ld a,$01
.skip	ld [_SCRN0],a
	ld a,LCDCF_ON|LCDCF_BG8000
	ld [rLCDC],a
.loop
	halt
	nop
	jr .loop

VBlank::
	reti

DisableLCD::
	ld a,[rLCDC]
	rlca
	ret nc
.loop	ld a,[rLY]
	cp 145
	jr nz,.loop
	ld a,[rLCDC]
	res 7,a
	ld [rLCDC],a
	ret

FillMem::
	inc b
	inc c
	jr .skip
.loop	ld [hli],a
.skip	dec c
	jr nz,.loop
	dec b
	jr nz,.loop
	ret

MemCopy::
	inc b
	inc c
	jr .skip
.loop	ld a,[hli]
	ld [de],a
	inc de
.skip	dec c
	jr nz,.loop
	dec b
	jr nz,.loop
	ret

