import struct

with open('Week 14/10float.tmp', 'wb') as io_write:
    data = [0 for _ in range(10)]
    bytes_data = struct.pack('>10f', *data)
    io_write.write(bytes_data)

with open('Week 14/10float.tmp', 'rb') as io_read:
    raw = io_read.read()
    data = struct.unpack('>10f', raw)
    print(data)