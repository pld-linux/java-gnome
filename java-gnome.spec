Summary:	Java-Gnome is a preliminary version of Java wrappers for GTK/GNOME.
Name:		java-gnome
Version:	0.5.0
Release:	2
Requires:	gtk+ >= 1.2.0
License:	GPL
Group:		Applications
Source0:	%{name}-%{version}.tar.gz
URL:		http://java-gnome.sourceforge.net/

%description
This is a very preliminary version of Java wrappers for GTK/GNOME and
should be deamed ALPHA although it might work for you.

%prep
%setup -q

%build
./configure --prefix %{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL README NEWS TODO THANKS doc
%{_libdir}/libGTKJava.so.0.5.0
%{_libdir}/libGTKJava.so
%{_libdir}/libGNOMEJava.so.0.5.0
%{_libdir}/libGNOMEJava.so
%{_datadir}/java-gnome/

%clean
rm -rf $RPM_BUILD_ROOT
