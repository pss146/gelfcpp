function(create_all)
    message("Test: Adding 'all-in-one' test")

    file(GLOB_RECURSE sources ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)

    add_executable(gelfcpp_test_all ${sources})
    target_link_libraries(gelfcpp_test_all PUBLIC gelfcpp ${CONAN_LIBS_GTEST} ${CONAN_LIBS})

    add_test(NAME GelfCppTestAll
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
            COMMAND gelfcpp_test_all)
endfunction()

create_all()
