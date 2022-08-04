"""Stream type classes for tap-lizard."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_lizard.client import lizardStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class OrganisationStream(lizardStream):
    """Define custom stream."""
    name = "organisations"
    path = "organisations"
    primary_keys = ["uuid"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "uuid",
            th.StringType,
            ),
        th.Property(
            "name",
            th.StringType,
        ),
    ).to_dict()

class TimeseriesStream(lizardStream):
    """Define custom stream."""
    name = "timeseries"
    path = "timeseries"
    primary_keys = ["uuid"]
    replication_key = "last_modified"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "uuid",
            th.StringType,
            ),
        th.Property(
            "code",
            th.StringType,
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "start",
            th.DateTimeType,
        ),
        th.Property(
            "end",
            th.DateTimeType,
        ),
        th.Property(
            "created",
            th.DateTimeType,
        ),
        th.Property(
            "last_modified",
            th.DateTimeType,
        ),
        th.Property(
            "access_modifier",
            th.StringType,
        ),
        th.Property(
            "location",
            th.ObjectType(),
        ),
    ).to_dict()

class LocationsStream(lizardStream):
    """Define custom stream."""
    name = "locations"
    path = "locations"
    primary_keys = ["uuid"]
    replication_key = "last_modified"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "uuid",
            th.StringType,
            ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "code",
            th.StringType,
        ),
        th.Property(
            "organisation",
            th.ObjectType(),
        ),
        th.Property(
            "access_modifier",
            th.StringType,
        ),
        th.Property(
            "location",
            th.ObjectType(),
        ),
        th.Property(
            "created",
            th.DateTimeType,
        ),
        th.Property(
            "last_modified",
            th.DateTimeType,
        ),
    ).to_dict()

class RasterStream(lizardStream):
    """Define custom stream."""
    name = "rasters"
    path = "rasters"
    primary_keys = ["uuid"]
    replication_key = "last_modified"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "uuid",
            th.StringType,
            ),
        th.Property(
            "last_modified",
            th.DateTimeType,
        ),
        th.Property(
            "created",
            th.DateTimeType,
        ),
        th.Property(
            "organisation",
            th.ObjectType(),
        ),
        th.Property(
            "access_modifier",
            th.StringType,
        ),
        th.Property(
            "writable",
            th.BooleanType,
        ),
        th.Property(
            "is_geoblock",
            th.BooleanType,
        ),
        th.Property(
            "weight",
            th.IntegerType,
        ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "temporal",
            th.BooleanType,
        ),
        th.Property(
            "first_value_timestamp",
            th.DateTimeType,
        ),
        th.Property(
            "last_value_timestamp",
            th.DateTimeType,
        ),
        th.Property(
            "projection",
            th.StringType,
        ),
        th.Property(
            "rescalable",
            th.BooleanType,
        ),
        th.Property(
            "aggregation_type",
            th.StringType,
        ),

    ).to_dict()

class ScenarioStream(lizardStream):
    """Define custom stream."""
    name = "scenarios"
    path = "scenarios"
    primary_keys = ["uuid"]
    replication_key = "last_modified"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property(
            "uuid",
            th.StringType,
            ),
        th.Property(
            "name",
            th.StringType,
        ),
        th.Property(
            "organisation",
            th.ObjectType(),
        ),
        th.Property(
            "access_modifier",
            th.StringType,
        ),
        th.Property(
            "created",
            th.DateTimeType,
        ),
        th.Property(
            "last_modified",
            th.DateTimeType,
        ),
        th.Property(
            "simulation_identifier",
            th.StringType,
        ),
        th.Property(
            "supplier",
            th.StringType,
        ),
        th.Property(
            "source",
            th.StringType,
        ),
        th.Property(
            "model_identifier",
            th.StringType,
        ),
        th.Property(
            "model_revision",
            th.StringType,
        ),
        th.Property(
            "has_raw_results",
            th.BooleanType,
        ),
        th.Property(
            "total_size",
            th.IntegerType,
        ),

    ).to_dict()