#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	C bindings for Google's Protocol Buffers
Summary(pl.UTF-8):	Wiązania C do biblioteki Google Protocol Buffers
Name:		protobuf-c
Version:	0.15
Release:	2
License:	Apache v2.0
Group:		Libraries
#Source0Download: http://code.google.com/p/protobuf-c/downloads/list
Source0:	http://protobuf-c.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	73ff0c8df50d2eee75269ad8f8c07dc8
URL:		http://code.google.com/p/protobuf-c/
BuildRequires:	libstdc++-devel
BuildRequires:	protobuf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protocol Buffers are a way of encoding structured data in an efficient
yet extensible format. This package provides a code generator and
run-time libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%description -l pl.UTF-8
Bufory protokołowe (Protocol Buffers) to sposób kodowania danych
strukturalnych w wydajny i rozszerzalny sposób. Ten pakiet dostarcza
generator kodu oraz biblioteki uruchomieniowe pozwalające na używanie
buforów protokołowych z czystego języka C (nie C++).

Wykorzystuje zmodyfikowaną wersję protoc o nazwie protoc-c.

%package devel
Summary:	Protocol Buffers C header files
Summary(pl.UTF-8):	Pliki nagłówkowe C biblioteki Protocol Buffers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains protobuf-c header files.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe protobuf-c.

%package static
Summary:	Static protobuf-c library
Summary(pl.UTF-8):	Statyczna biblioteka protobuf-c
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static protobuf-c library.

%description static -l pl.UTF-8
Statyczna biblioteka protobuf-c.

%prep
%setup -q

%build
%configure

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libprotobuf-c.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/protoc-c
%attr(755,root,root) %{_libdir}/libprotobuf-c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libprotobuf-c.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprotobuf-c.so
# XXX: dir shared with libtcmalloc and protobuf
%dir %{_includedir}/google
%{_includedir}/google/protobuf-c
%{_pkgconfigdir}/libprotobuf-c.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libprotobuf-c.a
