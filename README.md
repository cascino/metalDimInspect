# metalDimInspect

A work in progress sheet metal detection project that aims to reduce scraps by reporting defective cuts. Relies on opencv image processing functions. Project for my internship that started mid july. 

# Some History
Initially, I thought that I could just find a rough estimate of the maximum foreground/minimum background through using the watershed function and image segmentation, but this proved to be rather difficult since not only is the camera black and white, but is also taking pictures of... gray metal on a gray background. This process might have worked with better contrast, but if I were to go down the path of finding the bounding box/least bounding box, there would be approximation errors and biases. 

After some tinkering, I found it to be much more reliable if I detected lines using the built in opencv Hough line transform algoithms. Although they are better for detecting lines rather than measuring them precisely, it was a step in the right direction. I thought that the individual lines would not be subject to the "snapping" nature of the bounding box function. One thing that was particularly tricky about this approach was finding the intersections. The problem was that if I were to iterate through all of the lines and determine the intersections that they had with the other lines, I may have ended up with the possiblity of intersecting two lines that were near-parallel. I decided to tackle this by creating four "filter" lines that would detect if another line intersected with it, and verify that the point of intersection was within the screen. 

![image](https://github.com/cascino/metalDimInspect/assets/103715998/7bc0cac1-5618-4155-8f17-f4437a3f81bd)

This proved to be so-so, since the camera was not to move on the production line anyways. However, if you notice that there are two lines in the top right corner, you might realize one pitfall of the line detection method, which was that there was no reliable way to deal with incisions along the metal surface being detected as potential candidates for the hough line function. I tackled this by just picking the line with the most "votes", since the hough line function returned a list of lines in the image sorted by vote confidence. 

This was not super satisfactory, since sometimes the lines with the most confidence were still wrong lines. Instead, I began playing around with the idea of first finding some possible lines candidates, and then "zooming" in on their regions again, but this time to process with more confidence.  





Current Progress:
![image](https://github.com/cascino/metalDimInspect/assets/103715998/3b5a750d-b7f4-4174-a24e-493a803f1c8e)






Since I don't really know how to use github that well, I have included several past iterations of projects in the files as well. 
