import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class ResultResponder(Node):
    def __init__(self):
        super().__init__('result_responder')

        # Receive 1 or 0 from Node 2
        self.result_subscriber = self.create_subscription(
            Int32,
            '/palindrome_result',
            self.send_answer,
            10
        )

        # Send "Yes" or "No" back to Node 2
        self.answer_publisher = self.create_publisher(
            String,
            '/palindrome_answer',
            10
        )

    def send_answer(self, msg):
        answer = String()

        if msg.data == 1:
            answer.data = 'Yes'
        else:
            answer.data = 'No'

        self.answer_publisher.publish(answer)
        self.get_logger().info(f'Sending answer: {answer.data}')


def main(args=None):
    rclpy.init(args=args)
    node = ResultResponder()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

