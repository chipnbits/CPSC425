Estimating the shift between images earlier using SIFT and RANSAC using a fitted homography matrix $H$ fits all of the points into a single plane for it to be considered a projection transform.
![](https://i.imgur.com/NZZCjIF.png)


$\mathbf{R}$ represents a rotation matrix and $\mathbf{K}$ is a calibration matrix for a camera. The calibration can be done using a calibration scene that uses premeasured feature point distribution points in the FOV of the camera in order to determine the correct weights in the matrix.

The rotation matrix is dependent on the tilt of the actual camera in space relative to a common coordinate system
![](https://i.imgur.com/qTD20Bf.png)


The three points all lie in the same epipolar plane which gives what must be a volume of zero for the triple product. $p_2^T (t \times p_1) = 0$ 

This can be rewritten as a system of equations where $t = t_2-t_1$ and:
$p_1 \sim\mathbf{R}_1^T \mathbf{K_1}^{-1} u_1$    and  $p_2 \sim\mathbf{R}_2^T \mathbf{K_2}^{-1} u_2$   

### Computing Depth

The process to recover this information from two camera images in a stereo setup is to first compute common features with ratio test filtering using *SIFT* 

The features should show alignment over what would be the epipolar lines in the image. Once the points have been matched in both views we can use triangulation along with the $u_1$ and $u_2$ positioning to get the depth for each point.

![](https://i.imgur.com/B4RyqBj.png)

![600](https://i.imgur.com/dpdZ3rA.png)

$f$ is the focal distance and the formula comes from similar triangles

$u_1-u_2$ is the disparity
#### Stereo Camera Mapping
A simple configuration to explore for stereo imaging is two cameras that differ by translation and no rotation. In this case all the epipolar lines are horizontal.

**Stereo Rectification** takes images from two axes that are not optically aligned and applies a rotation (homography) to each of them to transform into an adjusted image that is optically aligned. This can be done by rotation so that the epipolar lines are horizontal for both images. Once the images are rectified then the class of techniques for two optically aligned images can be applied to them

For normalized windows we can find the SSD of the two by taking the dot product to get an angle of correlation for the two vectors. The best match along the epipolar line is going to be where the angle is smallest or the dot product is at a minimum.

![](https://i.imgur.com/62yKYJl.png)

The offset that is found can be viewed as the disparity, $u_1 - u_2$ . The depth

![400](https://i.imgur.com/nXmN5dF.png)

Oclussions and reversed ordering may be present in the stereo image:

![500](https://i.imgur.com/62u8AF0.png)

### Optical Flow

The stereo matching is done by searching for correspondence along a 1D epipolar line. The line is best found with aligned cameras, if they are not in alignment then a calibration can be performed to recover the rotation matrix along with the translation vector and rectification performs homography to return the images to horizontal epipolar lines. However with motion of the image subject, two frames can have movement in 2D space, we can't use epipolar lines to constrain to 1D

The motion of brightness patterns is known as *Optical Flow*. This motion can be from the subject or also from the camera itself.

![500](https://i.imgur.com/icAvanj.png)

Here in this example we have two sequential images:
![500](https://i.imgur.com/EPbdqaj.png)

Here the $I$ is referring to an image patch, $x$ is the vector location, $u$ is the difference in location.
The first order approximation gives $I(x+u) = I(x) + \nabla I(x) \cdot u$ 

The difference in unshifted images is $I_1 -I_0 = r$  is the residual and $J \Delta u$ is the gradient dot product

If we minimize the sum least squares: $|J \Delta u - r|^2$ then we can solve for $\Delta u$ to find the best fit for an overall frame shift in the image. The sum is done over all $x$ positions for some patch $I$

![](https://i.imgur.com/14Gmwfh.png)

The single patch can also have an optical flow assiciated to it. We look at the time difference and the motion difference to get a velocity.

![500](https://i.imgur.com/dy4LO14.png)

This allows for detection of motion based on overall brightness changes in the pixel value when the motion has occurred in a direction that is along the gradient.

![](https://i.imgur.com/ETutPLX.png)

To compute all of this we need the partial derivatives for $x,y$ at the image patches, which can be done using a filter or the forward difference.  The time derivative can be found from the frame differencing

![](https://i.imgur.com/YaO6Eau.png)


![](https://i.imgur.com/JDwM66M.png)

![](https://i.imgur.com/CtJvc72.png)

The flow ambiguity in the problem is exactly what leads to the barber pole effect or the aperature problem that was discussed earlier. All that we are able to compute is the amount of visual motion that is perpendicular to the contour line at that point in the image, or in line with the gradient.

When we have many points though, and we make the assumption that they are moving as part of a rigid body, then we can find a least squares solution to recover $u$ and $v$ as part of fitting of many equations. 

![](https://i.imgur.com/DvhrRgt.png)

This matrix is also what was used to find corners when it comes to corner detection. We get the flow vector by looking at a larger window of pixels as a rigid body.

### Optical Flow with Smoothness Prior

![](https://i.imgur.com/a7fLS8T.png)

we can add a smoothness prior by adding regularization to the motion of $u$ and $v$

![](https://i.imgur.com/blgUz8b.png)

#### Brightness Assumption

![](https://i.imgur.com/7oHkE4Z.png)

Since we are comparing pixel intensities to diffentiate motion, it is important to note that we must make a brightness constancy assumption for this to work. Over the small intervals between frames this fairly reasonable as long as the lighting has not drastically changed. This assumption on the larger flow function $I(x,y,t)$ with a change of zero means that the  total derivative is zero and recovers the same optical flow equation.

![](https://i.imgur.com/ttMQVTq.png)
