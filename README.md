# metalDimInspect

A work in progress sheet metal detection project that aims to reduce scraps by reporting defective cuts. Relies on opencv image processing functions. Project for my internship that started mid july. 


# Some History
Initially, I thought that I could just find a rough estimate of the maximum foreground/minimum background through using the watershed function and image segmentation, but this proved to be rather difficult since not only is the camera black and white, but is also taking pictures of... gray metal on a gray background. This process might have worked with better contrast, but if I were to go down the path of finding the bounding box/least bounding box, there would be approximation errors and biases. 

After some tinkering, I found it to be much more reliable if I detected lines using the built in opencv Hough line transform algoithms. Although they are better for detecting lines rather than measuring them precisely, it was a step in the right direction. I thought that the individual lines would not be subject to the "snapping" nature of the bounding box function. One thing that was particularly tricky about this approach was finding the intersections. The problem was that if I were to iterate through all of the lines and determine the intersections that they had with the other lines, I may have ended up with the possiblity of intersecting two lines that were near-parallel. I decided to tackle this by creating four "filter" lines that would detect if another line intersected with it, and verify that the point of intersection was within the screen. 

![image](https://github.com/cascino/metalDimInspect/assets/103715998/57b585e3-b143-48dc-bc74-88a9505fc1c7)


This proved to be so-so, since the camera was not to move on the production line anyways. However, if you notice that there are two lines in the top right corner, you might realize one pitfall of the line detection method, which was that there was no reliable way to deal with incisions along the metal surface being detected as potential candidates for the hough line function. I tackled this by just picking the line with the most "votes", since the hough line function returned a list of lines in the image sorted by vote confidence. 

![image](https://github.com/cascino/metalDimInspect/assets/103715998/d98cc5e3-1eb0-47f0-9e8c-ccaf4e0e95f2)


This was not super satisfactory, since sometimes the lines with the most confidence were still wrong lines. Instead, I began playing around with the idea of first finding some possible lines candidates, and then "zooming" in on their regions again, but this time to process with more confidence. This process proved to be much more accurate, since a) the built in Canny function works better on smaller images, and b) I could manually adjust the parameters for finding lines, processing the image, etc. on the smaller regions. 

![image](https://github.com/cascino/metalDimInspect/assets/103715998/7fc0ecca-80b7-41cf-91b1-384e7f5d06a9)

After processing the individual "snippets", I would find their new coordinates on their shifted canvases and apply an offset to bring them back to where they originally were on the source image. Here are the calculated pixel results of a few trials. Since we know that the sheet metal (before shearing at least) is rectangular, any differences between side measurements are error. For this camera, 10 pixels is about 2mm, which is beyond the tolerance level for the customers needs. 

![image](https://github.com/cascino/metalDimInspect/assets/103715998/f49613a6-17b2-4a60-b809-10dbffd93649)



# Next Steps
The week beginning july 31 will see the installation of another prototype camera above the shear line. I will be working with people on the floor to try and see if this early stage of a dimension measurement system is of any use. I may also get a chance to perhaps integrate some form of template matching, but I am afraid that the time will be too long. Since this is a live process, I was given the restraint that the robots could not wait on the line for more than half a second.


Thanks for reading!

-Jesse




Since I don't really know how to use github that well, I have included several past iterations of projects in the files as well. This is like my first time making a readme as well, sorry.... 
