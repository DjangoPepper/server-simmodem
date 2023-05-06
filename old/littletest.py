from sim_modem import Modem

modem = Modem('/dev/ttyS0')

signal_quality = modem.get_signal_quality()
print(signal_quality)

#modem.send_sms('+393383928434', 'Hello World!')
