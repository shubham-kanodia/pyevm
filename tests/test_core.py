import pytest
from evm.core import EVM


def test_add():
    evm = EVM()

    evm.stack = [2, 3]
    evm.add()

    assert evm.stack == [5]


def test_execute():
    evm = EVM()
    bytecode = bytearray([0x01])
    evm.stack = [4, 2]
    evm.execute(bytecode)

    assert evm.stack == [6]
