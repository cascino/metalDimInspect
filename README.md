# metalDimInspect

A work in progress sheet metal detection project that aims to reduce scraps by reporting defective cuts. Relies on opencv image processing functions


Initially, I thought that I could just find a rough estimate of the maximum foreground/minimum background through using the watershed function and image segmentation, but this proved to be rather difficult since not only is the camera black and white, but is also taking pictures of... gray metal on a gray background. This process might have worked with better contrast, but if I were to go down the path of finding the bounding box/least bounding box, there would be approximation errors and biases. 

After some tinkering, I found it to be much more reliable if I detected lines using the built in opencv Hough line transform algoithms. Although they are better for detecting lines rather than measuring them precisely, it was a step in the right direction. 




![image](https://github.com/cascino/metalDimInspect/assets/103715998/7bc0cac1-5618-4155-8f17-f4437a3f81bd)






Current Progress:
![image](https://github.com/cascino/metalDimInspect/assets/103715998/3b5a750d-b7f4-4174-a24e-493a803f1c8e)






Since I don't really know how to use github that well, I have included several past iterations of projects in the files as well. 
