%define url_ver %(echo %{version}|cut -d. -f1,2)

%define sname	msi
%define api	1.0
%define major	0
%define libname	%mklibname %{sname} %{major}
%define girname	%mklibname %{sname}-gir %{api}
%define devname	%mklibname -d %{sname}

Summary:	Tool to inspect and build Windows Installer (.MSI) files
Name:		msitools
Version:	0.99
Release:	1
Group:		Development/Databases
License:	GPLv2+
URL:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/msitools/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	vala-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libgcab-1.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(uuid)

%description
msitools is a set of programs to inspect and build Windows Installer
(.MSI) files.

%package -n %{libname}
Summary:	A support library for %{name}
Group:		System/Libraries

%description -n %{libname}
A support library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Other
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -q

%build
%configure

%make_build

%install
%make_install

%files 
%{_bindir}/*
%{_datadir}/bash-completion/completions/msitools
%{_datadir}/locale/*/LC_MESSAGES/msitools.mo

%files -n %{libname}
%{_libdir}/lib%{sname}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Libmsi-%{api}.typelib

%files -n %{devname}
%{_includedir}/lib%{sname}-%{api}/*
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Lib%{sname}-%{api}.gir
%{_datadir}/vala/vapi/lib%{sname}-%{api}.vapi
# MD I'm not sure what these are yet
%{_datadir}/wixl-%{version}/include/*.wxi

