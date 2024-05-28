import pytest

from qa_qc_check.model.metadata_model import MetadataModel, QaQcModel


@pytest.fixture()
def mock_extract_json():
    data = {
        "description": "/vsis3/satimg-to-be-deleted/Sentinel2/TCX8020/20161101_091032002000000_TCX8020.tif",
        "driverShortName": "GTiff",
        "driverLongName": "GeoTIFF",
        "files": [
            "/vsis3/satimg-to-be-deleted/Sentinel2/TCX8020/20161101_091032002000000_TCX8020.tif"
        ],
        "size": [11831, 11599],
        "coordinateSystem": {
            "wkt": "PROJCRS['WGS 84 / UTM zone 44N',\n    BASEGEOGCRS['WGS 84',\n        DATUM['World Geodetic System 1984',\n            ELLIPSOID['WGS 84',6378137,298.257223563,\n                LENGTHUNIT['metre',1,\n                    ID['EPSG',9001]]]],\n        PRIMEM['Greenwich',0,\n            ANGLEUNIT['degree',0.0174532925199433,\n                ID['EPSG',9122]]]],\n    CONVERSION['Transverse Mercator',\n        METHOD['Transverse Mercator',\n            ID['EPSG',9807]],\n        PARAMETER['Latitude of natural origin',0,\n            ANGLEUNIT['degree',0.0174532925199433],\n            ID['EPSG',8801]],\n        PARAMETER['Longitude of natural origin',81,\n            ANGLEUNIT['degree',0.0174532925199433],\n            ID['EPSG',8802]],\n        PARAMETER['Scale factor at natural origin',0.9996,\n            SCALEUNIT['unity',1],\n            ID['EPSG',8805]],\n        PARAMETER['False easting',500000,\n            LENGTHUNIT['metre',1],\n            ID['EPSG',8806]],\n        PARAMETER['False northing',0,\n            LENGTHUNIT['metre',1],\n            ID['EPSG',8807]]],\n    CS[Cartesian,2],\n        AXIS['(E)',east,\n            ORDER[1],\n            LENGTHUNIT['metre',1,\n                ID['EPSG',9001]]],\n        AXIS['(N)',north,\n            ORDER[2],\n            LENGTHUNIT['metre',1,\n                ID['EPSG',9001]]]]",
            "dataAxisToSRSAxisMapping": [1, 2],
        },
        "geoTransform": [415320, 10, 0, 2016620, 0, -10],
        "metadata": {
            "": {"AREA_OR_POINT": "Area"},
            "IMAGE_STRUCTURE": {
                "COMPRESSION": "LZW",
                "INTERLEAVE": "BAND",
                "LAYOUT": "COG",
            },
        },
        "cornerCoordinates": {
            "upperLeft": [415320, 2016620],
            "lowerLeft": [415320, 1900630],
            "lowerRight": [533630, 1900630],
            "upperRight": [533630, 2016620],
            "center": [474475, 1958625],
        },
        "wgs84Extent": {
            "type": "Polygon",
            "coordinates": [
                [
                    [80.1990385, 18.2372543],
                    [80.2036777, 17.1889343],
                    [81.3162626, 17.1902584],
                    [81.3181052, 18.2386645],
                    [80.1990385, 18.2372543],
                ]
            ],
        },
        "bands": [
            {
                "band": 1,
                "block": [512, 512],
                "type": "Byte",
                "colorInterpretation": "Gray",
                "computedMin": 50,
                "computedMax": 193,
                "minimum": 50,
                "maximum": 193,
                "mean": 155.318,
                "stdDev": 16.361,
                "noDataValue": 0,
                "overviews": [
                    {"size": [5915, 5799]},
                    {"size": [2957, 2899]},
                    {"size": [1478, 1449]},
                    {"size": [739, 724]},
                    {"size": [369, 362]},
                ],
                "metadata": {
                    "": {
                        "STATISTICS_MAXIMUM": "193",
                        "STATISTICS_MEAN": "155.31843492351",
                        "STATISTICS_MINIMUM": "50",
                        "STATISTICS_STDDEV": "16.361398072633",
                        "STATISTICS_VALID_PERCENT": "50.82",
                    }
                },
            }
        ],
        "stac": {
            "proj:shape": [11831, 11599],
            "proj:projjson": {
                "$schema": "https://proj.org/schemas/v0.5/projjson.schema.json",
                "type": "ProjectedCRS",
                "name": "WGS 84 / UTM zone 44N",
                "base_crs": {
                    "name": "WGS 84",
                    "datum": {
                        "type": "GeodeticReferenceFrame",
                        "name": "World Geodetic System 1984",
                        "ellipsoid": {
                            "name": "WGS 84",
                            "semi_major_axis": 6378137,
                            "inverse_flattening": 298.257223563,
                        },
                    },
                    "coordinate_system": {
                        "subtype": "ellipsoidal",
                        "axis": [
                            {
                                "name": "Latitude",
                                "abbreviation": "lat",
                                "direction": "north",
                                "unit": "degree",
                            },
                            {
                                "name": "Longitude",
                                "abbreviation": "lon",
                                "direction": "east",
                                "unit": "degree",
                            },
                        ],
                    },
                },
                "conversion": {
                    "name": "Transverse Mercator",
                    "method": {
                        "name": "Transverse Mercator",
                        "id": {"authority": "EPSG", "code": 9807},
                    },
                    "parameters": [
                        {
                            "name": "Latitude of natural origin",
                            "value": 0,
                            "unit": "degree",
                            "id": {"authority": "EPSG", "code": 8801},
                        },
                        {
                            "name": "Longitude of natural origin",
                            "value": 81,
                            "unit": "degree",
                            "id": {"authority": "EPSG", "code": 8802},
                        },
                        {
                            "name": "Scale factor at natural origin",
                            "value": 0.9996,
                            "unit": "unity",
                            "id": {"authority": "EPSG", "code": 8805},
                        },
                        {
                            "name": "False easting",
                            "value": 500000,
                            "unit": "metre",
                            "id": {"authority": "EPSG", "code": 8806},
                        },
                        {
                            "name": "False northing",
                            "value": 0,
                            "unit": "metre",
                            "id": {"authority": "EPSG", "code": 8807},
                        },
                    ],
                },
                "coordinate_system": {
                    "subtype": "Cartesian",
                    "axis": [
                        {
                            "name": "Easting",
                            "abbreviation": "E",
                            "direction": "east",
                            "unit": "metre",
                        },
                        {
                            "name": "Northing",
                            "abbreviation": "N",
                            "direction": "north",
                            "unit": "metre",
                        },
                    ],
                },
            },
            "proj:transform": [415320, 10, 0, 2016620, 0, -10],
            "raster:bands": [
                {
                    "data_type": "uint8",
                    "stats": {
                        "minimum": 50,
                        "maximum": 193,
                        "mean": 155.318,
                        "stddev": 16.361,
                    },
                    "nodata": 0,
                }
            ],
            "eo:bands": [{"name": "b1", "description": "Gray"}],
        },
    }
    return data


@pytest.fixture()
def mock_check_json():
    check_json = {
        "ndvi": {
            "entry": {},
            "exit": {
                "filename_parts_count": 3,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": [
                    "TCX8021",
                    "IS18021",
                    "TCX8020",
                    "IS18020",
                ],
                "filename_product_code_count": 7,
                "filename_season_code_count": 0,
                "filename_season_code_startswith": [""],
                "epsg_code_count": 5,
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 200],
                "compression_type": "LZW",
            },
            "product_list": ["TCX8021", "IS18021", "TCX8020", "IS18020"],
            "s3_bucket_names": ["satsure-satimg", "satimg-to-be-deleted"],
        },
        "ndwi": {
            "entry": {},
            "exit": {
                "filename_parts_count": 3,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": [
                    "TCX9021",
                    "IS19021",
                    "TCX9020",
                    "IS19020",
                ],
                "filename_product_code_count": 7,
                "filename_season_code_count": 0,
                "filename_season_code_startswith": [""],
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 200],
                "compression_type": "LZW",
            },
            "product_list": ["TCX9021", "IS19021", "TCX9020", "IS19020"],
            "s3_bucket_names": ["satsure-satimg", "satimg-to-be-deleted"],
        },
        "mndwi": {
            "entry": {},
            "exit": {
                "filename_parts_count": 3,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": [
                    "TCXD021",
                    "IS1D021",
                    "TCXD020",
                    "IS1D020",
                ],
                "filename_product_code_count": 7,
                "filename_season_code_count": 0,
                "filename_season_code_startswith": [""],
                "epsg_code_count": 5,
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 200],
                "compression_type": "LZW",
            },
            "product_list": ["TCXD021", "IS1D021", "TCXD020", "IS1D020"],
            "s3_bucket_names": ["satsure-satimg", "satimg-to-be-deleted"],
        },
        "fcc": {
            "entry": {},
            "exit": {
                "filename_parts_count": 3,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": ["IS51010", "IS51011"],
                "filename_product_code_count": 7,
                "filename_season_code_count": 0,
                "filename_season_code_startswith": [""],
                "epsg_code_count": 5,
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 10000],
                "compression_type": "LZW",
            },
            "product_list": ["IS51010", "IS51011"],
            "s3_bucket_names": ["satsure-satimg", "satimg-to-be-deleted"],
        },
        "cs": {
            "entry": {},
            "exit": {
                "filename_parts_count": 4,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": ["CS"],
                "filename_product_code_count": 7,
                "filename_season_code_count": 4,
                "filename_season_code_startswith": ["K", "R"],
                "epsg_code_count": 5,
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 1],
                "compression_type": "LZW",
            },
            "product_list": ["CS"],
            "s3_bucket_names": ["satsure-products"],
        },
        "ch": {
            "entry": {},
            "exit": {
                "filename_parts_count": 4,
                "filename_endswith": ".tif",
                "filename_date_chars": 8,
                "filename_product_code": ["CH"],
                "filename_product_code_count": 7,
                "filename_season_code_count": 4,
                "filename_season_code_startswith": ["K", "R"],
                "epsg_code_count": 5,
                "pixelsize": "10.0 -10.0",
                "nodata_value": "0.0",
                "values_range": [0, 1],
                "compression_type": "LZW",
            },
            "product_list": ["CH"],
            "s3_bucket_names": ["satsure-products"],
        },
    }

    return check_json


@pytest.fixture()
def mock_computed_values():
    meta_data_obj = MetadataModel(
        filename="20161101_091032002000000_TCX8020.tif",
        region="091032002000000",
        fileuri="s3://satimg-to-be-deleted/Sentinel2/TCX8020/20161101_091032002000000_TCX8020.tif",
        product="TCX8020",
        date="20161101",
        date_region_product="20161101_091032002000000_TCX8020",
        pixelsize="10.0 -10.0",
        upperleft="415320.0 2016620.0",
        lowerleft="415320.0 1900630.0",
        lowerright="533630.0 1900630.0",
        upperright="533630.0 2016620.0",
        nodata="0.0",
        width="11831",
        height="11599",
        datatype="Byte",
        max="193",
        min="50",
        mean="155.31843492351",
        stddev="16.361398072633",
        valid_perc="50.82",
        origin="415320.0 2016620.0",
        filesize_mb="56.69",
        compression="LZW",
    )

    return meta_data_obj


@pytest.fixture()
def mock_entry_values():
    qa_qc_obj = QaQcModel(
        filename_parts_count=3,
        filename_endswith=".tif",
        filename_date_chars=8,
        filename_product_code="TCX8020",
        filename_product_code_count=7,
        filename_season_code_count=0,
        filename_season_code_startswith="",
        pixelsize="10.0 -10.0",
        nodata_value="0.0",
        values_range=[50, 193],
        compression_type="LZW",
    )

    return qa_qc_obj
