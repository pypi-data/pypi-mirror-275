# react-i18next-lint

A small lint tool for [react-i18next][18n].

[18n]: https://react.i18next.com/

## Install

```bash
poetry install
```

## Execution

### Extract phrase keys from i18n directory

```bash
poetry run react_i18next_lint extract-keys [i18n resources dir] > resources.tsv
```

### Group phrase key and aggregate locales

```bash
poetry run react_i18next_lint group-key-locales resources.tsv by-locales.tsv
```

### Validate against source code files

```bash
poetry run react_i18next_lint validate-keys by-locales.tsv [source code files]
```

## Development

### Running pytest

```bash
poetry run pytest
```
