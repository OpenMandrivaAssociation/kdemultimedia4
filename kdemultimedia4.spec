%define revision 752124

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

Name: kdemultimedia4
Summary: K Desktop Environment
Version: 4.0.0
Group: Graphical desktop/KDE
Epoch: 3
License: GPL
URL: http://www.kde.org
%if %branch
Release: %mkrel 0.%revision.1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.%revision.tar.bz2
%else
Release: %mkrel 3
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: kdebase4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: cdparanoia 
BuildRequires: musicbrainz-devel
BuildRequires: mad-devel 
BuildRequires: oggvorbis-devel
BuildRequires: libxine-devel >= 1.1.9 
BuildRequires: libtunepimp-devel 
BuildRequires: libtheora-devel
BuildRequires: libcdda-devel
BuildRequires: libspeex-devel
BuildRequires: libsamplerate-devel
BuildRequires: X11-devel
BuildRequires: akode-devel
BuildRequires: libfreebob-devel
BuildRequires: alsa-lib-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libxcb-devel
BuildRequires: libtaglib-devel
Requires:      kde4-juk
Requires:      kde4-kmix
Requires:      kde4-kscd

Obsoletes:     kde4-noatun <  3:3.94.0-0.726889.1
Obsoletes:     %{_lib}noatun5 < 3:3.94.0-0.726889.1

%description
%{name} metapackage.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package   core
Summary:   %name core files
Group:     Graphical desktop/KDE
Requires:  kdelibs4-core
Conflicts: oxygen-icon-theme <= 1:3.94.0-0.726654.2

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*
%_kde_appsdir/kconf_update/*

#----------------------------------------------------------------------

%package -n kde4-juk
Summary:   %{name} juk
Group:     Graphical desktop/KDE
Requires:  %name-core = %epoch:%version
Obsoletes: %name-juk < 3:3.93.0-0.714637.1

%description -n kde4-juk
%{name} juk.

%files -n kde4-juk
%defattr(-,root,root)
%_kde_appsdir/juk
%_kde_bindir/juk
%_kde_datadir/applications/kde4/juk.desktop
%_kde_datadir/kde4/services/ServiceMenus/jukservicemenu.desktop
%_datadir/dbus-1/interfaces/org.kde.juk.collection.xml
%_datadir/dbus-1/interfaces/org.kde.juk.player.xml
%_datadir/dbus-1/interfaces/org.kde.juk.search.xml
%_kde_docdir/HTML/*/juk

#---------------------------------------------

%package -n kde4-audiocd
Summary: %{name} audiocd
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-audiocd < 3:3.93.0-0.714637.1

%description -n kde4-audiocd
%{name} audiocd.

%files -n kde4-audiocd
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_audiocd.so
%_kde_libdir/kde4/kio_audiocd.so
%_kde_libdir/kde4/libaudiocd_encoder_lame.so
%_kde_libdir/kde4/libaudiocd_encoder_vorbis.so
%_kde_libdir/kde4/libaudiocd_encoder_wav.so
%_kde_datadir/config.kcfg/audiocd_lame_encoder.kcfg
%_kde_datadir/config.kcfg/audiocd_vorbis_encoder.kcfg
%_kde_datadir/kde4/services/audiocd.desktop
%_kde_datadir/kde4/services/audiocd.protocol
%_kde_datadir/kde4/services/ServiceMenus/audiocd_play.desktop

#---------------------------------------------

%define libaudiocdplugins %mklibname %audiocdplugins_major
%define  audiocdplugins_major 4

%package -n %libaudiocdplugins
Summary:    KDE 4 library
Group:      System/Libraries
Obsoletes:  %{_lib}audiocdplugins1 < 3:4.0.0-1

%description -n %libaudiocdplugins
KDE 4 library

%post -n %libaudiocdplugins -p /sbin/ldconfig
%postun -n %libaudiocdplugins -p /sbin/ldconfig

%files -n %libaudiocdplugins
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so.%{audiocdplugins_major}*

#---------------------------------------------

%package -n kde4-kmix
Summary: %{name} kmix
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kmix < 3:3.93.0-0.714637.1

%description -n kde4-kmix
%{name} kmix.

%files -n kde4-kmix
%defattr(-,root,root)
%_kde_appsdir/kmix
%_kde_bindir/kmix
%_kde_bindir/kmixctrl
%_kde_datadir/applications/kde4/kmix.desktop
%_kde_datadir/autostart/restore_kmix_volumes.desktop
%_kde_datadir/kde4/services/kmixctrl_restore.desktop
%_kde_libdir/libkdeinit4_kmix*
%_datadir/dbus-1/interfaces/org.kde.KMix.xml
%_kde_docdir/HTML/*/kmix

#---------------------------------------------

%package -n kde4-kscd
Summary: %{name} kscd
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kscd < 3:3.93.0-0.714637.1

%description -n kde4-kscd
%{name} kscd.

%files -n kde4-kscd
%defattr(-,root,root)
%_kde_appsdir/profiles
%_kde_bindir/kscd
%_kde_bindir/workman2cddb.pl
%_kde_datadir/applications/kde4/kscd.desktop
%_kde_datadir/config.kcfg/kscd.kcfg
%_kde_docdir/HTML/*/kscd

#---------------------------------------------

%define libkcddb %mklibname kcddb %kcddb_major
%define  kcddb_major 4

%package -n %libkcddb
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcddb
KDE 4 library

%post -n %libkcddb -p /sbin/ldconfig
%postun -n %libkcddb -p /sbin/ldconfig

%files -n %libkcddb
%defattr(-,root,root)
%_kde_libdir/libkcddb.so.*
%_kde_libdir/kde4/kcm_cddb.so
%_kde_datadir/config.kcfg/libkcddb.kcfg
%_kde_datadir/kde4/services/libkcddb.desktop

#---------------------------------------------

%define libkcompactdisc %mklibname kcompactdisc %kcompactdisc_major
%define kcompactdisc_major 4

%package -n %libkcompactdisc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcompactdisc
KDE 4 library

%post -n %libkcompactdisc -p /sbin/ldconfig
%postun -n %libkcompactdisc -p /sbin/ldconfig

%files -n %libkcompactdisc
%defattr(-,root,root)
%_kde_libdir/libkcompactdisc.so.%{kcompactdisc_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libaudiocdplugins = %epoch:%version
Requires: %libkcddb = %epoch:%version
Requires: %libkcompactdisc = %epoch:%version
Requires: kdemultimedia4

%description  devel
This package contains header files needed if you wish to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so
%_kde_libdir/libkcddb.so
%_kde_libdir/libkcompactdisc.so
%_kde_includedir/*

#----------------------------------------------------------------------

%prep
%setup -q -n kdemultimedia-%version

%build
export CFLAGS="${CFLAGS} -DOCAMLIB=%_libdir/ocaml"
export CPPFLAGS="${CPPFLAGS} -DOCAMLIB=%_libdir/ocaml"

%cmake_kde4 

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# fwang: it conflicts with oxygen-icon-theme (see kde bug#151419)
rm -f %buildroot/%_kde_iconsdir/oxygen/22x22/actions/kscd-dock.png

%clean
rm -fr %buildroot

