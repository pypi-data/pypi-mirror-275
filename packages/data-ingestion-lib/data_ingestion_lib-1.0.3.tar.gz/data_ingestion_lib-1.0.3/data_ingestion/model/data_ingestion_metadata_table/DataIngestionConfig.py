class DataIngestionConfig:
    def __init__(
        self,
        domain_name: str,
        table_name: str,
        cron: str,
        status: str,
        config_timestamp: str,
    ):
        self.domain_name = domain_name
        self.table_name = table_name
        self.cron = cron
        self.status = status
        self.config_timestamp = config_timestamp

    def partition_key(self) -> dict:
        return {"PK": {"S": f"CONFIG#{self.domain_name}"}}

    def sort_key(self) -> dict:
        return {"SK": {"S": f"TABLE#{self.table_name}"}}

    def primary_key(self) -> dict:
        return {**self.partition_key(), **self.sort_key()}

    def non_key_attributes(self) -> dict:
        return {
            "cron": {"S": self.cron},
            "status": {"S": self.status},
            "config_timestamp": {"N": self.config_timestamp},
        }

    def to_dynamodb_item(self) -> dict:
        return {
            **self.partition_key(),
            **self.sort_key(),
            **self.non_key_attributes(),
        }


def config_from_dynamodb_item(item: dict) -> DataIngestionConfig:
    return DataIngestionConfig(
        domain_name=item["PK"]["S"].split("#")[1],
        table_name=item["SK"]["S"].split("#")[1],
        cron=item["cron"]["S"],
        status=item["status"]["S"],
        config_timestamp=item["config_timestamp"]["N"],
    )
