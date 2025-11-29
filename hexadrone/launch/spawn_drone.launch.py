#!/usr/bin/env python3
"""
Launch file to spawn the hexadrone in a custom world.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    # Get the package directory
    pkg_hexadrone = get_package_share_directory('hexadrone')
    
    # Get launch configuration
    world_file = LaunchConfiguration('world').perform(context)
    
    # Path to the world file
    world_path = PathJoinSubstitution([
        pkg_hexadrone,
        'worlds',
        world_file
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
    
    # Spawn the drone model
    spawn_drone = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'hexadrone',
            '-file', PathJoinSubstitution([pkg_hexadrone, 'models', 'hexadrone_model', 'model.sdf']),
            '-x', '0',
            '-y', '0',
            '-z', '0.12'
        ],
        output='screen'
    )
    
    # Bridge for IMU data
    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu@sensor_msgs/msg/Imu@gz.msgs.IMU'],
        output='screen'
    )
    
    return [gazebo, spawn_drone, imu_bridge]


def generate_launch_description():
    # Declare launch arguments
    world_arg = DeclareLaunchArgument(
        'world',
        default_value='hexadrone_runway.sdf',
        description='World file to load'
    )
    
    return LaunchDescription([
        world_arg,
        OpaqueFunction(function=launch_setup)
    ])