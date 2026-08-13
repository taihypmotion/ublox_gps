import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Đường dẫn chuẩn tới file yaml của bạn
    config_file = '/home/hyp-jetson-orin-1/gps_ublox/src/ublox/ublox_gps/config/ublox_raw_sat.yaml'

    return LaunchDescription([
        Node(
            package='ublox_gps',
            executable='ublox_gps_node',
            name='ublox_gps_node',
            output='screen',
            # Ép node phải load toàn bộ các cấu trúc phân cấp phức tạp (hpg, gnss)
            parameters=[config_file]
        )
    ])
