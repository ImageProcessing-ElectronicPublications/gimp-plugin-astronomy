%bcond_with     gimp3

%define         moname        %{name}
%define         abi_version   %{?with_gimp3:2.99}%{?!with_gimp3:2.0}
%define         plugindir     %{_libdir}/gimp/%{abi_version}/plug-ins
%define         scriptdir     %{_datadir}/gimp/%{abi_version}/scripts

Name:           gimp-plugin-astronomy
Version:        0.11
Release:        0
Summary:        Astronomy plugins for the GIMP graphic editor
License:        GPLv2+
Group:          Graphics/Editors and Converters

URL:            http://github.com/JoesCat/gimp-plugin-astronomy
Source0:        http://github.com/JoesCat/gimp-plugin-astronomy/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:  gettext-devel
%if %{with gimp3}
BuildRequires:  pkgconfig(gimp-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%else
BuildRequires:  pkgconfig(gimp-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)

%if %{with gimp3}
Requires:       gimp3 >= 2.99
%else
Requires:       gimp >= 2.6.0
%endif
Requires:       libfftw3
#Requires:       libgsl25


%description
Gimp Astronomy is a set of plug-ins for the Gimp graphic editor
intended for astronomical image processing. They support various basic
and more advanced tasks such as aligning and stacking images with
arithmetic, geometric, median, or sigma mean, removing dark frames and
dividing by a flat field. Some plug-gins are designed for creating
synthetic stars distribution or synthetic galaxy images.


%prep
%setup -q

%if %{with gimp3}
# build for gimp-3.0
sed -i \
  -e 's/gimp-2.0/gimp-3.0/g' \
  -e 's/gimpui-2.0/gimpui-3.0/g' \
  -e 's/gimptool-2.0/gimptool-2.99/g' \
  configure.ac
%endif

# make autoreconf happy
sed -i \
  -e 's/AM_GNU_GETTEXT_VERSION\(([*.*]*)\)/AM_GNU_GETTEXT_REQUIRE_VERSION\1/' \
  -e 's/AM_GNU_GETTEXT_VERSION$/AM_GNU_GETTEXT_REQUIRE_VERSION([0.19.1])/' \
  configure.ac

%build
aclocal --force
autoconf -f
automake --add-missing
%configure
%make_build


%install
%make_install INSTALLDIR="%{buildroot}/%{plugindir}" \
      LOCALEDIR="%{buildroot}/%{_datadir}/locale"
%find_lang %{moname}


# Upstream provides no tests.


%files -f %{moname}.lang
%license COPYING
%doc README AUTHORS
%doc documentation.pdf documentation.tex
%{scriptdir}/background_gradient_batch.scm
%{scriptdir}/border_information.scm
%{scriptdir}/brightness_contrast_batch.scm
%{scriptdir}/dark_subtraction.scm
%{scriptdir}/flat_division.scm
%{scriptdir}/mode_batch.scm
%{scriptdir}/normalize_batch.scm
%{plugindir}/astronomy-alignment
%{plugindir}/astronomy-artificial-galaxy
%{plugindir}/astronomy-artificial-stars
%{plugindir}/astronomy-background-gradient
%{plugindir}/astronomy-merge
%{plugindir}/astronomy-star-rounding


%changelog
