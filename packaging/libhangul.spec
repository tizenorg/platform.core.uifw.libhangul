Name:           libhangul
Version:        0.1.0
Release:        0
License:        LGPL-2.1
Group:          System/I18n/Korean
AutoReqProv:    on
Url:            http://code.google.com/p/libhangul
Source0:        %{name}-%{version}.tar.gz
Source1001:     libhangul.manifest
Summary:        Hangul input library used by scim-hangul and ibus-hangul
BuildRequires:  gettext-tools


%description
Hangul input library used by scim-hangul and ibus-hangul


Authors:
--------
    Choe Hwanjin <choe.hwanjin@gmail.com>
    Joon-cheol Park <jooncheol@gmail.com>

Hangul input library used by scim-hangul and ibus-hangul


%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          System/I18n/Korean
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.


%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/lib*.so.*
%dir %{_datadir}/libhangul/
%dir %{_datadir}/libhangul/hanja/
%{_datadir}/libhangul/hanja/hanja.txt
%{_bindir}/hangul
%{_datadir}/locale/ko/LC_MESSAGES/libhangul.mo

%files devel
%manifest %{name}.manifest
%defattr(-, root, root)
%{_includedir}/hangul-1.0/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libhangul.pc
