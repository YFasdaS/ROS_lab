
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='Solozobov_Kirill_pkg',           
            executable='even_publisher',
            name='even_publisher',
            output='screen',
        ),
        Node(
            package='Solozobov_Kirill_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])
