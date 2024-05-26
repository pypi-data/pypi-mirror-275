import unittest

import pytest

from geolysis.core.foundation import (
    CircularFooting,
    FootingCreationError,
    FootingSize,
    FoundationSize,
    Shape,
    SquareFooting,
    create_footing,
)


def test_create_footing():

    with pytest.raises(FootingCreationError):
        create_footing(thickness=0.5, width=1.3, footing_shape=Shape.RECTANGLE)

    with pytest.raises(FootingCreationError):
        create_footing(thickness=0.5, width=1.3, footing_shape="hexagonal")  # type: ignore


class TestCircularFooting(unittest.TestCase):
    def testAttributes(self):
        circ_footing = CircularFooting(diameter=1.2)
        circ_footing.width = 1.4
        self.assertAlmostEqual(circ_footing.length, 1.4)
        self.assertAlmostEqual(circ_footing.diameter, 1.4)

        circ_footing.length = 1.5
        self.assertAlmostEqual(circ_footing.width, 1.5)
        self.assertAlmostEqual(circ_footing.diameter, 1.5)


class TestSquareFooting(unittest.TestCase):
    def testAttributes(self):
        sqr_footing = SquareFooting(1.2)
        sqr_footing.length = 1.4
        self.assertAlmostEqual(sqr_footing.width, 1.4)


class TestFootingSize(unittest.TestCase):
    def testAttributes(self):
        footing_shape = SquareFooting(width=1.3)
        footing_size = FootingSize(thickness=0.45, footing_shape=footing_shape)
        footing_size.length = 1.4
        self.assertAlmostEqual(footing_size.width, 1.4)

        footing_size.width = 1.5
        self.assertAlmostEqual(footing_size.length, 1.5)


class TestFoundationSize(unittest.TestCase):
    def testAttributes(self):
        footing_size = create_footing(
            thickness=0.45, width=1.2, footing_shape=Shape.SQUARE
        )
        foundation_size = FoundationSize(depth=1.5, footing_size=footing_size)
        foundation_size.thickness = 0.3
        self.assertAlmostEqual(foundation_size.thickness, 0.3)

        foundation_size.width = 1.4
        self.assertAlmostEqual(foundation_size.width, 1.4)

        foundation_size.length = 1.5
        self.assertAlmostEqual(foundation_size.length, 1.5)

        footing_shape = CircularFooting(diameter=1.5)
        foundation_size.footing_shape = footing_shape
        self.assertEqual(
            foundation_size.footing_shape, CircularFooting(diameter=1.5)
        )
