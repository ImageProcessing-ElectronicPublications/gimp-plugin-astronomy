## Process this file with automake to produce Makefile.in

ACLOCAL_AMFLAGS=-I m4 ${ACLOCAL}

AM_CPPFLAGS = \
	-DLOCALEDIR=\""$(LOCALEDIR)"\"	\
	-DDATADIR=\""$(DATADIR)"\"	\
	-I$(builddir)			\
	-I$(srcdir)			\
	@GIMP_CFLAGS@			\
	-I$(includedir)

LDADD = $(LIBS) $(GSL_LIBS) $(FFTW_LIBS) $(GIMP_LIBS)

bin_PROGRAMS = astronomy-alignment astronomy-merge astronomy-background-gradient astronomy-artificial-stars astronomy-artificial-galaxy astronomy-star-rounding

bindir = ${GIMP_LIBDIR}/plug-ins

astronomy_alignment_SOURCES = \
	alignment.c

astronomy_merge_SOURCES = \
	merge.c

astronomy_background_gradient_SOURCES = \
	background_gradient.c

astronomy_artificial_stars_SOURCES = \
	artificial_stars.c

astronomy_artificial_galaxy_SOURCES = \
	artificial_galaxy.c

astronomy_star_rounding_SOURCES = \
	star_rounding.c

EXTRA_DIST = \
	alignment_autopano.c \
	plugin-intl.h \
	artificial_stars_temperature.h

strip:
	$(STRIP) ${builddir}/astronomy-alignment
	$(STRIP) ${builddir}/astronomy-artificial-galaxy
	$(STRIP) ${builddir}/astronomy-artificial-stars
	$(STRIP) ${builddir}/astronomy-background-gradient
	$(STRIP) ${builddir}/astronomy-merge
	$(STRIP) ${builddir}/astronomy-star-rounding

