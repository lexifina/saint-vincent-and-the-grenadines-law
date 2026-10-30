# How this repository was made (Saint Vincent and the Grenadines)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| legislation.gov.uk: The Saint Vincent Constitution Order 1979 (S.I. 1979/916), as made | <https://www.legislation.gov.uk/uksi/1979/916/made> | 2026-10-30 | Open Government Licence v3.0 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | The Constitution of Saint Vincent and the Grenadines (Schedule 1 to the Saint Vincent Constitution Order 1979) | 1 | 1979-10-27 to 1979-10-27 |
| `transitional` | Transitional provisions (Schedule 2 to the Saint Vincent Constitution Order 1979) | 1 | 1979-10-27 to 1979-10-27 |
| `order` | The Saint Vincent Constitution Order 1979 (the Order itself, articles 1 to 3) | 1 | 1979-10-27 to 1979-10-27 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/St_Vincent) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Order itself (art. 1(2)) came into operation on 27 October 1979, the day the Constitution took effect. https://www.legislation.gov.uk/uksi/1979/916/made

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `090e3ed62b4a1e4e47ebc1a2756cb05afab5b1c52777fd4b2932103099f5a199` (225470 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Order (S.I. 1979/916) was made on 26 July 1979 and came into operation on 27 October 1979 (art. 1(2)); every version is dated 1979-10-27, the day the Constitution took effect.
- The as-made Order exists on legislation.gov.uk only as a scanned image PDF (no text layer, no XML body). The text was read by Tesseract 5.4 OCR at 300 dpi (English), page by page, with word positions used to drop running headers and the marginal notes.
- The OCR text was not proof-read word by word; spot-checks against the scan found it faithful but residual errors (for example a stray footnote or a garbled letter) are possible. The original governs.
- Section titles come from the Order's own arrangement of sections; OCR repaired only the paragraph letters (b) misread as (5) or (6) between (a) and (c), line-end hyphenation, and quotation marks (normalised to straight quotes).
- One line the OCR dropped ("13.-(1) In this Schedule-", transitional provision 13) was restored by hand from the scan; a few obvious OCR slips were corrected by hand (No property in s. 6(1), (ii) in s. 44(a)).
- The Constitution has no later versions in this record: amendments (by Acts of Parliament of Saint Vincent and the Grenadines) are not on legislation.gov.uk. The explanatory note and the footnotes of the Order are not included.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- No model wrote or changed legal text. Tesseract OCR (software, not a language model) produced the text; counts: 78 pages, 105 sections, 13 transitional provisions.
