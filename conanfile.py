from conans import ConanFile, CMake, tools, Meson
import os

class GstpluginsbadConan(ConanFile):
    name = "gst-plugins-bad-1.0"
    version = "1.14.4"
    description = "'Bad' GStreamer plugins and helper libraries"
    url = "https://github.com/conan-multimedia/gst-plugins-bad-1.0"
    homepage = "https://github.com/GStreamer/gst-plugins-bad"
    license = "GPLv2+"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    #requires = ("bzip2/1.0.6@user/channel","expat/2.2.5@user/channel","faad2/2.7@user/channel",
    #            "gmp/6.1.2@user/channel","gobject-introspection-m4/1.54.1@user/channel","gtk-doc-lite/1.27@user/channel",
    #            "ladspa/1.13@user/channel","libdca/0.0.5@user/channel","libdvdread/5.0.0@user/channel",
    #            "libffi/3.99999@user/channel","libjpeg-turbo/1.5.3@user/channel","libmms/0.6.4@user/channel",
    #            "libogg/1.3.3@user/channel","libsrtp/1.6.0@user/channel","libtasn1/4.13@user/channel",
    #            "libvisual/0.4.0@user/channel","openh264/1.7.0@user/channel","openjpeg/2.3.0@user/channel",
    #            "opus/1.2.1@user/channel","orc/0.4.28@bincrafters/stable","pixman/0.34.0@user/channel",
    #            "sbc/1.3@user/channel","soundtouch/1.9.2@user/channel","vala-m4/0.35.2@user/channel",
    #            "vo-aacenc/0.1.3@user/channel","webrtc-audio-processing/0.2@user/channel",
    #            "zlib/1.2.11@user/channel","glib/2.54.3@bincrafters/stable","libdvdnav/5.0.1@user/channel","libpng/1.6.34@user/channel",
    #            "libvorbis/1.3.5@user/channel","libxml2/2.9.7@user/channel","nettle/3.4@user/channel","openssl/1.1.0h@user/channel",
    #            "tiff/4.0.9@user/channel","freetype/2.9@user/channel","fribidi/0.19.7@bincrafters/stable",
    #            "gnutls/3.5.18@user/channel","gobject-introspection/1.54.1@bincrafters/stable","libkate/0.4.1@user/channel",
    #            "libtheora/1.1.1@user/channel","spandsp/0.0.6@user/channel","fontconfig/2.12.6@user/channel",
    #            "gdk-pixbuf/2.36.2@bincrafters/stable","graphene/1.4.0@bincrafters/stable","gstreamer/1.14.3@bincrafters/stable",
    #            "librtmp/2.4_p20151223@user/channel","cairo/1.14.12@bincrafters/stable","libass/0.13.7@bincrafters/stable",
    #            "libcroco/0.6.12@bincrafters/stable","libnice/0.1.14@bincrafters/stable",
    #            "harfbuzz/1.7.5@bincrafters/stable","pango/1.40.14@bincrafters/stable",
    #            "gst-plugins-base/1.14.3@bincrafters/stable","librsvg/2.40.20@bincrafters/stable")
    requires = ("gstreamer-1.0/1.14.4@conanos/dev", "gst-plugins-base-1.0/1.14.4@conanos/dev", "bzip2/1.0.6@conanos/dev",
    "libass/0.13.7@conanos/dev", "faad2/2.7@conanos/dev","libkate/0.4.1@conanos/dev", "zlib/1.2.11@conanos/dev",
    "openh264/1.7.0@conanos/dev", "opus/1.2.1@conanos/dev", "nettle/3.4@conanos/dev", "librtmp/2.4_p20151223@conanos/dev",
    "libsrtp/1.6.0@conanos/dev", "libdca/0.0.5@conanos/dev", "libmms/0.6.4@conanos/dev", "libdvdnav/5.0.1@conanos/dev",
    "libnice/0.1.14@conanos/dev", "soundtouch/1.9.2@conanos/dev", "vo-aacenc/0.1.3@conanos/dev", "librsvg/2.40.20@conanos/dev",
    "openjpeg/2.3.0@conanos/dev", "openssl/1.1.1@conanos/dev", "spandsp/0.0.6@conanos/dev", "webrtc-audio-processing/0.2@conanos/dev",
    "sbc/1.3@conanos/dev", "ladspa/1.13@conanos/dev",
    
    
    "libffi/3.3-rc0@conanos/dev","glib/2.58.0@conanos/dev","orc/0.4.28@conanos/dev","gobject-introspection/1.58.0@conanos/dev",
    "libxml2/2.9.8@conanos/dev","pango/1.40.14@conanos/dev","cairo/1.14.12@conanos/dev","fribidi/0.19.7@conanos/dev",
    "fontconfig/2.12.6@conanos/dev","freetype/2.9.0@conanos/dev","libpng/1.6.34@conanos/dev","expat/2.2.5@conanos/dev",
    "gdk-pixbuf/2.36.2@conanos/dev", "libcroco/0.6.12@conanos/dev","pixman/0.34.0@conanos/dev","gnutls/3.5.18@conanos/dev",
    "gmp/6.1.2@conanos/dev","libtasn1/4.13@conanos/dev","libtiff/4.0.9@conanos/dev","harfbuzz/1.7.5@conanos/dev")

    source_subfolder = "source_subfolder"
    
    def source(self):
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = "gst-plugins-bad-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def build(self):
        #vars = {'PKG_CONFIG_PATH': "%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig:%s/lib/pkgconfig"
        #        ":%s/lib/pkgconfig"
        #        %(
        #            self.deps_cpp_info["gstreamer"].rootpath,self.deps_cpp_info["gst-plugins-base"].rootpath,
        #            self.deps_cpp_info["bzip2"].rootpath, self.deps_cpp_info["libass"].rootpath,
        #            self.deps_cpp_info["faad2"].rootpath,self.deps_cpp_info["libkate"].rootpath,
        #            self.deps_cpp_info["zlib"].rootpath,self.deps_cpp_info["openh264"].rootpath,
        #            self.deps_cpp_info["opus"].rootpath,self.deps_cpp_info["nettle"].rootpath,
        #            self.deps_cpp_info["librtmp"].rootpath,self.deps_cpp_info["libsrtp"].rootpath,
        #            self.deps_cpp_info["libdca"].rootpath,self.deps_cpp_info["libmms"].rootpath,
        #            self.deps_cpp_info["libdvdnav"].rootpath,self.deps_cpp_info["libnice"].rootpath,
        #            self.deps_cpp_info["soundtouch"].rootpath,self.deps_cpp_info["vo-aacenc"].rootpath,
        #            self.deps_cpp_info["librsvg"].rootpath,self.deps_cpp_info["openjpeg"].rootpath,
        #            self.deps_cpp_info["openssl"].rootpath,self.deps_cpp_info["spandsp"].rootpath,
        #            self.deps_cpp_info["webrtc-audio-processing"].rootpath,self.deps_cpp_info["sbc"].rootpath,
        #            self.deps_cpp_info["ladspa"].rootpath
        #        ),
        #        'LIBRARY_PATH':"%s/lib:$LIBRARY_PATH"%(self.deps_cpp_info["openjpeg"].rootpath),
        #        'C_INCLUDE_PATH':"%s/include:%s/include"%(self.deps_cpp_info["tiff"].rootpath,self.deps_cpp_info["soundtouch"].rootpath),
        #        'CPLUS_INCLUDE_PATH':"%s/include:%s/include"%(self.deps_cpp_info["tiff"].rootpath,self.deps_cpp_info["soundtouch"].rootpath)}

        #with tools.environment_append(vars):
        #    self.run('sh ./autogen.sh --noconfigure && ./configure --prefix %s/build --libdir %s/build/lib'
        #    ' --enable-introspection --enable-static --disable-introspection --disable-gsm --disable-examples --disable-festival         --disable-videomaxrate --disable-bz2 --disable-libde265         --disable-linsys --disable-fbdev --disable-apexsink         --disable-celt --disable-curl --disable-dc1394 --disable-directfb         --disable-dirac --disable-faac --disable-flite --disable-gme         --disable-lv2 --disable-mimic --disable-modplug         --disable-mpeg2enc --disable-mplex --disable-musepack --disable-mythtv         --disable-neon --disable-ofa --disable-openal --disable-opencv         --disable-pvr --disable-sdl --disable-sndfile         --disable-teletextdec --disable-timidity         --disable-vdpau --disable-voamrwbenc --disable-wildmidi         --disable-xvid --disable-zbar --disable-sdi --disable-srt --enable-bz2 --enable-assrender         --enable-faad --enable-kate --enable-openh264 --enable-opus         --enable-hls --enable-rtmp --enable-srtp --enable-dts         --enable-libmms --enable-resindvd --enable-soundtouch         --enable-voaacenc'
        #    ' --enable-rsvg --enable-openjpeg --enable-spandsp --enable-decklink --enable-webrtc --enable-dtls'%(os.getcwd(),os.getcwd()))
        #    self.run('make -j4')
        #    self.run('make install')

        #vars = {'LD_LIBRARY_PATH':'%s/lib:%s/lib'%(self.deps_cpp_info["libffi"].rootpath,self.deps_cpp_info["glib"].rootpath),
        #        'PATH':'%s/bin:%s/bin:%s/bin:%s'%(self.deps_cpp_info["gobject-introspection"].rootpath,
        #                                          self.deps_cpp_info["glib"].rootpath,
        #                                          self.deps_cpp_info["orc"].rootpath,os.getenv("PATH")),
        #        'C_INCLUDE_PATH' : '%s/include:%s/include'%(self.deps_cpp_info["cairo"].rootpath,self.deps_cpp_info["librsvg"].rootpath)
        #        }


        #with tools.environment_append(vars):

        #vars = {'LDFLAGS': '-L%s/lib -L%s/lib'%(self.deps_cpp_info["openjpeg"].rootpath,self.deps_cpp_info["gmp"].rootpath),
        #        'C_INCLUDE_PATH': '%s/include:%s/include'%(self.deps_cpp_info["cairo"].rootpath,self.deps_cpp_info["tiff"].rootpath),
        #        'CPLUS_INCLUDE_PATH':'%s/include'%(self.deps_cpp_info["soundtouch"].rootpath),
        #        'LD_LIBRARY_PATH':'%s/lib:%s/lib'%(self.deps_cpp_info["libffi"].rootpath,self.deps_cpp_info["glib"].rootpath)}
        #with tools.environment_append({}):

        with tools.chdir(self.source_subfolder):
            with tools.environment_append({
                'C_INCLUDE_PATH': '%s/include:%s/include:%s/include/librsvg-2.0:%s/include/cairo:%s/include/gdk-pixbuf-2.0:%s/include:%s/include:%s/include'
                %(self.deps_cpp_info["libass"].rootpath,self.deps_cpp_info["libdca"].rootpath,self.deps_cpp_info["librsvg"].rootpath,
                self.deps_cpp_info["cairo"].rootpath,self.deps_cpp_info["gdk-pixbuf"].rootpath,self.deps_cpp_info["cairo"].rootpath,
                self.deps_cpp_info["librtmp"].rootpath, self.deps_cpp_info["libtiff"].rootpath),
                'CPLUS_INCLUDE_PATH' : '%s/include'%(self.deps_cpp_info["soundtouch"].rootpath),
                'PATH':'%s/bin:%s/bin:%s'%(self.deps_cpp_info["orc"].rootpath,self.deps_cpp_info["gobject-introspection"].rootpath,os.getenv("PATH")),
                'LIBRARY_PATH':'%s/lib:%s/lib'%(self.deps_cpp_info["bzip2"].rootpath,self.deps_cpp_info["gmp"].rootpath),
                'LD_LIBRARY_PATH':'%s/lib:%s/lib'%(self.deps_cpp_info["libffi"].rootpath,self.deps_cpp_info["glib"].rootpath,)
                }):
                meson = Meson(self)
                meson.configure(
                    defs={'disable_introspection' : 'false',
                          'prefix':'%s/builddir/install'%(os.getcwd()), 'libdir':'lib',
                         },
                    source_dir = '%s'%(os.getcwd()),
                    build_dir= '%s/builddir'%(os.getcwd()),
                    pkg_config_paths=['%s/lib/pkgconfig'%(self.deps_cpp_info["gstreamer-1.0"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["gst-plugins-base-1.0"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["bzip2"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libass"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["faad2"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libkate"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["zlib"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["openh264"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["opus"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["nettle"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["librtmp"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libsrtp"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libdca"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libmms"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libdvdnav"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libnice"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["soundtouch"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["vo-aacenc"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["librsvg"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["openjpeg"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["openssl"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["spandsp"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["webrtc-audio-processing"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["sbc"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["ladspa"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libffi"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["glib"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["orc"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libxml2"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["pango"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["cairo"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["fribidi"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["fontconfig"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["freetype"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libpng"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["expat"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["gdk-pixbuf"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libcroco"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["pixman"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["gnutls"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["gmp"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libtasn1"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["libtiff"].rootpath),
                                      '%s/lib/pkgconfig'%(self.deps_cpp_info["harfbuzz"].rootpath),
                    ]
                                )
                meson.build(args=['-j4'])
                self.run('ninja -C {0} install'.format(meson.build_dir))

    def package(self):
        if tools.os_info.is_linux:
            with tools.chdir(self.source_subfolder):
                self.copy("*", src="%s/builddir/install"%(os.getcwd()))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

