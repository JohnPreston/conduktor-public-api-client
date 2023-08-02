from enum import Enum


class KafkaConnect1PermissionsItem(str, Enum):
    KAFKACONNECTORCREATE = "kafkaConnectorCreate"
    KAFKACONNECTORDELETE = "kafkaConnectorDelete"
    KAFKACONNECTOREDITCONFIG = "kafkaConnectorEditConfig"
    KAFKACONNECTORSTATUS = "kafkaConnectorStatus"
    KAFKACONNECTORUPDATE = "kafkaConnectorUpdate"
    KAFKACONNECTORVIEWCONFIG = "kafkaConnectorViewConfig"
    KAFKACONNECTPAUSERESUME = "kafkaConnectPauseResume"
    KAFKACONNECTRESTART = "kafkaConnectRestart"

    def __str__(self) -> str:
        return str(self.value)
