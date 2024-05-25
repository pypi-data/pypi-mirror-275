# yoli

A simply cli app that indexes videos using YOLOv10.

> [!WARNING]
> This is a work in progress. The code is not yet stable and just a quick sketch of an AI powered cli video indexer.

## Installation

```bash
pip install yoli
```

## Usage

```bash
yoli --help
```

# Video Indexing

```bash
yoli vindex data/city.mp4
Video file is valid: data/city.mp4
Processing frames: 100%|█████████████████████████████████████████████████████████████████| 275/275 [00:26<00:00, 10.45it/s]
Results saved to data/city.mp4.pt
```

# Most Common Objects

```bash
yoli common data/city.mp4.pt
car: 2364
person: 47
truck: 42
traffic light: 39
clock: 6
```

# Where and When an Object Appears

```bash
yoli where data/city.mp4.pt person
person appears between frames 0 and 40
```

## Development

some helpful commands for development

```bash
uv venv
source .venv/bin/activate
poetry build
poetry install
```
