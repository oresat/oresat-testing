#!/usr/bin/env python3

import socket, time, sys
import Hamlib
import pymap3d as pm
import logging as log
from opensky_api import OpenSkyApi

icao = sys.argv[1]
gs_lat,gs_lon,gs_alt = (45.509054, -122.681394, 50)

sky = OpenSkyApi()
log.basicConfig(filename=icao+".log", format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=log.INFO)
Hamlib.rig_set_debug (Hamlib.RIG_DEBUG_NONE)
r = Hamlib.Rot(Hamlib.ROT_MODEL_NETROTCTL)
r.set_conf('rot_pathname', 'localhost:4533')
r.open()

while True:
    s = sky.get_states(icao24=icao).states[0]
    az,el,ra = pm.geodetic2aer(s.latitude,s.longitude,s.geo_altitude,gs_lat,gs_lon,gs_alt)
    log.info("%.2f %.2f %.2f %r %r %r %r %r" % (az,el,ra,s.time_position,s.longitude,s.latitude,s.geo_altitude,s.baro_altitude))
    az += 180
    if az > 450:
        az %= 360
    el = 180-el
    r.set_position(az, el)
    time.sleep(30)

