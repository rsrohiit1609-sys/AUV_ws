#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SignalPublisher(Node):
    def __init__(self):
        super().__init__('signal_publisher')
        self.publisher_ = self.create_publisher(Int32, '/raw_signal', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        self.i += 2
        msg = Int32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SignalPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()