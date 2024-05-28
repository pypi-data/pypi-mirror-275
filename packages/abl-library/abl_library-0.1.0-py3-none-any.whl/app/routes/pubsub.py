from fastapi import APIRouter, HTTPException
from google.cloud import pubsub_v1
from app.core.config import settings

router = APIRouter()

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()
topic_path = publisher.topic_path(settings.GOOGLE_CLOUD_PROJECT, settings.PUBSUB_TOPIC)

@router.post("/publish")
async def publish_message(message: str):
    try:
        future = publisher.publish(topic_path, message.encode("utf-8"))
        future.result()
        return {"status": "Message published"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/pull")
async def pull_messages():
    subscription_path = subscriber.subscription_path(settings.GOOGLE_CLOUD_PROJECT, "my-subscription")

    def callback(message):
        print(f"Received message: {message.data}")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    try:
        streaming_pull_future.result(timeout=5)
    except Exception as e:
        streaming_pull_future.cancel()
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "Pulled messages"}
