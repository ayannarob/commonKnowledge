#!/usr/bin/env python3
# This program generates all of the possible Powerball combinations.
# In Powerball, there are 69 white balls and 26 red Powerballs.
# ((69 * 68 * 67 * 66 * 65) / (5 * 4 * 3 * 2 * 1)) * 26
import time
start_time = time.time()
f = open("AllPowerBallNumbers.csv", "w")
f.write("D1,D2,D3,D4,D5,PB,CT,CTP\n")
for b1 in range(1, 70):
    for b2 in range(b1 + 1, 70):
        for b3 in range(b2 + 1, 70):
            for b4 in range(b3 + 1, 70):
                for b5 in range(b4 + 1, 70):
                    for p in range(1, 27):
#                        print(b1, b2, b3, b4, b5, "Power:", p)
                        #print(b1, b2, b3, b4, b5, p)
                        CTP = (b1+b2+b3+b4+b5+p)
                        CT = (b1+b2+b3+b4+b5)
                        f.write(str(b1) + "," + str(b2) + "," + str(b3) + "," + str(b4) + "," + str(b5) + "," + str(p) + "," + str(CT) + "," + str(CTP) + "\n")
f.close()

elapsed_time = time.time() - start_time
elapsed_minutes = (elapsed_time // 60)
elapsed_seconds = (elapsed_time % 60)
print("This program took %d minutes and %d seconds to run." % (elapsed_minutes, elapsed_seconds))
