%define major 12
%define libname %mklibname xklavier %major
%define develname %mklibname -d xklavier
%define staticname %mklibname -s -d xklavier
Name:		libxklavier
Summary:	X Keyboard support library
Version:	3.9
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://gswitchit.sourceforge.net/
Patch:		libxklavier-3.9-format-strings.patch
# (fc) 3.1-3mdv fix realloc misuse (CVS)
Patch1:		libxklavier-3.1-realloc.patch
BuildRequires:	libxml2-devel
BuildRequires:	doxygen
BuildRequires:	libxkbfile-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	automake1.9
BuildRequires:	gettext-devel
BuildRequires:	iso-codes
Source: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
#Source0:	http://prdownloads.sourceforge.net/gswitchit/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library allows you simplify XKB-related development.


%package -n %libname
Summary:	X Keyboard support library
Group:		System/Libraries
Requires: iso-codes

%description -n %libname
This library allows you simplify XKB-related development.

%package -n %develname
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/C
Requires: %{libname} = %{version}
Provides: %name-devel = %version-%release
Conflicts: %{_lib}xklavier8-devel
Obsoletes: %mklibname -d xklavier 11

%description  -n %develname
Libraries, include files, etc you can use to develop libxklavier
applications.

%package -n %staticname
Group: Development/C
Summary: Static library of %name
Requires: %develname = %version
Provides: %{name}-static-devel = %{version}-%{release}
Obsoletes: %mklibname -s -d xklavier 11

%description -n %staticname
This package contains the static library required for statically
linking applications based on %{name}.

%prep
%setup -q
%patch -p1
%patch1 -p1 -b .fixrealloc

%build
if [ ! -f configure ]; then
    CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh
fi
%configure2_5x --enable-doxygen --with-xkb-base=%_datadir/X11/xkb/ --with-xkb-bin-base=%_bindir/ --enable-xmm-support
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf %{buildroot}


%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif


%files -n %libname
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB 
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%_datadir/gtk-doc/html/libxklavier/

%files -n %staticname
%defattr(-, root, root)
%{_libdir}/*.a


