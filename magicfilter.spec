Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	4
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
Copyright:	GPL
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}_1.2-28.diff.gz
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
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/{sbin,man/man8},etc/magicfilter}

make prefix=$RPM_BUILD_ROOT/usr/ bindir=$RPM_BUILD_ROOT/usr/sbin/ install
install magicfilterconfig $RPM_BUILD_ROOT/usr/sbin/
install filters/*-filter $RPM_BUILD_ROOT/etc/magicfilter

strip $RPM_BUILD_ROOT/usr/sbin/magicfilter

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* QuickInst ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {QuickInst,ChangeLog,TODO}.gz
%dir /etc/magicfilter

%attr(755,root,root) /usr/sbin/*
%attr(755,root,root) %config(noreplace) /etc/magicfilter/*
/usr/man/man*/*

%changelog
* Thu Apr 15 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.2-4]
- sloted BuildRoot into PLD standard
- removed man group from man pages
- gzipping documentation (instead bzipping)

* Sat Feb 13 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [1.2-3d]
- added patch from Debian
- rewrited %install
- few others modifications

* Mon Feb  8 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.2-2]
- added %attr(644, root, man) for man pages
- simpilification in %files
- removed Copying from %doc (GPL)
- added gzipping documentation

* Sun Feb  7 1999 Micha³ Kuratczyk <kura@pld.org.pl>
- initial rpm release
