import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String
from std_msgs.msg import Int32, String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')

        self.last_text = None

        # Receive the string from Node 1
        self.string_subscriber = self.create_subscription(
            RT2String,
            '/rt2_string',
            self.check_palindrome,
            10
        )

        # Send 1 or 0 to Node 3
        self.result_publisher = self.create_publisher(
            Int32,
            '/palindrome_result',
            10
        )

        # Receive "Yes" or "No" back from Node 3
        self.answer_subscriber = self.create_subscription(
            String,
            '/palindrome_answer',
            self.receive_answer,
            10
        )

    def check_palindrome(self, msg):
        text = msg.data

        # Node 1 repeats its message, so process each new string once
        if text == self.last_text:
            return

        self.last_text = text

        if text == text[::-1]:
            result = 1
        else:
            result = 0

        result_msg = Int32()
        result_msg.data = result
        self.result_publisher.publish(result_msg)

        self.get_logger().info(
            f'Checking "{text}" -> sending {result} to Node 3'
        )

    def receive_answer(self, msg):
        self.get_logger().info(f'Node 3 replied: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

