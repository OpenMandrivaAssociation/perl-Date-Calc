%define	upstream_name	 Date-Calc
%define upstream_version 6.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.300.0-5mdv2012.0
+ Revision: 765155
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.300.0-4
+ Revision: 763662
- rebuilt for perl-5.14.x

* Thu May 05 2011 Funda Wang <fwang@mandriva.org> 6.300.0-3
+ Revision: 669284
- clean file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 6.300.0-2mdv2010.1
+ Revision: 519978
- rebuild to use perl.req-from-meta

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 6.300.0-1mdv2010.1
+ Revision: 463020
- update to 6.3

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 5.800.0-1mdv2010.0
+ Revision: 439430
- update to 5.8

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 5.700.0-1mdv2010.0
+ Revision: 420896
- update to 5.7

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 5.600.0-1mdv2010.0
+ Revision: 415284
- update to 5.6

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 5.5.1-10mdv2009.1
+ Revision: 351707
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 5.5.1-9mdv2009.0
+ Revision: 223595
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 5.5.1-8mdv2008.1
+ Revision: 152050
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 5.5.1-7mdv2008.0
+ Revision: 23415
- 5.5.1


* Sat May 06 2006 Scott Karns <scottk@mandriva.org> 5.4-6mdk
- Remove mdkversion conditional surrounding BuildRequires perl-devel.
  (Needed for arch specific perl packages.)

* Thu May 04 2006 Scott Karns <scottk@mandriva.org> 5.4-5mdk
- Update BuildRequires and package file ownership to comply with Mandriva
  perl packaging policies

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.4-4mdk
- Rebuild

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.4-3mdk
- Rebuild, cleanup, %%check

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.4-2mdk
- rebuild for new perl

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.4-1mdk
- 5.4

* Thu Feb 12 2004 Luca Berra <bluca@vodka.it> 5.3-8mdk
- rebuild for perl 5.8.3

* Tue Dec 30 2003 Luca Berra <bluca@vodka.it> 5.3-7mdk
- add parent dirs (distriblint)

* Thu Dec 25 2003 Luca Berra <bluca@vodka.it> 5.3-6mdk
- changed requires syntax for perl-Bit-Vector
- fixed permissions on examples

* Wed Oct 15 2003 Luca Berra <bluca@vodka.it> 5.3-5mdk
- added examples to documentation

* Sun Oct 05 2003 Luca Berra <bluca@vodka.it> 5.3-4mdk
- removed Carp::Clam (provided in own package)

* Wed Aug 13 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 5.3-3mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro
- use %%make macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.3-2mdk
- fix unpackaged files
- rebuild for new auto{prov,req}

