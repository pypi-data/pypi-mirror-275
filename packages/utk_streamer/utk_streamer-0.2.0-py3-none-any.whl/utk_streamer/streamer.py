import click
from utk_streamer.download import StreamerDownload
from utk_streamer.convert import TTAFConverter
from csv import DictReader
from tqdm import tqdm
import os


@click.group()
def cli() -> None:
    pass

@cli.command("download", help="Download multiple files from a Spreadsheet")
@click.option(
    "--csv",
    "-c",
    required=True,
    help="Path to CSV to generate XML from",
)
@click.option(
    "--output",
    "-o",
    default="output",
    help="Destination directory to write files to",
)
@click.option(
    "--start",
    "-s",
    help="First file to download",
)
@click.option(
    "--end",
    "-e",
    help="Last file to download",
)
def download(
    csv: str,
    output: str,
    start: int,
    end: int,
) -> None:
    with open(csv, "r") as file:
        start = int(start) - 1
        reader = DictReader(file)
        rows = [row.get("paths_if_exists") for row in reader if row.get("paths_if_exists") is not ""]
        all_files = []
        for row in rows:
            in_row  = row.split(" | ")
            for file in in_row:
                all_files.append(file)
        print(f"Downloading files {start} to {end} to {output}.")
        for row in tqdm(all_files[int(start):int(end)]):
            StreamerDownload(row, output).download()
    return

@cli.command("get_captions", help="Download captions")
@click.option(
    "--captions_sheet",
    "-c",
    required=True,
    help="Path to text file with captions",
)
def get_captions(
    captions_sheet: str,
) -> None:
    with open(captions_sheet, "r") as file:
        captions = file.readlines()
        for caption in tqdm(captions):
            path = f"http://streamer-migration.lib.utk.edu/files/catstream/{caption.replace('./', '').strip()}"
            StreamerDownload(path, "captions").download()
    return

@cli.command("convert", help="Convert TTAF to VTT")
@click.option(
    "--path",
    "-p",
    required=True,
    help="Path to TTAFS",
)
def convert(
    path: str
) -> None:
    print(f"Converting TTAFS to VTT at {path}")
    for path_on_disk, directories, files in os.walk(path):
        for file in tqdm(files):
            x = TTAFConverter(f"{path}/{file}")
            x.write_vtt()