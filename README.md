[![CI](https://github.com/jbelew/translate-missing/actions/workflows/ci.yml/badge.svg)](https://github.com/jbelew/translate-missing/actions/workflows/ci.yml)

# 🌐 translate-missing

Keep your i18next translation files clean, complete, and up to date.  **translate-missing** scans your localization folders, finds missing keys, removes obsolete ones, and uses Google Translate to automatically fill in gaps — keeping your translations synchronized with your source language.

## Installation

```bash
pip install translate-missing
```

## Usage

Basic usage:
```bash
translate-missing --master-lang en --locales-dir path/to/locales
```

Using an optional marker for automated translations:
```bash
translate-missing --master-lang en --locales-dir path/to/locales --marker "GT"
```

To see what changes would be made without actually writing them to files, use the `--dry-run` option:
```bash
translate-missing --master-lang en --locales-dir path/to/locales --dry-run
```

## Example

Let's say you have the following translation files:

**en/translation.json**
```json
{
  "hello": "Hello",
  "world": "World"
}
```

**es/translation.json**
```json
{
  "hello": "Hola"
}
```

Running the tool with a marker:
```bash
translate-missing --master-lang en --locales-dir . --marker "GT"
```

The `es/translation.json` file will be updated to:
```json
{
  "hello": "Hola",
  "world": "[GT] Mundo"
}
```

## Contributing

This project uses [semantic-release](https://github.com/semantic-release/semantic-release) for versioning and releases. Please follow the [Conventional Commits specification](https://www.conventionalcommits.org/) for your commit messages.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
