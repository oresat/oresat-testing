### Rubidium Oscillator

This is a 10 MHz frequency standard that can be used as a reference for spectrum analyzers or
frequency counters when doing RF calibrations or confirmations of frequency.

The standard is based on a Symmetricom SA.22c Rubidium Oscillator module that is typically
used in telecom applications that need a precision frequency reference.
It's use here is intended as an atomic frequency standard that can be used in locations that
do not have easy access to a GPS constellation whereby a GPS disciplined oscillator could
provide the standard.

The Symmetricom SA.22c provides both a precision 10 MHz reference and a 1 pulse per second
timing signal. The 1 PPS signal is free runing and not syncronized to the UTC standard, such
as would be provided by the GPSDO.

Included in the repo are items used to construct the instrument starting with the
Symmetricom SA.22c atomic module.

* eagle:  Breakout board used to connect to pin header as described in table 1-1 on page 23.
* Manufacturers reference manual:
*
