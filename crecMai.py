#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

from src.sim_audio import *
from src.sim_sql import *
from src.sim_modem import *
from src.sim_hardaware import *

import time
import datetime
import wave 
import wavfile
import sys

FILENAME = ""

def CreateFileNameWithDate() -> str:
    time_now  = datetime.datetime.now().strftime('%Y-%m-%d_%H%M:%S')
    return time_now

def CreateFileNameForSoundFile(_APPELANT_SRV) -> str:
    # FILENAME = str(_APPELANT_SRV) + "_" + str(CreateFileNameWithDate()) + ".wav"
    FILENAME = str(_APPELANT_SRV) + "_" + str(CreateFileNameWithDate()) + ".amr"
    return FILENAME

modem = Modem('/dev/ttyS0', baudrate=115200, timeout=1, at_cmd_delay=0.1, debug=False,)

print(modem.get_signal_quality_range())

# AT+CREC=1,1,0 
# 1,record
# 1,id
# 0, amr
# 1, wav

AdataRecord = modem.get_crec_idone()
FILENAME = CreateFileNameForSoundFile(4444)
datafile=open(FILENAME, 'xb')

my_str = AdataRecord
my_str_as_bytes = str.encode(my_str)

#print(type(my_str_as_bytes)) # ensure it is byte representation
#my_decoded_str = my_str_as_bytes.decode()
#print(type(my_decoded_str)) # ensure it is string representation

datafile.write(my_str_as_bytes)