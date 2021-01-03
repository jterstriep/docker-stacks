# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/scipy-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Jeff Terstriep <jefft@illinois.edu>"

RUN conda install --yes -c conda-forge geopandas rasterio && \
    pip install --no-deps keras-spatial && \
    fix-permissions $CONDA_DIR && \
    fix-permissions /home/$NB_USER

