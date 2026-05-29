#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

PDF="Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.pdf"
EPUB="Design-and-Implementation-of-Mobile-Phone-Data-Initiatives.epub"
TMP_DIR="$(mktemp -d)"
BUILD_DIR="$TMP_DIR/source"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

mkdir -p "$BUILD_DIR"
cd "$ROOT"
tar   --exclude=".git"   --exclude=".quarto"   --exclude="_book"   --exclude=".DS_Store"   --exclude="index.aux"   --exclude="index.log"   --exclude="index.pdf"   --exclude="index.tex"   --exclude="index.toc"   -cf - . | tar -xf - -C "$BUILD_DIR"

cd "$BUILD_DIR"

quarto render --to pdf
cp "_book/$PDF" "$TMP_DIR/$PDF"

quarto render --to epub
cp "_book/$EPUB" "$TMP_DIR/$EPUB"

quarto render --to html
cp "$TMP_DIR/$PDF" "_book/$PDF"
cp "$TMP_DIR/$EPUB" "_book/$EPUB"

mkdir -p "$ROOT/_book"
cp -R "_book/." "$ROOT/_book/"
