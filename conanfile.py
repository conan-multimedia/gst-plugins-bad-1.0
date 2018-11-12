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
    remotes = {'origin': 'https://github.com/GStreamer/gst-plugins-bad.git'}

    def source(self):
        #tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, self.version))
        #extracted_dir = "gst-plugins-bad-" + self.version
        #os.rename(extracted_dir, self.source_subfolder)
        tools.mkdir(self.source_subfolder)
        with tools.chdir(self.source_subfolder):
            self.run('git init')
            for key, val in self.remotes.items():
                self.run("git remote add %s %s"%(key, val))
            self.run('git fetch --all')
            self.run('git reset --hard %s'%(self.version))
            self.run('git submodule update --init --recursive')


    def build(self):
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

