import os
from google.cloud import pubsub_v1
from app.core.config import settings

# Ensure the GOOGLE_APPLICATION_CREDENTIALS environment variable is set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(settings.GOOGLE_CLOUD_PROJECT, settings.PUBSUB_TOPIC)
