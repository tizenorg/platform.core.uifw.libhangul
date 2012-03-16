#sbs-git:slp/pkgs/l/libhangul libhangul 2.1.10 ff69a9eb13c322873f2fc93818273bea67f7862e
# >> macros
# << macros

Name:       libhangul
Summary:    Hangul keyboard input library
Version: 2.1.10
Release:    2
Group:      System/Libraries
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
This library implements Hangul keyboard input with various types of Korean keyboards.  It is intended to be a base library of Korean input methods on multiple platforms.
This package contains the shared library and the runtime data.

%package data
Summary:    Hangul keyboard input library - data
Group:      System/Libraries
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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static

# Call make instruction with smp support
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/lib*.so*
# << files


%files data
%defattr(-,root,root,-)
# >> files
%{_datadir}/libhangul/*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/hangul-1.0/*.h
%{_libdir}/pkgconfig/*.pc
# << files devel

