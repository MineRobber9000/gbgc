INCLUDE "ibmpc1.inc"
SECTION "Font stuff",ROMX[$4000]
LoadFullFont::
	ld hl,FontData1
	ld de,$8000
	ld bc,(FontDataEnd-FontData1)
	jp MemCopy
LoadFont::
	push hl
	pop de
	ld hl,FontDataPointers
	ld c,a
	ld b,$00
	add hl,bc
	add hl,bc
	ld bc,(FontData2-FontData1)
	jp MemCopy

FontDataPointers::
	dw FontData1
	dw FontData2
	dw FontData3
	dw FontData4
	dw FontData5
	dw FontData6
	dw FontData7
	dw FontData8
FontData1::
	chr_IBMPC1 1,1
FontData2::
	chr_IBMPC1 2,2
FontData3::
	chr_IBMPC1 3,3
FontData4::
	chr_IBMPC1 4,4
FontData5::
	chr_IBMPC1 5,5
FontData6::
	chr_IBMPC1 6,6
FontData7::
	chr_IBMPC1 7,7
FontData8::
	chr_IBMPC1 8,8
FontDataEnd::
