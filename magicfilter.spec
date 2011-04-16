Summary:	Printer filters
Summary(pl.UTF-8):	Filtry dla drukarek
Name:		magicfilter
Version:	2.3.i
%define	gitver	39e8faf
Release:	1
Group:		Applications/Printing
License:	BSD (magicfilter itself), GPL (man pages), Public Domain (filters)
Source0:	http://github.com/Orc/magicfilter/tarball/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7292fd304b7b752fddc3417646a7c8a6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-hpdj.patch
Patch2:		%{name}-configure.patch
URL:		http://www.pell.portland.or.us/~orc/Code/magicfilter/
BuildRequires:	bzip2
BuildRequires:	enscript
BuildRequires:	ghostscript
BuildRequires:	gzip
BuildRequires:	libjpeg-progs
BuildRequires:	libmagic-devel
BuildRequires:	m4
BuildRequires:	ncompress
BuildRequires:	netpbm-progs
BuildRequires:	tetex-dvips
BuildRequires:	transfig
# hp2pbm or lj2ps (for PCL conversion)
Requires:	bzip2
Requires:	enscript
Requires:	file
Requires:	ghostscript
Requires:	gzip
Requires:	libjpeg-progs
Requires:	ncompress
Requires:	netpbm-progs
Requires:	tetex-dvips
Requires:	transfig
Requires:	/usr/bin/lpr
Obsoletes:	apsfilter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magicfilter is a customizable, extensible automatic printer filter.

%description -l pl.UTF-8
Magicfilter jest konfigurowalnym i rozszerzalnym zbiorem filtrów dla
drukarek.

%prep
%setup -q -n Orc-magicfilter-%{gitver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
./configure.sh \
	--prefix=%{_prefix} \
	--execdir=%{_sbindir} \
	--filterdir=%{_sysconfdir}/magicfilter \
	--mandir=%{_mandir} \
	--with-papersize=a4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no ELFs in /etc
install -d $RPM_BUILD_ROOT%{_prefix}/lib/magicfilter
mv $RPM_BUILD_ROOT%{_sysconfdir}/magicfilter/textonly $RPM_BUILD_ROOT%{_prefix}/lib/magicfilter
ln -sf %{_prefix}/lib/magicfilter/textonly $RPM_BUILD_ROOT%{_sysconfdir}/magicfilter/textonly

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/magicfilter
%dir %{_sysconfdir}/%{name}
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/[!t]*
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/%{name}/tek*
%attr(755,root,root) %{_sysconfdir}/%{name}/textonly
%dir %{_prefix}/lib/%{name}
%attr(755,root,root) %{_prefix}/lib/%{name}/textonly
%{_mandir}/man5/magicfilter.5*
%{_mandir}/man8/magicfilter.8*
