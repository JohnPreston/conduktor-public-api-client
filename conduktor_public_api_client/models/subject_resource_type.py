from enum import Enum


class SubjectResourceType(str, Enum):
    CLUSTER = "Cluster"
    CONSUMERGROUP = "ConsumerGroup"
    KAFKACONNECT = "KafkaConnect"
    PLATFORM = "Platform"
    SUBJECT = "Subject"
    TOPIC = "Topic"

    def __str__(self) -> str:
        return str(self.value)
