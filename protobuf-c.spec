#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	C bindings for Google's Protocol Buffers
Summary(pl.UTF-8):	Wiązania C do biblioteki Google Protocol Buffers
Name:		protobuf-c
Version:	1.3.1
Release:	2
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/protobuf-c/protobuf-c/releases
Source0:	https://github.com/protobuf-c/protobuf-c/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ab3aa79312ed7b1fca401c8682e3aa7a
Patch0:		%{name}-update.patch
URL:		https://github.com/protobuf-c/protobuf-c
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	protobuf-devel >= 2.6.0
Requires:	protobuf >= 2.6.0
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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

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
%doc ChangeLog LICENSE README.md TODO
%attr(755,root,root) %{_bindir}/protoc-c
%attr(755,root,root) %{_bindir}/protoc-gen-c
%attr(755,root,root) %{_libdir}/libprotobuf-c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libprotobuf-c.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprotobuf-c.so
# XXX: dir shared with libtcmalloc and protobuf
%dir %{_includedir}/google
%{_includedir}/google/protobuf-c
%{_includedir}/protobuf-c
%{_pkgconfigdir}/libprotobuf-c.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libprotobuf-c.a
