#!/usr/bin/env python3
import argparse
import http.server
import os
import socketserver
import sys


class FileServerHandler(http.server.SimpleHTTPRequestHandler):
    # Минимум логов
    def log_message(self, fmt, *args):
        sys.stdout.write("%s - - [%s] %s\n" %
            (self.client_address[0], self.log_date_time_string(), fmt % args)
        )


def main():
    parser = argparse.ArgumentParser(
        description="Standalone HTTP file server for curl/Ansible"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host/interface to bind (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8002,
        help="Port to listen on (default: 8002)",
    )
    parser.add_argument(
        "--dir",
        dest="directory",
        default=".",
        help="Directory to serve (default: current directory)",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Directory '{args.directory}' does not exist")
        sys.exit(1)

    os.chdir(args.directory)

    print(f"Serving directory: {os.getcwd()}")
    print(f"Listening on: http://{args.host}:{args.port}/")
    print("Press Ctrl+C to stop.")

    with socketserver.TCPServer((args.host, args.port), FileServerHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.server_close()


if __name__ == "__main__":
    main()
