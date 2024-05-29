# AUTO GENERATED ON 2024-05-28 AT 14:45:32
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import cupy
import pytest

import awkward as ak
import awkward._connect.cuda as ak_cu
from awkward._backends.cupy import CupyBackend

cupy_backend = CupyBackend.instance()

def test_cudaawkward_ListArray32_rpad_axis1_64_1():
    toindex = cupy.array([123, 123, 123, 123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    fromstarts = cupy.array([2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1], dtype=cupy.int32)
    fromstops = cupy.array([3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 6, 11], dtype=cupy.int32)
    tostarts = cupy.array([123, 123, 123], dtype=cupy.int32)
    tostops = cupy.array([123, 123, 123], dtype=cupy.int32)
    target = 3
    length = 3
    funcC = cupy_backend['awkward_ListArray_rpad_axis1', cupy.int64, cupy.int32, cupy.int32, cupy.int32, cupy.int32]
    funcC(toindex, fromstarts, fromstops, tostarts, tostops, target, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [2, -1, -1, 0, 1, -1, 2, 3, -1]
    assert cupy.array_equal(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))
    pytest_tostarts = [0, 3, 6]
    assert cupy.array_equal(tostarts[:len(pytest_tostarts)], cupy.array(pytest_tostarts))
    pytest_tostops = [3, 6, 9]
    assert cupy.array_equal(tostops[:len(pytest_tostops)], cupy.array(pytest_tostops))

def test_cudaawkward_ListArray32_rpad_axis1_64_2():
    toindex = cupy.array([123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], dtype=cupy.int32)
    fromstops = cupy.array([8, 4, 5, 6, 5, 5, 7], dtype=cupy.int32)
    tostarts = cupy.array([123, 123, 123], dtype=cupy.int32)
    tostops = cupy.array([123, 123, 123], dtype=cupy.int32)
    target = 3
    length = 3
    funcC = cupy_backend['awkward_ListArray_rpad_axis1', cupy.int64, cupy.int32, cupy.int32, cupy.int32, cupy.int32]
    funcC(toindex, fromstarts, fromstops, tostarts, tostops, target, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, 0, 1, 2, 3, 4]
    assert cupy.array_equal(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))
    pytest_tostarts = [0, 7, 11]
    assert cupy.array_equal(tostarts[:len(pytest_tostarts)], cupy.array(pytest_tostarts))
    pytest_tostops = [7, 11, 16]
    assert cupy.array_equal(tostops[:len(pytest_tostops)], cupy.array(pytest_tostops))

def test_cudaawkward_ListArray32_rpad_axis1_64_3():
    toindex = cupy.array([123, 123, 123, 123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    fromstops = cupy.array([1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2], dtype=cupy.int32)
    tostarts = cupy.array([123, 123, 123], dtype=cupy.int32)
    tostops = cupy.array([123, 123, 123], dtype=cupy.int32)
    target = 3
    length = 3
    funcC = cupy_backend['awkward_ListArray_rpad_axis1', cupy.int64, cupy.int32, cupy.int32, cupy.int32, cupy.int32]
    funcC(toindex, fromstarts, fromstops, tostarts, tostops, target, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    assert cupy.array_equal(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))
    pytest_tostarts = [0, 3, 6]
    assert cupy.array_equal(tostarts[:len(pytest_tostarts)], cupy.array(pytest_tostarts))
    pytest_tostops = [3, 6, 9]
    assert cupy.array_equal(tostops[:len(pytest_tostops)], cupy.array(pytest_tostops))

def test_cudaawkward_ListArray32_rpad_axis1_64_4():
    toindex = cupy.array([123, 123, 123, 123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    fromstarts = cupy.array([1, 7, 6, 1, 3, 4, 2, 5, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2], dtype=cupy.int32)
    fromstops = cupy.array([1, 9, 6, 2, 4, 5, 3, 6, 3, 4, 2, 4, 5, 5, 7, 8, 2, 3], dtype=cupy.int32)
    tostarts = cupy.array([123, 123, 123], dtype=cupy.int32)
    tostops = cupy.array([123, 123, 123], dtype=cupy.int32)
    target = 3
    length = 3
    funcC = cupy_backend['awkward_ListArray_rpad_axis1', cupy.int64, cupy.int32, cupy.int32, cupy.int32, cupy.int32]
    funcC(toindex, fromstarts, fromstops, tostarts, tostops, target, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [-1, -1, -1, 7, 8, -1, -1, -1, -1]
    assert cupy.array_equal(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))
    pytest_tostarts = [0, 3, 6]
    assert cupy.array_equal(tostarts[:len(pytest_tostarts)], cupy.array(pytest_tostarts))
    pytest_tostops = [3, 6, 9]
    assert cupy.array_equal(tostops[:len(pytest_tostops)], cupy.array(pytest_tostops))

def test_cudaawkward_ListArray32_rpad_axis1_64_5():
    toindex = cupy.array([123, 123, 123, 123, 123, 123, 123, 123, 123], dtype=cupy.int64)
    fromstarts = cupy.array([0, 0, 0, 0, 0, 0, 0, 0], dtype=cupy.int32)
    fromstops = cupy.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=cupy.int32)
    tostarts = cupy.array([123, 123, 123], dtype=cupy.int32)
    tostops = cupy.array([123, 123, 123], dtype=cupy.int32)
    target = 3
    length = 3
    funcC = cupy_backend['awkward_ListArray_rpad_axis1', cupy.int64, cupy.int32, cupy.int32, cupy.int32, cupy.int32]
    funcC(toindex, fromstarts, fromstops, tostarts, tostops, target, length)

    try:
        ak_cu.synchronize_cuda()
    except:
        pytest.fail("This test case shouldn't have raised an error")
    pytest_toindex = [0, -1, -1, 0, -1, -1, 0, -1, -1]
    assert cupy.array_equal(toindex[:len(pytest_toindex)], cupy.array(pytest_toindex))
    pytest_tostarts = [0, 3, 6]
    assert cupy.array_equal(tostarts[:len(pytest_tostarts)], cupy.array(pytest_tostarts))
    pytest_tostops = [3, 6, 9]
    assert cupy.array_equal(tostops[:len(pytest_tostops)], cupy.array(pytest_tostops))

