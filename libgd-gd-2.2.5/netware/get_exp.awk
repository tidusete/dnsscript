#!awk
# awk hack to fetch libgd export functions from header
# and write them to STDOUT. Here you can get an awk version for Win32:
# http://www.gknw.net/development/prgtools/awk.zip
# $Id$
#
BEGIN {
  print "# Exports extracted from " ARGV[1] "";
  print "# Do not edit this file - it is created by make!";
  print "# All your changes will be lost!!";
  if (EPREFIX) {
    print "  (" EPREFIX ")";
  }
  print "  gdFontGetGiant,";
  print "  gdFontGetLarge,";
  print "  gdFontGetMediumBold,";
  print "  gdFontGetSmall,";
  print "  gdFontGetTiny,";
  print "  gdImageSquareToCircle,";
  print "  gdImageStringFTCircle,";
  print "  gdImageSharpen,";
}

# try to catch the function names from lines like:
# BGD_DECLARE(gdImagePtr) function ...
# BGD_DECLARE(void *) function ...
#
/^[ \t]*BGD_DECLARE\([^\)]*\) +(gd[A-Za-z0-9_]+)/ {
  sub(/^[ \t]*BGD_DECLARE\([^\)]+\) +/, "");
  sub(/[ \t]*\(.*$/, "");
  # hack to filter gdImageEllipse() since we have no C implementation.
  if ($0 != "gdImageEllipse") {
    print "  " $0 ",";
  }
}


