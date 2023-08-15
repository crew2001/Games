cmake_minimum_required(VERSION 3.12)
project(snakegame VERSION 0.1.0 LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 20)

include(CTest)
enable_testing()

find_package(SDL2 REQUIRED)
include_directories(${SDL2_INCLUDE_DIRS})

add_executable(snakegame main.cpp snake.cpp)
target_link_libraries(snakegame ${SDL2_LIBRARIES})

