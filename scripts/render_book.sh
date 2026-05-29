#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PDF="Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.pdf"
EPUB="Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.epub"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

quarto render --to pdf
cp "_book/$PDF" "$TMP_DIR/$PDF"

quarto render --to epub
cp "_book/$EPUB" "$TMP_DIR/$EPUB"

quarto render --to html
cp "$TMP_DIR/$PDF" "_book/$PDF"
cp "$TMP_DIR/$EPUB" "_book/$EPUB"
