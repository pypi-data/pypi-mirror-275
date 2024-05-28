import unittest
from unittest.mock import patch, MagicMock
from dlq_handler_lib.sqs_queue import SQSQueue

class TestSQSQueue(unittest.TestCase):

    @patch('dlq_handler_lib.sqs_queue.boto3.client')
    def setUp(self, mock_boto3_client):
        self.mock_sqs_client = MagicMock()
        mock_boto3_client.return_value = self.mock_sqs_client
        self.queue = SQSQueue('test-queue-url')

    def test_receive_messages_no_messages(self):
        self.mock_sqs_client.receive_message.return_value = {}
        messages = self.queue.receive_messages()
        
        self.mock_sqs_client.receive_message.assert_called_once()
        self.assertEqual(messages, [])

    def test_receive_messages_with_messages(self):
        self.mock_sqs_client.receive_message.return_value = {
            'Messages': [
                {'Body': 'message1', 'ReceiptHandle': 'handle1'},
                {'Body': 'message2', 'ReceiptHandle': 'handle2'}
            ]
        }
        messages = self.queue.receive_messages()
        print(f"Messages: {messages}")
        self.mock_sqs_client.receive_message.assert_called_once()
        self.assertEqual(messages, [('message1', 'handle1'), ('message2', 'handle2')])     

    def test_receive_messages_exception(self):
        self.mock_sqs_client.receive_message.side_effect = Exception("Error")
        messages = self.queue.receive_messages()
        print(f"Messages: {messages}")
        self.mock_sqs_client.receive_message.assert_called_once()
        self.assertEqual(messages, [])     

if __name__ == '__main__':
    unittest.main()