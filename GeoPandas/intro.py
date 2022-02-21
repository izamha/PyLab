import geopandas as gpd

fp = '/home/gilfoyle/PycharmProjects/PyLab/GeoPandas/Data/DAMSELFISH_distributions.shp'

data = gpd.read_file(fp)
print(data)
print(type(data))
