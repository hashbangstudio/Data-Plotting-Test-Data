#!/usr/bin/env python

#import the needed modules
import sys
from datetime import datetime, time, timedelta
from random import randint

if __name__ == "__main__":

    numOfRecsToGenerate = 0
    minTemp = 0
    maxTemp = 0
    timeStep = 0

    minNumOfArgs = 5
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == minNumOfArgs:
        try:
            numOfRecsToGenerate = int(sys.argv[1])
            minTemp = int(sys.argv[2])
            maxTemp = int(sys.argv[3])
            timeStep = int(sys.argv[4])
        except ValueError:
            print("Unexpected integer as argument but got %s" % sys.argv[1])
            sys.exit()
        except TypeError:
            print("Unexpected integer as argument but got %s" % sys.argv[1])
            sys.exit()

        filename = sys.argv[5]

        lines = ["#Time\tTemperature\n",]
        currentTime = datetime.now()
        for rec in range(numOfRecsToGenerate):
            currentTime += timedelta(minutes=timeStep)
            lines.append("%s\t%d\n" % (currentTime.strftime('%Y-%m-%d,%H:%M:%S'), randint(minTemp, maxTemp)))

        with open(filename, 'w') as f:
            for line in lines:
                f.write(line)

        if not(f.closed):
            f.close()
    else:
        print("Unexpected number of arguments, Expected %d but got %d" % (minNumOfArgs, numOfArgs))
        print("Usage: python numOfRecs minTemp maxTemp timestep filename")
        print("Generates a specified number of random temperature records separated by the number of minutes given in the timestep")
        print("File is tab-delimted file of type: Time Temperature")
        sys.exit()
