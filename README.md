# FlattenVideoCylinder

My mum had a favourite mug, said mug broke and we couldn't find the design anywhere. It was too involved to just draw from scratch so... I wrote some code for fun.

This code takes in a recording of a spinning object, divides the video per frame, and crops a thin, vertical segment at the centre of the frame. 
It then appends all of these segments horizontally to output a single image.

Its intention is to create a flattened image of the surface of a cylindircal shape.

## Video Requirements
There are a lot of assumptions made about the video here and no kind of error correction or aligning done.
The video requires:
- A stable, imobile video (i.e. prop up your camera and make sure it doesn't budge)
- An object centrally aligned in the middle of the camera (vertically and horizontally)
- An object rotating about its central vertical axis, with no precession
- Object rotating at a constant rate
- The video must start and stop when the rotation starts and stops (so crop in time if necessary)

- The best results come from a high frame rate video, high resolution video, and slow (but not snail-paced) rotation speed.
  - Yes there is probably some optimal combination of these factors, no I haven't worked it out. I spun the mug a few times and picked the best output, it was Christmas...
 
In layman's terms, place the object in the middle, on a flat surface, make sure it doesn't move in any direction other than spinning like a (slow) Beyblade.

Obviously, many of these aspects are difficult to control in a home environment. I recommend:
- Most microwave ovens have a rotating plate and wheel set. This works a charm, just place your object in the middle and turn
- Controlling the rotation speed is near impossible. Try and do it as consistently as you can (from experience, a very fast rotation will give the most uniform result but also lowest quality (unless you have a very fast camera, slow-motion on some phones perhaps I didn't try)
  - Maybe you have a remote control car or a rotating power tool you can keep pressed very lightly with a rubber wheel attached to the end, to spin the microwave oven plate slowly and uniformly. Or maybe you have a lab-based set up, who knows, the world is your oyster.
- Set up your phone as stabley as possible, maybe slightly raised if necessary to make sure it is as close to central as possible to both vertical and horizontal axes


## Python requirements:
- Python3 (written in 3.12)
- Packages: cv2, numpy, sys

## Usage:
- python Cylinder2Flat.py <input_video_path> <output_image_path> <clockwise (bool)>
  - Arguments:
    - input_video_path: The path/name of an .mp4 file
    - output_image_path: The path/name of the output .png file
    - clockwise (bool): "true/false", is entirely dependent on whether your video has an object turning clockwise (to the left) (true) or anticlockwise (to the right) (false)
   
## Disclaimer:
I made this as a fun mini-project just to recreate the surface of my mum's mug after it broke. The result wasn't perfect, but good enough to apply some post-processing colour correction, edge detection and a little bit of editing magic for blemish removal.
In theory, it should produce a perfect result, if the video conditions are also perfect, which they will never be...

Feel free to fork and modify this for fun, I hope it can help some people out (or inspire to do better), but I'm unlikely to make any modifications beyond this initial push. 
