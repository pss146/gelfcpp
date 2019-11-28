cmake_minimum_required(VERSION 3.14)
project(gelfcpp)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Initialize Conan #############################################################
if (NOT EXISTS conanbuildinfo.cmake)
    message(FATAL_ERROR "Run Conan first: conan install <path_to_your_conanfile.txt>")
endif ()
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Build options ################################################################
option(GELFCPP_BUILD_EXAMPLES       "Build gelfcpp examples"      OFF)
option(GELFCPP_BUILD_TESTS          "Build gelfcpp tests"          ON)
option(GELFCPP_BUILD_DOCUMENTATION  "Build doxygen documentation"  ON)
option(GELFCPP_WITH_COMPRESSION     "Enable compression support"   ON)

# Preprocessor definitions ######################################################
IF(MSVC)
    add_definitions(-D_WIN32_WINNT=0x0601)

    # suppress specific compiler warnings
    add_definitions(-D_CRT_SECURE_NO_WARNINGS)
    add_definitions(-D_SILENCE_CXX17_ITERATOR_BASE_CLASS_DEPRECATION_WARNING)
    add_definitions(-D_SILENCE_CXX17_OLD_ALLOCATOR_MEMBERS_DEPRECATION_WARNING)
ENDIF()

# Create library ###############################################################
add_library(gelfcpp INTERFACE)
target_include_directories(gelfcpp INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(gelfcpp INTERFACE ${CONAN_LIBS})

# Additional build options #####################################################
if (GELFCPP_BUILD_DOCUMENTATION)
    add_subdirectory(doc)
endif()
if (GELFCPP_BUILD_EXAMPLES)
    add_subdirectory(example)
endif()
if (GELFCPP_BUILD_TESTS)
    enable_testing()
    add_subdirectory(test)
endif()
