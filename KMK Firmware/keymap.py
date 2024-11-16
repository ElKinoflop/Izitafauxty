# Keymap Autogenerated by Pog do not edit
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.combos import Chord, Sequence

import pog
import customkeys

keymap = [
    [KC.NUMLOCK, KC.TD(KC.KP_MINUS,KC.KP_SLASH), KC.TD(KC.KP_PLUS,KC.KP_ASTERISK), KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.KP_7, KC.KP_8, KC.KP_9, KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, KC.KP_4, KC.KP_5, KC.KP_6, KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.TD(KC.QUOTE,KC.LSFT(KC.SCOLON)), KC.ENT, KC.KP_1, KC.KP_2, KC.KP_3, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.UP, KC.HT(KC.DEL,KC.RSFT), KC.KP_0, KC.KP_DOT, KC.LT(1,KC.KP_ENTER), KC.LCTL, KC.LGUI, KC.LALT, KC.LT(2, KC.SPC), KC.LT(1, KC.SPC), KC.LT(1, KC.SPC), KC.LT(2, KC.SPC), KC.LEFT, KC.DOWN, KC.RIGHT, KC.TRNS, KC.TRNS], [KC.TRNS, KC.TRNS, KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.KP_MINUS, KC.KP_PLUS, KC.TRNS, KC.GRV, KC.N7, KC.N8, KC.N9, KC.KP_MINUS, KC.KP_PLUS, KC.TRNS, KC.LBRC, KC.RBRC, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.TRNS, KC.KP_SLASH, KC.KP_ASTERISK, KC.EQL, KC.KP_ENTER, KC.N4, KC.N5, KC.N6, KC.KP_SLASH, KC.KP_ASTERISK, KC.EQL, KC.DQT, KC.TRNS, KC.TRNS, KC.SCLN, KC.TRNS, KC.KP_0, KC.KP_DOT, KC.TRNS, KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N0, KC.KP_DOT, KC.ASTERISK, KC.UNDERSCORE, KC.NONUS_BSLASH, KC.SLSH, KC.PGUP, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.QUES, KC.HOME, KC.PGDOWN, KC.END, KC.TRNS, KC.TRNS], [KC.TRNS, KC.TRNS, KC.TRNS, customkeys.ToggleDrive, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TG(3), KC.TRNS, KC.TRNS, KC.TRNS, KC.RESET, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.TRNS, KC.TRNS, KC.LBRC, KC.RBRC, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.CAPS, KC.F4, KC.F5, KC.F6, KC.TRNS, KC.F12, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.F1, KC.F2, KC.F3, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPLY, KC.VOLU, KC.MUTE, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPRV, KC.VOLD, KC.MNXT, KC.TRNS, KC.TRNS], [KC.F10, KC.F11, KC.F12, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.F7, KC.F8, KC.F9, KC.GRV, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, KC.F4, KC.F5, KC.F6, KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT, KC.F1, KC.F2, KC.F3, KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.UP, KC.RSFT, KC.KP_0, KC.KP_DOT, KC.KP_ENTER, KC.LCTL, KC.SLSH, KC.LALT, KC.SPC, KC.BSPC, KC.LT(1, KC.SPC), KC.LT(2, KC.SPC), KC.LEFT, KC.DOWN, KC.RIGHT, KC.TRNS, KC.TRNS]
]

encoderKeymap = []
for l, layer in enumerate(pog.config['encoderKeymap']):
    layerEncoders = []
    for e, encoder in enumerate(layer):
        layerEncoders.append(tuple(map(eval, encoder)))
    encoderKeymap.append(tuple(layerEncoders))
