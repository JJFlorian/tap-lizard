"""lizard tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_lizard.streams import (
    OrganisationStream,
    TimeseriesStream,
    LocationsStream,
    RasterStream,
    ScenarioStream,
    
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    OrganisationStream,
    TimeseriesStream,
    LocationsStream,
    RasterStream,
    ScenarioStream,
]


class Taplizard(Tap):
    """lizard tap class."""
    name = "tap-lizard"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "start_date",
            th.DateTimeType,
        ),
        th.Property(
            "stream_maps",
            th.ObjectType(),
        ),
        th.Property(
            "stream_map_config",
            th.ObjectType(),
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
