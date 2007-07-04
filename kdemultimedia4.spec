%define _requires_exceptions devel\(libnoatunarts\)\\|libnoatunarts.so\\|devel\(libnoatunarts\(.*\)\\|libwinskinvis.so\\|libartseffects.so\\|libmpeg-0.3.0.so\\|libyafcore.so\\|libyafxplayer.so\\|devel\(libartsbuilder\)

%define revision 682818

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define compile_smb 1
%{?_no_smb: %{expand: %%global compile_smb 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}

Name:		kdemultimedia4
Summary:	K Desktop Environment - Multimedia
Version: 	3.91
Release: 	%mkrel 0.%revision.2
Epoch: 1
Group:		Graphical desktop/KDE
License:	GPL
URL: 		http://www.kde.org
%if %branch
Source:         ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.%revision.tar.bz2
%else
Source:         ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.bz2
%endif
Source2:	kdemultimedia-3.3.2-add-multimedia-shortcuts-jukrc
BuildRequires:  kdelibs4-devel
BuildRequires:  cdparanoia 
BuildRequires:  musicbrainz-devel
BuildRequires:  mad-devel 
BuildRequires:  oggvorbis-devel
BuildRequires:  libxine-devel 
BuildRequires:  libtunepimp-devel 
BuildRequires:  libtheora-devel
BuildRequires:	libcdda-devel
BuildRequires:  libspeex-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  X11-devel
BuildRequires:	akode-devel
BuildRequires:  kdebase4-devel
BuildRequires:  libfreebob-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libgstreamer-plugins-base-devel

BuildRoot:	%_tmppath/%name-%version-%release-root

Requires: %name-core = %epoch:%version-%release
Requires: kde4-kmix = %epoch:%version-%release
Requires: kde4-kmid = %epoch:%version-%release
Requires: kde4-kaudiocreator = %epoch:%version-%release
Requires: kde4-kscd = %epoch:%version-%release
Requires: kde4-noatun = %epoch:%version-%release

%description
Multimedia tools for the K Desktop Environment.
	- noatun: a multimedia player for sound and movies, very extensible due 
			  to it's plugin interface
	- kaudiocreator: CD ripper and audio encoder frontend.
	- kmid: A standalone and embeddable midi player, includes a karaoke-mode
	- kmix: the audio mixer as a standalone program and Kicker applet
	- kscd: A CD player with an interface to the internet CDDB database
	- krec: A recording frontend using aRts

%files

#-------------------------------------------------------------------------

%package core
Summary:	Common files for kdemultimedia
Group:		Graphical desktop/KDE
Requires:	vorbis-tools
Obsoletes:      %name-common
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: kde-config-file

%description core
Common files for kdemultimedia

%post core
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun core
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files core
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_audiocd.so
%_kde_libdir/kde4/kcm_cddb.so
%_kde_libdir/kde4/kcm_phononxine.so
%_kde_libdir/kde4/kio_audiocd.so
%_kde_libdir/kde4/phonon_xine.so
%_kde_configdir/xdg/menus/applications-merged/kde-multimedia-music.menu
%_kde_datadir/desktop-directories/kde-multimedia-music.directory
%_kde_appsdir/kappfinder/apps/Multimedia/ams.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/amsynth.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/ardour.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/djplay.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/ecamegapedal.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/freebirth.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/freqtweak.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/galan.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/hydrogen.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/jack-rack.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/jamin.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/meterbridge.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/mixxx.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/muse.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/qjackctl.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/qsynth.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/vkeybd.desktop
%_kde_appsdir/kappfinder/apps/Multimedia/zynaddsubfx.desktop
%_kde_appsdir/kconf_update/kcmcddb-emailsettings.upd
%_kde_appsdir/kconf_update/upgrade-metadata.sh
%_kde_appsdir/konqueror/servicemenus/audiocd_play.desktop
%_kde_datadir/config.kcfg/libkcddb.kcfg
%_kde_datadir/kde4/services/audiocd.desktop
%_kde_datadir/kde4/services/audiocd.protocol
%_kde_datadir/kde4/services/kcm_phononxine.desktop
%_kde_datadir/kde4/services/libkcddb.desktop
%_kde_datadir/kde4/services/phononbackends/xine.desktop
%_kde_datadir/kde4/servicetypes/audiomidi.desktop

#-------------------------------------------------------------------------

%package -n %lib_name-devel
Summary:	Header files for kdemultimedia
Group:		Development/KDE and Qt
#Requires:	%lib_name-common = %epoch:%version-%release

Provides:   %name-devel = %epoch:%version-%release

#Provides:       %lib_name-devel = %epoch:%version-%release
Provides:	%lib_name_orig-devel = %epoch:%version-%release

%description -n %lib_name-devel
Header files needed for developing kdemultimedia applications.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%{_kde_libdir}/libaudiocdplugins.so
%{_kde_libdir}/libkcddb.so
%{_kde_libdir}/libkcompactdisc.so
%{_kde_libdir}/libkdeinit4_kmix.so
%{_kde_libdir}/libkdeinit4_kmixctrl.so
%{_kde_libdir}/libkdeinit4_kmixd.so
%{_kde_libdir}/libkdeinit4_noatun.so
%{_kde_libdir}/libkmidlib.so
%{_kde_libdir}/liblibkmid.so
%{_kde_libdir}/libnoatun.so

%_kde_includedir/audiocdencoder.h
%dir %_kde_includedir/libkcompactdisc
%_kde_includedir/libkcompactdisc/*
%dir %_kde_includedir/noatun
%_kde_includedir/noatun/*
%dir %_kde_includedir/libkmid
%_kde_includedir/libkmid/*
%dir %_kde_includedir/libkcddb
%_kde_includedir/libkcddb/*

#--------------------------------------------------------------------
%package -n kde4-juk
Summary:       JuK is a jukebox and music manager for the KDE desktop.
Group:         Graphical desktop/KDE
Requires:      %name-common = %epoch:%version-%release
Provides:	juk4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description  -n kde4-juk
JuK is a jukebox and music manager for the KDE desktop similar to 
jukebox software on other platforms such as iTunes or RealOne. 
Its features include support for Ogg Vorbis and MP3 formats, 
tag editing support for both formats (including ID3v2 for MP3 files), 
output to aRts or GStreamer, multiple playlists, and lots of other 
groovy stuff.

%post  -n kde4-juk 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  -n kde4-juk 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files  -n kde4-juk
%defattr(-,root,root,-)
%_kde_datadir/config/jukrc

#-------------------------------------------------------------------------

%package  -n kde4-kmix
Summary:       kmix, kmixctrl program
Group:         Graphical desktop/KDE
Provides:	kmix4, kmixctrl4
Requires:	 alsa-utils

%description  -n kde4-kmix
The audio mixer as a standalone program and Kicker applet

%post  -n kde4-kmix 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun   -n kde4-kmix 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor


%files  -n kde4-kmix
%defattr(-,root,root,-)
%_kde_bindir/kmix
%_kde_bindir/kmixctrl
%_kde_bindir/kmixd
%_kde_datadir/applications/kde4/kmix.desktop
%_kde_appsdir/kicker/applets/kmixapplet.desktop
%_kde_appsdir/kmix/kmixui.rc
%_kde_appsdir/kmix/pics/*.png
%_kde_appsdir/kmix/profiles/ALSA.default.xml
%_kde_appsdir/kmix/profiles/OSS.default.xml
%_kde_datadir/autostart/restore_kmix_volumes.desktop
%dir %_kde_docdir/HTML/en/kmix
%doc %_kde_docdir/HTML/en/kmix/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmix/index.docbook
%doc %_kde_docdir/HTML/en/kmix/*.png
%_kde_datadir/icons/hicolor/*/apps/kmix.png
%_kde_datadir/kde4/services/kmixctrl_restore.desktop
%_kde_libdir/kde4/kmix_panelapplet.so
%_datadir/dbus-1/interfaces/org.kde.KMix.xml
#-------------------------------------------------------------------------

%package  -n kde4-krec
Summary:       krec program
Group:         Graphical desktop/KDE
Requires:	%lib_name-common = %epoch:%version-%release
Provides:	krec4

%description  -n kde4-krec
A recording frontend using aRts

%post   -n kde4-krec 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun   -n kde4-krec 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-krec
%defattr(-,root,root,-)


#-------------------------------------------------------------------------

%package  -n kde4-kscd
Summary:       kscd program
Group:         Graphical desktop/KDE

Provides:	kscd4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description  -n kde4-kscd
A CD player with an interface to the internet CDDB database

%post   -n kde4-kscd 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun   -n kde4-kscd 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files  -n kde4-kscd
%defattr(-,root,root,-)
%_kde_bindir/kscd
%_kde_datadir/applications/kde4/kscd.desktop
%_kde_appsdir/profiles/kscd.profile.xml
%_kde_datadir/config.kcfg/kscd.kcfg
%_kde_docdir/HTML/en/kscd/index.cache.bz2
%_kde_docdir/HTML/en/kscd/index.docbook
%_kde_docdir/HTML/en/kscd/*.png
%_kde_datadir/icons/hicolor/*/apps/kscd.png

#-------------------------------------------------------------------------

%package  -n kde4-kmid
Summary:       kmid program
Group:         Graphical desktop/KDE
Provides: kmid4
Provides: kmidi4
Provides: %name-kmidi = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description  -n kde4-kmid
Kmid program

%post   -n kde4-kmid 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun   -n kde4-kmid 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files  -n kde4-kmid
%defattr(-,root,root,-)
%_kde_bindir/kmid
%_kde_datadir/applications/kde4/kmid.desktop
%_kde_appsdir/kmid/DiesIrae.kar
%_kde_appsdir/kmid/Guantanamera.kar
%_kde_appsdir/kmid/MariaDeLasMercedes.kar
%_kde_appsdir/kmid/OFortuna.kar
%_kde_appsdir/kmid/fm/drums.o3
%_kde_appsdir/kmid/fm/drums.sb
%_kde_appsdir/kmid/fm/std.o3
%_kde_appsdir/kmid/fm/std.sb
%_kde_appsdir/kmid/icons/button1.xpm
%_kde_appsdir/kmid/icons/button2.xpm
%_kde_appsdir/kmid/icons/keyboard.xpm
%_kde_appsdir/kmid/icons/oxygen/*/*/*
%_kde_appsdir/kmid/kmid_partui.rc
%_kde_appsdir/kmid/kmidui.rc
%_kde_appsdir/kmid/maps/YamahaPSR500.map
%_kde_appsdir/kmid/maps/YamahaPSS790.map
%_kde_appsdir/kmid/maps/YamahaQY10.map
%_kde_appsdir/kmid/maps/gm.map
%doc %_kde_docdir/HTML/en/kmid/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmid/index.docbook
%_kde_datadir/icons/hicolor/*/apps/kmid.png
%_kde_libdir/kde4/libkmidpart.so
%_datadir/dbus-1/interfaces/org.kde.KMid.xml

#-------------------------------------------------------------------------

%package  -n kde4-kaudiocreator
Summary:       kaudiocreator program
Group:         Graphical desktop/KDE
Provides:	kaudiocreator4
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	%name-common = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description  -n kde4-kaudiocreator
CD ripper and audio encoder frontend.

%post   -n kde4-kaudiocreator 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor
%update_icon_cache locolor

%postun   -n kde4-kaudiocreator 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_icon_cache locolor

%files  -n kde4-kaudiocreator
%defattr(-,root,root,-)
%_kde_bindir/kaudiocreator
%_kde_bindir/workman2cddb.pl
%_kde_datadir/applications/kde4/kaudiocreator.desktop
%_kde_appsdir/kaudiocreator/kaudiocreator.notifyrc
%_kde_appsdir/kaudiocreator/kaudiocreatorui.rc
%_kde_appsdir/konqueror/servicemenus/audiocd_extract.desktop
%_kde_appsdir/kconf_update/kaudiocreator-libkcddb.upd
%_kde_appsdir/kconf_update/kaudiocreator-meta.upd
%_kde_appsdir/kconf_update/upgrade-kaudiocreator-metadata.sh
%_kde_datadir/config.kcfg/kaudiocreator.kcfg
%_kde_datadir/config.kcfg/kaudiocreator_encoders.kcfg
%_kde_docdir/HTML/en/kaudiocreator/*.png
%_kde_docdir/HTML/en/kaudiocreator/index.cache.bz2
%_kde_docdir/HTML/en/kaudiocreator/index.docbook
%_kde_datadir/icons/hicolor/*/apps/kaudiocreator.png
%_kde_datadir/icons/locolor/*/apps/kaudiocreator.png
%_kde_datadir/config.kcfg/audiocd_lame_encoder.kcfg
%_kde_datadir/config.kcfg/audiocd_vorbis_encoder.kcfg
%_kde_libdir/kde4/libaudiocd_encoder_lame.so
%_kde_libdir/kde4/libaudiocd_encoder_vorbis.so
%_kde_libdir/kde4/libaudiocd_encoder_wav.so
%_kde_datadir/apps/kconf_update/audiocd.upd

#-------------------------------------------------------------------------


%package  -n kde4-noatun
Summary:       noatun program
Group:         Graphical desktop/KDE
Requires:	%lib_name-noatun = %epoch:%version-%release
Requires:	%lib_name-common = %epoch:%version-%release

Provides:	noatun4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description  -n kde4-noatun
A multimedia player for sound and movies, very extensible due to 
it's plugin interface

%post   -n kde4-noatun 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun   -n kde4-noatun 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files  -n kde4-noatun
%defattr(-,root,root,-)
%_kde_bindir/noatun
%_kde_datadir/applications/kde4/noatun.desktop
%_kde_appsdir/noatun/eq.preset/*
%_kde_appsdir/noatun/icons/oxygen/*/*/*
%_kde_appsdir/noatun/noatun.rc
%_kde_appsdir/noatun/splui.rc
%dir %_kde_docdir/HTML/en/noatun
%doc %_kde_docdir/HTML/en/noatun/index.cache.bz2
%doc %_kde_docdir/HTML/en/noatun/index.docbook
%_kde_datadir/kde4/services/noatun/noatun_milkchocolate.desktop
%_kde_datadir/kde4/services/noatun/noatun_splitplaylist.desktop
%_kde_datadir/kde4/servicetypes/noatunplugin.desktop
%_kde_iconsdir/oxygen/*/*/*
%_kde_libdir/kde4/noatun_*

#-----------------------------------------------------------------------------

%define libaudiocdplugins %mklibname audiocdplugins 1

%package -n %libaudiocdplugins
Summary:    KDE 4 library
Group:      System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %libaudiocdplugins
KDE 4 library.

%post -n %libaudiocdplugins -p /sbin/ldconfig
%postun -n %libaudiocdplugins -p /sbin/ldconfig

%files -n %libaudiocdplugins
%defattr(-,root,root)
%_kde_libdir/libaudiocdplugins.so.*

#-----------------------------------------------------------------------------

%define libkcddb %mklibname kcddb 5

%package -n %libkcddb
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %libkcddb
KDE 4 library.

%post -n %libkcddb -p /sbin/ldconfig
%postun -n %libkcddb -p /sbin/ldconfig

%files -n %libkcddb
%defattr(-,root,root)
%_kde_libdir/libkcddb.so.*

#-----------------------------------------------------------------------------

%define libkcompactdisc %mklibname kcompactdisc 5

%package -n %libkcompactdisc
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %libkcompactdisc
KDE 4 library.

%post -n %libkcompactdisc -p /sbin/ldconfig
%postun -n %libkcompactdisc -p /sbin/ldconfig

%files -n %libkcompactdisc
%defattr(-,root,root)
%_kde_libdir/libkcompactdisc.so.*

#-----------------------------------------------------------------------------

%define libkmidlib %mklibname kmidlib 1

%package -n %libkmidlib
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %libkmidlib
KDE 4 library.

%post -n %libkmidlib -p /sbin/ldconfig
%postun -n %libkmidlib -p /sbin/ldconfig

%files -n %libkmidlib
%defattr(-,root,root)
%_kde_libdir/libkmidlib.so.*

#-----------------------------------------------------------------------------

%define liblibkmid %mklibname libkmid 0.95.0

%package -n %liblibkmid
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %liblibkmid
KDE 4 library.

%post -n %liblibkmid -p /sbin/ldconfig
%postun -n %liblibkmid -p /sbin/ldconfig

%files -n %liblibkmid
%defattr(-,root,root)
%_kde_libdir/liblibkmid.so.*

#-----------------------------------------------------------------------------

%define libnoatun %mklibname noatun 1.2.0

%package -n %libnoatun
Summary: KDE 4 library
Group: System/Libraries
Conflicts:  %lib_name-common < 3.91

%description -n %libnoatun
KDE 4 library.

%post -n %libnoatun -p /sbin/ldconfig
%postun -n %libnoatun -p /sbin/ldconfig

%files -n %libnoatun
%defattr(-,root,root)
%_kde_libdir/libnoatun.so.*

#-----------------------------------------------------------------------------

%prep
%setup -q -nkdemultimedia-%version

%build
cd $RPM_BUILD_DIR/kdemultimedia-%version

%cmake_kde4 \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debug
%endif

%make

%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdemultimedia-%version
cd build

%makeinstall_std

# David - 2.2-0.beta1.1mdk - Remove some non legal songs
for i in %buildroot/%_kde_appsdir/kmidi/*.mid ; do rm -f $i ; done

install -d -m 0775 %buildroot/%_kde_datadir/config/
install -m 0644 %SOURCE2 %buildroot/%_kde_datadir/config/jukrc

%clean
rm -fr %buildroot
