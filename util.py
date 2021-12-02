
  
def read_file(file, transform=str):
    with open(file) as f:
        return [transform(l.strip()) for l in f.readlines() if l.strip()]