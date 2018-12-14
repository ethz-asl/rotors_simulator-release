Name:           ros-melodic-rotors-gazebo-plugins
Version:        2.2.3
Release:        0%{?dist}
Summary:        ROS rotors_gazebo_plugins package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/rotors_simulator
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       glog-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       ros-melodic-cmake-modules
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-gazebo-plugins
Requires:       ros-melodic-gazebo-ros
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-mav-msgs
Requires:       ros-melodic-mavros
Requires:       ros-melodic-octomap
Requires:       ros-melodic-octomap-msgs
Requires:       ros-melodic-octomap-ros
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rotors-comm
Requires:       ros-melodic-rotors-control
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
Requires:       yaml-cpp-devel
BuildRequires:  gazebo-devel
BuildRequires:  glog-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-gazebo-plugins
BuildRequires:  ros-melodic-gazebo-ros
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-mav-msgs
BuildRequires:  ros-melodic-mavros
BuildRequires:  ros-melodic-octomap
BuildRequires:  ros-melodic-octomap-msgs
BuildRequires:  ros-melodic-octomap-ros
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rotors-comm
BuildRequires:  ros-melodic-rotors-control
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf
BuildRequires:  yaml-cpp-devel

%description
The rotors_gazebo_plugins package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Dec 14 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.2.3-0
- Autogenerated by Bloom

* Wed Dec 12 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.2.2-0
- Autogenerated by Bloom

