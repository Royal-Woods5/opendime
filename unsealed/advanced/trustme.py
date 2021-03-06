#!/usr/bin/env pythonw
#
# Python code to verify the legitamacy of this Opendime.
#
# You can run this with python2 or python3. Perhaps you can just
# double click it? If not, in a Terminal window, type this command:
#
#   python trustme.py
#
#
# Since this code is running from inside the Opendime it is verfying,
# it is somewhat questionable to trust what it says. It's better to use
# code from a trusted source to verify an Opendime. That can be the
# code on another Opendime that you know is good. To test between
# two units, provide path to the *other* as the argument:
#
#   python trustme.py /Volumes/OPENDIME\ 2
#
#   python trustme.py G:\
#
# IMPORTANT: 
#
# - An Internet connection is required (to fetch pycoin), but your
#   privacy should not be impacted because the payment address and
#   other details specific to this Opendime are not sent over the network
#   and all tests are completely local.
#
# - If you have libusb and PyUSB installed, additional checks
#   will be performed. On MacOS, try install with:
#
#       brew install libusb ; pip install PyUSB
#
# - You may inspect the code by unzipping support/pycode.zip 
#   It makes heavy use of pycoin, which it downloads before running.
#
import os, sys; sys.path.insert(0, os.path.normpath(__file__ + '/../../support/pycode.zip'))
import pycode.trust_me; pycode.trust_me.main()
