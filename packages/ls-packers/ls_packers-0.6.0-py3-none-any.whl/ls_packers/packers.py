import numpy
import msgpack
from ls_packers.converters import float_array_as_int
from ls_packers.converters import int_list_as_square_float_array

def float_array_int_pack(numpyMatrix):
    intMatrix = float_array_as_int(numpyMatrix)
    return msgpack.dumps(intMatrix.tolist(), use_single_float=True)

def float_array_int_unpack(binaryData):
    listData = msgpack.loads(binaryData)
    return int_list_as_square_float_array(listData)

def msgpack_encode(x):
    v = msgpack.packb(x)
    return v

def msgpack_decode(x):
    v = msgpack.unpackb(x)
    return v