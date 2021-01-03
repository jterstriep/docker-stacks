[![docker pulls](https://img.shields.io/docker/pulls/jterstriep/geo-notebook.svg)](https://hub.docker.com/r/jterstriep/docker-stack/)
[![docker stars](https://img.shields.io/docker/stars/jterstriep/geo-notebook.svg)](https://hub.docker.com/r/jterstriep/docker-stack/)
[![image metadata](https://images.microbadger.com/badges/image/jterstriep/geo-notebook.svg)](https://microbadger.com/images/jterstriep/geo-notebook "jterstriep/docker-stack image metadata")

# jterstriep Notebook Geosptatial Python Stack

**jterstriep/geo-notebook** inherits from jupyter/scipy-notebook and adds
the geospatial library GDAL and python packages rasterio, geopandas and
other dependencies in those software stacks.

The keras-spatial package was also added. Keras-spatial package provides
a SpatialDataGenerator class for extracting raster samples from larger raster 
data sources. Originally designed to provide data preprocessing similar to
Keras ImageDataGenerator, Keras-spatial is a powerful and flexible tool for
coverting from vector space to raster space. Find out more about 
[Keras-spatial](https://github.com/NCSA/keras-spatial).


GitHub Actions in the https://github.com/jterstriep/docker-stacks 
project builds and pushes this image to Docker Hub.

Please visit the project documentation site for help using and 
contributing to this image and others.

- [Jupyter Docker Stacks on ReadTheDocs](http://jupyter-docker-stacks.readthedocs.io/en/latest/index.html)
