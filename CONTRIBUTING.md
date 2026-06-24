# Contributing to the Mobile Phone Data Manual

Thank you for helping improve *Design and Implementation of Mobile Phone Data Initiatives: A Practical Manual*. Contributions are welcome from technical contributors, policy specialists, data governance experts, practitioners, editors, and readers who notice something that should be corrected or clarified.

This repository supports two contribution routes:

- **GitHub contributors:** Use GitHub issues or pull requests when you are comfortable working in GitHub. See [docs/contributing-with-github.qmd](docs/contributing-with-github.qmd) or the [PDF version](docs/contributing-with-github.pdf).
- **Non-GitHub contributors:** Send structured feedback by email, shared document, annotated PDF, or meeting notes when GitHub is not practical. See [docs/contributing-without-github.qmd](docs/contributing-without-github.qmd) or the [PDF version](docs/contributing-without-github.pdf).

Both routes are equally valuable. The main requirement is that suggestions are specific enough for maintainers to review, discuss, and incorporate.

## What to Contribute

Useful contributions include:

- corrections to wording, definitions, references, links, tables, or figures;
- specialist comments on mobile phone data methods, policy use cases, partnerships, legal frameworks, safeguards, quality assurance, or communications;
- proposed examples, case studies, definitions, or practical checklists;
- comments on structure, readability, accessibility, or navigation;
- suggestions for updated references or companion resources.

## What to Include

For each suggestion, please include:

- the chapter, section, page URL, heading, or file name;
- the current text or object that should change;
- the proposed replacement text, if you have one;
- the reason for the change;
- supporting evidence, references, or practical experience where relevant;
- any constraints, uncertainty, or permissions that maintainers should know about.

Create separate suggestions for unrelated topics. This makes review easier and reduces the risk that a useful correction is delayed by a larger discussion.

## Content and Permission Checks

Please do not submit confidential, proprietary, restricted, or personally identifiable information. Examples involving mobile phone data should be public, aggregated, anonymised, synthetic, or clearly approved for open publication.

By contributing text, examples, or other material, you confirm that you have the right to share it and that it can be included in the manual under the repository licence unless a different permission statement is agreed in advance. The manual text is licensed under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0), except where otherwise noted.

## Review Process

Maintainers review contributions for accuracy, relevance, clarity, consistency with the manual, permissions, and publication readiness. They may edit accepted contributions for style, structure, terminology, or length. Substantive changes may require discussion with the contributor or wider task team before they are merged.

For larger contributions, maintainers may first ask for a short outline or a focused review note before drafting final text.

## Local Preview for Repository Contributors

If you are editing the repository locally, preview the manual with:

```bash
quarto preview
```

Render all outputs with:

```bash
bash scripts/render_book.sh
```

For small documentation changes, a targeted Quarto render of the edited file is usually enough before opening a pull request.
