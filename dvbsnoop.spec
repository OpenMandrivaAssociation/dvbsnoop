%define mdkversion %(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandriva-release)

%define name	dvbsnoop
%define version 1.4.50
%define mdkrel	%mkrel 2
%define beta	0

%if %beta
%define release 0.%{beta}.%{mdkrel}
%else
%define release %{mdkrel}
%endif

Summary:	A simple dvb/mpeg stream analyzer program
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://osdn.dl.sourceforge.net/dvbsnoop/%{name}-%{version}.tar.gz
URL:		http://dvbsnoop.sf.net
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
Prefix:		%{_prefix}
BuildRequires:	glibc-devel

%description
dvbsnoop is a simple dvb/mpeg stream analyzer program. The program can
be used to sniff, monitor, debug, dump or view dvb/mpeg/dsm-cc/MHP
stream information (digital television) send via satellite, cable or
terrestrial.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING 
%_bindir/*
%_mandir/man1/*

