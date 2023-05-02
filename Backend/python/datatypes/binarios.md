# Secuencias Binarias

## Boolean

´´´pyhton
    b = (5 == 6)
    # False
    b = (5 < 6)
    # True
´´´

Cualquier objeto es verdadero a no ser que esté vacío:
´´´pyhton
    b = bool()
    b = bool([])
    b = bool(())
    b = bool({})
    b = bool(False)
    b = bool(0)
    b = bool(None)
    # False
    b = bool(non_empty_obj)
    # True
´´´ 

## Bytes

Array de Bytes inmutable:
´´´pyhton
    b = bytes(4)
    # b'\x00\x00\x00\x00'
    b[1] = 5
    # ERROR!!

    s = "cadena"
    # 'cadena'
    b = bytes(cadena, 'UTF-8')
    # b'cadena'
    s[1]
    # 'a'
    a[1]
    # 97

´´´

## Bytearray

Array de Bytes mutable:
´´´pyhton
    b = bytearray(4)
    # bytearray(b'\x00\x00\x00\x00')
    b[1] = 5
    # bytearray(b'\x00\x05\x00\x00')
´´´

## Mamoryview

´´´pyhton
    x = memoryview(b"cadena")
    # <memory at 0xMEMADDRESS>
    x[1]
    # 97

    ba = bytearray(4)
    x = memoryview(ba)
    x[1]
    # 0

    bs = bytes(b'\x01\x0a\x10\x2b')
    x = memoryview(bs)
    x[1]
    # 10
    x[3]
    # 43
´´´
