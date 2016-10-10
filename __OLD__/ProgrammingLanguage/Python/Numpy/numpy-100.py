#1. import the numpy package under the name np
import numpy as np


#1. print the numpy version and the configuration
#print(np.__version__)
#np.show_config()

#2. create a null vector of size 10
z = np.zeros(10)

#3. how to get the documentation of the numpy add function from the command line?
#python -c "import numpy; numpy.info(numpy.add)"
#print(np.info(np.add))

#4. create a null vector of size 10 but the fifth value which is 1
z = np.zeros(10) 
z[4] = 1

#5. create a vector with values ranging from 10 to 49
z = np.arange(10,50)

#6. reverse a vector (first element becomes last)
z = np.arange(50)
z = z[::-1]

#7. create a 3x3 matrix with values ranging from 0 to 8
z = np.arange(9).reshape(3,3)

#8. find indices of non-zero elements from [1,2,0,0,4,0]
z = np.nonzero([1,2,0,0,4,0])

#9. create a 3x3 identity matrix
z = np.eye(3)

#10. create a 10x10 array with randomi values and find the minimum and maximum values
z = np.random.random((10,10))
zmin , zmax = z.min() , z.max()

#11. create a random vector of size 30 and find the mean value
z = np.random.random(30)
z = z.mean()

#12. create a 2d array with 1 on the border and 0 inside
z = np.ones((10,10))
z[1:-1,1:-1] = 0

#13. what is the result of the following expression
z = 0 * np.nan
z = np.nan==np.nan
z = np.inf > np.nan
z = np.nan - np.nan
z = 0.3==3*0.1

#14. create a 5x5 matrix with values 1,2,3,4 just below the diagonal
z = np.diag(1+np.arange(4) , k=-1)

#15. create a  8x8 matrix and fill it with a checkerboard pattern
z = np.zeros((8,8) , dtype=int)
z[1::2 , ::2] = 1
z[::2 , 1::2] = 1

#16. consider a (6,7,8) shape array,what is the index (x,y,z) of the 100th element?
z = np.unravel_index(100 , (6,7,8))
z = np.arange(336).reshape(6,7,8)

#17. create a checkboard 8x8 matrix using the tile function
z = np.tile(np.array([[0,1],[1,0]]) , (4,4))

#18. Normalize a 5x5 random matrix
z = np.random.random((5,5))
zmax , zmin = z.max() , z.min()
z = (z - zmin) / (zmax - zmin)

#19. Multiply a 5x3 matrix by a 3x2 matrix
z = np.dot(np.ones((5,3)) , np.ones((3,2)))

#20. Given a 1D array,negate all elements which are between 3 and 8,in place.
z = np.arange(11)
z[(3<z) & (z<=8)] *= -1

#21. Create a 5x5 matrix with row values ranging from 0 to 4
z = np.zeros((5,5))
z += np.arange(5)

#22. Consider a generator function that generates 10 intergers and use it to build an array
def generate() :
    for x in xrange(10) :
        yield x
z = np.fromiter(generate() , dtype=float , count=-1)

#23. Create a vector of size 10 with values ranging from 0 to 1,both excluded
z = np.linspace(0 , 1 , 12 , endpoint=True)[1:-1]

#24. Create a random vector of size 10 and sort it
z = np.random.random(10)
z.sort()

#25. How to sum a small array faster than np.sum?
z = np.arange(10)
z = np.add.reduce(z)

#26. Consider two random array A and B,check if they ary equal
a = np.random.randint(0 , 2 , 5)
b = np.random.randint(0 , 2 , 5)
equal = np.allclose(a , b)
z = equal

#27. Make an array immutable(read-only)
z = np.zeros(10)
z.flags.writeable = False
#z[0] = 1 #ValueError: assignment destination is read-only

#28. Consider a random 10x2 matrix representing cartesian coordinates,convert them to polar coordinates
z = np.random.random((10 , 2))
x , y = z[:,0] , z[:,1]
r = np.sqrt(x**2 + y**2)
t = np.arctan2(y , x)

#29. Create random vector of size 10 and replace the maximum value by 0
z = np.random.random(10)
z[z.argmax()] = 0

#30. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area
z = np.zeros((5 , 5) , [("x" , float) , ("y" , float)])
z["x"] , z["y"] = np.meshgrid(np.linspace(0 , 1 , 5) , np.linspace(0 , 1 , 5))

#31. Given two arrays,x and y,construct the Cauchy matrix c(cij = 1/(xi-yj))
x = np.arange(8)
y = x + 0.5
c = 1.0 / np.subtract.outer(x , y)
z = np.linalg.det(c)

#32. Print the minimum and maximum representable value for each numpy scalar type
"""
for dtype in [np.int8 , np.int32 , np.int64] :
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32 , np.float64] :
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
"""

#33. How to print all the values of an array?
np.set_printoptions(threshold=np.nan)
z = np.zeros((25 , 25))

#34. How to find the closest value (to a given scalar) in an array?
z = np.arange(100)
v = np.random.uniform(0 , 100)
index = (np.abs(z-v)).argmin()
z = z[index]
z = index


print(z)


