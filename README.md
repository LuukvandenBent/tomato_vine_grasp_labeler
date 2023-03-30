# tomato_vine_grasp_labeler
Custom made labeling software to label the correct (2D) grasping position and orientation 

# How to use:
1. : Run the python3 script from a terminal, and place your images in the ./images/ folder. 
2. : Use the left mouse button to click the position of the grasp on the image, click again with the left mouse button to select an angle. 
3. : To try again, click the left mouse and repeat step 2.
4. : If the grasp pose/orientation is satifactoy, click the right mouse button to save the current.
5. : Repeat step 2-4 untill all possible grasping poses are labeled.
6. : Press escape to go to the next image.

All labeles will be saved in the ./labels/ folder in xml format.
