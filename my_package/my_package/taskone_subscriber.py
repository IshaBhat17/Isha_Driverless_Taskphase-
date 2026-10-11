import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne


class TaskOneSubscriber(Node):

    def __init__(self):
        super().__init__('taskone_subscriber')

        self.subscription = self.create_subscription(
            TaskOne,
            '/taskone',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        speed = msg.ang_vel * msg.radius

        self.get_logger().info(
            f'Longitudinal speed = {speed:.3f} m/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = TaskOneSubscriber()

    try:
        rclpy.spin(node) #keeps the subscriber running so it can receive messages continuously.
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
