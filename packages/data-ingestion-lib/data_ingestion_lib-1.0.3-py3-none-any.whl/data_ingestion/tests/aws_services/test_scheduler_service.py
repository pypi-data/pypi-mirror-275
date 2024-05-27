from unittest.mock import Mock

import pytest

from data_ingestion.aws_services import scheduler_service


def test_create_scheduler(scheduler_client):
    scheduler_client.create_schedule = Mock(
        return_value={
            "ScheduleArn": "arn:aws:scheduler:us-east-1:000000000000:schedule/test-schedule"
        }
    )

    response = scheduler_service.create_schedule(
        "test-schedule", "rate(30 seconds)", scheduler_client
    )

    assert response == {
        "ScheduleArn": "arn:aws:scheduler:us-east-1:000000000000:schedule/test-schedule"
    }


def test_create_scheduler_exception(scheduler_client, caplog):
    scheduler_client.create_schedule = Mock(side_effect=Exception("An error occurred"))

    scheduler_service.create_schedule(
        "test-schedule", "rate(30 seconds)", scheduler_client
    )

    assert "An error occurred" in caplog.text


def test_update_scheduler(scheduler_client):
    scheduler_client.update_schedule = Mock(
        return_value={
            "ScheduleArn": "arn:aws:scheduler:us-east-1:000000000000:schedule/test-schedule"
        }
    )

    response = scheduler_service.update_schedule(
        "test-schedule", "rate(30 seconds)", scheduler_client
    )

    assert response == {
        "ScheduleArn": "arn:aws:scheduler:us-east-1:000000000000:schedule/test-schedule"
    }


def test_update_scheduler_exception(scheduler_client, caplog):
    scheduler_client.update_schedule = Mock(side_effect=Exception("An error occurred"))

    scheduler_service.update_schedule(
        "test-schedule", "rate(30 seconds)", scheduler_client
    )

    assert "An error occurred" in caplog.text


def test_delete_scheduler(scheduler_client):
    scheduler_client.delete_schedule = Mock(return_value={})

    response = scheduler_service.delete_schedule("test-schedule", scheduler_client)

    assert response == {}


def test_delete_scheduler_exception(scheduler_client, caplog):
    scheduler_client.delete_schedule = Mock(side_effect=Exception("An error occurred"))

    scheduler_service.delete_schedule("test-schedule", scheduler_client)

    assert "An error occurred" in caplog.text
