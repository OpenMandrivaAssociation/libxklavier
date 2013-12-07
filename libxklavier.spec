%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	16
%define gimajor	1.0
%define libname %mklibname xklavier %{major}
%define girname %mklibname xkl-gir %{gimajor}
%define devname %mklibname -d xklavier

Summary:	X Keyboard support library
Name:		libxklavier
Version:	5.3
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gswitchit.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxklavier/%{url_ver}/%{name}-%{version}.tar.xz

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
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Summary:	Libraries, includes, etc to develop libxklavier applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description  -n %{devname}
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

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Xkl-%{gimajor}.typelib

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README COPYING.LIB 
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Xkl-%{gimajor}.gir
%{_datadir}/gtk-doc/html/%{name}/*

