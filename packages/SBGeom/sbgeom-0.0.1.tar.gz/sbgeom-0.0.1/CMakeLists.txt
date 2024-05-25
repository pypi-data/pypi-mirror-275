cmake_minimum_required(VERSION 3.10)
project(SBGeom)

# Debug options (for asserts)
if (CMAKE_BUILD_TYPE STREQUAL "")
    message(STATUS "  Diag: Build type was unspecified, set to Release")
    set(CMAKE_BUILD_TYPE Release)
else ()
    message(STATUS "  Diag: Build type specified as '${CMAKE_BUILD_TYPE}'")
endif ()

if (CMAKE_BUILD_TYPE STREQUAL Debug)
    set_directory_properties(PROPERTIES COMPILE_DEFINITIONS "_DEBUG")
else ()
    set_directory_properties(PROPERTIES COMPILE_DEFINITIONS "NDEBUG")
endif ()
cmake_policy(SET CMP0074 NEW)
message(${CMAKE_BUILD_TYPE})
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -fPIC -march=native -std=c++17")
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "-O3  -g -fPIC -march=native -std=c++17")

find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    link_libraries(OpenMP::OpenMP_CXX)
endif()

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})
set(EIGEN3_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/src/eigen/")
add_definitions(-DSTELL_BLANKET_DIR="${CMAKE_CURRENT_SOURCE_DIR}") 
find_package(pybind11 CONFIG  REQUIRED)
#=========================================================================================================
#||                                             TARGETS                                                 ||
#=========================================================================================================
    
    add_subdirectory(src/stellgeom/demeter_util/math)    
    add_subdirectory(src/stellgeom/demeter_util/Input_Output)
    add_subdirectory(src/stellgeom/Flux_Surfaces_Geometry)
    add_subdirectory(src/stellgeom/Coils)    
    
    list(APPEND EXTRA_LIBS Input_Output)
    list(APPEND EXTRA_LIBS math)
    list(APPEND EXTRA_LIBS Flux_Surfaces_Geometry)
    list(APPEND EXTRA_LIBS Coils)
        
    pybind11_add_module(SBGeom_cpp src/main.cpp)
    target_link_libraries(SBGeom_cpp PRIVATE ${EXTRA_LIBS})
    target_include_directories(SBGeom_cpp PUBLIC "{PROJECT_BINARY_DIR}")
    set_target_properties(SBGeom_cpp PROPERTIES POSITION_INDEPENDENT_CODE ON)
    install(TARGETS SBGeom_cpp DESTINATION SBGeom)

