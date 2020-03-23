# 一百万
import datetime

millions = list(range(1, 1000001))
print(min(millions))
print(max(millions))
startTime = datetime.datetime.now()

print(sum(millions))

endTime = datetime.datetime.now()
runTime = endTime - startTime
print(runTime.seconds)