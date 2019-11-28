from conans import ConanFile, CMake, tools

class ppConsul(ConanFile):
    name = "gelfcpp"
    version = "0.1"
    license = "Boost Software License v1.0"
    author = "Perepelitsyn Stanislav <stas.perepel@gmail.com>"
    url = "https://github.com/pss146/gelfcpp"
    description = "Library for sending Graylog Extended Log Format (GELF) messages from C++ applications"
    topics = ("gelfcpp", "gelf")
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports = ("LICENSE")
    exports_sources = ("include/*", "CMakeLists.txt", "README.md", "doc/*", "example/*", "test/*")
    no_copy_source = True

    def requirements(self):
        self.requires.add("boost/1.70.0@conan/stable")
        self.requires.add("gtest/1.8.1@bincrafters/stable")
        self.requires.add("rapidjson/1.1.0@bincrafters/stable")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self): # this is not building a library, just tests
        cmake = self._configure_cmake()
        cmake.build()
        if tools.get_env("CONAN_RUN_TESTS", True):
            cmake.test()

    def package(self):
        self.copy("*", dst="include", src="include")
        self.copy(pattern="LICENSE.txt", dst="licenses")

    def package_id(self):
        self.info.header_only()

