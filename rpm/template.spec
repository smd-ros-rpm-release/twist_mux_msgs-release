Name:           ros-hydro-twist-mux-msgs
Version:        0.0.1
Release:        1%{?dist}
Summary:        ROS twist_mux_msgs package

Group:          Development/Libraries
License:        CC BY-NC-SA 4.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-actionlib
Requires:       ros-hydro-actionlib-msgs
Requires:       ros-hydro-message-runtime
BuildRequires:  ros-hydro-actionlib
BuildRequires:  ros-hydro-actionlib-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation

%description
The twist_mux msgs and actions package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sun Nov 16 2014 Enrique Fernandez <enrique.fernandez@pal-robotics.com> - 0.0.1-1
- Autogenerated by Bloom

* Thu Nov 13 2014 Enrique Fernandez <enrique.fernandez@pal-robotics.com> - 0.0.1-0
- Autogenerated by Bloom

