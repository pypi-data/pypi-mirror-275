# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring

from src.python_rebase.rotation import Rotation

class TestRotation:
    def test_init(self):
        rotation = Rotation(1, 2, 3)
        rotation2 = Rotation(1, 2)
        rotation3 = Rotation()

        assert rotation.x == 1
        assert rotation.y == 2
        assert rotation.z == 3

        assert rotation2.x == 1
        assert rotation2.y == 2
        assert rotation2.z == 0

        assert rotation3.x == 0
        assert rotation3.y == 0
        assert rotation3.z == 0

    def test_str(self):
        rotation = Rotation(1, 2, 3)
        rotation2 = Rotation(1, 2.5)

        assert str(rotation) == '[1, 2, 3]'
        assert str(rotation2) == '[1, 2.5, 0]'

    def test_to_list(self):
        rotation = Rotation(1, 2, 3)
        assert rotation.to_list() == [1, 2, 3]

    def test_to_tuple(self):
        rotation = Rotation(1, 2, 3)
        assert rotation.to_tuple() == (1, 2, 3)

    def test_eq(self):
        assert Rotation(1, 2, 3) == Rotation(1, 2, 3)
        assert Rotation(1, 2, 3) != Rotation(1, 2)
        assert Rotation(1, 2, 3) != Rotation(1, 2, 5)
        assert Rotation(1, 2, 3) != 7

# pylint: enable=missing-module-docstring, missing-class-docstring, missing-function-docstring
