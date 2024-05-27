```
┏┓┓ ┏┓┏┓┏┓┳┓┳┓┏┓┳┓ 
┣┫┃ ┣┫┃ ┃┃┣┫┃┃┣ ┣┫ 
┛┗┗┛┛┗┗┛┗┛┛┗┻┛┗┛┛┗ 
(c) 2023 Sam Robson
```
# **Alacorder**
### Alacorder collects and processes case detail PDFs into data tables suitable for research purposes.

<sup>[GitHub](https://github.com/sbrobson959/alacorder)  | [PyPI](https://pypi.org/project/alacorder/)     | [Report an issue](mailto:sbrobson@crimson.ua.edu)
</sup>

## **Installation**

**If your device can run Python 3.10+, it can run Alacorder. Use `pip` to install the command line interface.**

* Install [Anaconda Distribution](https://www.anaconda.com/products/distribution) to install the latest Python.
* Once your Anaconda environment is configured, open a terminal from Anaconda Navigator and enter `pip install -U alacorder` to install.

```

 Usage: alacorder [OPTIONS] COMMAND [ARGS]...

 Alacorder collects case detail PDFs from Alacourt.com and processes them into
 data tables suitable for research purposes.

╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --version          Show the version and exit.                                │
│ --help             Show this message and exit.                               │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ autofilter      Automatically filter `party_search_results` using crawl-adoc │
│                 outputs, so that cases with mismatching DOBs are removed.    │
│ autopair        Automatically generate filled pairs template from party      │
│                 search results table with 'Search' and 'Name' columns.       │
│ crawl-adoc      Collect full inmates list from ADOC Inmate Search and write  │
│                 to table at `output_path` (.xlsx, .csv, .json, .parquet).    │
│ fetch-cases     From a queue table with 'Case Number' or 'CaseNumber'        │
│                 column, download case detail PDFs to directory at            │
│                 `output_path`.                                               │
│ launch          Launch textual user interface.                               │
│ make-archive    Create case text archive from directory of case detail PDFs. │
│ make-documents  Make .docx summaries with voting rights information for each │
│                 unique identifier in `pairs` at `output_dir`.                │
│ make-summary    Create voting rights summary grouped by person using a       │
│                 completed name/AIS pairing template (use make-template to    │
│                 create empty template).                                      │
│ make-table      Create table at `output_path` from archive or directory at   │
│                 `input_path`.                                                │
│ make-template   Create empty pairing template to be used as input for        │
│                 make-summary to create a voting rights summary grouped by    │
│                 person instead of by case.                                   │
│ party-search    Collect results from Alacourt Party Search into a table at   │
│                 `output_path`. Input `queue_path` table from .xlsx, .csv,    │
│                 .json, or .parquet with columns corresponding to Alacourt    │
│                 Party Search fields: 'Name', 'Party Type', 'SSN', 'DOB',     │
│                 'County', 'Division', 'Case Year', 'Filed Before', 'Filed    │
│                 After', 'No Records'.                                        │
│ rename-cases    Rename all cases in a directory to full case number.         │
│                 Duplicates will be removed.                                  │
│ search-adoc     Search ADOC using queue with 'First Name', 'Last Name', and  │
│                 'AIS' columns to retrieve sentencing information from ADOC.  │
│                 Record table to `output_path`.                               │
╰──────────────────────────────────────────────────────────────────────────────╯

```