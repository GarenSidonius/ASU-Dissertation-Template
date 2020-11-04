# `latexmk` docker action

This action runs [latexmk](https://personal.psu.edu/~jcc8/software/latexmk/)
against a source PDF with the following options:

    -f -cd -interaction=batchmode -pdf

## Inputs

### `engine`

LaTeX engine to use; this value should be written as the corresponding
`latexmk` option and is typically blank (for pdfTeX) or "-xelatex" (for XeTeX)

### `source`

**Required** The TeX filename to send to `latexmk`

## Outputs

None

## Example usage

    uses: actions/latexmk@v1
    with:
      engine: '-xelatex'
      source: 'dissertation.tex'

This usage would run the following command:

    perl latexmk.pl -f -cd -interaction=batchmode -pdf -xelatex dissertation.tex
