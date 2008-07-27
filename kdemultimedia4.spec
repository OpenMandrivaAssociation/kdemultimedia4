Name: kdemultimedia4
Summary: K Desktop Environment
Version: 4.1.0
Group: Graphical desktop/KDE
Epoch: 3
License: GPL
URL: http://multimedia.kde.org/
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.bz2
Buildroot: %_tmppath/%name-%version-%release-root
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
BuildRequires: libfreebob-devel
BuildRequires: alsa-lib-devel
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libxcb-devel
BuildRequires: libtaglib-devel
BuildRequires: libflac-devel
Requires:      juk = %epoch:%version
Requires:      kmix = %epoch:%version
Requires:      kscd = %epoch:%version
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
%if %mdkversion > 200810
Conflicts: kdemultimedia-kmix < 1:3.5.9-4
Conflicts: kdemultimedia-kscd < 1:3.5.9-4
%endif

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*
%_kde_appsdir/kconf_update/*

#----------------------------------------------------------------------

%package -n juk
Summary:   A music player and manager for KDE
Group:     Graphical desktop/KDE
Requires:  %name-core = %epoch:%version
Obsoletes: %name-juk < 3:3.93.0-0.714637.1
Obsoletes: kde4-juk < 3:4.0.68
Provides: kde4-juk = %epoch:%version

%description -n juk
JuK is a music player and manager for KDE.

%files -n juk
%defattr(-,root,root)
%_kde_appsdir/juk
%_kde_bindir/juk
%_kde_datadir/applications/kde4/juk.desktop
%_kde_datadir/kde4/services/ServiceMenus/jukservicemenu.desktop
%_kde_docdir/HTML/*/juk

#----------------------------------------------------------------------

%package -n dragonplayer
Summary:   A simple video player for KDE 4
Group:     Graphical desktop/KDE
URL: http://www.dragonplayer.org/
Requires:  %name-core = %epoch:%version
Obsoletes: dragonplayer <= 2.0.1-1
Provides:  dragonplayer = %epoch:%version
Obsoletes: kde4-videoplayer <= 1.0.1-0.745290.4
Provides:  kde4-videoplayer 


%description -n dragonplayer
Dragon Player is a simple video player for KDE 4.

%files -n dragonplayer
%defattr(-,root,root)
%_kde_bindir/dragon
%dir %_kde_appsdir/dragonplayer
%_kde_appsdir/dragonplayer/*
%_kde_libdir/kde4/dragonpart.so
%_kde_datadir/applications/kde4/dragonplayer.desktop
%_kde_datadir/kde4/services/ServiceMenus/dragonplayer_*
%_kde_datadir/kde4/services/dragonplayer_part.desktop
%_kde_configdir/dragonplayerrc
%doc %_kde_docdir/*/*/dragonplayer

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
%_kde_libdir/kde4/libaudiocd_*
%_kde_datadir/config.kcfg/audiocd_*
%_kde_datadir/kde4/services/audiocd.desktop
%_kde_datadir/kde4/services/audiocd.protocol
%_kde_datadir/kde4/services/ServiceMenus/audiocd_play.desktop
%_kde_appsdir/konqsidebartng/virtual_folders/services/audiocd.desktop

#---------------------------------------------

%define libaudiocdplugins %mklibname audiocdplugins %audiocdplugins_major
%define  audiocdplugins_major 4

%package -n %libaudiocdplugins
Summary:    KDE 4 library
Group:      System/Libraries
Obsoletes:  %{_lib}audiocdplugins1 < 3:4.0.0-2
%if %mdkversion > 200810
Obsoletes:  %{_lib}4 < 3:4.0.73-4
%endif

%description -n %libaudiocdplugins
KDE 4 library

%if %mdkversion < 200900
%post -n %libaudiocdplugins -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libaudiocdplugins -p /sbin/ldconfig
%endif

%files -n %libaudiocdplugins
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so.*

#---------------------------------------------

%package -n kmix
Summary: %{name} Digital Mixer
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kmix < 3:3.93.0-0.714637.1
Obsoletes: kde4-kmix < 3:4.0.68
Provides: kde4-kmix = %epoch:%version

%description -n kmix
%{name} Digital Mixer.

%files -n kmix
%defattr(-,root,root)
%_kde_appsdir/kmix
%_kde_bindir/kmix
%_kde_bindir/kmixctrl
%_kde_datadir/applications/kde4/kmix.desktop
%_kde_datadir/autostart/restore_kmix_volumes.desktop
%_kde_datadir/kde4/services/kmixctrl_restore.desktop
%_kde_libdir/libkdeinit4_kmix*
%_kde_autostart/kmix_autostart.desktop
%_kde_docdir/HTML/*/kmix

#---------------------------------------------

%package -n kscd
Summary: %{name} Audio CD Player
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version
Obsoletes: %name-kscd < 3:3.93.0-0.714637.1
Obsoletes: kde4-kscd < 3:4.0.68
Provides: kde4-kscd = %epoch:%version

%description -n kscd
%{name} audio CD Player.

%files -n kscd
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
%if %mdkversion > 200810
Conflicts: kdemultimedia-kscd < 1:3.5.9-4
%endif 

%description -n %libkcddb
KDE 4 library

%if %mdkversion < 200900
%post -n %libkcddb -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkcddb -p /sbin/ldconfig
%endif

%files -n %libkcddb
%defattr(-,root,root)
%_kde_libdir/libkcddb.so.%{kcddb_major}*
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

%if %mdkversion < 200900
%post -n %libkcompactdisc -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkcompactdisc -p /sbin/ldconfig
%endif

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
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so
%_kde_libdir/libkcddb.so
%_kde_libdir/libkcompactdisc.so
%_kde_includedir/*
%_kde_datadir/dbus-1/interfaces/*

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

