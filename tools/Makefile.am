
bin_PROGRAMS = hangul

hangul_SOURCES = hangul.c
hangul_CFLAGS = -DLOCALEDIR=\"$(localedir)\" -fPIE
hangul_LDADD = ../hangul/libhangul.la $(LTLIBINTL) $(LTLIBICONV)
hangul_LDFLAGS = -pie
