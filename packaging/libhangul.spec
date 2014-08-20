Name:       libhangul
Summary:    Hangul keyboard input library
Version:    0.0.10
Release:    1
Group:      System Environment/Libraries
License:    LGPL
Source0:    %{name}-%{version}.tar.bz2
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
This library implements Hangul keyboard input with various types of Korean keyboards.  It is intended to be a base library of Korean input methods on multiple platforms.
This package contains the shared library and the runtime data.

%package data
Summary:    Hangul keyboard input library - data
Group:      System Environment/Libraries
Requires:   %{name} = %{version}-%{release}

%description data
This package contains the architecture independent data.


%package devel
Summary:    Hangul keyboard input library - development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and the static library.


%prep
%setup -q -n %{name}-%{version}


%build
%reconfigure --disable-static

# Call make instruction with smp support
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/lib*.so*


%files data
%defattr(-,root,root,-)
%{_datadir}/libhangul/*


%files devel
%defattr(-,root,root,-)
%{_includedir}/hangul-1.0/*.h
%{_libdir}/pkgconfig/*.pc

