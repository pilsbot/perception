import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Generate launch description with multiple components."""
    container = ComposableNodeContainer(
            package='rclcpp_components',
            node_name='ComponentManager',
            node_namespace=None,
            node_executable='component_container',
            composable_node_descriptions=[
                ComposableNode(
                    package='jetson_camera',
                    node_plugin='jetson_camera::JetsonCameraNode',
                    remappings=[('/image_raw', '/apriltag/image'), ('/camera_info', '/apriltag/camera_info')], 
                ), 
                ComposableNode(
                    package='apriltag_ros',
                    node_plugin='AprilTagNode',
                    parameters=[
                        '../config/apriltag.yaml', 
                    ]
                ), 
            ],
            #output='screen',
    )

    return launch.LaunchDescription([container])
