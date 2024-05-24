"""
===================================
#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
@Author: chenxw
@Email : gisfanmachel@gmail.com
@File: shpTools.py
@Date: Create in 2021/1/22 13:43
@Description: 对geojson文件的操作类
@ Software: PyCharm

===================================
"""

import json
import os

import geopandas as gpd

from vgis_utils.vgis_file.fileTools import FileHelper


class GeoJsonHelper:

    def __init__(self):
        pass

    @staticmethod
    # 合并多个同类geojson
    def merge_geojsons(geojson_files_path, merge_result_file):
        index = 0
        all_data = {}
        encoding = FileHelper.get_file_encoding(geojson_files_path)
        for file_name in os.listdir(geojson_files_path):
            geojson_file = os.path.join(geojson_files_path, file_name)
            with open(geojson_file, 'r', encoding=encoding) as fp:
                each_data = json.load(fp)
            if index == 0:
                all_data = each_data
            else:
                all_data["features"] += each_data["features"]
        result_file = open(merge_result_file, "w")
        json.dump(all_data, result_file)

    # 将geojson转换为shp
    @staticmethod
    def convert_geojson_to_shp(geojson_path, shp_path):
        # 读取 GeoJSON 文件
        gdf = gpd.read_file(geojson_path, engine='pyogrio')
        # 保存为 Shapefile
        gdf.to_file(shp_path, driver='ESRI Shapefile', engine='pyogrio')

    # geojson里增加epsg
    @staticmethod
    def add_epsg_value_in_geojson(geojson_path, espg_value):
        encoding = FileHelper.get_file_encoding(geojson_path)
        data = json.load(open(geojson_path, encoding=encoding))
        if "crs" not in data:
            data['crs'] = {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::{}".format(espg_value)}}
        with open(geojson_path, 'w') as fp:
            json.dump(data, fp)

    # 获取geojson的几何类型和坐标信息
    @staticmethod
    def get_geojson_geometry_info(geojson_path):
        encoding = FileHelper.get_file_encoding(geojson_path)
        epsg_value, geometry_type = None, None
        f = open(geojson_path, encoding=encoding)
        data = json.load(f)
        if "crs" in data:
            epsg_info = data["crs"]["properties"]["name"]
            if "urn:ogc:def:crs:EPSG" in epsg_info:
                epsg_value = int(epsg_info.split("::")[1])
        if "features" in data:
            features = data["features"]
            if len(features) > 0:
                geometry_type = features[0]["geometry"]["type"]
                if epsg_value is None:
                    coordinates = str(features[0]["geometry"]["coordinates"])
                    print(coordinates)
                    x_coord = coordinates.split(",")[0].replace("[", "")
                    y_coord = coordinates.split(",")[1].replace("]", "")
                    x_coord = float(x_coord)
                    y_coord = float(y_coord)
                    # 这里只是简单做了判断
                    if x_coord <= 180 and y_coord <= 90:
                        epsg_value = 4326
                    else:
                        epsg_value = 3857

        return epsg_value, geometry_type

    @staticmethod
    def get_envlope_of_geojson(geojson_path):
        # 读取GeoJSON文件
        gdf = gpd.read_file(geojson_path, engine='pyogrio')
        # 获取坐标范围
        bounds = gdf.total_bounds
        return bounds


if __name__ == '__main__':
    geojson_path = "e:\\tttt-2.geoJson"
    # geojson_path = "e:\\110000.geoJson"
    shp_path = "e:\\tttt.shp"
    # GeoJsonHelper.convert_geojson_to_shp(geojson_path, shp_path)
    print(GeoJsonHelper.get_geojson_geometry_info(geojson_path))
    print(GeoJsonHelper.get_envlope_of_geojson(geojson_path)[0])
