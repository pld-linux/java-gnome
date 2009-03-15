Summary:	Java bindings for the GNOME desktop environment
Summary(pl.UTF-8):	Wiązania Javy dla środowiska graficznego GNOME
Name:		java-gnome
Version:	4.0.10
Release:	1
License:	GPL v2
Group:		Libraries/Java
Source0:	http://ftp.gnome.org/pub/GNOME/sources/java-gnome/4.0/%{name}-%{version}.tar.bz2
# Source0-md5:	d52c1fd907824c6ed3f4b8b125f48e6c
Patch0:		%{name}-configure.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	jdk >= 1.1.7
BuildRequires:	junit
BuildRequires:	libglade2-devel >= 1:2.6.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java bindings for the GNOME desktop environment.

%description -l pl.UTF-8
Wiązania Javy dla środowiska graficznego GNOME.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	jdk_home=%{java_home}

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README doc/examples
%attr(755,root,root) %{_libdir}/libgtkjni-4.0.10.so
%{_javadir}/gtk-4.0.jar
%{_javadir}/gtk.jar
