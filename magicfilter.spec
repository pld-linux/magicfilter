Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	1
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc COPYING ChangeLog README

%attr(755, root, root) /usr/bin/*
/usr/share/magicfilter/*
/usr/man/man*/*

%changelog
* Sun Feb  7 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- initial rpm release
