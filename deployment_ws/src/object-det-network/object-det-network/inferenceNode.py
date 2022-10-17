import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import torch

class InferenceNode(Node):
    def __init__(self):
        super().__init__('Yolov5 Detector')

        # ROS Members
        self.subscription = self.create_subscription(Image,'/images',
            self.inference_callback,2)
        self.cv_bridge = CvBridge()

        # Yolov5 Definition
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5n', pretrained=True)
        self.model.to('cuda:0') # Move model to GPU

    def inference_callback(self, msg):
        # Image Convertion
        frame_cv = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

        # Inference & Logging
        results = self.model(frame_cv)
        results.save()
        self.get_logger().info(f'New Image for Inference')

def main(args=None):
    rclpy.init(args=args)
    inference_node = InferenceNode()
    rclpy.spin(inference_node )
    inference_node .destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
