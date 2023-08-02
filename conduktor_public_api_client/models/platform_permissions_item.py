from enum import Enum


class PlatformPermissionsItem(str, Enum):
    AUDITLOGVIEW = "auditLogView"
    CERTIFICATEMANAGE = "certificateManage"
    CLUSTERCONNECTIONSMANAGE = "clusterConnectionsManage"
    DATAMASKINGMANAGE = "datamaskingManage"
    DATAMASKINGVIEW = "datamaskingView"
    NOTIFICATIONCHANNELMANAGE = "notificationChannelManage"
    TAASMANAGE = "taasManage"
    TAASVIEW = "taasView"
    TESTINGVIEW = "testingView"
    USERMANAGE = "userManage"

    def __str__(self) -> str:
        return str(self.value)
