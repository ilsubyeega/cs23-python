import struct

in_data, in_height, in_gender = 20, 1.75, True
binary_data = struct.pack('>if?', in_data, in_gender, in_height)
print(len(binary_data), binary_data.hex())

print(struct.unpack('>if?', binary_data))