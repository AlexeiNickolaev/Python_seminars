# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

from task_rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(1)
        self.r2 = Rectangle(1)
        self.r3 = Rectangle(1, 2)
        self.r4 = Rectangle(4, 6)
        self.r5 = Rectangle(3, 5)


def test_get_perim(self):
    self.assertEqual(self.r1.perimetr(), self.r2.perimetr())
    self.assertNotEqual(self.r1.perimetr(), 2)


def test_equal_rects(self):
    self.assertFalse(self.r1 == self.r3)


def test_sub_rects(self):
    self.assertEqual(self.r4 - self.r1, self.r5)


if __name__ == '__main__':
    unittest.main(verbosity=10)
