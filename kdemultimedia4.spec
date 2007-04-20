%define _requires_exceptions devel\(libnoatunarts\)\\|libnoatunarts.so\\|devel\(libnoatunarts\(.*\)\\|libwinskinvis.so\\|libartseffects.so\\|libmpeg-0.3.0.so\\|libyafcore.so\\|libyafxplayer.so\\|devel\(libartsbuilder\)

# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418


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
Version: 	3.80.3
Release: 	%mkrel 0.%branch_date.1
Epoch: 1
Group:		Graphical desktop/KDE
License:	GPL
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
URL: 		http://www.kde.org
%if %branch
Source:         ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version-%branch_date.tar.bz2
%else
Source:         ftp://ftp.kde.org/pub/kde/stable/%version/src/kdemultimedia-%version.tar.bz2
%endif
Source2:	kdemultimedia-3.3.2-add-multimedia-shortcuts-jukrc

%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release

BuildRequires: cdparanoia 
BuildRequires: musicbrainz-devel
BuildRequires: mad-devel 
BuildRequires: oggvorbis-devel
BuildRequires: libxine-devel 
#BuildRequires: libtaglib-devel >= 0.96 
#BuildRequires: libflac++-devel
BuildRequires: libtunepimp-devel 
BuildRequires: libtheora-devel
BuildRequires:	libcdda-devel
#BuildRequires: libflac++-devel
#BuildRequires: liboggflac++-devel
BuildRequires: libspeex-devel
BuildRequires: libsamplerate-devel
BuildRequires: X11-devel
BuildRequires:	akode-devel
BuildRequires: kdebase4-devel
BuildRequires:  libfreebob-devel
BuildRequires: alsa-lib-devel

BuildRoot:	%_tmppath/%name-%version-%release-root
# Don't add kdemultimedia-arts package on meta provides
# This package have offensive mcop files and is usefull just
# if you want develop new synthesizer objects with artsbuilder 
Requires: %name-common = %epoch:%version-%release
Requires: %name-kmix = %epoch:%version-%release
Requires: %name-kmid = %epoch:%version-%release
Requires: %name-kaudiocreator = %epoch:%version-%release
Requires: %name-kscd = %epoch:%version-%release
Requires: %name-noatun = %epoch:%version-%release

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

%package common
Summary:	Common files for kdemultimedia
Group:		Graphical desktop/KDE
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	vorbis-tools
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: kde-config-file

%description common
Common files for kdemultimedia

%post common 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun common 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files common
%defattr(-,root,root)
%_sysconfdir/xdg/menus/applications-merged/kde-multimedia-music.menu
%_libdir/kde4/kfile_*.so
%_libdir/kde4/kcm_audiocd.*
%_libdir/kde4/kio_audiocd.*
%_datadir/apps/konqueror/servicemenus/audiocd_play.desktop
%_datadir/apps/konqueror/servicemenus/audiocd_extract.desktop
%_datadir/desktop-directories/kde-multimedia-music.directory
%_datadir/apps/kconf_update/audiocd.upd
%_datadir/apps/kconf_update/upgrade-metadata.sh
%_datadir/services/audiocd.desktop
%_datadir/services/audiocd.protocol
%_datadir/services/kfile_*
%_libdir/kde4/libaudiocd_*
%_datadir/apps/kappfinder/apps/Multimedia/*.desktop
%_datadir/config.kcfg/audiocd_lame_encoder.kcfg
%_datadir/config.kcfg/audiocd_vorbis_encoder.kcfg
%_libdir/kde4/phonon_xine.so
%_datadir/icons/crystalsvg/22x22/actions/cdsmall.png
%_datadir/services/phononbackends/xine.desktop
%_datadir/services/kcm_phononxine.desktop
%_iconsdir/crystalsvg/128x128/apps/xinelogo.png

#-------------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Header files for kdemultimedia
Group:		Development/KDE and Qt
Requires:		%lib_name-common = %epoch:%version-%release

Provides:   %name-devel = %epoch:%version-%release

Provides:   %lib_name-devel = %epoch:%version-%release
Provides:	%lib_name_orig-common-devel = %epoch:%version-%release

%description -n %lib_name-common-devel
Header files needed for developing kdemultimedia applications.

%files -n %lib_name-common-devel
%defattr(-,root,root,-)
%_includedir/*
%_libdir/libaudiocdplugins.so
%_libdir/libkcddb.so
%_libdir/libkmidlib.so
%_libdir/liblibkmid.so
%_libdir/libphononxineengine.so
%_libdir/libkcompactdisc.so
%exclude %_includedir/noatun
%_datadir/dbus-1/interfaces/org.kde.KMid.xml
%_datadir/dbus-1/interfaces/org.kde.KMix.xml

#-------------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Libraries files for kdemultimedia
Group:         Graphical desktop/KDE
Provides: %lib_name = %epoch:%version-%release
Provides: %lib_name_orig-common = %epoch:%version-%release

%description -n %lib_name-common
Libraries files needed for developing kdemultimedia applications.

%post -n %lib_name-common -p /sbin/ldconfig
%postun -n %lib_name-common -p  /sbin/ldconfig

%files -n %lib_name-common
%defattr(-,root,root,-)
%_libdir/libkmidlib.so.*
%_libdir/libkcddb.so.*
%_libdir/libaudiocdplugins.so.*
%_libdir/libkcompactdisc.so.*
%_libdir/liblibkmid.so.*
%_libdir/libphononxineengine.so.*
%_libdir/kde4/kcm_phononxine.so
#-------------------------------------------------------------------------

%package juk
Summary:       JuK is a jukebox and music manager for the KDE desktop.
Group:         Graphical desktop/KDE
Requires:      %name-common = %epoch:%version-%release
Provides:	juk4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description juk
JuK is a jukebox and music manager for the KDE desktop similar to 
jukebox software on other platforms such as iTunes or RealOne. 
Its features include support for Ogg Vorbis and MP3 formats, 
tag editing support for both formats (including ID3v2 for MP3 files), 
output to aRts or GStreamer, multiple playlists, and lots of other 
groovy stuff.

%post  juk 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  juk 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files juk
%defattr(-,root,root,-)
#%_bindir/juk
#%_datadir/applications/kde4/juk.desktop
#%_iconsdir/*/*/*/juk*
%config(noreplace) %_datadir/config/jukrc
#%dir %_datadir/apps/juk
#%_datadir/apps/juk/*
#%_datadir/apps/konqueror/servicemenus/jukservicemenu.desktop
#%doc %_docdir/HTML/en/juk/*.png
#%doc %_docdir/HTML/en/juk/*.bz2
#%doc %_docdir/HTML/en/juk/*.docbook

#-------------------------------------------------------------------------

%package kmix
Summary:       kmix, kmixctrl program
Group:         Graphical desktop/KDE
Provides:	kmix4, kmixctrl4
Requires:	 alsa-utils

%description kmix
The audio mixer as a standalone program and Kicker applet

%post kmix 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  kmix 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor


%files kmix
%defattr(-,root,root,-)
%_bindir/kmix
%_bindir/kmixd
%_bindir/kmixctrl
%_libdir/kde4/kmix*.so
%_datadir/autostart/restore_kmix_volumes.desktop
%_iconsdir/*/*/*/kmix*
%_datadir/services/kmixctrl_restore.desktop
%_datadir/applications/kde4/kmix.desktop
%dir %_datadir/apps/kmix/
%_datadir/apps/kmix/*
%_datadir/apps/kicker/applets/kmixapplet.desktop
%_libdir/libkdeinit_kmix.*
%_libdir/libkdeinit_kmixctrl.*
%_libdir/libkdeinit_kmixd.so

%doc %_docdir/HTML/en/kmix/*.bz2
%doc %_docdir/HTML/en/kmix/*.docbook
%doc %_docdir/HTML/en/kmix/*.png

#-------------------------------------------------------------------------

%package krec
Summary:       krec program
Group:         Graphical desktop/KDE
Requires:	%lib_name-common = %epoch:%version-%release
Provides:	krec4

%description krec
A recording frontend using aRts

%post  krec 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  krec 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files krec
%defattr(-,root,root,-)

#-------------------------------------------------------------------------

%package kscd
Summary:       kscd program
Group:         Graphical desktop/KDE

Provides:	kscd4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kscd
A CD player with an interface to the internet CDDB database

%post  kscd 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  kscd 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kscd
%defattr(-,root,root,-)
%_bindir/kscd
%_bindir/workman2cddb.pl
%_iconsdir/*/*/*/kscd*
%_datadir/config.kcfg/kscd.kcfg
%_datadir/config.kcfg/libkcddb.kcfg
%_datadir/services/libkcddb.desktop
%_datadir/applications/kde4/kscd.desktop
#%dir %_datadir/apps/kscd/
#%_datadir/apps/kscd/*
%_datadir/apps/profiles/kscd.profile.xml
%_datadir/apps/kconf_update/kcmcddb-emailsettings.upd
%_libdir/kde4/kcm_cddb.*
%_datadir/mimelnk/text/xmcd.desktop
%doc %_docdir/HTML/en/kscd/*.bz2
%doc %_docdir/HTML/en/kscd/*.docbook
%doc %_docdir/HTML/en/kscd/*.png

#-------------------------------------------------------------------------

%package kmid
Summary:       kmid program
Group:         Graphical desktop/KDE
Provides: kmid4
Provides: kmidi4
Provides: %name-kmidi = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kmid
Kmid program

%post  kmid 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  kmid 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kmid
%defattr(-,root,root,-)
%_bindir/kmid
%_iconsdir/*/*/*/kmid.*
%_libdir/kde4/libkmidpart.*
%dir %_datadir/apps/kmid/
%_datadir/apps/kmid/*
%_datadir/mimelnk/audio/x-karaoke.desktop
%_datadir/servicetypes/audiomidi.desktop
%_datadir/applications/kde4/kmid.desktop
%doc %_docdir/HTML/en/kmid/*.bz2
%doc %_docdir/HTML/en/kmid/*.docbook

#-------------------------------------------------------------------------

%package kaudiocreator
Summary:       kaudiocreator program
Group:         Graphical desktop/KDE
Provides:	kaudiocreator4
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	%name-common = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kaudiocreator
CD ripper and audio encoder frontend.

%post  kaudiocreator 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  kaudiocreator 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files kaudiocreator
%defattr(-,root,root,-)
%_bindir/kaudiocreator
%_datadir/applications/kde4/kaudiocreator.desktop
%dir %_datadir/apps/kaudiocreator/
%_datadir/apps/kaudiocreator/*
%_iconsdir/*/*/*/kaudiocreator*
%_datadir/apps/kconf_update/kaudiocreator-libkcddb.upd
%_datadir/config.kcfg/kaudiocreator.kcfg
%_datadir/config.kcfg/kaudiocreator_encoders.kcfg
%_datadir/apps/kconf_update/kaudiocreator-meta.upd
%_datadir/apps/kconf_update/upgrade-kaudiocreator-metadata.sh
%doc %_docdir/HTML/en/kaudiocreator/*.png
%doc %_docdir/HTML/en/kaudiocreator/*.bz2
%doc %_docdir/HTML/en/kaudiocreator/*.docbook

#-------------------------------------------------------------------------


%package noatun
Summary:       noatun program
Group:         Graphical desktop/KDE
Requires:	%lib_name-noatun = %epoch:%version-%release
Requires:	%lib_name-common = %epoch:%version-%release

Provides:	noatun4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description noatun
A multimedia player for sound and movies, very extensible due to 
it's plugin interface

%post  noatun 
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun  noatun 
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files noatun
%defattr(-,root,root,-)
%_bindir/noatun
%dir %_datadir/apps/noatun
%_datadir/apps/noatun/*
%_iconsdir/*/*/*/noatun*
%_datadir/applications/kde4/noatun.desktop
#%_datadir/mimelnk/interface/x-winamp-skin.desktop
%doc %_docdir/HTML/en/noatun/*.bz2
%doc %_docdir/HTML/en/noatun/*.docbook
%_datadir/services/noatun/noatun_milkchocolate.desktop
%_datadir/services/noatun/noatun_splitplaylist.desktop
%_datadir/servicetypes/noatunplugin.desktop

#-------------------------------------------------------------------------

%package -n %lib_name-noatun
Summary:       Librarie for Noatun  program
Group:         Development/KDE and Qt
Provides:	%lib_name_orig-noatun = %epoch:%version-%release

%description -n %lib_name-noatun
Library for noatun program

%post -n %lib_name-noatun -p /sbin/ldconfig
%postun -n %lib_name-noatun -p  /sbin/ldconfig

%files -n %lib_name-noatun
%defattr(-,root,root,-)
%_libdir/libnoatun.so.*
%_libdir/libkdeinit_noatun.so
%_libdir/kde4/noatun_milkchocolate.so
%_libdir/kde4/noatun_splitplaylist.so
#-------------------------------------------------------------------------

%package -n %lib_name-noatun-devel
Summary:       Devel files for Noatun  program
Group:         Development/KDE and Qt
Requires:	%lib_name-noatun = %epoch:%version-%release
Provides:	%lib_name_orig-noatun-devel
Provides:	noatun4-devel

%description -n %lib_name-noatun-devel
Devel files for noatun program

%files -n %lib_name-noatun-devel
%defattr(-,root,root,-)
%dir %_includedir/noatun/
%_includedir/noatun/*.h
%_libdir/libnoatun.so

#-------------------------------------------------------------------------

%prep
%setup -q -nkdemultimedia-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdemultimedia-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make

%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdemultimedia-%version-%branch_date
cd build

%makeinstall_std




# Create LMDK structure
# Need to port it

#kdedesktop2mdkmenu.pl kdemultimedia Multimedia/Sound %buildroot/%_datadir/applications/kde4/juk.desktop %buildroot/%_menudir/kdemultimedia-juk kde
#kdedesktop2mdkmenu.pl kdemultimedia-kmid Multimedia/Sound %buildroot/%_datadir/applications/kde4/kmid.desktop %buildroot/%_menudir/kdemultimedia-kmid kde
#kdedesktop2mdkmenu.pl kdemultimedia-kmid Multimedia/Sound %buildroot/%_datadir/applications/kde4/kmid.desktop %buildroot/%_menudir/kdemultimedia-kmid kde
#kdedesktop2mdkmenu.pl kdemultimedia-kmix Multimedia/Sound %buildroot/%_datadir/applications/kde4/kmix.desktop %buildroot/%_menudir/kdemultimedia-kmix kde
#kdedesktop2mdkmenu.pl kdemultimedia-kscd Multimedia/Sound %buildroot/%_datadir/applications/kde4/kscd.desktop %buildroot/%_menudir/kdemultimedia-kscd kde
#kdedesktop2mdkmenu.pl kdemultimedia-noatun Multimedia/Sound %buildroot/%_datadir/applications/kde4/noatun.desktop %buildroot/%_menudir/kdemultimedia-noatun kde
#kdedesktop2mdkmenu.pl kdemultimedia-kaudiocreator Multimedia/Sound %buildroot/%_datadir/applications/kde4/kaudiocreator.desktop %buildroot/%_menudir/kdemultimedia-kaudiocreator kde
#kdedesktop2mdkmenu.pl kdemultimedia-krec Multimedia/Sound %buildroot/%_datadir/applications/kde4/krec.desktop %buildroot/%_menudir/kdemultimedia-krec kde
#kdedesktop2mdkmenu.pl kdemultimedia-common System/Configuration/KDE/Sound %buildroot/%_datadir/applications/kde4/audiocd.desktop %buildroot/%_menudir/kdemultimedia-audiocd kde
#kdedesktop2mdkmenu.pl kdemultimedia-kscd System/Configuration/KDE/Sound %buildroot/%_datadir/applications/kde4/libkcddb.desktop %buildroot/%_menudir/kdemultimedia-libkcddb kde




# David - 2.2-0.beta1.1mdk - Remove some non legal songs
for i in %buildroot/%_datadir/apps/kmidi/*.mid ; do rm -f $i ; done


install -d -m 0775 %buildroot/%_datadir/config/
install -m 0644 %SOURCE2 %buildroot/%_datadir/config/jukrc


%clean
rm -fr %buildroot



