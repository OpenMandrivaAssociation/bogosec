Name:           bogosec
Version:        20050315
Release:        %mkrel 3
Epoch:          0
Summary:        Source code security quality metric
URL:            http://bogosec.sourceforge.net/
Source0:        http://download.sourceforge.net/bogosec/bogosec-%{version}.tar.bz2
Patch0:         %{name}-build.patch
License:        CPL
Group:          Development/Other
Requires:       flawfinder
Requires:       gzip
Requires:       perl
Requires:       rpm
Requires:       rpm-build
Requires:       tar
BuildRequires:  flawfinder
BuildArch:      noarch

%description
BogoSec is a command-line perl script that wraps various scanners 
available on the system. Currently, BogoSec has support to analyze C/C++ 
code. Easily extendabile framework (with accompanying perl modules for 
each scanner).

%prep
%setup -q
%patch0 -p1

%build
./configure

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}_wrapper
%{_datadir}/%{name}
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
