
To track across images we need to be able to match locations between the two images and ideally these mapping points are rotation, translation, scale, and even perspective invariant.

The main step to begin with is to select good feature keypoints. Canny edges, Harris corners, with difference of gaussian pyramids or MSERS. Corners make for good feature points because they can be located in 2D, while edges are 1D features.

Harris corner detection is a good way to find corner features or points of interest. We use the gradient around the pixel being evaluated after filtering the image with a Gaussian (or likewise we can apply a gaussian gradient filter.) We then sum using either a box weighting or a gaussian weighting on the covariance (Harris) matrix and then do some type of eigen value analysis to recover a corner strength.

#### LoG

The Laplacian of gaussian actually looks for maxima across scale and space in the sub-octave set of Laplacian pyramid images. This is a complementary operation to the Harris corners detector. The operation can be applied to found Harris corners to determine their scale at which they occur.

For the regular LoG or DoG approach, the hessian of the image can be computed for all the pixels and the keypoints can be verified for too much asymmetry which would indicate an edge instead of a corner.

![](https://i.imgur.com/Xo5rJlZ.png)

#### MSERs
Maximally Stable Regions
![500](https://i.imgur.com/nMaKMJv.png)

The goal of these keypoints is to have affine transformation invariance.

To detect MSERs, binary regions are computed by thresholding the image at all possible gray levels (the technique therefore only works for grayscale images). This operation can be performed efficiently by first sorting all pixels by gray value and then incrementally adding pixels to each connected component as the threshold is changed (Nist´er and Stew´enius 2008). As the threshold is changed, the area of each component (region) is monitored; regions whose rate of change of area with respect to the threshold is minimal are defined as maximally stable. Such regions are therefore invariant to both affine geometric and photometric (linear bias-gain or smooth monotonic) transformations.

![500](https://i.imgur.com/9YiCDRn.png)


**Rotational Invariance**
Once establishing a good keypoint it is best to work from within local coordinates. Once the local orientation and the scale of the keypoint are extracted they can be normalized back to a single scale and orientation for comparison. For this reason we look at the dominant orientation. The gradient direction is useful for this computation.

We could take an average of all the orientations weighted by their magnitudes or thresholding out small magnitudes such as noise. This can be accomplished with a convolution with the gaussian gradient result and essentially a box filter, it is best if the filter size is larger than the gradient window that was used though (larger neighborhood scan).

Using a binned histogram can be more effective when dealing with smaller gradient magnitudes.

![500](https://i.imgur.com/wDoCOVg.png)


### SIFT

![500](https://i.imgur.com/Prpy0nz.png)


##### Selection and Detection:
Use a LoG or DoG filter and find the local maxima for the response. These are areas where the laplacian is strong which indicates a lot of curvature in the image gradient.
![400](https://i.imgur.com/9yORnK2.png)

The exercise is repeated over octaves that have around 4 images per octave so that the maximum is located both in space and in scale. A maximum must be present in a $3 \times 3 \times 3$ sized window to be included. The coordinate along with the scale at which it occurs is recorded and labeled on the image.

This gives the scale and position selection for the feature. Note that the Laplacian is rotationally invariant for a 2D function.

##### Orientation Selection
The orientation is found by taking a histogram of all the different gradient vectors over a neighborhood. Some of these methods have been also listed earlier.

![400](https://i.imgur.com/8w1oYR8.png)

##### Descriptor

Once the location, scale, and orientation have all been determined then the keypoint can be added as a sort of dictionary entry, along with a descriptor. We create the descriptor in terms of the *local* coordinates for that keypoint. It should aim to be invariant to distortions, lighting changes, etc.

A histogram of entries computed at the descriptor scale can be used, with the peak histogram bin giving the 'orientation'.  multiple surrounding patches can be used to reconstruct the larger neighborhood around the localized patch and to provide a solid basis for a match.

![500](https://i.imgur.com/L91pQCd.png)

The descriptor is a 128 dimension vector:
![500](https://i.imgur.com/w0MyKYh.png)
![300](https://i.imgur.com/cz7eYJG.png)

The descriptor is normalized to suppress the effects of change in illumination intensity.
The descriptor is a set of histograms of image gradients that are then normalized. These histograms expose general spatial trends in the image gradients in the patch but suppress detail.

#### Recap

![500](https://i.imgur.com/jk3GCLM.png)

#### Matching

The goal to track objects between pictures then is to have a list of SIFT features and descriptors for two images and then try to match a good series of points between the two. 

One way to do this is to make a nearest neighbor match in the normalised 128-D space (recall that we are comparing the two points from their respective local coordinates.)

We need to know if this a *good* match though, so to do this we can compare the nearest neighbor against the 2nd nearest one and ensure that the nearest point is distinctly matching:

![500](https://i.imgur.com/noy1Otk.png)

Feature matching returns a set of noisy correspondences, to get further, we will have to know something about the geometry of the images.

## SIFT Database

We can try to match against a known database of SIFT descriptors that are available. In this case we are trying to match against a very large set of photos and it would be easy to mismatch when only checking against 1-NN so for this reason the check is don against the second nearest.  Once a match has been made then the transform from the original (often planar) instance can be made by finding the affine transform. Once the transform is found then we can run a pose prediction which will fill in the space where the object may be that is even occluded. 

![500](https://i.imgur.com/6SVsK0F.png)


