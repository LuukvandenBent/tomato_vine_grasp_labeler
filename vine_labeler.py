import cv2
import numpy as np
import copy
import os
import xml.etree.cElementTree as ET
from pathlib import Path

class DetermineGraspPoseManual():
    def __init__(self):
        self._reset()
    
    def _reset(self):
        self.x, self.y, self.angle = None, None, None
        self.image, self.image_copy = None, None
        self.labels = []
    
    def load_images_from_folder(self, folder="./images/"):
        self.images = []
        self.filenames = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            if img is not None:
                self.images.append(img)
                self.filenames.append(filename)
        
    def click_event(self, event,x,y,flags,param):
        #Click once for a point, second time for a angle, third time to reset
        if event == cv2.EVENT_LBUTTONDOWN and self.angle is not None:
            self.x,self.y,self.angle = None, None, None
        elif event == cv2.EVENT_LBUTTONDOWN and self.x is not None:
            p1,p2 = ((x-2*(x-self.x), y-2*(y-self.y)),(x,y))
            self.angle = np.arctan2(y-self.y, x-self.x)
            cv2.line(self.image, p1, p2, (255,0,0), 2)
        elif event == cv2.EVENT_LBUTTONDOWN:
            self.angle = None
            if self.image_copy is not None:
                self.image = self.image_copy
            self.image_copy = copy.deepcopy(self.image)
            self.x, self.y = x,y
            cv2.circle(self.image, (x,y), 5, (255,255,255), 1)
        
        #Keep current pos/orientation
        if event == cv2.EVENT_RBUTTONDOWN and self.x is not None and self.y is not None and self.angle is not None:
            self.labels.append([self.x, self.y, self.angle])
            self.image_copy = copy.deepcopy(self.image)
            self.x, self.y, self.angle = None, None, None
            
    
    def process_images(self):
        for i, image in enumerate(self.images):
            self._process_individual_image(image = image, filenames=self.filenames[i])
    
    def _process_individual_image(self, image, filenames):
        self._reset()
        self.image = image
        cv2.namedWindow('select_grasp_pose')
        cv2.setMouseCallback('select_grasp_pose', self.click_event)
        while(True):
            cv2.imshow('select_grasp_pose', self.image)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()
        
        #SAVE LABELS
        root = ET.Element("label")
        for i, label in enumerate(self.labels):
            doc = ET.SubElement(root, f"grasp_point{i}")

            ET.SubElement(doc, "x").text = str(label[0])
            ET.SubElement(doc, "y").text = str(label[1])
            ET.SubElement(doc, "angle").text = str(label[2])

        tree = ET.ElementTree(root)
        tree.write(f"./labels/{filenames}.xml")

if __name__ == "__main__":
    Path("./labels/").mkdir(parents=True, exist_ok=True)
    Path("./images/").mkdir(parents=True, exist_ok=True)
    labeler = DetermineGraspPoseManual()
    labeler.load_images_from_folder()
    if len(labeler.images) == 0:
        print("NO IMAGES FOUND")
    labeler.process_images()