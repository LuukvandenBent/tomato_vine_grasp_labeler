# tomato_vine_grasp_labeler
Custom made labeling software to label the correct (2D) grasping position and orientation 

#How to use:
Step 1: Run the python3 script from a terminal, and place your images in the ./images/ folder. 
Step 2: Use the left mouse button to click the position of the grasp on the image, click again with the left mouse button to select an angle. 
Step 3: To try again, click the left mouse and repeat step 2.
Step 4: If the grasp pose/orientation is satifactoy, click the right mouse button to save the current.
Step 5: Repeat step 2-4 untill all possible grasping poses are labeled.
Step 6: Press escape to go to the next image.

All labeles will be saved in the ./labels/ folder in xml format.
