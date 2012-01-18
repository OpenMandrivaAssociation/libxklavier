%define major 16
%define libname %mklibname xklavier %{major}
%define develname %mklibname -d xklavier

Name:		libxklavier
Summary:	X Keyboard support library
Version:	5.2
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gswitchit.sourceforge.net/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	iso-codes
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xkbfile)

%description
This library allows you simplify XKB-related development.


%package -n %{libname}
Summary:	X Keyboard support library
Group:		System/Libraries

%description -n %{libname}
This library allows you simplify XKB-related development.

%package -n %{develname}
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: %{_lib}xklavier8-devel
Obsoletes: %mklibname -d xklavier 11

%description  -n %{develname}
Libraries, include files, etc you can use to develop libxklavier
applications.

%prep
%setup -q

%build
if [ ! -f configure ]; then
    CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh
fi
%configure2_5x \
	--disable-static \
	--with-xkb-base=%{_datadir}/X11/xkb/ \
	--with-xkb-bin-base=%{_bindir}/

%make 

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc COPYING.LIB 
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*
%{_datadir}/gtk-doc/html/%{name}/*
