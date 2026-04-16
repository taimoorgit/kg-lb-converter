# kg-lb-converter

Minimal Python CLI for kilogram and pound conversions.

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
```

## Development

Install and lock the local environment:

```bash
uv sync
```
