#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL2
Version  : 2.0.4
Release  : 1
URL      : https://www.libsdl.org/release/SDL2-2.0.4.tar.gz
Source0  : https://www.libsdl.org/release/SDL2-2.0.4.tar.gz
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : CPL-1.0 Zlib
Requires: SDL2-bin
Requires: SDL2-lib
BuildRequires : cmake

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL2 package.
Group: Binaries

%description bin
bin components for the SDL2 package.


%package dev
Summary: dev components for the SDL2 package.
Group: Development
Requires: SDL2-lib
Requires: SDL2-bin
Provides: SDL2-devel

%description dev
dev components for the SDL2 package.


%package lib
Summary: lib components for the SDL2 package.
Group: Libraries

%description lib
lib components for the SDL2 package.


%prep
%setup -q -n SDL2-2.0.4

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

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
/usr/include/SDL2/SDL_config_android.h
/usr/include/SDL2/SDL_config_iphoneos.h
/usr/include/SDL2/SDL_config_macosx.h
/usr/include/SDL2/SDL_config_minimal.h
/usr/include/SDL2/SDL_config_pandora.h
/usr/include/SDL2/SDL_config_psp.h
/usr/include/SDL2/SDL_config_windows.h
/usr/include/SDL2/SDL_config_winrt.h
/usr/include/SDL2/SDL_config_wiz.h
/usr/include/SDL2/SDL_copying.h
/usr/include/SDL2/SDL_cpuinfo.h
/usr/include/SDL2/SDL_egl.h
/usr/include/SDL2/SDL_endian.h
/usr/include/SDL2/SDL_error.h
/usr/include/SDL2/SDL_events.h
/usr/include/SDL2/SDL_filesystem.h
/usr/include/SDL2/SDL_gamecontroller.h
/usr/include/SDL2/SDL_gesture.h
/usr/include/SDL2/SDL_haptic.h
/usr/include/SDL2/SDL_hints.h
/usr/include/SDL2/SDL_joystick.h
/usr/include/SDL2/SDL_keyboard.h
/usr/include/SDL2/SDL_keycode.h
/usr/include/SDL2/SDL_loadso.h
/usr/include/SDL2/SDL_log.h
/usr/include/SDL2/SDL_main.h
/usr/include/SDL2/SDL_messagebox.h
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
/usr/include/SDL2/SDL_test_random.h
/usr/include/SDL2/SDL_thread.h
/usr/include/SDL2/SDL_timer.h
/usr/include/SDL2/SDL_touch.h
/usr/include/SDL2/SDL_types.h
/usr/include/SDL2/SDL_version.h
/usr/include/SDL2/SDL_video.h
/usr/include/SDL2/begin_code.h
/usr/include/SDL2/close_code.h
/usr/lib/*.so
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib/*.so.*
