Summary:	A simple dvb/mpeg stream analyzer program
Name:		dvbsnoop
Version:	1.4.50
Release:	10
License:	GPLv2
Group:		Video
Url:		http://dvbsnoop.sf.net
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

