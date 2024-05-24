import numpy

def float_array_as_int(numpyMatrix):
    numpyMatrix = numpy.float32(numpyMatrix)
    floatBytes = numpyMatrix.tobytes()
    numpyIntArray = numpy.frombuffer(floatBytes, dtype=numpy.int32)
    return numpyIntArray

def int_list_as_float_array(listData):
    numpyIntArray = numpy.array(listData, dtype=numpy.int32)
    binaryNumpy = numpyIntArray.tobytes()
    numpy1DArray = numpy.frombuffer(binaryNumpy, dtype=numpy.float32)
    return numpy1DArray

def int_list_as_square_float_array(listData):
    numpy1DArray = int_list_as_float_array(listData)
    varCount = numpy.int32(numpy.sqrt(numpy1DArray.size))
    return numpy1DArray.reshape(varCount, varCount)

def numpy_array_to_triu_flat(array):
    triuIndices = numpy.triu_indices_from(array)
    triuFlat = array[triuIndices]
    return triuFlat

def triu_flat_to_square_matrix(flatList):
    listLength = len(flatList)
    varCount = numpy.int32(numpy.sqrt(0.25 + (2 * listLength)) - 0.5)
    matrix = numpy.zeros((varCount, varCount), dtype=numpy.float32)
    matrix[numpy.triu_indices(varCount)] = numpy.array(flatList)
    matrix = (matrix + matrix.T) * 0.5
    return matrix


