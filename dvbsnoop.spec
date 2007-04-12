%define mdkversion %(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandrake-release)

%define name	dvbsnoop
%define version 1.4.00
%define mdkrel	%mkrel 2
%define beta	0



%if %mdkversion < 1000
%define kernel_rel 2.4.22-28.tmb.1mdk
%define kernel_dir /usr/src/linux-%{kernel_rel}
%define kernel_inc %kernel_dir/3rdparty/mod_dvb/include
%else
#define kernel_rel 2.6.3-7mdk
%define kernel_dir /usr/src/linux
#-#{kernel_rel}
%define kernel_inc %kernel_dir/include
%endif

%if %beta
%define release 0.%{beta}.%{mdkrel}
%else
%define release %{mdkrel}
%endif

Summary:	A simple dvb/mpeg stream analyzer program
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://osdn.dl.sourceforge.net/dvbsnoop/%{name}-%{version}.tar.bz2
Patch:		dvbsnoop-1.3.0_drop_FE_CAN_CLEAN_SETUP.patch
URL:		http://dvbsnoop.sf.net
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
Prefix:		%{_prefix}
BuildRequires:	glibc-devel

%description
 dvbsnoop is a simple dvb/mpeg stream analyzer program.
 The program can be used to sniff, monitor, debug, dump
 or view dvb/mpeg/dsm-cc/MHP stream information (digital television)
 send via satellite, cable or terrestrial.

%prep
%setup -q
#%if %mdkversion > 1000
#%patch -p1
#%endif

%build
%configure CPPFLAGS=-I%kernel_inc
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
#make install DESTDIR=%buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING 
%_bindir/*
%_mandir/man1/*

