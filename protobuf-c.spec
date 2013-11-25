#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	C bindings for Google's Protocol Buffers
Name:		protobuf-c
Version:	0.15
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://protobuf-c.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	73ff0c8df50d2eee75269ad8f8c07dc8
URL:		http://code.google.com/p/protobuf-c/
BuildRequires:	protobuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. This package provides a code generator and
run-time libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package devel
Summary:	Protocol Buffers C headers and libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_libdir}/libprotobuf-c.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO ChangeLog
%attr(755,root,root) %{_bindir}/protoc-c
%attr(755,root,root) %{_libdir}/libprotobuf-c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libprotobuf-c.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprotobuf-c.so
%{_includedir}/google
%{_pkgconfigdir}/libprotobuf-c.pc
