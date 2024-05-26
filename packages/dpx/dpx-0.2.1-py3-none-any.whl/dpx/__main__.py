import sys
import argparse
from .interactive import go


parser = argparse.ArgumentParser(prog="het", description="Hetzner REST Assistant")
parser.add_argument(
    "-i",
    action="store_true",
    help="Help for BLA_4"
)


args = parser.parse_args()

if args.i:
    go(args)

sys.exit(0)
