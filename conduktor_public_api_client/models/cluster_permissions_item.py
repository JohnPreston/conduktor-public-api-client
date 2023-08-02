from enum import Enum


class ClusterPermissionsItem(str, Enum):
    CLUSTEREDITBROKER = "clusterEditBroker"
    CLUSTEREDITSRCOMPATIBILITY = "clusterEditSRCompatibility"
    CLUSTERMANAGEACL = "clusterManageACL"
    CLUSTERVIEWACL = "clusterViewACL"
    CLUSTERVIEWBROKER = "clusterViewBroker"

    def __str__(self) -> str:
        return str(self.value)
