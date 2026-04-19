import rclpy
from rclpy.node import Node
import cv2
import numpy as np

class VisualLockNode(Node):
    def __init__(self):
        super().__init__('visual_lock')
        
        video_path = '/home/rohiitrs/auv_ws/src/task4/data/test_video.mp4'
        self.cap = cv2.VideoCapture(video_path)
        
        # State Machine Variable
        self.state = "SEARCHING"

        self.timer = self.create_timer(0.033, self.process_frame)
        self.get_logger().info("Visual Lock Node Started")

    def process_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return

        # 1. HSV Color Masking for Green
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = np.array([40, 50, 50])
        upper_green = np.array([80, 255, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        
        # Clean up noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # 2. Find Object Centroid
        moments = cv2.moments(mask)
        width = frame.shape[1]
        cx = None

        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            
        # 3. Finite State Machine Logic
        if cx is None:
            self.state = "SEARCHING"
            output = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        elif cx < (width / 3):
            self.state = "ALIGNING LEFT"
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
        elif cx > (2 * width / 3):
            self.state = "ALIGNING RIGHT"
            output = cv2.Canny(frame, 100, 200)
            output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
        else:
            self.state = "LOCKED ON"
            output = frame

        # Logging and Visualization
        self.get_logger().info(f"State: {self.state} | X: {cx}")
        cv2.imshow('Visual Lock Feed', output)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            rclpy.shutdown()

    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = VisualLockNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
