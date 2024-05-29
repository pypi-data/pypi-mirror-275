import unittest
from dtl.lib import transpose2d, window1d


class TestTransposing(unittest.TestCase):
    parametrized = (
        # i=0
        # squared matrix
        (
            [
                [1, 2],
                [3, 4],
            ],
            [
                [1, 3],
                [2, 4],
            ]
        ),
        # i=1
        # rectangular matrix
        (
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [1, 4],
                [2, 5],
                [3, 6],
            ],
        ),
        # i=2
        # single element
        (
            [
                [5],
            ],
            [
                [5],
            ],
        ),
        # i=3
        # single column
        (
            [
                [1],
                [2],
                [3],
            ],
            [
                [1, 2, 3],
            ],
        ),
        # i=4
        # single row
        (
            [
                [1, 2, 3],
            ],
            [
                [1],
                [2],
                [3]
            ],
        ),
    )


    def test_ok(self) -> None:
        for i, (input_matrix, expected_result) in enumerate(self.parametrized):
            with self.subTest(i=i):
                self.assertEqual(transpose2d(input_matrix), expected_result)


class TestWindowing(unittest.TestCase):
    parametrized = (
        (
            list(range(1, 6)),
            {"size": 3, "stride": 1, "shift": 1},
            [[1, 2, 3], [2, 3, 4], [3, 4, 5]],
        ),
    )

    def test_pass_invalid_size(self) -> None:
        with self.assertRaises(ValueError):
            window1d([], size=0)

    def test_pass_invalid_shift(self) -> None:
        with self.assertRaises(ValueError):
            window1d([], size=1, shift=0)

    def test_pass_invalid_stride(self) -> None:
        with self.assertRaises(ValueError):
            window1d([], size=1, shift=1, stride=0)

    def test_ok(self) -> None:
        for i, (input_array, kwargs, expected_result) in enumerate(self.parametrized):
            with self.subTest(i=i):
                self.assertEqual(window1d(input_array, **kwargs), expected_result)

