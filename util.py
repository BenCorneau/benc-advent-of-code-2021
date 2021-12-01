def read_file(file):
    with open(file) as f:
        return [l.strip() for l in f.readlines() if l.strip()]