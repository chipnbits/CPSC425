To downsample an image we should first apply a lowpass filter to it in order to prevent aliasing. This is because as we saw in ELEC 221 the sampling causes a repetition in the Frequency domain that is related to the sampling frequency. The low pass filter ensures that the repetitions do not collide

![400](https://i.imgur.com/bc9AS7l.png)

In general we can capture a *band limited* image using a frequency of sampling that is double the highest frequency. 

![400](https://i.imgur.com/lxfiMfZ.png)

A Gaussian with $\sigma=3$ can be used as a low pass filter.
But also recall the relation between the $\frac{\sin(x)}{x}$ sinc function and the box or sliding window filter. The interpolation of a bandlimited signal can be done by box filtering the lowest frequencies as shown in the image above. This can be done with a smooth sinc function in the time domain.


#### Demosaicing

The grid arrangement for a CCD needs to have its mosaic effect undone to get single pixel values. For example:

![](https://i.imgur.com/HmJfQEA.png)

This naive method can lead some amount of color artifacts. Many techniques use edge information from the densely sampled green channel, and some form of image prior.

The reason that there are twice as many green filters as red and blue is because the luminance signal is mostly determined by green values and the visual system is much more sensitive to high-frequency detail in luminance than in chrominance (a fact that is exploited in color image compression—see Section 2.3.3). The process of interpolating the missing color values so that we have valid RGB values for all the pixels is known as demosaicing

#### The Image Processing Pipeline
![](https://i.imgur.com/KuTfHyu.png)

### Image Processing

![600](https://i.imgur.com/4JPEAQs.png)

![](https://i.imgur.com/66EHDcz.png)


![600](https://i.imgur.com/B6DjVqm.png)

Gamma is the conversion between the actual luminance and the human perception of luminance, especially when it comes to sensor counts.

![](https://i.imgur.com/PFpAgWh.png)


The gamma gives a curve that relates the actual luminance from the detected value

#### Cosine DFT and Image Compression
![600](https://i.imgur.com/goYd1bh.png)

This function can be used to find only the frequency and not the phase dependent parts of the DFT. The structure of it is similar to the DFT

![600](https://i.imgur.com/KZnsQvq.png)

The JPEG will reduce high frequencies with a table

The image is stored as a series of 8x8 blocks and encoded 
![](https://i.imgur.com/iDbIj9U.png)

