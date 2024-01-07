## Derivatives

The derivative is an operator which can be convolved with the original image to get the partial derivatives at all locations. Because of image noise that is inherent in images due to thermal noise in sensors, it is better to first apply smoothing to the image before taking the derivative or else we get large changes from the noise itself on a pixel to pixel basis.

**Convolution is Commutative**
If the derivative operator is modeled as a convolution with a kernel then it does not matter the order in which we apply smoothing or the derivative. So we take the derivative of the Gaussian Kernel first and apply the filter to the original image to recover a smoothed derivative. Noise is being modeled as a random variable with a gaussian distribution for this model.

![600](https://i.imgur.com/iP2oif3.png)

![600](https://i.imgur.com/0TgtyS9.png)

Choosing $\sigma$:
The choice for std deviation determines the response scale. 

When working numerically we have forward, backward, and centered differences that are given as filter kernels that depend on the centering:
![500](https://i.imgur.com/akmICgE.png)

The Sobel gradient also picks up the upper and lower rows by introducing a 1,2,1 weighting.

$$\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
$$

#### Gradient

We can be interested in both the magnitude and the direction of the gradient. Edges result from large changes in the magnitude of the gradient, while corners arise from large changes in direction.

![600](https://i.imgur.com/Q4pimRv.png)


**Edge Detection**
![600](https://i.imgur.com/4wzHsTg.png)

For gradient based edge detection we can try to form connected streams of high intensity gradient that compose the edge.

![600](https://i.imgur.com/HbBFWOz.png)
![400](https://i.imgur.com/mrvU0yn.png)

The orientation field of the gradient is less sensitive to lighting which generally scales the whole image including the gradient magnitude. It is particularly useful for texture characterization.

### Canny Edge Detector

![600](https://i.imgur.com/WorhBi6.png)

![600](https://i.imgur.com/MGrqBTS.png)

1. We apply directional derivatives as shown above to get the gradient vector.
2. Get both the magnitude and the direction of the gradient into two arrays of values for each point that is in the original image.
3. The non-maximum suppression is a policy that checks in the gradient direction to make sure that the point that is found is the local maximum (the interpolated points in gradient direction have a smaller magnitude regardless if the direction)
4. The linking action requires looking at the gradient in directions that are adjacent to it and finding if there is a continuation that is significant enough to carry over the edge further. We can also include some hysteresis in the edge thresholding where a lower threshold is required for edge continuation versus the start of an edge. Typically this ratio is roughly two: $\frac{k_{high}}{k_{low}} = 2$
5. 
### Corners

Corners are of interest because they represent a localized point and are less general than edges.

We can compute an important matrix that will help with identifying corners, it is the symmetric  matrix of second derivatives:

$$
H = \begin{bmatrix}
I_x^2 & I_xI_y \\
I_xI_y & I_y^2
\end{bmatrix}
$$
IWe take the image patch and apply the direction derivatives to get the gradient at each point. The outer product then give the matrix. We then sum over these matrices to form a single matrix that is the sum or average over the patch. In this case we expect there to be two large eigenvalued eigenvectors for a corner representing two primary directional derivatives. I the case of an edge there is only one large eigen value, and in thhe case of noise, there is no large value.

The **Harris corner detector** looks for the local maxima of 
$$
R = \det(H) - k*\text{trace}(H)^2
$$

$k=.5$ can be used for example. It tests that the product of eigenvalues which is the determinant is larger than the square of the average. The product of eigen values is biggest when both values are big, not just one, so it works well as a test.

---
Corners can also be found by comparing a keypoint of an image to find how localized it is relative to surrounding areas. This is the sum squared difference **SSD** function.
![](https://i.imgur.com/Kg93kL8.png)

We compare a local window around the keypoint to shifts in any direction. With an edge we will find one dimension of maintained correlation of the filter kernel, where it looks similar with a minimal trough. With a noisy area things will look roughly the same in all directions as well. With a proper keypoint or 2D feature location, there will be a single defined minimal point:

![400](https://i.imgur.com/ZhHW5k8.png)

Note that **SSD** gives a low value for high similarity. The first order approximation of the SSD function is infact the Harris Corners function described earlier.

![](https://i.imgur.com/qvsQP6A.png)

It is important to note that these values for $I$ are a matrix of values that occur over the region of the patch. The computing implementation can be done as:

![500](https://i.imgur.com/mnhcMa5.png)

When this function is large for all shifts we get a large matrix and in turn large eigenvalues as seen for Harris corners.

We can compute the eigen values for a matrix using the traditional techniques as have been used before:

$(A-\lambda I )x = 0$ which means that a linear combination of column vectors is zero, which means rank deficiency or that the determinant will be zero. We solve for the $\lambda$ values that create this condition in the determinant based polynomial. Using those values we then solve the system using RREF to get the corresponding eigen vector.

### Harris Algorithm:
1. Compute image gradients over small region
2. Compute the covariance matrix 
3. Compute eigenvectors and eigenvalues
4. Use threshold on eigenvalues to detect corners

Some functions that are used to threshold on are as follows:

![250](https://i.imgur.com/dWSknOT.png)

Use the top one in general for now. Note that $C$ is a weighted window, we use a Gaussian weighting instead of a box filter window for the operation to improve results.
$$
A = w *\begin{bmatrix}
I_x^2 & I_xI_y \\
I_xI_y & I_y^2
\end{bmatrix}
$$
where $w$ is a weighting kernel. The box filter would give the basic summation result from earlier when it comes to convolving, but the more general $w$ can be a Gaussian filter.

#### Example
![600](https://i.imgur.com/mdZmBI4.png)

If we are using a $3 \times 3$ window with no Gaussian, then for the location centered at the green pixel we compute the $C$ matrix. The sum of all $I_x I_x$ element-wise is $3$, and the sum of all $I_y I_y$ will be $4$ the $I_x I_y$ case will be $2$  :

![](https://i.imgur.com/mfIJLKe.png)

This gives the value at a single pixel and at this scale. We can window over all of the pixels in a similar manner, and also over all of the colors if it is RGB for example.

### Difference of Gaussian
![400](https://i.imgur.com/PqmcYKJ.png)

The difference of gaussian is a good approximation for the actual Laplacian of gaussian. The width of the $\sigma$ parameter which is measured in pixels indicates over what scale we are performing feature detection

![400](https://i.imgur.com/EDEn8Pw.png)

![400](https://i.imgur.com/HrU5h0q.png)

This is the same as the Laplacian Pyramid that was made earlier. We can search for the local maxima to find blobs at different scales.

in the context of image processing and particularly in multi-scale representations like the Laplacian Pyramid, an "octave" refers to a halving of the image scale. When you move up an octave in such a pyramid, the image's resolution is typically reduced by half, both in terms of width and height. This reduction in resolution means that each subsequent level of the pyramid represents the image at a coarser scale compared to the previous level.

To clarify:

- At the first level (or the base level) of the pyramid, you have the original image at its full resolution.
- At the next level (the first octave), the image's resolution is reduced to half of the original in each dimension, resulting in an image that is a quarter of the original in terms of total pixel count.
![](https://i.imgur.com/sfUsUON.png)

![400](https://i.imgur.com/9BgHVlw.png)

## Feature Detection

**What is a Good Feature Detector?**

- Local: features are local, robust to occlusion and clutter
- Accurate: precise localization
- Robust: noise, blur, compression, etc. do not have a big impact on the feature.
- Distinctive: individual features can be easily matched
- Efficient: close to real-time performance
## Textures

**Texture** is detail in an image that is at a scale too small to be resolved into its constituent elements and at a scale large enough to be apparent in the spatial distribution of image measurements

Sometimes, textures are thought of as patterns composed of repeated
instances of one (or more) identifiable elements, called **textons**.

### Oriented Pyramid

We apply a texture primative filter bank to the image using multiple base kernels, such as:

![300](https://i.imgur.com/uwigtGn.png)

The filters are at different orientations and also over multiple scales, the multi-scaling is where the pyramid comes in.

Steps:
1. Compute oriented pyramid or other filter bank responses at each pixel
2. Square the output (makes values positive)
3. Average responses over a neighborhood or image
4. Take statistics of responses— e.g., histogram of sum-square filter responses over the image
5. Use these statistics to classify different textures

We can consider each filter response to be a dimension, the net response over all filters is a high-dimensional vector.

The average over a neighborhood can be done using a normalized gaussian.

**k-means** algorithm or other clustering methods can be used to quantize the resulting vectors into a single histogram bin. We can use these cluster centers in a nearest neighbor configuration to classify future textures based on a texton dictionary.

#### Texture Synthesis

![](https://i.imgur.com/BnUjbQM.png)

The algorithm scans an existing sample texture to evaluate its SSD over all sample windows that matches the pixel to be infilled within a threshold. Then a random candidate match is selected from the potential matches that are found.

![600](https://i.imgur.com/8gGtsch.png)

When computing the SSD it is better to have a Gaussian dropoff weighting for the matching so we can apply a Gaussian filter to the sum squared differences

$$\sum_{(i,j) \in \text{patch}, (i,j) \neq (0,0)} (A_{ij} - B_{ij})^2 \exp\left(-\frac{i^2 + j^2}{2\sigma^2}\right)$$
A better strategy to find matching neighborhoods is to select all whose similarity value is less than $(1+\epsilon)s_{min}$, where $s_{min}$ is the similarity function of the closest neighborhood and $\epsilon$ is a parameter.

![500](https://i.imgur.com/aLeNSDI.png)

The sum squared distance can also be viewed as being a distance vector lying between two pixel neighborhood patches. The selection algorithm then has an objective to find the nearest neighbors and form a match from them in a stochastic manner. This is the non-parametric modelling or sampling, it is a nearest neighbors approach.

![600](https://i.imgur.com/KVhNWVt.png)

1. Create a short list of a few hundred “best matching" images based on global image statistics
2. Find patches in the short list that match the context surrounding the image region we want to fill
3. Blend the match into the original image 

Purely *data-driven*, requires no manual labeling of images

#### Using CNNs

![800](https://i.imgur.com/NdjqNwk.png)

A CNN that is pretrained to work on visual recognition gives a feature response. Starting from random noise in the original image we minimize the loss in feature space via gradient descent for a loss until we find an image with the same image response. We can also follow the same sort of strategy by looking at the number of activations on a set of filter banks as the feature space which is a bit more classical of a method.