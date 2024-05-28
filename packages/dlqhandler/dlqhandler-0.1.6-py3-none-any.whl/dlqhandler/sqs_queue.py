import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class SQSQueue:
    def __init__(self, queue_url, max_attempts=5):
        self.queue_url = queue_url
        self.max_attempts = max_attempts
        self.sqs_client = boto3.client("sqs", region_name="sa-east-1")
    def receive_messages(self, max_number=10, wait_time=0):
        try:
            logger.info('Fetching messages from SQS queue')
            messages = self.sqs_client.receive_message(
                QueueUrl=self.queue_url,
                AttributeNames=['All'],
                MaxNumberOfMessages=max_number,
                WaitTimeSeconds=wait_time
            )
            logger.info('Received messages from SQS: %s', messages)

            if 'Messages' not in messages:
                logger.info('No messages to retrieve from SQS: Empty content')
                return []

            parsed_messages = [(msg['Body'], msg['ReceiptHandle']) for msg in messages['Messages']]
            logger.debug('Parsed messages: %s', parsed_messages)
            return parsed_messages
        except Exception as e:
            logger.exception("Error receiving messages: %s", e)
            return []

    def delete_message(self, receipt_handle):
        try:
            response = self.sqs_client.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            logger.info("Message deleted from the queue: %s", response)
        except Exception as e:
            logger.exception("Error deleting message: %s", e)
            raise e