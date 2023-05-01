# Using filters to create mazes -> (filter 2 maze)
How the algorithm works
---
> What is maze creation with filters?
> 1. Generate a matrix of size m*n of random numbers. 

![Alt text](./matrix.png)

> 2. Expand the generated random number matrix by putting a value of zero between each element.

![Alt text](./matrix-T.png)

>> 

> 3. Taking the starting coordinates x,y and the 

        i = x+(-1~1)

        j = y+(-1~1)

>>  Use the formula 

        matrix[i][j]

>> to get the values in the neighbourhood and find the closest value to the value at the curren
<br/> 

> 4. Clear the value of the current coordinates and move to the coordinates found in step 3 and repeat step 3.   
<br/> 

> Tip: The deformation algorithm in step 2 is taken from the process of a **convolutional neural network**.
