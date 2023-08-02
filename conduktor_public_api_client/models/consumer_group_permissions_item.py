from enum import Enum


class ConsumerGroupPermissionsItem(str, Enum):
    CONSUMERGROUPCREATE = "consumerGroupCreate"
    CONSUMERGROUPDELETE = "consumerGroupDelete"
    CONSUMERGROUPRESET = "consumerGroupReset"
    CONSUMERGROUPVIEW = "consumerGroupView"

    def __str__(self) -> str:
        return str(self.value)
