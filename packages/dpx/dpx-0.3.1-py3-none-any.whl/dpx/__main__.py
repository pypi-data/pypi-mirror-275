import sys
import argparse
from .interactive import go
from .conf import load_conf


parser = argparse.ArgumentParser(prog="het", description="Hetzner REST Assistant")
parser.add_argument(
    "-i",
    action="store_true",
    help="Help for BLA_4"
)


args = parser.parse_args()
conf = load_conf(args)



if args.i:
    go(args, conf)

sys.exit(0)
