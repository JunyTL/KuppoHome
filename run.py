#!/usr/bin/env python3
import argparse
import logging
import os
import pathlib

from kuppo import create_app


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument('-p', '--port', type=int,
                    default=int(os.environ.get('PORT', 9999)),
                    help='port number to listen')
parser.add_argument('-H', '--host', default='0.0.0.0')
parser.add_argument('-d', '--debug', action='store_true', default=False)
parser.add_argument('--without-alembic-upgrade', action='store_true')


def main():
    args = parser.parse_args()
    logging.basicConfig(
        format='%(levelname).1s | %(name)s | %(message)s',
        level=logging.INFO
    )
    wsgi_app = create_app()
    if args.debug:
        logging.getLogger('kuppo').setLevel(logging.DEBUG)
    wsgi_app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == '__main__':
    main()
