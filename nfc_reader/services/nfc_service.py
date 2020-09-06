import RPi.GPIO as GPIO

import nfc_reader.lib.pn532.pn532 as nfc
from nfc_reader.lib.pn532 import *

import time
from multiprocessing import Process

TIME_FREQUENCY=3 # seconds

class NfcService():
    def __init__(self):
        self.pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = self.pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with NTAG215 cards
        self.pn532.SAM_configuration()

    def start(self):
        print('Waiting for RFID/NFC card to read from!')
        p = Process(target=self._start, args=())
        p.start()
        

    def _start(self):
        while True:
            # Check if a card is available to read
            uid = self.pn532.read_passive_target(timeout=0.5)
            # print('.', end="")
            # Try again if no card is available.
            if uid is not None:
                print('Found card with UID:', [hex(i) for i in uid])
                print('waiting for {} seconds before next scan...'.format(TIME_FREQUENCY))
                
                # TODO is it good to use Process here??
                p = Process(target=self.read_value, args=())
                p.start()
                p.join()
                
                time.sleep(TIME_FREQUENCY)  


    # TODO use a callback here maybe?
    def read_value(self):
        result = ''
        end_of_nfc_value = False # We loop until we reach the end of NFC value (00)
        # Here we start reading NFC value from 6, as the beginning is not related to the stored value
        for i in range(6, 135):
            try:
                for x in self.pn532.ntag2xx_read_block(i):
                    value = '%02X' % x
                    if value == '00':
                        end_of_nfc_value = True
                        break
                    result = result + ('%02X' % x) + ' '
            except nfc.PN532Error as e:
                print(e.errmsg)
                break  
            if end_of_nfc_value is True:
                break
        print('Encoded result: {}'.format(result))
        raw_result = bytes.fromhex(result).decode("latin-1")
        print('Decoded result: {}'.format(raw_result))
        self.process_value(raw_result)

    def process_value(self, decoded_value):
        # curated_url = self._curate_url(decoded_value)
        print('Curated URL: {}'.format(decoded_value))

        # TODO technically, we should not store an entire URL in the NFC tag, but an folder index or folder name instead should be good enough.
        # That would help scanning the value faster 
        # The server can be retreived with hostname functions...
        import requests
        requests.get(curated_url)


    def _curate_url(self, raw_decoded_url):
        '''
        We expect to retrieve a URL starting with `http` and ending with `/`.
        '''
        from_ = raw_decoded_url.index("http")
        to_ = raw_decoded_url.rfind('/')
        return raw_decoded_url[from_:to_]
    