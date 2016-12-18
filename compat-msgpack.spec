%global real_name msgpack 

Name:		compat-msgpack
Version:	0.5.9
Release:	1%{?dist}
Summary:	Binary-based efficient object serialization library
Group:		System Environment/Libraries

License:	ASL 2.0
URL:		http://msgpack.org
Source0:	https://github.com/msgpack/msgpack-c/releases/download/cpp-%{version}/msgpack-%{version}.tar.gz
Patch0:		msgpack-fix-int-float-test.patch

# for regenerating configure
BuildRequires:	libtool
# for %%check
BuildRequires:	gtest-devel
BuildRequires:	zlib-devel

Conflicts:	%{real_name}

%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.


%package devel
Summary:	Libraries and header files for %{real_name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Conflicts:	%{real_name}-devel

%description devel
Libraries and header files for %{real_name}


%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p1 -b .fix-int-float-test


%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING ChangeLog LICENSE NOTICE README README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/msgpack.pc


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.9-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Daiki Ueno <dueno@redhat.com> - 0.5.9-1
- new upstream release
- apply patch to fix int->float test failure

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan  9 2014 Daiki Ueno <dueno@redhat.com> - 0.5.8-1
- new upstream release
- remove patches that are no longer needed

* Tue Aug 27 2013 Dan Horák <dan[at]danny.cz> - 0.5.7-5
- apply upstream fix for big endians

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 15 2012 Daiki Ueno <dueno@redhat.com> - 0.5.7-1
- initial packaging for Fedora

