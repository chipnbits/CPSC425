![](https://i.imgur.com/kKNKfFI.png)
![](https://i.imgur.com/W1NLioW.png)

We apply sift to get feature points as well as their descriptors as we have done before. RANSAC can go through and find the best set of points that are in agreement within some tolerance. The planar transformation was an affine transformation, but if the camera has moved in a projective motion, we can try to actually capture what this motion is.  Once we know the motion we can do triangulation with the stereo images to get the depth and 3D structure from the image.

The motion of the camera itself is prone to drift because each calculation is based off of a delta from the previous frame and the errors accumulate. 

![](https://i.imgur.com/Eki2Tps.png)

**Bundle Adjustment** can help to compensate for this. We find and filter features as before using SIFT and RANSAC, looking for features that are in more than just two frames. Features that are matched across 3 or more views provide stronger constraints on the 3D reconstruction
![](https://i.imgur.com/rKYIRQV.png)

![](https://i.imgur.com/x9TncuQ.png)

We start off with three views and then successively add frames with the new 3D points while jointly optimizing the minimum sum of residuals using least squares.

![](https://i.imgur.com/ucgnsTR.png)

WE iteratively add new cameras and run the SIFT/RANSAC on them to estimate the new camera transition matrix and best fitting points. Then we add these points to the mix and jointly optimize for actual camera motion and triangulation or depth.

![](https://i.imgur.com/CUfqqaI.png)
![](https://i.imgur.com/ttNxrFx.png)
