ab = int(input())
bc = int(input())
import cmath,math

coordinate = complex(bc,ab) #make the complex no. and use 
                            #the phase method to find the angle using polar coordinates
val = cmath.phase(coordinate)

print(round(math.degrees(val)), '°',sep='') #convert to degree and print it.
