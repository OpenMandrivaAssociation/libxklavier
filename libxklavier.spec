%define major 11
%define libname %mklibname xklavier %major
Name:		libxklavier
Summary:	X Keyboard support library
Version:	3.2
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
Url:		http://gswitchit.sourceforge.net/
# (fc) 3.1-3mdv fix realloc misuse (CVS)
Patch1:		libxklavier-3.1-realloc.patch
BuildRequires:	libxml2-devel
BuildRequires:	doxygen
BuildRequires:	libxkbfile-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	automake1.9
BuildRequires:	gettext-devel
Source0:	http://prdownloads.sourceforge.net/gswitchit/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library allows you simplify XKB-related development.

%package data
Summary:	Keyboard description data
Group:		System/Libraries

%description data
This contains the data files needed by %name.

%package -n %libname
Summary:	X Keyboard support library
Group:		System/Libraries
Requires: 	%name-data >= %version-%release

%description -n %libname
This library allows you simplify XKB-related development.

%package -n %libname-devel
Summary: Libraries, includes, etc to develop libxklavier applications
Group: Development/C
Requires: %{libname} = %{version}
Provides: %name-devel = %version-%release
Conflicts: %{_lib}xklavier8-devel

%description  -n %libname-devel
Libraries, include files, etc you can use to develop libxklavier
applications.

%package -n %libname-static-devel
Group: Development/C
Summary: Static library of %name
Requires: %libname-devel = %version
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %libname-static-devel
This package contains the static library required for statically
linking applications based on %{name}.

%prep
%setup -q
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


%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig


%files data
%defattr(-, root, root)
%doc README
%{_datadir}/libxklavier


%files -n %libname
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README COPYING.LIB 
%{_libdir}/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%_datadir/gtk-doc/html/libxklavier/

%files -n %libname-static-devel
%defattr(-, root, root)
%{_libdir}/*.a


