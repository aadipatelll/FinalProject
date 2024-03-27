import h5py
def print_keys(obj, name):
    print(name)
    if isinstance(obj, h5py.Group):
        for key in obj.keys():
            print_keys(obj[key], name + '/' + key)
filename = "dataset.h5"
try:
    with h5py.File(filename, 'r') as f:
        print_keys(f, '/')
except Exception as e:
    print("dang")