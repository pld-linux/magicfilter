Summary:	Printer filters
Summary(pl):	Filtry dla drukarek
Name:		magicfilter
Version:	1.2
Release:	8
Group:		Applications/Printing
License:	GPL
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/printing/%{name}-%{version}.tar.gz
# Source0-md5:	dcece221e363ca5dbc79bdd84713c04e
Patch0:		%{name}_1.2-28.diff.gz
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-hpdj.patch
BuildRequires:	a2ps
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	gzip
BuildRequires:	libjpeg-progs
BuildRequires:	libtiff-progs
BuildRequires:	netpbm-progs
BuildRequires:	tetex-dvips
BuildRequires:	transfig
BuildRequires:	smtpdaemon
Requires:	a2ps
Requires:	ghostscript
Requires:	groff
Requires:	gzip
Requires:	libjpeg-progs
Requires:	libtiff-progs
Requires:	netpbm-progs
Requires:	tetex-dvips
Requires:	transfig
Requires:	/usr/bin/lpr
Requires:	smtpdaemon
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
%patch2 -p1

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--bindir=%{_sbindir} \
	--mandir=%{_mandir}/man8

%{__make} bindir=%{_sbindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_sbindir} \
	mandir=%{_mandir}/man8

install magicfilterconfig $RPM_BUILD_ROOT%{_sbindir}
install filters/*-filter $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc QuickInst ChangeLog TODO
%dir %{_sysconfdir}/%{name}

%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man*/*
