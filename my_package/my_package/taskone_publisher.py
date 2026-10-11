import rclpy   #allows Python programs to communicate with ROS 2. We use it to initialise ROS 2 and shut it down.
from rclpy.node import Node  #Importing Node lets us create a ROS 2 node using Python.
from taskone_msgs.msg import TaskOne  
import time 

class TaskOnePublisher(Node):

    def __init__(self):
        super().__init__('taskone_publisher') #initialises the parent ROS 2 Node class and gives your node the name taskone_publisher.
        self.publisher = self.create_publisher(
            TaskOne,
            '/taskone',
            10)
    def publish_data(self, ang_vel, radius):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.publisher.publish(msg)  #publishes that message on /taskone
        self.get_logger().info(
            f'Published ang_vel={ang_vel}, radius={radius}'
        )  

        #The f before the string lets Python insert the values of ang_vel and radius into it
        #the get_logger prints a message to the terminal 


    
def main(args=None):
    rclpy.init(args=args)
    node = TaskOnePublisher()

    try:
        ang_vel = float(input("Enter angular velocity (rad/s): "))
        radius = float(input("Enter wheel radius (m): "))

        while rclpy.ok():
            node.publish_data(ang_vel, radius)
            time.sleep(1)

    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
#tell Python to call main() when you run this file directly as a program.


