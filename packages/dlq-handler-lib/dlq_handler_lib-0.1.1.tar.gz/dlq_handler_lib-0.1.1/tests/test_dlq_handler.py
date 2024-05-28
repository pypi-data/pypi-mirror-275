import unittest
from unittest.mock import patch, MagicMock
from dlq_handler_lib.handler import DLQHandler

class TestDLQHandler(unittest.TestCase):

    @patch('dlq_handler_lib.handler.SQSQueue')
    def setUp(self, MockSQSQueue):
        self.mock_sqs_queue = MockSQSQueue.return_value
        self.handler = DLQHandler(
            queue_url='test-queue-url',
            original_queue_url='original-queue-url',
            max_attempts=5
        )

    def test_process_messages_no_messages(self):
        self.mock_sqs_queue.receive_messages.return_value = []
        self.handler.process_messages()
        self.mock_sqs_queue.receive_messages.assert_called_once()
        # Ensure no messages are processed
        self.mock_sqs_queue.delete_message.assert_not_called()

    def test_process_messages_with_messages(self):
        self.mock_sqs_queue.receive_messages.return_value = [
            ('{"Attributes": {"Attempts": "1"}}', 'handle1'),
            ('{"Attributes": {"Attempts": "2"}}', 'handle2')
        ]
        self.handler.send_message_to_original_queue = MagicMock()
        self.handler.process_messages()
        self.mock_sqs_queue.receive_messages.assert_called_once()
        self.handler.send_message_to_original_queue.assert_called()
        self.mock_sqs_queue.delete_message.assert_called()

    def test_process_messages_reach_max_attempts(self):
        self.mock_sqs_queue.receive_messages.return_value = [
            ('{"Attributes": {"Attempts": "5"}}', 'handle1')
        ]
        self.handler.send_message_to_original_queue = MagicMock()
        self.handler.process_messages()
        self.mock_sqs_queue.receive_messages.assert_called_once()
        self.handler.send_message_to_original_queue.assert_not_called()
        self.mock_sqs_queue.delete_message.assert_called_once_with('handle1')

    def test_send_message_to_original_queue(self):
        message = {"Attributes": {"Attempts": "1"}}
        self.handler.send_message_to_original_queue(message)
        self.mock_sqs_queue.sqs_client.send_message.assert_called_once_with(
            QueueUrl='original-queue-url',
            MessageBody='{"Attributes": {"Attempts": "1"}}'
        )

if __name__ == '__main__':
    unittest.main()