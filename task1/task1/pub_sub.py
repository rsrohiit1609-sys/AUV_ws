#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys
import threading

class ChatNode(Node):
    def __init__(self, username):
        # Unique node name to prevent conflicts
        super().__init__(f'chat_node_{username}')
        self.username = username

        self.publisher_ = self.create_publisher(String, 'chat', 10)
        self.subscription = self.create_subscription(
            String, 'chat', self.listener_callback, 10)
        
        self.get_logger().info(f"Chat initialized as {self.username}.")
        self.get_logger().info("Type your message and press Enter to send.")
        
    def listener_callback(self, msg):
        if not msg.data.startswith(f"[{self.username}]"):
            print("\r" + " " * 40 + "\r", end="", flush=True)
            print(f"{msg.data}")
            print(f"[{self.username}]: ", end='', flush=True)

    def send_message(self, text):
        msg = String()
        msg.data = f"[{self.username}]: {text}"
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    
    # Check for username argument
    if len(sys.argv) < 2:
        print("Usage: ros2 run <package_name> chat_node <username>")
        return

    username = sys.argv[1]
    node = ChatNode(username)

    # Use a thread to run the ROS 2 spin so we can still accept input()
    spin_thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    spin_thread.start()

    print(f"--- Welcome, {username}! ---")
    
    try:
        while rclpy.ok():
            # Show a prompt before waiting for input
            print(f"[{username}]: ", end='', flush=True)
            user_input = input()
            
            if user_input.lower() in ['exit', 'quit']:
                break
                
            node.send_message(user_input)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
        spin_thread.join()

if __name__ == '__main__':
    main()