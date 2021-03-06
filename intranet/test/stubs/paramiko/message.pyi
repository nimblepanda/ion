# Stubs for paramiko.message (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Message:
    big_int = ... # type: Any
    packet = ... # type: Any
    def __init__(self, content=None): ...
    def asbytes(self): ...
    def rewind(self): ...
    def get_remainder(self): ...
    def get_so_far(self): ...
    def get_bytes(self, n): ...
    def get_byte(self): ...
    def get_boolean(self): ...
    def get_adaptive_int(self): ...
    def get_int(self): ...
    def get_int64(self): ...
    def get_mpint(self): ...
    def get_string(self): ...
    def get_text(self): ...
    def get_binary(self): ...
    def get_list(self): ...
    def add_bytes(self, b): ...
    def add_byte(self, b): ...
    def add_boolean(self, b): ...
    def add_int(self, n): ...
    def add_adaptive_int(self, n): ...
    def add_int64(self, n): ...
    def add_mpint(self, z): ...
    def add_string(self, s): ...
    def add_list(self, l): ...
    def add(self, *seq): ...
