Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	5
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
Copyright:	GPL
Source:		%{name}-%{version}.tar.gz
Patch0:		magicfilter_1.2-28.diff.gz
Patch1:		magicfilter-DESTDIR.patch
Requires:	lpr
Obsoletes:	apsfilter
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_sysconfdir	/etc

%description
Magicfilter is a customizable, extensible automatic printer filter.

%description -l pl
Magicfilter jest konfigurowalnym i rozszerzalnym zbiorem filtrów dla
drukarek.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--bindir=%{_sbindir} \
	--mandir=%{_mandir}/man8

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_sbindir} \
	mandir=%{_mandir}/man8
	
install magicfilterconfig $RPM_BUILD_ROOT%{_sbindir}
install filters/*-filter $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

strip $RPM_BUILD_ROOT%{_sbindir}/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	QuickInst ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {QuickInst,ChangeLog,TODO}.gz
%dir %{_sysconfdir}/%{name}

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man*/*
