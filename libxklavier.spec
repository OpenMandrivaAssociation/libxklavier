%define major 16
%define gir_major 1.0
%define libname %mklibname xklavier %{major}
%define girname %mklibname xkl-gir %{gir_major}
%define develname %mklibname -d xklavier

Name:		libxklavier
Summary:	X Keyboard support library
Version:	5.2.1
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gswitchit.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	iso-codes
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
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

%package -n %{girname}
Group: System/Libraries
Summary: GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: %{girname} = %{version}-%{release}
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

