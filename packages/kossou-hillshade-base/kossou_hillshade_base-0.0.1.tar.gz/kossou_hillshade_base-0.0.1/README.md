# Python-based analysis of geospatial data

Replication of results described in [^1].

## Download elevation file

To download the elevation file, first register an account on the [USGS EROS registration system](https://ers.cr.usgs.gov/login) to get download access via [EarthExplorer](https://earthexplorer.usgs.gov) and/or [GloVis](https://glovis.usgs.gov/).

### EarthExplorer

Under the Datasets tab, under the Digital Elevation category, under the SRTM subcategory, select SRTM Void Filled.

<img src="figure/dataset-tab-ee.png" width="200" />

Under the Additional Criteria tab, set Entity ID to SRTM3N07W006V2.

<img src="figure/additional-criteria-tab-ee.png" width="200" />

The results tab will then contain the SRTM Void Filled DEM entity with ID SRTM3N07W006V2, as described in [^1].

<img src="figure/results-tab-ee.png" width="200" />

You can select the Download Options icon and download the GeoTIFF 3 Arc-second file, `n07_w006_3arc_v2.tif`.

<img src="figure/download-options-ee.png" width="500" />

### GloVis

Under the Interface Controls, click the "+" next to "Selected Data Set(s) and add the SRTM Void Filled data set.

<img src="figure/add-dataset-gv.png" width="200" />

<img src="figure/selected-dataset-gv.png" width="200" />

Add a Dataset Metadata Filter for the SRTM Void Filled dataset with Entity ID SRTM3N07W006V2, and apply the filter.

<img src="figure/add-dataset-filter-gv.png" width="200" />

<img src="figure/dataset-metadata-filter-gv.png" width="200" />

You may need to scroll the map view to west Africa in order to find the result. The scene will appear in the Scene Navigator, where you can view the download options and download the GeoTIFF 3 Arc-second file `n07_w006_3arc_v2.tif`.

<img src="figure/download-options-gv.png" width="200" />

## Download landsat files

Similar to above, use EarthExplorer or GloVis to search the Landsat 8-9 OLI/TIRS C2 L1 dataset for a result with Landsat Product Identifier L1 of LC09_L1TP_197055_20220111_20230502_02_T1.

## Generate plots

The results of [^1] may be replicated by running:

```
python plot_geotiff.py n07_w006_3arc_v2.tif Figure_2_DEM_Kossou_1609.jpg
python plot_hillshade.py n07_w006_3arc_v2.tif Figure_3_Hillshade_Kossou_1609.jpg
python plot_hillshade.py --azimuth 230 --colormap plasma n07_w006_3arc_v2.tif Figure_4_Azimuth_hillshade_Kossou.jpg
python plot_hillshade.py --altitude 10 --colormap magma n07_w006_3arc_v2.tif Figure_5_Angle_hillshade_Kossou.jpg
```

[^1]: Polina Lemenkova and Olivier Debeir, [Satellite Image Processing by Python and R Using Landsat 9 OLI/TIRS and SRTM DEM Data on Côte d’Ivoire, West Africa](https://www.mdpi.com/2313-433X/8/12/317). J. Imaging 2022