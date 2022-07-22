# ACE Nano
This repo contains the work done to integreate the Nvidia Nano IoT device into the ACE framework. 
It is setup in two components. Jetson setup and the YOLO (darknet) inference server. 

# Projects
Each folder is represenative of its own project. And can be used independently of one another.  

## Jetson Setup
This contains the information needed to recreate the setup that was deployed on the Jetson Nano. 
It contains its own `README.md` which explains the setup process.

## Yolo Object Detector (darknet_infra)
This projcet is containes the inference server for a yolo object detector derived from darknet. 
It contains its own `README.md` which explains the setup and how to run the server.

Note: The weights for the model will need to be downloaded and placed in the appropriate folder:
```
$ wget http://pjreddie.com/media/files/yolov2.weights
```
