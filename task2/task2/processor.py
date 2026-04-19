#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class ProcessorNode(Node):
    def __init__(self):
        super().__init__('processor_node')
        self.subscription = self.create_subscription(Int32, '/raw_signal', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int32, '/processed_signal', 10)

    def listener_callback(self, msg):
        result = msg.data * 5
        new_msg = Int32()
        new_msg.data = result
        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Received: {msg.data}, Published: {result}')

def main(args=None):
    rclpy.init(args=args)
    node = ProcessorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()