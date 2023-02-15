input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showString("Vse nej Domi!!!")
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        # . # # #
        # . . . #
        # . . # #
        # . . . #
        # . # # #
        `)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
    basic.showLeds(`
        # . # # #
        # . . . #
        # . . # #
        # . . . #
        # . # # #
        `)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
    basic.showLeds(`
        # . # # #
        # . . . #
        # . . # #
        # . . . #
        # . # # #
        `)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
    basic.showLeds(`
        # . # # #
        # . . . #
        # . . # #
        # . . . #
        # . # # #
        `)
})
music.playMelody("C C D C F E - - ", 120)
music.playMelody("C C D C G F - - ", 120)
music.playMelody("C C C A F E D - ", 120)
music.playMelody("B B A F G F - - ", 120)
