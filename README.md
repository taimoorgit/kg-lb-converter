# kg-lb-converter

Minimal Python CLI for common metric and imperial conversions.

This is a standard `uv` project with a console entry point named `converter`.

## Usage

Run the CLI with `uv`:

```bash
uv run converter 30
```

In restricted environments like this sandbox, point `uv` at a local cache directory:

```bash
UV_CACHE_DIR=.uv-cache uv run converter 30
```

You can also run the module directly:

```bash
uv run python -m kg_lb_converter 30
```

Example output:

```text
30 kg = 66.14 lb
30 lb = 13.61 kg

30 g = 1.06 oz
30 oz = 850.49 g

30 mg = 0.001058 oz
30 oz = 850485.69 mg

30 mL = 1.01 fl oz
30 fl oz = 887.21 mL

30 L = 7.93 gal
30 gal = 113.56 L

30 ng/dL = 1.04 nmol/L
30 nmol/L = 865.20 ng/dL

30 km = 18.64 mi
30 mi = 48.28 km

30 m = 98.43 ft
30 ft = 9.14 m

30 cm = 11.81 in
30 in = 76.20 cm

30 C = 86.00 F
30 F = -1.11 C
```

## Development

Install and lock the local environment:

```bash
uv sync
```
