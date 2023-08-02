from enum import Enum


class TopicPermissionsItem(str, Enum):
    TOPICADDPARTITION = "topicAddPartition"
    TOPICCONSUME = "topicConsume"
    TOPICCREATE = "topicCreate"
    TOPICDELETE = "topicDelete"
    TOPICEDITCONFIG = "topicEditConfig"
    TOPICEMPTY = "topicEmpty"
    TOPICPRODUCE = "topicProduce"
    TOPICVIEWCONFIG = "topicViewConfig"

    def __str__(self) -> str:
        return str(self.value)
