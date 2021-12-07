from day07 import part2 as part
import time

print("running", part)
print("")
ts = time.time()
part.run()
te = time.time()
print("")
print(f"runtime:{te-ts:.3}")

