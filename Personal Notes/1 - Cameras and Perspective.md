### Math and Vectors
![300](https://i.imgur.com/GMFRDe0.png)


<!--⚠️Imgur upload failed, check dev console-->
![[Pasted image 20231224135615.png]]
In images we are looking at a 2d projection onto the plane facing us. So a position in 3D space can be normalized by removing the $w$ component completely and working more closely with the underlying projection.

If we apply this to $$\mathbf{\bar x} \cdot \mathbf{l} = 0$$ for the definition of a line, then the augmented vector form is essentially fixing the distance $w$ at one value in the equation. The $\mathbf{\bar x}$ is a freely moving coordinate system for $x$ and $y$ while the normal vector $\mathbf{l}=(a,b,c)$ is fixed

### Light Refection

**Diffuse Reflection**

The light scatters in all directions and the intensity is dependent on the surface incident angle and a diffusion coefficient. The power intensity diminishes with shallower angles but it conserves the total power that is incident on the surface:

![Uploading file...2pwvr]()

This gives the formula $$I_d = k_d i_d \cos \theta$$
**Specular Reflections**

The other component is one of specular reflection which is only over a smaller range that is more of a reflective mirror effect from the light source. Either a cosine power or an exponential rule can be used. Here the angle is measured as the distance off from the perfect reflection $\phi$

![](https://i.imgur.com/hkR6b1y.png)

**Focal Lengths**

The diagram uses similar triangles to show that $x' = f' \frac{x}{z}$

This same scaling applies to the $y'$ coordinates and so overall everything is scaled by this factor of $s$


![500](https://i.imgur.com/sYTRhz7.png)
![500](https://i.imgur.com/c9fdguY.png)

The orthographic projection treats the object as though it is at infinity so that $<x,y,z> \rightarrow <x',y'>$ 

![](https://i.imgur.com/FCgbVKj.png)

#### Field of View

![](https://i.imgur.com/rWSQcba.png)
![](https://i.imgur.com/DzdujFb.png)


#### Focal Length and Lensing

![](https://i.imgur.com/MMAMbcX.png)

![](https://i.imgur.com/0O1zeLq.png)

At infinite distance the focusing distance is the same as the focal length.

>A 50mm lens is focussed at infinity. It now moves to focus on something 5m away. How far does the lens move?
>$\frac{1}{50} = \frac{1}{5000} + \frac{1}{z_i}$
>50.5mm distance so the movement is 0.5mm

Smaller aperture ⇒ smaller blur, larger depth of field

![500](https://i.imgur.com/mQ7S0l2.png)

Aperture size = f/N, ⇒ large N = small aperture


#### Refraction
![](https://i.imgur.com/9WaFxq6.png)



