import requests
from model.barcode import SpotifyBarcode


def from_uri(uri: str) -> SpotifyBarcode:
    response = requests.get('https://scannables.scdn.co/uri/plain/svg/000000/white/1080/' + uri)
    if response.status_code != 200:
        raise RuntimeError("Your URI could not be fetched")

    result_code = SpotifyBarcode()

    for index, line in enumerate(response.text.splitlines()):
        if index == 1 or not line.startswith("<rect"):
            continue

        for params in [param for param in line.split(' ') if param.startswith('height')]:
            result_code.bars.append(int(int(float(params[len('height="'):-1]) - 11) / 7))

    return result_code
