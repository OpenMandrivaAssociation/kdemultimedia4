%define revision 693475

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

Name: kdemultimedia4
Summary: K Desktop Environment
Version: 3.92.0
Release: %mkrel 0.%revision.1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.%revision.tar.bz2
%else
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel
BuildRequires: cdparanoia 
BuildRequires: musicbrainz-devel
BuildRequires: mad-devel 
BuildRequires: oggvorbis-devel
BuildRequires: libxine-devel 
BuildRequires: libtunepimp-devel 
BuildRequires: libtheora-devel
BuildRequires: libcdda-devel
BuildRequires: libspeex-devel
BuildRequires: libsamplerate-devel
BuildRequires: X11-devel
BuildRequires: akode-devel
BuildRequires: kdebase4-devel
BuildRequires: libfreebob-devel
BuildRequires: alsa-lib-devel
BuildRequires: libgstreamer-plugins-base-devel
Requires: kde4-juk
Requires: kde4-kaudiocreator
Requires: kde4-audiocd
Requires: kde4-kmid
Requires: kde4-kmix
Requires: kde4-kscd
Requires: kde4-phonon-xine
Requires: kde4-noatun

%description
%{name} metapackage.

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package core
Summary: %name core files
Group: Graphical desktop/KDE
Requires: kdelibs4-core

%description core
Core files for %{name}.

%files core
%defattr(-,root,root)
%_kde_iconsdir/*/*/*/*
%_kde_appsdir/kconf_update/*
%_kde_appsdir/kappfinder/apps/*
%_kde_prefix/etc/xdg/menus/applications-merged/*
%_kde_datadir/desktop-directories/*

#----------------------------------------------------------------------

%package -n kde4-juk
Summary: %{name} juk
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-juk

%description -n kde4-juk
%{name} juk.

%files -n kde4-juk
%defattr(-,root,root)
%_kde_appsdir/juk
%_kde_appsdir/konqueror
%_kde_bindir/juk
%_kde_datadir/applications/kde4/juk.desktop
%_datadir/dbus-1/interfaces/org.kde.juk.collection.xml
%_datadir/dbus-1/interfaces/org.kde.juk.player.xml
%_datadir/dbus-1/interfaces/org.kde.juk.search.xml
%_kde_docdir/HTML/*/juk

#---------------------------------------------

%package -n kde4-kaudiocreator
Summary: %{name} kaudiocreator
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kaudiocreator

%description -n kde4-kaudiocreator
%{name} kaudiocreator.

%files -n kde4-kaudiocreator
%defattr(-,root,root)
#%_kde_appsdir/kconf_update
%_kde_appsdir/kaudiocreator
%_kde_appsdir/konqueror
%_kde_bindir/kaudiocreator
%_kde_datadir/applications/kde4/kaudiocreator.desktop
%_kde_datadir/config.kcfg/kaudiocreator.kcfg
%_kde_datadir/config.kcfg/kaudiocreator_encoders.kcfg
%_kde_docdir/HTML/*/kaudiocreator

#---------------------------------------------

%package -n kde4-audiocd
Summary: %{name} audiocd
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-audiocd

%description -n kde4-audiocd
%{name} audiocd.

%files -n kde4-audiocd
%defattr(-,root,root)
#%_kde_appsdir/kconf_update
%_kde_libdir/kde4/kcm_audiocd.so
%_kde_libdir/kde4/kio_audiocd.so
%_kde_libdir/kde4/libaudiocd_encoder_flac.so
%_kde_libdir/kde4/libaudiocd_encoder_lame.so
%_kde_libdir/kde4/libaudiocd_encoder_vorbis.so
%_kde_libdir/kde4/libaudiocd_encoder_wav.so
%_kde_datadir/config.kcfg/audiocd_lame_encoder.kcfg
%_kde_datadir/config.kcfg/audiocd_vorbis_encoder.kcfg
%_kde_datadir/kde4/services/audiocd.desktop
%_kde_datadir/kde4/services/audiocd.protocol

#---------------------------------------------

%define libaudiocdplugins %mklibname audiocdplugins 1

%package -n %libaudiocdplugins
Summary: KDE 4 library
Group: System/Libraries

%description -n %libaudiocdplugins
KDE 4 library

%post -n %libaudiocdplugins -p /sbin/ldconfig
%postun -n %libaudiocdplugins -p /sbin/ldconfig

%files -n %libaudiocdplugins
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so.*

#---------------------------------------------

%package -n kde4-kmid
Summary: %{name} kmid
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmid

%description -n kde4-kmid
%{name} kmid.

%files -n kde4-kmid
%defattr(-,root,root)
%_kde_appsdir/kmid
%_kde_bindir/kmid
%_kde_libdir/kde4/libkmidpart.so
%_kde_datadir/applications/kde4/kmid.desktop
%_kde_datadir/kde4/servicetypes/audiomidi.desktop
%_datadir/dbus-1/interfaces/org.kde.KMid.xml
%_kde_docdir/HTML/*/kmid

#---------------------------------------------

%define liblibkmid %mklibname libkmid 0

%package -n %liblibkmid
Summary: KDE 4 library
Group: System/Libraries

%description -n %liblibkmid
KDE 4 library

%post -n %liblibkmid -p /sbin/ldconfig
%postun -n %liblibkmid -p /sbin/ldconfig

%files -n %liblibkmid
%defattr(-,root,root)
%_kde_libdir/liblibkmid.so.*

#---------------------------------------------

%define libkmidlib %mklibname kmidlib 1

%package -n %libkmidlib
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmidlib
KDE 4 library

%post -n %libkmidlib -p /sbin/ldconfig
%postun -n %libkmidlib -p /sbin/ldconfig

%files -n %libkmidlib
%defattr(-,root,root)
%_kde_libdir/libkmidlib.so.*

#---------------------------------------------

%package -n kde4-kmix
Summary: %{name} kmix
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-kmix

%description -n kde4-kmix
%{name} kmix.

%files -n kde4-kmix
%defattr(-,root,root)
%_kde_appsdir/kmix
%_kde_appsdir/kicker
%_kde_bindir/kmix
%_kde_bindir/kmixctrl
%_kde_bindir/kmixd
%_kde_libdir/kde4/kmix_panelapplet.so
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
Requires: %name-core = %version
Obsoletes: %name-kscd

%description -n kde4-kscd
%{name} kscd.

%files -n kde4-kscd
%defattr(-,root,root)
%_kde_appsdir/profiles
%_kde_appsdir/konqueror
%_kde_bindir/kscd
%_kde_bindir/workman2cddb.pl
%_kde_datadir/applications/kde4/kscd.desktop
%_kde_datadir/config.kcfg/kscd.kcfg
%_kde_docdir/HTML/*/kscd

#---------------------------------------------

%define libkcddb %mklibname kcddb 4

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

%define libkcompactdisc %mklibname kcompactdisc 4

%package -n %libkcompactdisc
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkcompactdisc
KDE 4 library

%post -n %libkcompactdisc -p /sbin/ldconfig
%postun -n %libkcompactdisc -p /sbin/ldconfig

%files -n %libkcompactdisc
%defattr(-,root,root)
%_kde_libdir/libkcompactdisc.so.*

#---------------------------------------------

%package -n kde4-phonon-xine
Summary: %{name} phonon-xine
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-phonon-xine

%description -n kde4-phonon-xine
%{name} phonon-xine.

%files -n kde4-phonon-xine
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_libdir/kde4/phonon_xine.so
%_kde_datadir/kde4/services/kcm_phononxine.desktop
%_kde_datadir/kde4/services/phononbackends/xine.desktop

#---------------------------------------------

%package -n kde4-noatun
Summary: %{name} noatun
Group: Graphical desktop/KDE
Requires: %name-core = %version
Obsoletes: %name-noatun

%description -n kde4-noatun
%{name} noatun.

%files -n kde4-noatun
%defattr(-,root,root)
%_kde_appsdir/noatun
%_kde_bindir/noatun
%_kde_libdir/kde4/noatun_milkchocolate.so
%_kde_libdir/kde4/noatun_splitplaylist.so
%_kde_datadir/applications/kde4/noatun.desktop
%_kde_datadir/kde4/services/noatun/noatun_milkchocolate.desktop
%_kde_datadir/kde4/services/noatun/noatun_splitplaylist.desktop
%_kde_datadir/kde4/servicetypes/noatunplugin.desktop
%_kde_libdir/libkdeinit4_noatun*
%_kde_docdir/HTML/*/noatun

#---------------------------------------------

%define libnoatun %mklibname noatun 1

%package -n %libnoatun
Summary: KDE 4 library
Group: System/Libraries

%description -n %libnoatun
KDE 4 library

%post -n %libnoatun -p /sbin/ldconfig
%postun -n %libnoatun -p /sbin/ldconfig

%files -n %libnoatun
%defattr(-,root,root)
%_kde_libdir/libnoatun.so.*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %libaudiocdplugins = %version
Requires: %libkmidlib = %version
Requires: %libkcddb = %version
Requires: %libkcompactdisc = %version
Requires: %libnoatun = %version
Requires: kdemultimedia4

%description  devel
This package contains header files needed if you wish to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_libdir/*.so
%_kde_prefix/include/*

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

%clean
rm -fr %buildroot

