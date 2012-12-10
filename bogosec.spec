Name:           bogosec
Version:        20050315
Release:        %mkrel 7
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:20050315-7mdv2011.0
+ Revision: 616811
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0:20050315-6mdv2010.0
+ Revision: 424666
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:20050315-5mdv2009.0
+ Revision: 243359
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 19 2007 David Walluck <walluck@mandriva.org> 0:20050315-3mdv2008.1
+ Revision: 100271
- rebuild


* Wed May 10 2006 David Walluck <walluck@mandriva.org> 0:20050315-1mdk
- release

