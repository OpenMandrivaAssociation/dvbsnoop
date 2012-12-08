Summary:	A simple dvb/mpeg stream analyzer program
Name:		dvbsnoop
Version:	1.4.50
Release:	6
License:	GPL
Group:		Video
URL:		http://dvbsnoop.sf.net
Source0:	http://osdn.dl.sourceforge.net/dvbsnoop/%{name}-%{version}.tar.gz
BuildRequires:	glibc-devel

%description
dvbsnoop is a simple dvb/mpeg stream analyzer program. The program can
be used to sniff, monitor, debug, dump or view dvb/mpeg/dsm-cc/MHP
stream information (digital television) send via satellite, cable or
terrestrial.

%prep
%setup -q
# Fix permissions
find . -perm 0744 -exec chmod 0644 '{}' \;

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README COPYING 
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.50-2mdv2011.0
+ Revision: 663926
- mass rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.4.50-1mdv2011.0
+ Revision: 360509
- Updated to version 1.4.50
- Drop unused patch: dvbsnoop-1.3.0_drop_FE_CAN_CLEAN_SETUP.patch
- Spec file cleanup.

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.4.00-4mdv2009.0
+ Revision: 220709
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.4.00-3mdv2008.1
+ Revision: 149681
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun May 14 2006 Stefan van der Eijk <stefan@eijk.nu> 1.4.00-2mdk
- rebuild for sparc

* Sun Oct 02 2005 Erwan Velu <erwan@seanodes.com> 1.4.0-1mdk
- 1.4.0

* Mon May 09 2005 Erwan Velu <erwan@seanodes.com> 1.3.77-1mdk
- 1.3.77

* Tue Oct 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3.35-1mdk
- 1.3.35

* Tue Jun 08 2004 Svetoslav Slavtchev <svetljo@gmx.de> 1.3.0-3mdk
- drop club macros
- rebuild

* Sun Apr 04 2004 Svetoslav Slavtchev <svetljo@gmx.de> 1.3.0-2mdk
- fix group

* Sun Apr 04 2004 Svetoslav Slavtchev <svetljo@gmx.de> 1.3.0-1mdk
- initial build for club

