import argparse
from ..services import events

def main():
  
    parser = argparse.ArgumentParser(prog='smartcal',
        description='A smarter way to timeblock your Google calendar.')
    
    parser.add_argument('-g', '--get', help='returns events to the console.', dest='get')

    args = parser.parse_args()

    if 'get' in args:
        print('getting events...')
        events.get_events()