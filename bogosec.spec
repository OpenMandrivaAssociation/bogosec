Name:		bogosec
Version:	2.3
Release:	1
Summary:	Source code security quality metric
URL:		https://bogosec.sourceforge.net/
Source0:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/bogosec/%{version}-0ubuntu1/bogosec_%{version}.orig.tar.gz
#Patch0:		%{name}-build.patch
License:	CPL
Group:		Development/Other
Requires:	flawfinder
Requires:	gzip
Requires:	perl
Requires:	rpm
Requires:	rpm-build
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	flawfinder
BuildArch:	noarch

%description
BogoSec is a command-line perl script that wraps various scanners 
available on the system. Currently, BogoSec has support to analyze C/C++ 
code. Easily extendabile framework (with accompanying perl modules for 
each scanner).

%prep
%autosetup -p1 -n %{name}.orig

%build
./configure

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir} %{buildroot}%{_mandir}/man1
%make_install

%files
%doc README
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}_wrapper
%{_prefix}/lib/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
