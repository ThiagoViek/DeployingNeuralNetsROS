import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('Image Publisher')
        self.img_publisher = self.create_publisher(Image, 'images', 2)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cam = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()

    def timer_callback(self):
        _,frame = self.cam.read()
        msg = self.cv_bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.img_publisher.publish(msg)
        self.get_logger().info('Publishing new Image')

def main(args=None):
    rclpy.init(args=args)
    image_publisher= ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
