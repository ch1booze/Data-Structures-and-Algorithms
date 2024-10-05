# LeetCode 539: Minimum Time Difference
def findMinDifference(timePoints):
        def getTimeInMinsFromTimePoint(timePoint):
            hrs, mins = timePoint.split(":")
            return (int(hrs) * 60) + int(mins)

        refTimeInMins = getTimeInMinsFromTimePoint(timePoints[0])
        uniqueTimePoints = set([timePoints[0]])
        minTimeDiffToRef = 100000
        secondMinTimeToRef = 100000

        def calcTimeDiffToRef(timePoint):
            timeInMins = getTimeInMinsFromTimePoint(timePoint)
            timeDiff0 = abs(timeInMins - refTimeInMins)
            timeDiff1 = abs((timeInMins - (24 * 60)) - refTimeInMins) if timeInMins > refTimeInMins else abs((timeInMins + (24 * 60)) - refTimeInMins)
            return min([timeDiff0, timeDiff1])

        for i in range(1, len(timePoints)):
            # If time point exists, return the minimun time difference as zero
            if timePoints[i] in uniqueTimePoints:
                return 0
            
            uniqueTimePoints.add(timePoints[i])
            timeDiffToRef = calcTimeDiffToRef(timePoints[i])
            if timeDiffToRef < minTimeDiffToRef:
                secondMinTimeToRef = minTimeDiffToRef
                minTimeDiffToRef = timeDiffToRef
                
        return minTimeDiffToRef if secondMinTimeToRef == 100000 else secondMinTimeToRef - minTimeDiffToRef
        
if __name__ == "__main__":
    print(findMinDifference(["00:00", "23:59", "00:00"]))