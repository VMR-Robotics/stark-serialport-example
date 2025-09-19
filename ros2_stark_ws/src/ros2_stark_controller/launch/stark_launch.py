from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 右手控制器节点
        Node(
            package='ros2_stark_controller',
            executable='stark_node',
            name='right_hand_controller',
            namespace='right_hand',
            output='screen',
            parameters=[
                {'port': "/dev/ttyUSB0"},
                {'baudrate': 460800},
                {'slave_id': 2},
                {'protocol_type': 1},  # Modbus RTU
                {'log_level': 2}       # Info
            ]
        ),
        
        # 左手控制器节点
        Node(
            package='ros2_stark_controller',
            executable='stark_node',
            name='left_hand_controller',
            namespace='left_hand',
            output='screen',
            parameters=[
                {'port': "/dev/ttyUSB1"},
                {'baudrate': 460800},
                {'slave_id': 1},
                {'protocol_type': 1},  # Modbus RTU
                {'log_level': 2}       # Info
            ]
        ),
    ])
