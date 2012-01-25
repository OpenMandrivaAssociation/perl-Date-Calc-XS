%define upstream_name    Date-Calc-XS
%define upstream_version 6.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

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


