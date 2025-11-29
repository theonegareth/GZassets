#!/usr/bin/env python3
"""
Launch file to bring up the hexadrone simulation in Gazebo.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    # Get the package directory
    pkg_hexadrone = get_package_share_directory('hexadrone')
    
    # Declare launch arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='hexadrone_runway.sdf',
        description='World file to load'
    )
    
    # Path to the world file
    world_path = PathJoinSubstitution([
        pkg_hexadrone,
        'worlds',
        LaunchConfiguration('world')
    ])
    
    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ]),
        launch_arguments={'gz_args': ['-r ', world_path]}.items()
    )
    
    # Bridge for IMU data (if needed)
    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu@sensor_msgs/msg/Imu@gz.msgs.IMU'],
        output='screen'
    )
    
    return LaunchDescription([
        world_arg,
        gazebo,
        imu_bridge
    ])