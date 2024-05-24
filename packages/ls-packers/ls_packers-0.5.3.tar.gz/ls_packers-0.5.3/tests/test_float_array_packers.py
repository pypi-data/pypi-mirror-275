import numpy
from ls_packers import float_array_int_pack
from ls_packers import float_array_int_unpack

def test_sanity():
    quboProblemData = numpy.sign(numpy.random.rand(4,4)-0.5)
    quboProblemData = quboProblemData + quboProblemData.T

    quboProblemData32 = numpy.float32(quboProblemData)

    packed = float_array_int_pack(quboProblemData32)

    unpacked = float_array_int_unpack(packed)

    assert (unpacked == quboProblemData32).all()

def test_4000_vars():
    quboProblemData = numpy.sign(numpy.random.rand(4,4)-0.5)
    quboProblemData = quboProblemData + quboProblemData.T

    quboProblemData32 = numpy.float32(quboProblemData)

    packed = float_array_int_pack(quboProblemData32)

    unpacked = float_array_int_unpack(packed)

    assert (unpacked == quboProblemData32).all()