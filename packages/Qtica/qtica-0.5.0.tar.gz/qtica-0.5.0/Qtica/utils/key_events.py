#!/usr/bin/python3

from typing import Union
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QKeySequence


class Modifiers:
    Modifier = Qt.KeyboardModifier

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, *modifier: list[Qt.KeyboardModifier]) -> bool:
        return Modifiers.matches(self._event, *modifier)

    @classmethod
    def matches(cls,
                event: QKeyEvent, 
               *modifier: list[Qt.KeyboardModifier]) -> bool:

        _modifier = None
        if len(modifier) > 1:
            _modifier = modifier[0]
            for mod in modifier[1:]:
                _modifier |= mod
        else:
            _modifier = modifier[0]
        return event.modifiers() == _modifier

    @classmethod
    def is_shift(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.ShiftModifier)

    @classmethod
    def is_alt(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.AltModifier)

    @classmethod
    def is_ctrl(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.ControlModifier)

    @classmethod
    def is_meta(cls, event: QKeyEvent) -> bool:
        return cls.matches(event, Qt.KeyboardModifier.MetaModifier)

    @classmethod
    def is_win(cls, event: QKeyEvent) -> bool:
        return cls.is_meta(event)


class Keys:
    Key = Qt.Key

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, key: Union[Qt.Key, int]) -> bool:
        return Keys.matches(self._event, key)

    @staticmethod
    def matches(event: QKeyEvent, key: Union[Qt.Key, int]) -> bool:
        return event.key() == key


class KeySequence:
    Standard = QKeySequence.StandardKey

    def __init__(self, event: QKeyEvent = None) -> None:
        self._event = event

    def matche(self, 
               modifier: Union[Qt.KeyboardModifier, list[Qt.KeyboardModifier]],
               key: Union[int, Qt.Key]) -> bool:
        return KeySequence.matches(self._event, modifier, key)

    def matche_seq(self, key: QKeySequence.StandardKey) -> bool:
        return self._event.matches(key)

    @staticmethod
    def matches(event: QKeyEvent, 
                key: Union[int, Qt.Key],
                *modifier: list[Qt.KeyboardModifier]) -> bool:

        return Modifiers.matches(event, *modifier) and Keys.matches(event, key)

    @staticmethod
    def matches_seq(event: QKeyEvent, key: QKeySequence.StandardKey) -> bool:
        return event.matches(key)
