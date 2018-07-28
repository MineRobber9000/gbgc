INCLUDE "gbhw.inc"
SECTION "Serial stuffs",ROM0[$0250]
SendByte::
	ld [rSB],a
	ld a,$81 ; (0bSXXXXXXM (S=Start transfer, M=master)
	ld [rSC],a
.loop	ld a,[rSC]
	bit 7,a
	jr z,.loop
	ld a,[rSB]
	cp $ff
	ret ; if z flag is set, $FF was recieved.

