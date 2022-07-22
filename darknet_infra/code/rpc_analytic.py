from ctypes import *
import random
import os
import cv2
import time
import darknet
import argparse
from threading import Thread, enumerate
from queue import Queue
import time
import sys

from os import listdir
from os.path import isfile, join
from datetime import datetime

from ace import analytic_pb2, analyticservice, grpcservice


def parser():
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--weights", default="/data/yolo/yolov2.weights",
                        help="yolo weights path")
    parser.add_argument("--config_file", default="/data/yolo/yolov2.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", default="/data/yolo/coco.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.70,
                        help="remove detections with confidence below this value")
    parser.add_argument("--grpc", default=False, 
                        help="If true, this analytic will set up a gRPC service instead of a REST service.", action="store_true")
    parser.add_argument("--grpc_port", default=50052, 
                        help="Port the analytic will run on.")
    return parser.parse_args()

def str2int(video_path):
    """
    argparse returns and string althout webcam uses int (0, 1 ...)
    Cast to int if needed
    """
    try:
        return int(video_path)
    except ValueError:
        return video_path


def check_arguments_errors(args):
    assert 0 < args.thresh < 1, "Threshold should be a float between zero and one (non-inclusive)"
    if not os.path.exists(args.config_file):
        raise(ValueError("Invalid config path {}".format(os.path.abspath(args.config_file))))
    if not os.path.exists(args.weights):
        raise(ValueError("Invalid weight path {}".format(os.path.abspath(args.weights))))
    if not os.path.exists(args.data_file):
        raise(ValueError("Invalid data file path {}".format(os.path.abspath(args.data_file))))


def convert2relative(bbox):
    """
    YOLO format use relative coordinates for annotation
    """
    x, y, w, h  = bbox
    _height     = darknet_height
    _width      = darknet_width
    return x/_width, y/_height, w/_width, h/_height


def convert2original(image, bbox):
    x, y, w, h = convert2relative(bbox)

    image_h, image_w, __ = image.shape

    orig_x       = int(x * image_w)
    orig_y       = int(y * image_h)
    orig_width   = int(w * image_w)
    orig_height  = int(h * image_h)

    bbox_converted = (orig_x, orig_y, orig_width, orig_height)
    return bbox_converted


def array_to_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (darknet_width, darknet_height),
                    interpolation=cv2.INTER_LINEAR)
    img = img.transpose(2, 0, 1)
    return img


def detect(handler):
    width, height = 608, 608
    darknet_image = darknet.make_image(width, height, 3)

    image_orig= handler.get_frame()
    image = array_to_image(image_orig)
    darknet.copy_image_from_bytes(darknet_image, image.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image, thresh=args.thresh)
    darknet.free_image(darknet_image)
    print("Detected: {}".format(datetime.now().strftime('%H:%M:%S')))

    for d in detections:
        x1,y1,x2,y2 = convert2original(image_orig,d[2])
        handler.add_bounding_box(
                        classification=d[0],
                        confidence=float(d[1]),
                        x1 = int(x1),
                        y1 = int(y1),
                        x2 = int(x2),
                        y2 = int(y2))
                        

if __name__ == '__main__':
    args = parser()
    check_arguments_errors(args)

    network, class_names, class_colors = darknet.load_network(
            args.config_file,
            args.data_file,
            args.weights,
            batch_size=1
        )
    darknet_width = darknet.network_width(network)
    darknet_height = darknet.network_height(network)

    # Ace suff
    if args.grpc:
        svc = grpcservice.AnalyticServiceGRPC()
        svc.register_name("jetson_yolo")
        svc.RegisterProcessVideoFrame(detect)
        sys.exit(svc.Run(analytic_port=args.grpc_port))
    else:
        svc = analyticservice.AnalyticService(__name__,)  
        svc.register_name("jetson_yolo")
        svc.RegisterProcessVideoFrame(detect)
        sys.exit(svc.Run())













