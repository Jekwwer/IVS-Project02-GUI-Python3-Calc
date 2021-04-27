#!/bin/sh

./change_path.sh gui.py
mkdir -p '../install/usr/share/WaterLift_calc' 2>/dev/null
cp gui.py '../install/usr/share/WaterLift_calc/gui.py'
cp manual_for_help_window.pdf '../install/usr/share/WaterLift_calc/manual_for_help_window.pdf'
cp math_lib.py '../install/usr/share/WaterLift_calc/math_lib.py'
mkdir -p '../install/usr/share/pixmaps' 2>/dev/null
cp ../images/WaterLift_Calculator_logo.png '../install/usr/share/pixmaps/WaterLift_Calculator_logo.png'
mkdir -p '../install/usr/bin' 2>/dev/null
ln -sf /usr/share/WaterLift_calc/gui.py '../install/usr/bin/WaterLift_calc'
chmod 0775 '../install/DEBIAN/postinst'
chmod 0775 '../install/DEBIAN/control'
dpkg-deb --build '../install/' '../install/WaterLift_Calc-1.0-ubuntu20.04-x64.deb'
