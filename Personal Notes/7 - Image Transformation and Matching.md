Once we have extracted features from images, the next stage in many vision algorithms is to match these features across different images. We use homogenous coordinates which make it easy and convenient to apply many of the operations on geometric spaces using matrices where something like translation would not be possible with just a matrix. It allows for chaining the operations after. To convert over to homogenous coordinates, just add an extra $1$ dimension. To convert back, divide the whole vector by the extra $w$ value to renormalize, then convert that the a lower dimension.  In effect this is the same as dividing by $w$ on the $x$ and the $y$ coordinates. For a $w=0$ it means that the coordinate is off at infinity.

![700](https://i.imgur.com/bCBjWSv.png)


![400](https://i.imgur.com/nFiBuKv.png)

For **affine** transformations the transformed points are a linear function of the input points.

>[!example]
>Let's compute an affine transform from correspondences:
$$
\begin{bmatrix}
x' \\
y' \\
1
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

![350](https://i.imgur.com/icFGYsw.png)


#### Mapping Images
We can compute the affine transformation that is present in between two different images by comparing the locations of the feature points and then finding how many and which parameters are needed to fit in-between them. 

Some of the simpler transformations are simpler subsets of the more general affine transformation:

![550](https://i.imgur.com/OVPhDv0.png)

##### Projective Transforms

We add an $s$ as a scaling factor and require at least $4$ points to form a mapping:

![500](https://i.imgur.com/aupD96a.png)

![500](https://i.imgur.com/CgBKjb1.png)


#### LS Regression
Once we have a set of feature point matches we can perform a least squares regression to find the matrix weights for a most general matrix transformation, the projective. Note that all the other transforms are a subset of a projective transform.

Likewise we can compare the change in position: $\Delta \mathbf{x} = \mathbf{x'} - \mathbf{x} = \mathbf{J}(\mathbf{x})\mathbf{p}$  where we then solve for the linear regression of:

$E_{\text{LLS}} = \sum_i \left\| J(x_i)p - \Delta x_i \right\|^2$

Often is is good to add an uncertainty weighting when doing least squares  for each point, since some matches are better than others and this will reduce the impact of outliers.

While linear least squares is the simplest method for estimating parameters, most problems in computer vision do not have a simple linear relationship between the measurements and the unknowns. In this case, the resulting problem is called *non-linear regression.*

#### RANSAC
![](https://i.imgur.com/tDUOYyW.png)
![500](https://i.imgur.com/rpWv4kS.png)



![450](https://i.imgur.com/25zD8Xf.png)

The example above is for a transform, so we only need to match two points. We compute the transform as shown above, then we check the total number of points that can still be classified as inliers withing some threshold value that is given by $\epsilon$ usually just a few pixels of difference is desired. We check the number of inliers that are still remaining.  The goal is to find the "test transform" that can maximize the number of inliers. Once we have the best hypothesis for a match, we perform least squares only using the inlier values.

#### Required Number  Of Points

Assuming a probability that a randomly drawn feature match is correct or an inlier we get $p(\text{inlier})= 1 - p_{o}$  or the complement to it being an outlier. The probability of getting a somewhat correct transformation match that uses $n$ points is $p_i^n$ because we need all $n$ points ($n=3$ points for affine transform for example) to be an inlier. We can then run a number of trials to try and find a good match. The probability of all of them failing is $P_{\text{fail}} = (1-p_i^n)^k$ 

We find solutions to this for a desired max probability of failure and $n$ to come up with the minimum number of samples that are required.  The following gives a good chart for reaching the $99\%$ success rate:

![500](https://i.imgur.com/lLS3r0B.png)


![500](https://i.imgur.com/4OcTIGd.png)


