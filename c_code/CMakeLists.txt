cmake_minimum_required(VERSION 3.0.0)
project(proj VERSION 0.0.1)

include(CTest)
enable_testing()

set(CMAKE_C_COMPILER    "C:\\mingw64\\bin\\gcc.exe")
set(CMAKE_CXX_COMPILER  "C:\\mingw64\\bin\\g++.exe")

set(CMAKE_C_STANDARD    11)
set(CMAKE_CXX_STANDARD  17)

# header files folder
include_directories(
    "libs/"
)
# c source files
file(GLOB_RECURSE SOURCES 
    "libs/*.c"
)

set(CMAKE_BUILD_TYPE "Debug")

add_executable(proj main.c ${SOURCES})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
