Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	2
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
Copyright:	GPL
Source:		%{name}-%{version}.tar.gz
Requires:	lpr
Obsoletes:	apsfilter
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
Magicfilter is a customizable, extensible automatic printer filter.

%description -l pl
Magicfilter jest konfigurowalnym i rozszerzalnym zbiorem filtrów dla
drukarek.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr 
make magicfilter magicfilter.man 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man8,share/magicfilter}

install -s magicfilter  $RPM_BUILD_ROOT/usr/bin
install magicfilter.man $RPM_BUILD_ROOT/usr/man/man8

mv filters $RPM_BUILD_ROOT/usr/share/magicfilter

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*
gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README ChangeLog

%attr(755, root, root) /usr/bin/*
%attr(644, root, man)  /usr/man/man*/*
/usr/share/magicfilter

%changelog
* Mon Feb  8 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.2-2]
- added %attr(644, root, man) for man pages
- simpilification in %files
- removed Copying from %doc (GPL)
- added gzipping documentation

* Sun Feb  7 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- initial rpm release
