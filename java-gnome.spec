Summary:	Java-Gnome is a preliminary version of Java wrappers for GTK/GNOME
Summary(pl.UTF-8):   Java-Gnome jest wczesną wersją systemu javowych wrapperów dla GTK/GNOME
Name:		java-gnome
Version:	0.5.0
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/java-gnome/%{name}-%{version}.tar.gz
# Source0-md5:	5f566b967152240c6ba26b2e238e339a
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	jdk >= 1.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very preliminary version of Java wrappers for GTK/GNOME and
should be deamed ALPHA although it might work for you.

%description -l pl.UTF-8
To jest bardzo wczesna wersja javowych wrapperów dla GTK/GNOME i
powinna być traktowana jako ALPHA nawet jeżeli działa.

%prep
%setup -q

%build
./configure --prefix %{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS TODO THANKS doc
%{_libdir}/libGTKJava.so.0.5.0
%{_libdir}/libGTKJava.so
%{_libdir}/libGNOMEJava.so.0.5.0
%{_libdir}/libGNOMEJava.so
%{_datadir}/java-gnome
