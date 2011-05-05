%define	upstream_name	 Date-Calc
%define upstream_version 6.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary: 	Gregorian calendar date calculations
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

# these versioned requires are expressed in Makefile.PL, but not in module
BuildRequires:	perl(Bit::Vector) >= 6.400.0
BuildRequires:	perl(Carp::Clan)  >= 5.3
BuildRequires:	perl-devel

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch
Obsoletes:	%{name} < %version-%release

%description
This library provides all sorts of date calculations based on the Gregorian
calendar (the one used in all western countries today), thereby complying
with all relevant norms and standards: ISO/R 2015-1971, DIN 1355 and, to
some extent, ISO 8601 (where applicable).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} -pi -e 's,^#!perl,#!/usr/bin/perl,' examples/*.{pl,cgi}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make  CFLAGS="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc README.txt CHANGES.txt CREDITS.txt META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/Date
