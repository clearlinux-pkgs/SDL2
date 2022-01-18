#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2
Version  : 2.0.20
Release  : 48
URL      : https://www.libsdl.org/release/SDL2-2.0.20.tar.gz
Source0  : https://www.libsdl.org/release/SDL2-2.0.20.tar.gz
Source1  : https://www.libsdl.org/release/SDL2-2.0.20.tar.gz.sig
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : BSD-3-Clause CPL-1.0 GPL-3.0 ISC OFL-1.1 Zlib
Requires: SDL2-bin = %{version}-%{release}
Requires: SDL2-filemap = %{version}-%{release}
Requires: SDL2-lib = %{version}-%{release}
Requires: SDL2-license = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : libXScrnSaver-dev
BuildRequires : libXxf86vm-dev
BuildRequires : libsamplerate-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : wayland-dev

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL2 package.
Group: Binaries
Requires: SDL2-license = %{version}-%{release}
Requires: SDL2-filemap = %{version}-%{release}

%description bin
bin components for the SDL2 package.


%package dev
Summary: dev components for the SDL2 package.
Group: Development
Requires: SDL2-lib = %{version}-%{release}
Requires: SDL2-bin = %{version}-%{release}
Provides: SDL2-devel = %{version}-%{release}
Requires: SDL2 = %{version}-%{release}

%description dev
dev components for the SDL2 package.


%package filemap
Summary: filemap components for the SDL2 package.
Group: Default

%description filemap
filemap components for the SDL2 package.


%package lib
Summary: lib components for the SDL2 package.
Group: Libraries
Requires: SDL2-license = %{version}-%{release}
Requires: SDL2-filemap = %{version}-%{release}

%description lib
lib components for the SDL2 package.


%package license
Summary: license components for the SDL2 package.
Group: Default

%description license
license components for the SDL2 package.


%prep
%setup -q -n SDL2-2.0.20
cd %{_builddir}/SDL2-2.0.20
pushd ..
cp -a SDL2-2.0.20 buildavx2
popd
pushd ..
cp -a SDL2-2.0.20 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642545014
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static --enable-sdl-dlopen \
--enable-pulseaudio-shared \
--enable-alsa \
--enable-video-wayland
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-sdl-dlopen \
--enable-pulseaudio-shared \
--enable-alsa \
--enable-video-wayland
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static --enable-sdl-dlopen \
--enable-pulseaudio-shared \
--enable-alsa \
--enable-video-wayland
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1642545014
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2
cp %{_builddir}/SDL2-2.0.20/Xcode-iOS/Demos/data/bitmapfont/license.txt %{buildroot}/usr/share/package-licenses/SDL2/40e37820c4fd40cc2914e1df5b24158e312e9623
cp %{_builddir}/SDL2-2.0.20/debian/copyright %{buildroot}/usr/share/package-licenses/SDL2/2ee92026bffdc5470dfc89e2a28e72f7804ebd91
cp %{_builddir}/SDL2-2.0.20/src/hidapi/LICENSE-bsd.txt %{buildroot}/usr/share/package-licenses/SDL2/7dde42b4c6fdafae722d8d07556b6d9dba4d2963
cp %{_builddir}/SDL2-2.0.20/src/hidapi/LICENSE-gpl3.txt %{buildroot}/usr/share/package-licenses/SDL2/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/SDL2-2.0.20/src/hidapi/LICENSE-orig.txt %{buildroot}/usr/share/package-licenses/SDL2/66047dbcf3fd689c99472266f5ad141c53d6f2c6
cp %{_builddir}/SDL2-2.0.20/src/video/yuv2rgb/LICENSE %{buildroot}/usr/share/package-licenses/SDL2/763a61ff74960ead36b9ef5f5db65d083d7466c1
cp %{_builddir}/SDL2-2.0.20/test/unifont-13.0.06-license.txt %{buildroot}/usr/share/package-licenses/SDL2/ee06847a47ae566e1f69859ef1b1621189c0e03c
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdl2-config

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL.h
/usr/include/SDL2/SDL_assert.h
/usr/include/SDL2/SDL_atomic.h
/usr/include/SDL2/SDL_audio.h
/usr/include/SDL2/SDL_bits.h
/usr/include/SDL2/SDL_blendmode.h
/usr/include/SDL2/SDL_clipboard.h
/usr/include/SDL2/SDL_config.h
/usr/include/SDL2/SDL_cpuinfo.h
/usr/include/SDL2/SDL_egl.h
/usr/include/SDL2/SDL_endian.h
/usr/include/SDL2/SDL_error.h
/usr/include/SDL2/SDL_events.h
/usr/include/SDL2/SDL_filesystem.h
/usr/include/SDL2/SDL_gamecontroller.h
/usr/include/SDL2/SDL_gesture.h
/usr/include/SDL2/SDL_haptic.h
/usr/include/SDL2/SDL_hidapi.h
/usr/include/SDL2/SDL_hints.h
/usr/include/SDL2/SDL_joystick.h
/usr/include/SDL2/SDL_keyboard.h
/usr/include/SDL2/SDL_keycode.h
/usr/include/SDL2/SDL_loadso.h
/usr/include/SDL2/SDL_locale.h
/usr/include/SDL2/SDL_log.h
/usr/include/SDL2/SDL_main.h
/usr/include/SDL2/SDL_messagebox.h
/usr/include/SDL2/SDL_metal.h
/usr/include/SDL2/SDL_misc.h
/usr/include/SDL2/SDL_mouse.h
/usr/include/SDL2/SDL_mutex.h
/usr/include/SDL2/SDL_name.h
/usr/include/SDL2/SDL_opengl.h
/usr/include/SDL2/SDL_opengl_glext.h
/usr/include/SDL2/SDL_opengles.h
/usr/include/SDL2/SDL_opengles2.h
/usr/include/SDL2/SDL_opengles2_gl2.h
/usr/include/SDL2/SDL_opengles2_gl2ext.h
/usr/include/SDL2/SDL_opengles2_gl2platform.h
/usr/include/SDL2/SDL_opengles2_khrplatform.h
/usr/include/SDL2/SDL_pixels.h
/usr/include/SDL2/SDL_platform.h
/usr/include/SDL2/SDL_power.h
/usr/include/SDL2/SDL_quit.h
/usr/include/SDL2/SDL_rect.h
/usr/include/SDL2/SDL_render.h
/usr/include/SDL2/SDL_revision.h
/usr/include/SDL2/SDL_rwops.h
/usr/include/SDL2/SDL_scancode.h
/usr/include/SDL2/SDL_sensor.h
/usr/include/SDL2/SDL_shape.h
/usr/include/SDL2/SDL_stdinc.h
/usr/include/SDL2/SDL_surface.h
/usr/include/SDL2/SDL_system.h
/usr/include/SDL2/SDL_syswm.h
/usr/include/SDL2/SDL_test.h
/usr/include/SDL2/SDL_test_assert.h
/usr/include/SDL2/SDL_test_common.h
/usr/include/SDL2/SDL_test_compare.h
/usr/include/SDL2/SDL_test_crc32.h
/usr/include/SDL2/SDL_test_font.h
/usr/include/SDL2/SDL_test_fuzzer.h
/usr/include/SDL2/SDL_test_harness.h
/usr/include/SDL2/SDL_test_images.h
/usr/include/SDL2/SDL_test_log.h
/usr/include/SDL2/SDL_test_md5.h
/usr/include/SDL2/SDL_test_memory.h
/usr/include/SDL2/SDL_test_random.h
/usr/include/SDL2/SDL_thread.h
/usr/include/SDL2/SDL_timer.h
/usr/include/SDL2/SDL_touch.h
/usr/include/SDL2/SDL_types.h
/usr/include/SDL2/SDL_version.h
/usr/include/SDL2/SDL_video.h
/usr/include/SDL2/SDL_vulkan.h
/usr/include/SDL2/begin_code.h
/usr/include/SDL2/close_code.h
/usr/lib64/cmake/SDL2/sdl2-config-version.cmake
/usr/lib64/cmake/SDL2/sdl2-config.cmake
/usr/lib64/libSDL2.so
/usr/lib64/pkgconfig/sdl2.pc
/usr/share/aclocal/*.m4

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-SDL2

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2-2.0.so.0
/usr/lib64/libSDL2-2.0.so.0.18.2
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2/2ee92026bffdc5470dfc89e2a28e72f7804ebd91
/usr/share/package-licenses/SDL2/40e37820c4fd40cc2914e1df5b24158e312e9623
/usr/share/package-licenses/SDL2/66047dbcf3fd689c99472266f5ad141c53d6f2c6
/usr/share/package-licenses/SDL2/763a61ff74960ead36b9ef5f5db65d083d7466c1
/usr/share/package-licenses/SDL2/7dde42b4c6fdafae722d8d07556b6d9dba4d2963
/usr/share/package-licenses/SDL2/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/SDL2/ee06847a47ae566e1f69859ef1b1621189c0e03c
