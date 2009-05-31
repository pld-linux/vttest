Summary:	Test VT100-type terminal
Summary(pl.UTF-8):	Narzędzie do testowania terminala typu VT100
Name:		vttest
Version:	20071216
Release:	1
License:	MIT-like
Group:		Applications
Source0:	ftp://invisible-island.net/vttest/%{name}-%{version}.tgz
# Source0-md5:	490cebc85e531c833dcf14c32790184b
URL:		http://dickey.his.com/vttest/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program to test the compatibility (or to demonstrate the
non-compatibility) of so-called "VT100-compatible" terminals.

%description -l pl.UTF-8
Ten program służy do testowania kompatybilności (lub demonstrowania
niekompatybilności) tak zwanych terminali "zgodnych z VT100".

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES COPYING README
%attr(755,root,root) %{_bindir}/vttest
%{_mandir}/man1/vttest.1*
