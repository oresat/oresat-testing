This is a mess. Consider yourself warned.

### rtl-multi-beacon-parse.sh
This script uses an SDR to capture OreSat0 beacons, then decodes them to show L-Band and UHF packet counters and RSSI values. Pack1VBatt was added at the last minute. It depends on an RTL-SDR with a known ppm correction and some software:

- rtl_fm (`sudo apt install rtl-sdr`)
- multimon-ng (we have to use a patched version, see hdlc.c.patch section below)

If your RTL-SDR has a low precision oscillator, you will have to set the ppm correction value following the -p flag to rtl_fm. You can dial this in by looking at a waterfall of a signal with a known frequency. Or try running `rtl_test -p` long enough to let the radio warm up and see the suggested ppm stablize. If the temperature of your operating environment changes significantly, you may need to adjust the ppm again. If you have a fancy RTL-SDR with the 0.5 ppm TCXO, then you can remove the `-p 38` from this script entirely and not worry about temperatures.

If you try running this script and get a message like `User cancel, exiting...` then you probably need to correct the path to multimon-ng.

### hdlc.c.patch
This patch modifies multimon-ng so that full FSK9600 APRS packets are dumped in hex. Without this patch, multimon-ng will only give us "." characters for any non-printing bytes. Most of the stuff we care about in our beacon is not ASCII. So prepare to build multimon-ng. Try these steps:

```bash
git clone https://github.com/EliasOenal/multimon-ng.git
cd multimon-ng/
patch <path/to/hdlc.c.patch
mkdir build
cd build
cmake ..
make -j
```

Be sure to substitute the `path/to/hdlc.c.patch` with the actual path on your system to the hdlc.c.patch file found in this repo. If you are lucky, these steps will produce a `multimon-ng` executable in your present directory. See if it runs with `./multimon-ng -h`.

### plane_track.py
This takes a single argument of an icao 24-bit identifier, uses the OpenSKY API to get position updates every 30 seconds, converts the position into az/el based on the hard-coded GPS coordinates for the ground station, and uses Hamlib to point the rotator. Python library dependencies that you may not already have:

- Hamlib and pymap3d (`sudo apt install python3-hamlib python3-pymap3d`)
- OpenSky (`git clone https://github.com/openskynetwork/opensky-api.git` and follow install instructions found in that repo)

Assuming you want to track `a1d296`, try this:

```bash
./plane_track.py a1d296 &
tail -f a1d296.log
```
