# Saint Vincent and the Grenadines: law history in git

The law of Saint Vincent and the Grenadines as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

The Constitution of Saint Vincent and the Grenadines as made by the Saint Vincent Constitution Order 1979 (S.I. 1979/916), with the Order's own articles and its transitional provisions. English, the original language of the Order.

**The text was read by OCR.** legislation.gov.uk publishes the Order, as made, only as a scanned image PDF with no text layer, so the text here was read from the scan by Tesseract OCR (software, not a language model), with headers, marginal notes and footnotes removed. It was spot-checked against the scan but not proof-read word by word, so small slips are possible. One line the OCR missed (the opening of transitional provision 13) was restored by hand from the scan. The original governs.

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | The Constitution of Saint Vincent and the Grenadines (Schedule 1 to S.I. 1979/916): preamble, sections 1 to 105 and the Schedule | 1 | As made, in force 27 October 1979 |
| `transitional/` | Transitional provisions (Schedule 2 to S.I. 1979/916), paragraphs 1 to 13 | 1 | As made, in force 27 October 1979 |
| `order/` | The Saint Vincent Constitution Order 1979, articles 1 to 3 | 1 | As made, in force 27 October 1979 |

## Source

The National Archives, legislation.gov.uk: The Saint Vincent Constitution Order 1979 (S.I. 1979/916), as made (https://www.legislation.gov.uk/uksi/1979/916/made), image PDF retrieved 30 October 2026. Contains public sector information licensed under the Open Government Licence v3.0. The Government of Saint Vincent and the Grenadines' own site (legal.gov.vc) was unavailable when we tried it, so this UK copy is the source of the text.

## Dates

Every version is dated **27 October 1979**, the day the Order came into operation (article 1(2)) and the Constitution took effect. The Order was made on 26 July 1979 and the commits are credited to it (`si-1979-916`).

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law (or, for facts, the retrieval) that made the change, with an e-mail address that cannot exist (`<law key>@nationalarchives.invalid`). The committer is always Lexifina.

## Limits

- Only the Constitution as made. Later amendments by Acts of the Parliament of Saint Vincent and the Grenadines are not on legislation.gov.uk and are not in this record, so the text may differ from the Constitution as it reads today.
- The Order's explanatory note and the footnotes of the scan are left out; marginal notes are replaced by the section titles of the Order's own arrangement of sections.
- OCR limits as described above.
