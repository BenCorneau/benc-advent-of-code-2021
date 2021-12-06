
  
def read_file(file, transform=str):
    with open(file, encoding="utf8") as f:
        return [transform(l.strip()) for l in f.readlines() if l.strip()]

def read_line(file, transform=str):
    with open(file, encoding="utf8") as f:
        line = f.readline()
        return [transform(v.strip()) for v in line.split(",") if v.strip()]