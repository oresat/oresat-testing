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

### Breakout Board

The SA.22c provides a Samtec 2.00 mm 2x9 socket for mating with the Samtec header [TMMH-109-01-G-DV-ES-A](https://www.samtec.com/products/tmmh-109-01-g-dv-es-a). The breakout board provides these features:

* Phoenix connectors for power (up to 14 AWG), UART, and analog in and outs (up to 20 AWG)
  * Power: 15V, 5V, and grounds
  * UART: in, out, and ground
  * Analog in: Frequency control and ground
    * 0 to 5V range for 2E-12 incremental frequency adjustment
  * Analog out: Lock and service indicators and grounds
    * Ready for driving LEDs!
    * Lock (green LED): indicates when the internal voltage controlled crystal oscillator (VCXO) is locked to the atomic transition
    * Service (red LED): indicates when internal operating parameters are near the end of their tuning or adjustment range; see pg. 30 for details
* SMA (female) connectors for RF
  * RF out: ACMOS - 10 MHz
  * 1 PPS: in and out

Note: Lock and service outputs on the SA.22c are active low.  The breakout board inverts these and is ready to drive low voltage LEDs or lamps using a [p-channel MOSFET](https://www.digikey.com/product-detail/en/diodes-incorporated/ZXMP10A13FTA/ZXMP10A13FCT-ND/560670).  Resistors R1 and R2 have been chosen to drive a standard green and red LEDs with 3 mA.
