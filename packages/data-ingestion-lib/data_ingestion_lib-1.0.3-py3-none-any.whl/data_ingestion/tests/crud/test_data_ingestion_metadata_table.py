from copy import deepcopy

import pytest
from pytest import MonkeyPatch

from data_ingestion.crud.data_ingestion_metadata_table.DataIngestionConfig import (
    add_config,
    get_config_by_pk,
    update_config,
)
from data_ingestion.model.data_ingestion_metadata_table.DataIngestionConfig import (
    DataIngestionConfig,
)

PK = "CONFIG#TEST"
table_name = "table"
ITEM = DataIngestionConfig("TEST", table_name, "0 0 * * * *", "enabled", "122792905")


def test_get_data_ingestion_config(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):

    add_config(
        ITEM.to_dynamodb_item(),
        dynamodb_client,
    )

    response = get_config_by_pk(PK, dynamodb_client)

    assert response is not None
    assert response[0].table_name == table_name
    assert response[0].cron == "0 0 * * * *"


def test_get_data_ingestion_config_no_config(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    response = get_config_by_pk(PK, dynamodb_client)

    assert response == []


def test_get_data_ingestion_exception(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    MonkeyPatch().setattr(dynamodb_client, "query", lambda *args, **kwargs: Exception)
    with pytest.raises(Exception):
        get_config_by_pk(PK, dynamodb_client)


def test_update_data_ingestion_config(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):

    add_config(
        ITEM.to_dynamodb_item(),
        dynamodb_client,
    )

    updated_item = deepcopy(ITEM)
    updated_item.cron = "0 1 * * * *"
    updated_item.config_timestamp = "122792906"

    update_config(updated_item, dynamodb_client)

    response = get_config_by_pk(PK, dynamodb_client)

    assert response is not None
    assert response[0].table_name == table_name
    assert response[0].cron == "0 1 * * * *"


def test_update_data_ingestion_conflict(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    add_config(
        ITEM.to_dynamodb_item(),
        dynamodb_client,
    )

    updated_item = deepcopy(ITEM)
    updated_item.cron = "0 1 * * * *"
    updated_item.config_timestamp = "122792904"

    response = update_config(updated_item, dynamodb_client)

    assert response == 409


def test_update_data_ingestion_exception(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    MonkeyPatch().setattr(
        dynamodb_client, "update_item", lambda *args, **kwargs: Exception
    )
    with pytest.raises(Exception):
        update_config(ITEM, dynamodb_client)


def test_add_data_ingestion_conflict(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    add_config(
        ITEM.to_dynamodb_item(),
        dynamodb_client,
    )

    response = add_config(
        ITEM.to_dynamodb_item(),
        dynamodb_client,
    )

    assert response == 409


def test_add_data_ingestion_exception(
    dynamodb_client, mock_create_data_ingestion_metadata_table
):
    MonkeyPatch().setattr(
        dynamodb_client, "put_item", lambda *args, **kwargs: Exception
    )
    with pytest.raises(Exception):
        add_config(ITEM.to_dynamodb_item(), dynamodb_client)
