# Streamer Download

Tool to easily download multiple files from streamer.

## Installation

Easiest way to install is to use `pipx`:

```shell
pipx install utk-streamer
```

## Usage

To use, download the streamer file as a CSV and specify the range of files you want to download.

Because multiple files can exist in a row, this doesn't align to rows but the range of files to download.

For instance, to download the first 10 files and your csv is called `example.csv`:

```shell

streamer download -c example.csv -o output -s 1 -e 10
```

To convert TTAFS to VTTS, use:

```shell

streamer convert -p /path/to/ttafs 
```