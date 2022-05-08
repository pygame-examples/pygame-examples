"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.
"""

import os

import pygame


def _load_image(path):
    return pygame.image.load(os.path.join(os.path.dirname(__file__), "assets", path))


class BaseCharacter:
    name = ""
    image = pygame.Surface((1, 1))
    velocity = 5


class Guy(BaseCharacter):
    name = "Guy"
    image = _load_image("guy.png")
    velocity = 5


DefaultCharacter = Guy


class Mage(BaseCharacter):
    name = "Mage"
    image = _load_image("mage.png")
    velocity = 3


class Knight(BaseCharacter):
    name = "Knight"
    image = _load_image("knight.png")
    velocity = 1


class Archer(BaseCharacter):
    name = "Archer"
    image = _load_image("archer.png")
    velocity = 7


class Pawn(BaseCharacter):
    name = "Black e5 pawn"
    image = _load_image("pawn.png")
    velocity = 1


characters = BaseCharacter.__subclasses__()
