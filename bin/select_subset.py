import xarray as xr
import argparse
from pathlib import Path



def main():
    parser = argparse.ArgumentParser(prog='select_subset.py', description="Select a subset of stations from a set of intensity measures, or waveforms")
    parser.add_argument('dataset', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('-p', '--pattern', default=r'^\w{3,4}$')
    args = parser.parse_args()
    with xr.open_dataset(args.dataset, engine='h5netcdf') as dset:
        selected_dset = dset.sel(station=dset.station.str.match(args.pattern))
        selected_dset.to_netcdf(args.output, engine='h5netcdf')

        
if __name__ == '__main__':
    main()
