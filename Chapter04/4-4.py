# 一百万
import datetime

startTime = datetime.datetime.now()

for value in range(1, 1000001):
    print(value)

endTime = datetime.datetime.now()
runTime = endTime - startTime
print(runTime.seconds)