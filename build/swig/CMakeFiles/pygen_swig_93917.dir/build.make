# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/adam/src/gr-messageutils

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/adam/src/gr-messageutils/build

# Utility rule file for pygen_swig_93917.

# Include the progress variables for this target.
include swig/CMakeFiles/pygen_swig_93917.dir/progress.make

swig/CMakeFiles/pygen_swig_93917: swig/messageutils_swig.pyc
swig/CMakeFiles/pygen_swig_93917: swig/messageutils_swig.pyo

swig/messageutils_swig.pyc: swig/messageutils_swig.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating messageutils_swig.pyc"
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/python /home/adam/src/gr-messageutils/build/python_compile_helper.py /home/adam/src/gr-messageutils/build/swig/messageutils_swig.py /home/adam/src/gr-messageutils/build/swig/messageutils_swig.pyc

swig/messageutils_swig.pyo: swig/messageutils_swig.py
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating messageutils_swig.pyo"
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/python -O /home/adam/src/gr-messageutils/build/python_compile_helper.py /home/adam/src/gr-messageutils/build/swig/messageutils_swig.py /home/adam/src/gr-messageutils/build/swig/messageutils_swig.pyo

swig/messageutils_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gnuradio.i
swig/messageutils_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_extras.i
swig/messageutils_swigPYTHON_wrap.cxx: ../swig/messageutils_swig.i
swig/messageutils_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_shared_ptr.i
swig/messageutils_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gnuradio_swig_bug_workaround.h
swig/messageutils_swigPYTHON_wrap.cxx: /usr/local/include/gnuradio/swig/gr_types.i
swig/messageutils_swigPYTHON_wrap.cxx: swig/messageutils_swig.tag
swig/messageutils_swigPYTHON_wrap.cxx: ../swig/messageutils_swig.i
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Swig source"
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/cmake -E make_directory /home/adam/src/gr-messageutils/build/swig
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/swig2.0 -python -fvirtual -modern -keyword -w511 -module messageutils_swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/home/adam/src/gr-messageutils/swig -I/home/adam/src/gr-messageutils/build/swig -outdir /home/adam/src/gr-messageutils/build/swig -c++ -I/home/adam/src/gr-messageutils/lib -I/home/adam/src/gr-messageutils/include -I/home/adam/src/gr-messageutils/build/lib -I/home/adam/src/gr-messageutils/build/include -I/usr/include -I/usr/local/include -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/home/adam/src/gr-messageutils/swig -I/home/adam/src/gr-messageutils/build/swig -o /home/adam/src/gr-messageutils/build/swig/messageutils_swigPYTHON_wrap.cxx /home/adam/src/gr-messageutils/swig/messageutils_swig.i

swig/messageutils_swig.py: swig/messageutils_swigPYTHON_wrap.cxx

swig/messageutils_swig.tag: swig/messageutils_swig_doc.i
swig/messageutils_swig.tag: swig/_messageutils_swig_swig_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating messageutils_swig.tag"
	cd /home/adam/src/gr-messageutils/build/swig && ./_messageutils_swig_swig_tag
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/cmake -E touch /home/adam/src/gr-messageutils/build/swig/messageutils_swig.tag

swig/messageutils_swig_doc.i: swig/messageutils_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating messageutils_swig_doc.i"
	cd /home/adam/src/gr-messageutils/docs/doxygen && /usr/bin/python -B /home/adam/src/gr-messageutils/docs/doxygen/swig_doc.py /home/adam/src/gr-messageutils/build/swig/messageutils_swig_doc_swig_docs/xml /home/adam/src/gr-messageutils/build/swig/messageutils_swig_doc.i

swig/messageutils_swig_doc_swig_docs/xml/index.xml: swig/_messageutils_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/adam/src/gr-messageutils/build/CMakeFiles $(CMAKE_PROGRESS_6)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for messageutils_swig_doc docs"
	cd /home/adam/src/gr-messageutils/build/swig && ./_messageutils_swig_doc_tag
	cd /home/adam/src/gr-messageutils/build/swig && /usr/bin/doxygen /home/adam/src/gr-messageutils/build/swig/messageutils_swig_doc_swig_docs/Doxyfile

pygen_swig_93917: swig/CMakeFiles/pygen_swig_93917
pygen_swig_93917: swig/messageutils_swig.pyc
pygen_swig_93917: swig/messageutils_swig.pyo
pygen_swig_93917: swig/messageutils_swigPYTHON_wrap.cxx
pygen_swig_93917: swig/messageutils_swig.py
pygen_swig_93917: swig/messageutils_swig.tag
pygen_swig_93917: swig/messageutils_swig_doc.i
pygen_swig_93917: swig/messageutils_swig_doc_swig_docs/xml/index.xml
pygen_swig_93917: swig/CMakeFiles/pygen_swig_93917.dir/build.make
.PHONY : pygen_swig_93917

# Rule to build all files generated by this target.
swig/CMakeFiles/pygen_swig_93917.dir/build: pygen_swig_93917
.PHONY : swig/CMakeFiles/pygen_swig_93917.dir/build

swig/CMakeFiles/pygen_swig_93917.dir/clean:
	cd /home/adam/src/gr-messageutils/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/pygen_swig_93917.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/pygen_swig_93917.dir/clean

swig/CMakeFiles/pygen_swig_93917.dir/depend:
	cd /home/adam/src/gr-messageutils/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/adam/src/gr-messageutils /home/adam/src/gr-messageutils/swig /home/adam/src/gr-messageutils/build /home/adam/src/gr-messageutils/build/swig /home/adam/src/gr-messageutils/build/swig/CMakeFiles/pygen_swig_93917.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/pygen_swig_93917.dir/depend

