Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	2d
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
Copyright:	GPL
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}_1.2-28.diff.gz
Requires:	lpr
Obsoletes:	apsfilter
BuildRoot:   	/tmp/buildroot-%{name}-%{version}

%description
Magicfilter is a customizable, extensible automatic printer filter.

%description -l pl
Magicfilter jest konfigurowalnym i rozszerzalnym zbiorem filtrów dla
drukarek.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{sbin,man/man8},etc/magicfilter}

make prefix=$RPM_BUILD_ROOT/usr/ bindir=$RPM_BUILD_ROOT/usr/sbin/ install
install magicfilterconfig $RPM_BUILD_ROOT/usr/sbin/
install filters/*-filter $RPM_BUILD_ROOT/etc/magicfilter

strip $RPM_BUILD_ROOT/usr/sbin/magicfilter

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/*
gzip -9nf QuickInst ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc QuickInst.gz ChangeLog.gz TODO.gz

%attr(755, root, root) /usr/sbin/*
%attr(644, root, man)  /usr/man/man*/*
%attr(755,root,root) %config(noreplace) /etc/magicfilter/*
%dir /etc/magicfilter

%changelog
* Sat Feb 13 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- added patch from Debian
- rewrited %install
- few others modifications

* Mon Feb  8 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.2-2]
- added %attr(644, root, man) for man pages
- simpilification in %files
- removed Copying from %doc (GPL)
- added gzipping documentation

* Sun Feb  7 1999 Micha³ Kuratczyk <kurkens@polbox.com>
- initial rpm release
