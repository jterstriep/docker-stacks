# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import logging

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "name,command_list",
    [
        (
            "Create GeoDataFrame",
            [
                "import geopandas as gpd",
                "import pandas as pd",
                "import numpy as np",
                "lat,lng = 84*np.random.rand(10), 360*np.random.rand(10)-180",
                "df = pd.DataFrame(dict(lat=lat, lng=lng))",
                "gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lng, df.lat))"
            ]
        ),
    ],
)
def test_geopandas(container, name, command_list):
    """Basic geopandas tests"""
    LOGGER.info(f"Testing geopandas: {name} ...")
    command = ';'.join(command_list)
    c = container.run(tty=True, command=["start.sh", "python", "-c", command])
    rv = c.wait(timeout=30)
    assert rv == 0 or rv["StatusCode"] == 0, f"Command {command} failed"
    logs = c.logs(stdout=True).decode("utf-8")
    LOGGER.debug(logs)
