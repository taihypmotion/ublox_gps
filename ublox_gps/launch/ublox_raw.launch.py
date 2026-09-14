import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory('ublox_gps'),
        'config',
        'ublox_raw_sat.yaml'
    )

    return LaunchDescription([
        Node(
            package='ublox_gps',
            executable='ublox_gps_node',
            name='ublox_gps_node',
            output='screen',
            parameters=[config_file],
            # The serial worker exits on USB EOF. Respawn resolves the stable
            # by-id path again after the receiver has re-enumerated.
            respawn=True,
            respawn_delay=2.0,
        )
    ])
