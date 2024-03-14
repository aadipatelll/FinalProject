import h5py

filename = "dataset.h5"
try:
    with h5py.File(filename, 'r') as f:
        print("Hey")
except Exception as e:
    print("dang")