Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	5
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(pl):	Aplikacje/Drukowanie
License:	GPL
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}_1.2-28.diff.gz
Patch1:		%{name}-DESTDIR.patch
Requires:	lpr
Obsoletes:	apsfilter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--bindir=%{_sbindir} \
	--mandir=%{_mandir}/man8

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_sbindir} \
	mandir=%{_mandir}/man8
	
install magicfilterconfig $RPM_BUILD_ROOT%{_sbindir}
install filters/*-filter $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

gzip -9nf QuickInst ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {QuickInst,ChangeLog,TODO}.gz
%dir %{_sysconfdir}/%{name}

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man*/*
