# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geomockimages', 'geomockimages.test']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.26.4,<2.0.0',
 'rasterio>=1.3.10,<2.0.0',
 'rio-cogeo>=5.3.0,<6.0.0',
 'scikit-image>=0.23.2,<0.24.0',
 'scipy>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'geomockimages',
    'version': '0.2.4',
    'description': 'A module to programmatically create geotiff images which can be used for unit tests.',
    'long_description': '# geomockimages\n\nA module to programmatically create geotiff images which can be used for unit tests.\n\nThe underlying idea is that in order to write unit tests for geospatial image processsing algorithms,\nit is necessary to have an actual input image file or array. Organising these test images becomes a chore over time,\nthey should not be stored in git as they are large binary data and when stored outside, there always\nis the danger that they are not updated according to changes in the code repo.\n\n**geomockimages** provides a solution to the problem by providing simple code that allows to create\ngeospatial images (so far geotiffs) in a parameterised way.\n\n**geomockimages** is able to create both electro-optical as well as SAR images. More specificially, 4-band optical images and SAR images with one or two polarizations are supported explicitely. It is also possible to create images with more or less images, but the results will be less realistic.\n\nBesides singe image tests, **geomockimages** can also create image pairs with small differences. This allows to do basic testing of change detection algorithms.\n\n## Install package\n```bash\npip install geomockimages\n```\n\n## Usage\n\nIn the following an example unit test for a hypothetical NDVI function.\n\n```python\nimport numpy as np\nimport rasterio as rio\nfrom pathlib import Path\n\nfrom rasterio.transform import from_origin\nfrom my_image_processing import ndvi\nfrom geomockimages.imagecreator import GeoMockImage\n\ndef test_ndvi():\n    """\n    A unit test if an NDVI method works in general\n    """\n    # Create 4-band image simulating RGBN as needed for NDVI\n    test_image, _ = GeoMockImage(\n        300,\n        150,\n        4,\n        "uint16",\n        out_dir=Path("/tmp"),\n        crs=4326,\n        nodata=0,\n        nodata_fill=3,\n        cog=False,\n    ).create(seed=42, transform=from_origin(13.428596, 52.494384, 0.000006, 0.000006))\n\n    ndvi_image = ndvi(test_image)\n\n    with rio.open(str(ndvi_image)) as src:\n        ndvi_array = src.read()\n        # NDVI only has one band of same size as input bands\n        assert ndvi_array.shape == (1, 150, 300)\n        # NDVI has float values between -1 and 1\n        assert ndvi_array.dtype == np.dtype(\'float32\')\n        assert np.nanmin(ndvi_array) >= -1\n        assert np.nanmax(ndvi_array) <= 1\n\n```\n\n## Documentation\n\n**geomockimages** was written for python engineers. The best way to learn about the option it offers do:\n\n```python\nfrom geomockimages.imagecreator import GeoMockImage\nhelp(GeoMockImage)\n```\n\n## More examples\n...can be found within two jupyter notebooks:\n\n[Basic 4-band optical example](https://github.com/markusuwe/geomockimages/blob/main/notebooks/example1_radiance.ipynb)\n\n[SAR images and change detection](https://github.com/markusuwe/geomockimages/blob/main/notebooks/example2_sar_imagepair.ipynb)\n',
    'author': 'Markus Müller',
    'author_email': 'markus.u.mueller@zoho.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/markusuwe/geomockimages',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
