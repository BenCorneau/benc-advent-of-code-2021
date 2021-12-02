def read_file_int(file):
    return read_file(file, int)

def read_file_str(file):
    return read_file(file, str)
    

def read_file(file, transform):
    with open(file) as f:
        return [transform(l.strip()) for l in f.readlines() if l.strip()]