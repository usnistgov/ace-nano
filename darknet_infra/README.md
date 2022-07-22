# Yolo ACE Analytic
ACE Analytic: Yolo Object Detector using coco labels. 

This analytic integrates a YOLO object detector with ACE. This is done in a four step process:  registering the analytic, using ACE video frame handler to get video frames, yolo to process video frame, and ACE video frame handler to return results.
This example highlights the ease which ACE can integrate with analytics. 

Note: many of the commands' scripts have placeholder that will need to be adapted to your network/ACE configuration to work properly.

## Setup

### Download Yolov2 Weights
Download Yolov2 weights using the command `$ wget http://pjreddie.com/media/files/yolov2.weights` and place them in the `data/yolo` folder.

### Build
Build the container using the `build.sh` script. This container is built for a jetson nano.

## Run Analytic

### Quick Start
Run `detect.sh` in the base repo. This will stop all docker containers, start the container, and then start the analytic. 

### Scripted Start
Use Scripts to automate process.
1. Start Docker container with `run_bash.sh`. Verify the working dir is `/code`. All the following commands are meant to be run from within the container.
2. Start analytic with `run.sh`. This will both registar the analytic with the remote server, and start the yolo analytic.


### Run Detector Manually

This example runs yolo as an ACE Analytic, and connects to a remote server to provide results to the user. This is a multi-step process:
1. Start Docker container with `run_bash.sh`. Verify the working dir is `/code`. All the following commands are menat to be run from within the container.
2. Register the Analytic with the ACE-UI server (for ACE-UI setup see https://github.com/usnistgov/ace-ui). Run `python registar_analytic.py`. This will send a request to the ACE-UI server telling it to add a connection to the analytic for the given IP address. This should return an id message. If the analytic has already been registered, then an error will be returned. NOTE: Inside the `registar_analytic.py` file, the analytic host value will need to match the actual ip address of the machine that is running the analytic. 
3. Start the Analytic. Run `python rpc_analytic.py`. This will load Yolo, add the detector to the ACE handler object, and wait to recieve messages from the ACE-UI server. Once a message is recieved, it will process the frame and return it to the ACE-UI server.
4. From the ACE-UI webpage, select a video stream, the analytic named `ip@jetson` and hit run. This will send the video frames to the jetson and run the analytic, returning the results to the ACE-UI server.
5. To tear down the analytic, run `ctrl-c`. 

## Accreditation 
Original Yolo Work: https://github.com/AlexeyAB/darknet
