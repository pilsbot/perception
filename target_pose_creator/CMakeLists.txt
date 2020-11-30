cmake_minimum_required(VERSION 3.5)
project(target_pose_creator)

set(CMAKE_CXX_STANDARD 14)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)


ament_package()

