### Sum Square Difference Template Matching

![600](https://i.imgur.com/GYLTr3q.png)

If the vectors or pixel bodies that are being compared are normalized, then talking the sum squared difference gives a nested dot-product or correlation indication.
![600](https://i.imgur.com/ggZXlsV.png)

To implement this correctly it is easy to normalize the template or filter but the image section that is being filtered also needs to be normalized. There is an efficient method of correlation as follows:

![600](https://i.imgur.com/KrSdJ0D.png)

In step 2 we can convolve the whole image to get the norm that is centered at that pixel along with element wise squaring and sqrt before and after.

#### Threshold Selection
![](https://i.imgur.com/91PKxvg.png)
![400](https://i.imgur.com/BNz4PgQ.png)

More info on ROC in ML can be found at https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc

![400](https://i.imgur.com/oGSK1iZ.png)


#### Pyramid Scaling
![](https://i.imgur.com/GkYUMvh.png)

Pyramid scaling applies a sequence of filtering and down sampling to achieve results.

![300](https://i.imgur.com/FCTJTlq.png)

**Applications**

The pyramid allows for inspection of the image at different scales of coarseness. The 128 or 64 image above might be better for observing the level of detail required for the stripes of the zebra.

We can use the downsampled images in *facial recognition* by finding the right stage that matches the coarser features that form the face

A spatial search may try to *match a point* in one image to another which could be inefficient. Instead we look for a match in a heavy smoothed and downsampled image. We can then refine the search working back up the pyramid in the smaller search window.

*Feature Tracking* is another application.

### Laplacian Pyramid
We make the same Gaussian pyramid as before but now the reconstruction values are stored for the intermediate steps:
![600](https://i.imgur.com/i4hrZAI.png)
Basically the low pass and high pass portions are both stored which makes the step-down lossless.

![600](https://i.imgur.com/cwTrhOJ.png)

The Laplacian is an approximation of an exact low pass filter as shown with the sinc function.

![600](https://i.imgur.com/DcarNeO.png)

#### Reconstruction

1. **Upsampling:**    
    - Start with the smallest (topmost) level of the Laplacian pyramid.
    - Upsample this image to the size of the next level in the pyramid. This upsampling can be done using nearest-neighbor or linear interpolation, but this will create a blocky, pixelated image.
2. **Smoothing (Important):**    
    - After upsampling, the image should be smoothed to reduce the pixelation and artifacts. This smoothing is often done using the same Gaussian filter that was used during the downsampling process.
    - The purpose of this step is to interpolate the upsampled image in a way that approximates the original smoothing that occurred during the downsampling. Without this smoothing step, the reconstructed image would have aliasing artifacts.
3. **Adding Back the Laplacian Level:**    
    - Once the image is upsampled and smoothed, add the corresponding level of the Laplacian pyramid to it. This step reintroduces the detailed information (like edges) that was lost during the downsampling process.
    - This addition is what differentiates the Laplacian pyramid reconstruction from simple Gaussian pyramid reconstruction. It allows the restoration of details that would otherwise be lost.
4. **Repeat for Each Level:**    
    - Repeat this process (upsample, smooth, add the Laplacian level) for each level of the pyramid until you reach the original size of the image.
5. **Final Image:**    
    - The final step should give you an image that closely approximates the original image, with much of the detail restored.