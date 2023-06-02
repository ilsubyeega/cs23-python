import struct

# NOTE: From `assignment_9_5_4.py`,
# > This problem does not solve the problem of three lecture? not sure what the textbook going to say.

def read_bytes(io_read):
    raw = io_read.read(4)
    if len(raw) == 0:
        return None
    len_lecture = struct.unpack('>i', raw)[0]
    raw = io_read.read(len_lecture + 12)
    lecture_name, *scores = struct.unpack(f'>{len_lecture}s3i', raw)
    return lecture_name.decode(), scores, [len_lecture]

# There is no way to use variable length of data without reading first, so read first for calculating the length and read again.
data1 = []
with open('Week 14/lecture_dump.tmp', 'rb') as io_read:
    while True:
        data = read_bytes(io_read)
        if data is None:
            break
        data1.append(data)

with open('Week 14/lecture_dump.tmp', 'rb') as io_read:
    identifier = []
    for i in data1:
        identifier.append(4 + i[2][0] + 12 - 1)
    
    io_read.seek(identifier[1], 0) # Seek second one.
    print(read_bytes(io_read))

    io_read.seek(0, 0) # Read the first one.
    print(read_bytes(io_read))