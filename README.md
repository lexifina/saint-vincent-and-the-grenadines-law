# Saint Vincent and the Grenadines: law history in git


The law of Saint Vincent and the Grenadines as a git history: one file per section, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a section; picking a date gives the text in force that day. Each part here has one version so far, the text as made in 1979.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Saint Vincent and the Grenadines' national law, which global-law reads at `saint-vincent-and-the-grenadines/national/acts/`.

**What is in it now:** one law, the Saint Vincent Constitution Order 1979 (S.I. 1979/916), as made, in three parts with 121 provisions: the Constitution (Schedule 1: the preamble, sections 1 to 105 and its Schedule), the transitional provisions (Schedule 2, paragraphs 1 to 13) and the Order's own articles 1 to 3. [`data/laws.csv`](data/laws.csv) gives the Order's days; each folder's `README.md` lists its provisions.

Each part is a folder, one file per section or paragraph: `constitution/sec-010.md` is section 10 of the Constitution, protection of freedom of expression; `transitional/transitional-13.md` is transitional paragraph 13; `order/articles.md` holds the Order's three articles.

The text is in English, as the Order was made. legislation.gov.uk has it only as a scanned PDF, so it was read by Tesseract OCR (software, not a language model) and spot-checked against the scan, not proof-read word by word; small slips are possible, and the original governs.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to section 10 of the Constitution | `git log -p --word-diff -- constitution/sec-010.md` |
| Which law wrote each line of section 10? | `git blame constitution/sec-010.md` |
| Every version of the Constitution, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution ':!*/README.md'` |
| Section 10 as the record holds it on 1 January 2026 | `python tools/on.py 2026-01-01 constitution 10` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Vincentian law](https://global-law.lexifina.com/v1/try_claude?country=saint-vincent-and-the-grenadines)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=saint-vincent-and-the-grenadines)**: the same question in ChatGPT.
- **[Search Vincentian law on our site](https://lexifina.com/law?country=saint-vincent-and-the-grenadines&q=freedom+of+expression)**: a search for "freedom of expression", with each provision's text and its versions, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=freedom+of+expression&jurisdiction=saint-vincent-and-the-grenadines)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add saint-vincent-and-the-grenadines/national/acts
python3 tools/law.py show 2026-01-01 saint-vincent-and-the-grenadines/national/acts/constitution/sec-010.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/St_Vincent, on the day the version took effect, and carries it in its `In-force:` trailer; `Enacted:` gives the day the Order was made:

- all three parts are dated 27 October 1979, the day the Order came into operation (article 1(2)) and the Constitution took effect; the Order was made on 26 July 1979;
- since the text is the one made in 1979, that is the day the Constitution began; no amendment has a commit yet.

Every version is credited to the Order, `S.I. 1979/916 <si-1979-916@nationalarchives.invalid>` (an address that cannot exist); the committer is Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before and compares it with the corpus it was built from; it also checks that every commit's trailers parse, that there are no merge commits and that no date goes backwards or lies in the future. [`REPRODUCE.md`](REPRODUCE.md) does not yet record a run for this build, nor a second build.
- `REPRODUCE.md` gives the corpus's sha256 and the builder's hashes; [`data/versions.json`](data/versions.json) gives the source PDF's sha256.
- The OCR repairs made by hand (one line restored from the scan, a few obvious slips corrected) are listed in `REPRODUCE.md`.

## What it does not show

- **Amendments.** Only the Constitution as made. Later Acts of Parliament amending it are not on legislation.gov.uk and are not here, so the text may differ from the Constitution as it reads today, and any later date still gives the 1979 text.
- **The rest of Vincentian law.** No other Acts, no statutory rules and orders and no case law.
- **All of the Order as printed.** Its explanatory note and the scan's footnotes are left out; marginal notes are replaced by the section titles of the Order's own arrangement of sections.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [legislation.gov.uk](https://www.legislation.gov.uk/uksi/1979/916/made) (The National Archives) | UK official legislation site: S.I. 1979/916, as made | no, as made only, as a scanned PDF | Read by OCR; the Government's own site (legal.gov.vc) was unavailable when tried |

## Licence

See [`LICENSE`](LICENSE). The text contains public sector information licensed under the Open Government Licence v3.0; Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the public domain under CC0 1.0.

No AI model wrote, translated or corrected legal text, and no model runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
