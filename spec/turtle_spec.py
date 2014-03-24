# coding: spec

from noseOfYeti.tokeniser.support import noy_sup_setUp
from unittest import TestCase
from mock import MagicMock
import os
import nose

from turtlecraft import Turtlecraft  # Sets and appends MCPIPY path
from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft

describe TestCase, 'Turtle':
    before_each:
        mc = minecraft.Minecraft
        mc_mock = MagicMock()
        mc.create = MagicMock(return_value=mc_mock)
        mc_mock.player.getPos = MagicMock(return_value=Vec3(0, 0, 0))
        self.T = Turtlecraft()
        self.T.Turtle.setPos(0, 0, 0)
        if os.path.isfile(self.T.history_file_path()):
            os.remove(self.T.history_file_path())

    it 'should move forward':
        self.T.fd(2)
        self.assertEqual(self.T.history[-1], [1, 0, 0, 2])

    it 'should turn right':
        self.T.rt(90)
        self.T.fd(2)
        self.assertEqual(self.T.history[-1], [0, 0, 1, 2])

    it 'should turn left':
        self.T.lt(90)
        self.T.fd(2)
        self.assertEqual(self.T.history[-1], [0, 0, -1, 2])

    it 'should tilt forward':
        self.T.tilt_fd(90)
        self.T.fd(2)
        self.assertEqual(self.T.history[-1], [0, -1, 0, 2])

    it 'should tilt back':
        self.T.tilt_bk(90)
        self.T.fd(2)
        self.assertEqual(self.T.history[-1], [0, 1, 0, 2])
