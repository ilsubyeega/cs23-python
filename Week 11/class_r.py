class HyperParameter:
    units = [32, 64, 128]
    batch_size = 128
    split = 0.2

for v in HyperParameter.units:
    print(v)
print(HyperParameter.batch_size * HyperParameter.split)

# ??
HyperParameter.batch_size = 1
instance = HyperParameter()
print(instance.batch_size)