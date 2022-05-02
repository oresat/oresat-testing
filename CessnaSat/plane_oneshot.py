#!/usr/bin/env python3

import socket, time, sys
import Hamlib
import pymap3d as pm
import logging as log

lat = float(sys.argv[1])
lon = float(sys.argv[2])
alt = float(sys.argv[3])
gs_lat,gs_lon,gs_alt = (45.509054, -122.681394, 50)

log.basicConfig(filename="oneshot.log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=log.INFO)

Hamlib.rig_set_debug (Hamlib.RIG_DEBUG_NONE)
r = Hamlib.Rot(Hamlib.ROT_MODEL_NETROTCTL)
r.set_conf('rot_pathname', 'localhost:4533')
r.open()

az,el,ra = pm.geodetic2aer(lat,lon,alt,gs_lat,gs_lon,gs_alt)
log.info("%.2f %.2f %.2f %r %r %r" % (az,el,ra,lat,lon,alt))
print("%.2f %.2f %.2f %r %r %r" % (az,el,ra,lat,lon,alt))

# Face south but tip the head back until it is looking north.
# This way we don't run into the 0-degree az hard-stop.
az += 180
if az > 450:
    az %= 360
el = 180-el
r.set_position(az, el)
