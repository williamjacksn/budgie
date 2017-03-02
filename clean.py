import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()

folder = pathlib.Path(args.path)
for p in folder.iterdir():
    if p.suffix == '.pdf':
        orig_name = p.name
        new_name = '{}-{}-{}.pdf'.format(orig_name[:4], orig_name[4:6], orig_name[6:8])
        p.rename(p.with_name(new_name))
