Summary:	Java-Gnome is a preliminary version of Java wrappers for GTK/GNOME
Summary(pl):	Java-Gnome jest wczesn� wersj� systemu javowych wrapper�w dla GTK/GNOME
Name:		java-gnome
Version:	0.5.0
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/java-gnome/%{name}-%{version}.tar.gz
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	jdk >= 1.1.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a very preliminary version of Java wrappers for GTK/GNOME and
should be deamed ALPHA although it might work for you.

%description -l pl
To jest bardzo wczesna wersja javowych wrapper�w dla GTK/GNOME i
powinna by� traktowana jako ALPHA nawet je�eli dzia�a.

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
