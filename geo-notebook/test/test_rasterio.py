# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import logging

import pytest
from pathlib import Path

LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "name,command_list",
    [
        (
            "Read tif",
            [
                "import rasterio as rio",
                "src = rio.open('{data_dir}/float.tif')",
            ]
        ),
    ],
)
def test_rasterio(container, name, command_list):
    """Basic rasterio tests"""
    host_data_dir = Path(__file__).parent / "data"
    cont_data_dir = "/home/jovyan/data"
    LOGGER.info(f"Testing rasterio: {name} ...")
    command = ';'.join(command_list).format(data_dir=cont_data_dir)
    c = container.run(
            volumes={host_data_dir: {"bind": cont_data_dir, "mode": "ro"}},
            tty=True, 
            command=["start.sh", "python", "-c", command])
    rv = c.wait(timeout=30)
    assert rv == 0 or rv["StatusCode"] == 0, f"Command {command} failed"
    logs = c.logs(stdout=True).decode("utf-8")
    LOGGER.debug(logs)
