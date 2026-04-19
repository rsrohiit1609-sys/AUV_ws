#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OutputNode(Node):
    def __init__(self):
        super().__init__('output_node')
        self.subscription = self.create_subscription(Int32, '/processed_signal', self.listener_callback, 10)

    def listener_callback(self, msg):
        final_result = msg.data + 10
        self.get_logger().info(f'Final Output: {final_result}')

def main(args=None):
    rclpy.init(args=args)
    node = OutputNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()