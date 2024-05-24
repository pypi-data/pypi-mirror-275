import numpy
from ls_packers import numpy_array_to_triu_flat
from ls_packers import triu_flat_to_square_matrix

def test_sanity():
    testArr = numpy.float32(numpy.random.rand(4,4))
    testArr = testArr + testArr.T

    flatArr = numpy_array_to_triu_flat(testArr)

    resultArr = triu_flat_to_square_matrix(flatArr)

    numpy.diagonal(testArr)

    assert (resultArr == testArr).all(), "Output array not equal to input"

def test_10K_vars():
    testArr = numpy.float32(numpy.random.rand(10000, 10000))
    testArr = testArr + testArr.T

    flatArr = numpy_array_to_triu_flat(testArr)

    resultArr = triu_flat_to_square_matrix(flatArr)

    numpy.diagonal(testArr)

    assert (resultArr == testArr).all(), "Output array not equal to input"