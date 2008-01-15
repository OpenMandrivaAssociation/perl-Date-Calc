%define	module	Date-Calc
%define	version	5.5.1
%define	release	%mkrel 8
%define	pdir	Date

Summary: 	Gregorian calendar date calculations
Name: 		perl-%{module}
Version: 	%{version}
Release:	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	perl-devel
# these versioned requires are expressed in Makefile.PL, but not in module
BuildRequires:	perl(Bit::Vector) >= 6.4
BuildRequires:	perl(Carp::Clan) >= 5.3
Requires:	perl-Bit-Vector >= 6.4
Requires:	perl-Carp-Clan >= 5.3

%description
This library provides all sorts of date calculations based on the Gregorian
calendar (the one used in all western countries today), thereby complying
with all relevant norms and standards: ISO/R 2015-1971, DIN 1355 and, to
some extent, ISO 8601 (where applicable).

%prep
%setup -q -n %{module}-%{version}
chmod -R u+w examples

%build
%{__perl} -pi -e 's,^#!perl,#!/usr/bin/perl,' examples/*.{pl,cgi}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}  CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root,755)
%doc README.txt CHANGES.txt CREDITS.txt EXAMPLES.txt examples
%{_mandir}/man3/*
%{perl_vendorarch}/Date
%{perl_vendorarch}/auto/Date

