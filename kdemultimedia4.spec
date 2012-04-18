Name: kdemultimedia4
Summary: K Desktop Environment
Version: 4.8.2
Release: 1
Epoch: 3
Group: Graphical desktop/KDE
License: GPL
URL: http://multimedia.kde.org/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.xz
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.4.3-7
BuildRequires: phonon-devel >= 2:4.3.50
BuildRequires: libmusicbrainz3-devel
BuildRequires: oggvorbis-devel
BuildRequires: ffmpeg-devel
BuildRequires: libflac-devel
BuildRequires: taglib-devel
BuildRequires: libtunepimp-devel 
BuildRequires: libtheora-devel
BuildRequires: libcdda-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: ffmpeg-devel 
BuildRequires: pulseaudio-devel
BuildRequires:  automoc4
Requires:      juk = %epoch:%version
Requires:      kmix = %epoch:%version
Requires:      kscd = %epoch:%version
Obsoletes:     kde4-noatun <  3:3.94.0-0.726889.1
Obsoletes:     %{_lib}noatun5 < 3:3.94.0-0.726889.1
Obsoletes: kdemultimedia-common < 1:3.5.10-2
Obsoletes: %{_lib}kdemultimedia1-common < 1:3.5.10-2
Obsoletes: kdemultimedia-krec < 1:3.5.10-2
Obsoletes: kdemultimedia-kmid < 1:3.5.10-2

%description
%{name} metapackage.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package -n juk
Summary:   A music player and manager for KDE
Group:     Graphical desktop/KDE
Conflicts: %name-core < 3:4.5.71
Obsoletes: %name-juk < 3:3.93.0-0.714637.1
Obsoletes: kde4-juk < 3:4.0.68
Provides: kde4-juk = %epoch:%version
Obsoletes: kdemultimedia-juk < 1:3.5.10-2
Obsoletes: kdemultimedia-kaboodle < 1:3.5.10-2
Obsoletes: kdemultimedia-arts < 1:3.5.10-2
Obsoletes: %{_lib}kdemultimedia1-arts < 1:3.5.10-2
Obsoletes: kdemultimedia-noatun < 1:3.5.10-2
Obsoletes: %{_lib}kdemultimedia1-noatun < 1:3.5.10-2

%description -n juk
JuK is a music player and manager for KDE.

%files -n juk
%defattr(-,root,root)
%_kde_appsdir/juk
%_kde_bindir/juk
%_kde_iconsdir/*/*/apps/juk.*
%_kde_datadir/applications/kde4/juk.desktop
%_kde_datadir/kde4/services/ServiceMenus/jukservicemenu.desktop
%_kde_docdir/HTML/*/juk

#----------------------------------------------------------------------

%package -n dragonplayer
Summary:   A simple video player for KDE 4
Group:     Graphical desktop/KDE
URL: http://www.dragonplayer.org/
Conflicts: %name-core < 3:4.5.71
Obsoletes: dragonplayer <= 2.0.1-1
Provides:  dragonplayer = %epoch:%version
Obsoletes: kde4-videoplayer <= 1.0.1-0.745290.4
Provides:  kde4-videoplayer 
Obsoletes: codeine < 1.0.1-3
Provides:  codeine = %epoch:%version-%release

%description -n dragonplayer
Dragon Player is a simple video player for KDE 4.

%files -n dragonplayer
%defattr(-,root,root)
%_kde_bindir/dragon
%dir %_kde_appsdir/dragonplayer
%_kde_appsdir/dragonplayer/*
%_kde_iconsdir/*/*/apps/dragonplayer.*
%_kde_libdir/kde4/dragonpart.so
%_kde_datadir/applications/kde4/dragonplayer.desktop
%_kde_datadir/kde4/services/ServiceMenus/dragonplayer_*
%_kde_datadir/kde4/services/dragonplayer_part.desktop
%_kde_appsdir/solid/actions/dragonplayer-opendvd.desktop
%_kde_configdir/dragonplayerrc
%doc %_kde_docdir/HTML/en/dragonplayer

#---------------------------------------------

%package -n kde4-audiocd
Summary: %{name} audiocd
Group: Graphical desktop/KDE
Obsoletes: %name-audiocd < 3:3.93.0-0.714637.1
Conflicts: %name-core < 3:4.5.71

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
%_kde_appsdir/kconf_update/audiocd.upd
%_kde_appsdir/kconf_update/kcmcddb-emailsettings.upd
%_kde_appsdir/kconf_update/upgrade-metadata.sh
%_kde_appsdir/konqsidebartng/virtual_folders/services/audiocd.desktop
%_kde_appsdir/solid/actions/solid_audiocd.desktop
%_kde_docdir/HTML/en/kioslave/audiocd
%_kde_docdir/HTML/en/kcontrol/cddbretrieval

#---------------------------------------------

%define libaudiocdplugins %mklibname audiocdplugins %audiocdplugins_major
%define  audiocdplugins_major 4

%package -n %libaudiocdplugins
Summary:    KDE 4 library
Group:      System/Libraries
Obsoletes:  %{_lib}audiocdplugins1 < 3:4.0.0-2
Obsoletes:  %{_lib}4 < 3:4.0.73-4

%description -n %libaudiocdplugins
KDE 4 library

%files -n %libaudiocdplugins
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so.*

#---------------------------------------------

%package -n kmix
Summary: %{name} Digital Mixer
Group: Graphical desktop/KDE
Conflicts: %name-core < 3:4.5.71

Obsoletes: %name-kmix < 3:3.93.0-0.714637.1
Obsoletes: kde4-kmix < 3:4.0.68
Obsoletes: kdemultimedia-kmix < 1:3.5.10-2
Obsoletes: %name-core < 3:4.5.71

Provides: kde4-kmix = %epoch:%version

%description -n kmix
%{name} Digital Mixer.

%files -n kmix
%defattr(-,root,root)
%_kde_appsdir/kmix
%_kde_bindir/kmix
%_kde_bindir/kmixctrl
%_kde_iconsdir/*/*/apps/kmix.*
%_kde_iconsdir/*/*/actions/player-volume-muted.*
%_kde_datadir/applications/kde4/kmix.desktop
%_kde_datadir/autostart/restore_kmix_volumes.desktop
%_kde_datadir/kde4/services/kmixctrl_restore.desktop
%_kde_libdir/libkdeinit4_kmix*
%_kde_libdir/kde4/kded_kmixd.so
%_kde_services/kded/kmixd.desktop
%_kde_autostart/kmix_autostart.desktop
%_kde_docdir/HTML/*/kmix
%_kde_libdir/kde4/plasma_engine_mixer.so
%_kde_appsdir/plasma/services/mixer.operations
%_kde_datadir/kde4/services/plasma-engine-mixer.desktop

#---------------------------------------------

%package -n kscd
Summary: %{name} Audio CD Player
Group: Graphical desktop/KDE
Conflicts: %name-core < 3:4.5.71

Obsoletes: %name-kscd < 3:3.93.0-0.714637.1
Obsoletes: kde4-kscd < 3:4.0.68
Obsoletes: kdemultimedia-kscd < 1:3.5.10-2

Provides: kde4-kscd = %epoch:%version
Suggests: gstreamer0.10-cdparanoia 

%description -n kscd
%{name} audio CD Player.

%files -n kscd
%defattr(-,root,root)
%_kde_bindir/kscd
%_kde_datadir/applications/kde4/kscd.desktop
%_kde_datadir/config.kcfg/kscd.kcfg
%_kde_appsdir/kscd
%_kde_iconsdir/*/*/apps/kscd.*
%_kde_iconsdir/*/*/*/kscd-dock.*
%_kde_appsdir/solid/actions/kscd-play-audiocd.desktop

#---------------------------------------------

%package -n mplayerthumbs
Summary: %{name} Video thumbnail generator for KDE4 file managers
Group: Graphical desktop/KDE

# We do not requires mplayer as by default we now use the phonon engine
# Requires:      mplayer

%description -n mplayerthumbs
MPlayerThumbs is a video thumbnail generator for KDE file managers
(Konqueror, Dolphin, ...) , now available also for KDE 4.
It needs mplayer (of course) to generate thumbnails, and it contains
no linking to any library, so in a x86_64 system you can freely use the
32bit mplayer binary with win32codecs by configuring the application launching
the mplayerthumbsconfig helper application.
It catches a random frame from 15% to 70%, checking also how contrasted is the
image, and dropping bad frames.

%files -n mplayerthumbs
%defattr(-,root,root)
%{_kde_bindir}/mplayerthumbsconfig
%{_kde_libdir}/kde4/videopreview.so
%{_kde_appsdir}/videothumbnail
%{_kde_datadir}/config.kcfg/mplayerthumbs.kcfg
%{_kde_datadir}/kde4/services/videopreview.desktop

#---------------------------------------------

%package -n ffmpegthumbs
Summary: %{name} Video thumbnail generator for KDE4 file managers
Group: Graphical desktop/KDE

Requires:      ffmpeg

%description -n ffmpegthumbs
FFmpegThumbs is a video thumbnails implementation for KDE4 based on
FFmpegThumbnailer. 
This thumbnailer uses FFmpeg to decode frames from the video files, 
so supported video formats depend on the configuration flags of ffmpeg.

This thumbnailer was designed to be as fast and lightweight as possible.

%files -n ffmpegthumbs
%defattr(-,root,root)
%{_kde_libdir}/kde4/ffmpegthumbs.so
%{_kde_datadir}/kde4/services/ffmpegthumbs.desktop

#---------------------------------------------

%define libkcddb %mklibname kcddb %kcddb_major
%define  kcddb_major 4

%package -n %libkcddb
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: kdemultimedia-kscd < 1:3.5.10-4

%description -n %libkcddb
KDE 4 library

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

%files -n %libkcompactdisc
%defattr(-,root,root)
%_kde_libdir/libkcompactdisc.so.%{kcompactdisc_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Obsoletes: %{_lib}kdemultimedia1-common-devel < 1:3.5.10-2
Obsoletes: %{_lib}kdemultimedia1-arts-devel < 1:3.5.10-2
Obsoletes: %{_lib}kdemultimedia1-noatun-devel < 1:3.5.10-2
Requires: kdelibs4-devel >= 2:4.2.98
Requires: %libaudiocdplugins = %epoch:%version
Requires: %libkcddb = %epoch:%version
Requires: %libkcompactdisc = %epoch:%version

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
%cmake_kde4 -DENABLE_PHONON_SUPPORT=ON

%make

%install
%makeinstall_std -C build

