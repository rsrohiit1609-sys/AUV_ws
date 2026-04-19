import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Commander(Node):
    def __init__(self):
        super().__init__('commander')
        self.pub = self.create_publisher(String, '/cmd', 10)
        self.get_logger().info("Commander Ready. Commands: 'forward', 'backward', 'turn left', 'turn right'")

def main(args=None):
    rclpy.init(args=args)
    node = Commander()
    try:
        while rclpy.ok():
            cmd = input("Enter command: ")
            msg = String()
            msg.data = cmd
            node.pub.publish(msg)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()