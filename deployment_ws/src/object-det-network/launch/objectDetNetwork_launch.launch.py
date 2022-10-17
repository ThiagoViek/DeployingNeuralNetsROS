from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='object-det-network',
            executable='inferenceNode',
            output='screen'),

        Node(
            package='object-det-network',
            executable='imagePublisherNode',
            output='screen'),
    ])
