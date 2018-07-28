all: game.gb

SRC:=$(wildcard src/*.asm)
OBJ:=$(SRC:asm=o)

%.o: %.asm
	rgbasm -iinc/ -o $*.o $*.asm

game.gb: $(OBJ)
	rgblink -n game.sym -m game.map -o $@ $(OBJ)
	rgbfix -jv -k XX -l 0x33 -m 0x01 -p 0 -r 0 -t GAMESCOM $@

clean:
	rm -f game.gb game.sym game.map $(OBJ)
