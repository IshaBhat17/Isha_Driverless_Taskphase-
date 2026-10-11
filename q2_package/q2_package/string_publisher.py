import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')

        # Create a publisher using our custom message
        self.publisher = self.create_publisher(
            RT2String, '/rt2_string', 10
        )

        # Ask the user for a string and save it
        self.text = input("Enter a string: ")

        # Call timer_callback every 0.5 seconds
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        # Create a message
        msg = RT2String()

        # Store the entered string in the message
        msg.data = self.text

        # Publish the message
        self.publisher.publish(msg)

        self.get_logger().info(f'Published: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

