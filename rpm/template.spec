Name:           ros-indigo-rotors-hil-interface
Version:        2.2.1
Release:        0%{?dist}
Summary:        ROS rotors_hil_interface package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/rotors_simulator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mav-msgs
Requires:       ros-indigo-mavros
Requires:       ros-indigo-mavros-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mav-msgs
BuildRequires:  ros-indigo-mavros
BuildRequires:  ros-indigo-mavros-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
RotorS Hardware-in-the-loop interface package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Dec 10 2018 Pavel Vechersky <pvechersky@gmail.com> - 2.2.1-0
- Autogenerated by Bloom

* Thu Apr 27 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.1-0
- Autogenerated by Bloom

* Thu Apr 27 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.0-4
- Autogenerated by Bloom

* Mon Apr 10 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.0-3
- Autogenerated by Bloom

* Mon Apr 10 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.0-2
- Autogenerated by Bloom

* Sun Apr 09 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Sun Apr 09 2017 Pavel Vechersky <pvechersky@gmail.com> - 2.1.0-0
- Autogenerated by Bloom

