import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import task3_msgs.msg

class Navigator(Node):
    def __init__(self):
        super().__init__('navigator')
        # FSM Setup
        self.states = ["North", "East", "South", "West"]
        self.state_idx = 0  # Starts at North
        self.x, self.y = 0.0, 0.0
        
        self.sub = self.create_subscription(String, '/cmd', self.cmd_callback, 10)
        self.pub = self.create_publisher(task3_msgs.msg.BotPose, '/bot_pose', 10)

    def cmd_callback(self, msg):
        cmd = msg.data.lower()
        
        # State Transition Logic
        if cmd == "turn right":
            self.state_idx = (self.state_idx + 1) % 4
        elif cmd == "turn left":
            self.state_idx = (self.state_idx - 1) % 4
        elif cmd == "forward":
            self.move(1.0)
        elif cmd == "backward":
            self.move(-1.0)
            
        # Publish current state
        pose = task3_msgs.msg.BotPose()
        pose.x, pose.y = self.x, self.y
        pose.facing_direction = self.states[self.state_idx]
        self.pub.publish(pose)
        self.get_logger().info(f"State: {pose.facing_direction}, Pos: ({self.x}, {self.y})")

    def move(self, dist):
        direction = self.states[self.state_idx]
        if direction == "North": self.y += dist
        elif direction == "South": self.y -= dist
        elif direction == "East": self.x += dist
        elif direction == "West": self.x -= dist

def main(args=None):
    rclpy.init(args=args)
    node = Navigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()