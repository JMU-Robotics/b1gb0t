import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    urg_dir = get_package_share_directory('urg_node2')
    urg_launch_file_dir = os.path.join(urg_dir, 'launch')

    rover_dir = get_package_share_directory('roverrobotics_driver')
    rover_launch_file_dir = os.path.join(rover_dir, 'launch')

    return LaunchDescription([
        # LIDAR
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([urg_launch_file_dir,
                                           '/urg_node2.launch.py']),
        ),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([rover_launch_file_dir,
                                           '/pro.launch.py']),
        ),
        
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=["0", "0", "0", "0", "0", "0","base_link", "laser"],
            name='transform'
        ),
    ])
