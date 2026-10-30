import sys
sys.path.insert(0, r'~/Documents/lexifina/scripts/world-law')
from p3lib import write_docs
rows = [('constitution', 'The Constitution of Saint Vincent and the Grenadines (Schedule 1 to S.I. 1979/916): preamble, sections 1 to 105 and the Schedule', 1, 'As made, in force 27 October 1979'),
        ('transitional', 'Transitional provisions (Schedule 2 to S.I. 1979/916), paragraphs 1 to 13', 1, 'As made, in force 27 October 1979'),
        ('order', 'The Saint Vincent Constitution Order 1979, articles 1 to 3', 1, 'As made, in force 27 October 1979')]
holds = """The Constitution of Saint Vincent and the Grenadines as made by the Saint Vincent Constitution Order 1979 (S.I. 1979/916), with the Order's own articles and its transitional provisions. English, the original language of the Order.

**The text was read by OCR.** legislation.gov.uk publishes the Order, as made, only as a scanned image PDF with no text layer, so the text here was read from the scan by Tesseract OCR (software, not a language model), with headers, marginal notes and footnotes removed. It was spot-checked against the scan but not proof-read word by word, so small slips are possible. One line the OCR missed (the opening of transitional provision 13) was restored by hand from the scan. The original governs."""
source = """The National Archives, legislation.gov.uk: The Saint Vincent Constitution Order 1979 (S.I. 1979/916), as made (https://www.legislation.gov.uk/uksi/1979/916/made), image PDF retrieved 30 October 2026. Contains public sector information licensed under the Open Government Licence v3.0. The Government of Saint Vincent and the Grenadines' own site (legal.gov.vc) was unavailable when we tried it, so this UK copy is the source of the text."""
dates = """Every version is dated **27 October 1979**, the day the Order came into operation (article 1(2)) and the Constitution took effect. The Order was made on 26 July 1979 and the commits are credited to it (`si-1979-916`)."""
limits = """- Only the Constitution as made. Later amendments by Acts of the Parliament of Saint Vincent and the Grenadines are not on legislation.gov.uk and are not in this record, so the text may differ from the Constitution as it reads today.
- The Order's explanatory note and the footnotes of the scan are left out; marginal notes are replaced by the section titles of the Order's own arrangement of sections.
- OCR limits as described above."""
lic = """The legal text is the Saint Vincent Constitution Order 1979 (S.I. 1979/916), as made, from legislation.gov.uk (The National Archives), read from the scanned PDF by OCR.

Contains public sector information licensed under the Open Government Licence v3.0 (https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)."""
write_docs(r'~/Documents/lexifina/scripts/saint-vincent-and-the-grenadines-law', 'saint-vincent-and-the-grenadines', 'VC', 'Saint Vincent and the Grenadines', rows, holds, source, dates, limits, lic, 'nationalarchives')
