"""CRUD for data_ingestion_metadata_table."""

from http import HTTPStatus

from botocore.exceptions import ClientError
from mypy_boto3_dynamodb.client import DynamoDBClient

from data_ingestion.model.data_ingestion_metadata_table.DataIngestionConfig import (
    DataIngestionConfig,
    config_from_dynamodb_item,
)
from data_ingestion.utils.common import DATA_INGESTION_METADATA_TABLE
from data_ingestion.utils.logger import configure_logging

logger = configure_logging()


def get_config_by_pk(pk: str, dynamodb_client: DynamoDBClient):
    """
    Get data ingestion configuration from DynamoDB
    """
    try:
        response = dynamodb_client.query(
            TableName=DATA_INGESTION_METADATA_TABLE,
            KeyConditionExpression="PK = :PK",
            ExpressionAttributeValues={
                ":PK": {"S": pk},
            },
        )
        items = response.get("Items")
        if items:
            return [config_from_dynamodb_item(item) for item in items]
        return []
    except Exception as ex:
        logger.exception(ex)
        raise ex


def add_config(item: dict, dynamodb_client: DynamoDBClient):
    """
    Add data ingestion configuration item to DynamoDB
    """
    try:
        response = dynamodb_client.put_item(
            TableName=DATA_INGESTION_METADATA_TABLE,
            Item=item,
            ConditionExpression="attribute_not_exists(config_timestamp) OR config_timestamp < :config_timestamp",
            ExpressionAttributeValues={
                ":config_timestamp": item["config_timestamp"],
            },
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except ClientError as err:
        if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
            logger.info("add_config: timestamp is older than the current timestamp")
            return HTTPStatus.CONFLICT
        else:
            logger.exception(err)
            raise err
    except Exception as ex:
        logger.exception(ex)
        raise ex


def update_config(item: DataIngestionConfig, dynamodb_client: DynamoDBClient):
    """
    Update data ingestion configuration item to DynamoDB
    """
    try:
        response = dynamodb_client.update_item(
            TableName=DATA_INGESTION_METADATA_TABLE,
            Key=item.primary_key(),
            ExpressionAttributeNames={
                "#C": "cron",
                "#S": "status",
                "#T": "config_timestamp",
            },
            ExpressionAttributeValues={
                ":c": {"S": str(item.cron)},
                ":s": {"S": item.status},
                ":t": {"N": item.config_timestamp},
                ":config_timestamp": {"N": item.config_timestamp},
            },
            UpdateExpression="SET #C = :c , #S = :s, #T = :t",
            ConditionExpression="attribute_not_exists(config_timestamp) OR config_timestamp < :config_timestamp",
        )
        return response["ResponseMetadata"]["HTTPStatusCode"]
    except ClientError as err:
        if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
            logger.info("update_config: timestamp is older than the current timestamp")
            return HTTPStatus.CONFLICT
        else:
            logger.exception(err)
            raise err
    except Exception as ex:
        logger.exception(ex)
        raise ex
