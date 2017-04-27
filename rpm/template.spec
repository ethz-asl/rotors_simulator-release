Name:           ros-indigo-rotors-simulator
Version:        2.1.0
Release:        4%{?dist}
Summary:        ROS rotors_simulator package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/rotors_simulator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-rotors-comm
Requires:       ros-indigo-rotors-control
Requires:       ros-indigo-rotors-description
Requires:       ros-indigo-rotors-evaluation
Requires:       ros-indigo-rotors-gazebo
Requires:       ros-indigo-rotors-gazebo-plugins
Requires:       ros-indigo-rotors-hil-interface
Requires:       ros-indigo-rotors-joy-interface
Requires:       ros-indigo-rqt-rotors
BuildRequires:  ros-indigo-catkin

%description
RotorS is a MAV gazebo simulator.

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
* Thu Apr 27 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-4
- Autogenerated by Bloom

* Mon Apr 10 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-3
- Autogenerated by Bloom

* Mon Apr 10 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-2
- Autogenerated by Bloom

* Sun Apr 09 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-1
- Autogenerated by Bloom

* Sun Apr 09 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.1.0-0
- Autogenerated by Bloom

* Mon Aug 10 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.1-0
- Autogenerated by Bloom

* Sun Aug 09 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.0-0
- Autogenerated by Bloom

* Thu Jun 11 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.6-0
- Autogenerated by Bloom

* Tue Jun 09 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.5-0
- Autogenerated by Bloom

* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.4-0
- Autogenerated by Bloom

* Thu May 28 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.3-0
- Autogenerated by Bloom

* Wed May 27 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.2-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 1.1.1-0
- Autogenerated by Bloom

