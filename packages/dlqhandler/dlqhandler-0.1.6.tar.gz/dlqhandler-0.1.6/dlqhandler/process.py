import json
import logging
from .sqs_queue import SQSQueue

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DLQHandler:
    def __init__(self, queue_url, original_queue_url, max_attempts=5):
        self.dlq_queue = SQSQueue(queue_url, max_attempts)
        self.original_queue_url = original_queue_url
        self.max_attempts = max_attempts

    def execute(self):
        messages = self.dlq_queue.receive_messages()
        if not messages:
            return

        for body, receipt_handle in messages:
            message = json.loads(body)
            logger.info(f"Processing message: {message}")

            attempts = int(message.get('Attributes', {}).get('Attempts', 0))
            if attempts >= self.max_attempts:
                logger.error(f"Message reached max attempts: {message}")
                self.dlq_queue.delete_message(receipt_handle) 
                continue

            # Process message logic here

            attempts += 1
            message['Attributes']['Attempts'] = attempts
            # Resend message to original queue
            self.send_message_to_original_queue(message)

            self.dlq_queue.delete_message(receipt_handle)

    def send_message_to_original_queue(self, message):
        try:
            response = self.dlq_queue.sqs_client.send_message(
                QueueUrl=self.original_queue_url,
                MessageBody=json.dumps(message)
            )
            logger.info(f"Message resent to original queue: {response}")
        except Exception as e:
            logger.exception("Error sending message to original queue: %s", e)
            raise e