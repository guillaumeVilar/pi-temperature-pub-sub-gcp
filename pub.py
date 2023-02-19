#!/usr/bin/env python

from google.cloud import pubsub_v1

def publish(message: str, project_id: str, topic_id: str) -> None:
    """Publishes a message to a Pub/Sub topic."""
    # Initialize a Publisher client.
    client = pubsub_v1.PublisherClient()
    # Create a fully qualified identifier of form `projects/{project_id}/topics/{topic_id}`
    topic_path = client.topic_path(project_id, topic_id)

    # Data sent to Cloud Pub/Sub must be a bytestring.
    data = str.encode(message)

    # When you publish a message, the client returns a future.
    api_future = client.publish(topic_path, data)
    message_id = api_future.result()

    print(f"Published {data.decode()} to {topic_path}: {message_id}")
