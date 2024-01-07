### Convolutional Kernels and Filters

#### Correlation vs Convolution 

![600](https://i.imgur.com/NI1kLml.png)

**Intuition**
Correlation is a sliding window dot product, convolution is a sliding window impulse response. In a conv neural network where the values are learned, the two are interchangeable since for a sliding window, the rotation of one gives the other.

![600](https://i.imgur.com/OsapAjM.png)
![600](https://i.imgur.com/Lr7RfxZ.png)

#### Box Filter
![200](https://i.imgur.com/rVEXvkv.png)
It is a smoothing or averaging filter

#### Pillbox Filter
![600](https://i.imgur.com/Vmi09kG.png)
It is a circular shape instead of the square box
Good for camera blurring
Not separable
#### Gaussian
For blurring we can use a normalized Gaussian kernel such that the sum of elements is one for a $2k+1 \times 2k+1$ kernel. The array construction is given as:

![](https://i.imgur.com/viw4IjB.png)

For the $i,j \ th$ element. Sigma controls the width of the Gaussian. Note that the center pixel will always be 
![600](https://i.imgur.com/torWEBV.png)
A good guideline for the Gaussian filter is to capture ± 3 $\sigma$ so for $\sigma = 1$ this is a $7\times7$ filter The filter also needs to be normalized to one, usually also using a rational expression:
![200](https://i.imgur.com/sSDelCX.png)

#### Derivative

#### Separable Filters
Kernel size $K^2$ Can be separated into a vertical and horizontal convolution if it is formed from the outer product of two vectors, the horizontal and the vertical elements. We can check if the kernel is seperable by taking the SVD and checking that it only has one non-zero singular value. The resulting vectors give the parts of the outer product. 

If a filter is separable then the convolution can be done as two passes of 1D filters for a total cost of $2K$ which is a large computational advantage. The order of 1D convolutions does not matter

#### High/Low Pass
The blurring filters tend to be low pass. A high pass filter can be made by subtracting the low pass from the original image to isolate the high frequency content.

#### Perimeter Handling
![600](https://i.imgur.com/OOaTTY4.png)

### Non-Linear Filters
These will not have the property of superposition. A good example is a median filter of a max-pooling filter.

![600](https://i.imgur.com/oHjWCQI.png)

#### Bilateral Filter

This is similar to the Gaussian where weights are determined by the distance from the center point, but in this case we also take into account the z-coordinate for the pixel in space as well for the weighting. So the kernel to be used is not solely $X,Y$ values but also the pixel values. Pixels that are closer in value exert more influence

![600](https://i.imgur.com/xjRyHCR.png)

Note that there are two sigma values, one that is for domain distance, and the other one is for range. The range kernel works best when it has first been normalized for the image:

![600](https://i.imgur.com/25qQK6a.png)

The filter can work well for denoising without blurring all the edges of the picture![](https://i.imgur.com/OW9oWmr.png)

It can also be used to create a cartoon effect:
![600](https://i.imgur.com/FrURw2T.png)

If a second image is used for the range kernel (the edge or similarity), the Gaussian denoising and range kernel can be combined to give detail transfer:

![600](https://i.imgur.com/sFpjHHa.png)

#### ReLU 

![600](https://i.imgur.com/3ard1qj.png)

We apply the filter and the use ReLU for clipping the negative values. This opens up the possibility of using filters with negative values

![](https://i.imgur.com/TPRQhti.png)


