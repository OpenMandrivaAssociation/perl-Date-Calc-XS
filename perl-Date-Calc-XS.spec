%define upstream_name    Date-Calc-XS
%define upstream_version 6.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 6.3
Release:	3

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Date/Date-Calc-XS-6.3.tar.gz

BuildRequires: perl(Bit::Vector)
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Date::Calc)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
You never use this module directly. Use the Date::Calc(3) manpage instead!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml license
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 6.200.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.200.0-1
+ Revision: 634010
- import perl-Date-Calc-XS


