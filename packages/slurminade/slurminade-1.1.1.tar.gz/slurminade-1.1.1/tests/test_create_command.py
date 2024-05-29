import unittest
from pathlib import Path

import slurminade

test_file_path = Path("./f_test_file.txt")


@slurminade.slurmify()
def f(s):
    with open(test_file_path, "w") as file:
        file.write(s)


class TestCreateCommand(unittest.TestCase):
    def test_dispatch_with_temp_file(self):
        slurminade.set_entry_point(__file__)
        if test_file_path.exists():
            test_file_path.unlink()
        dispatcher = slurminade.SubprocessDispatcher()
        dispatcher.max_arg_length = 1
        slurminade.set_dispatcher(dispatcher)
        s = "test"
        f.distribute(s)
        assert test_file_path.is_file()
        with open(test_file_path) as file:
            assert file.readline() == s
        if test_file_path.exists():  # delete the file
            test_file_path.unlink()
