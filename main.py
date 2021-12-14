from day13 import part2 as part
import time

print("running", part)
print("")

ts = time.time()
result = part.run()
te = time.time()

print(f"runtime:{te-ts:.3}")
print ("result", result)
