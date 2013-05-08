def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal('pdflatex is required')
    conf.find_program('pandoc')


def build(bld):
    PANDOC_RULE = '${PANDOC} -S -o ${TGT} --bibliography=../bib.bib --natbib ${SRC}'

    bld(
        rule   = PANDOC_RULE,
        source = 'Introduction.pd',
        target = 'Introduction.latex',
    )
    bld(
        rule   = PANDOC_RULE,
        source = 'Index.pd',
        target = 'Index.latex',
    )
    bld(
        rule   = PANDOC_RULE,
        source = 'Search.pd',
        target = 'Search.latex',
    )
    bld(
        rule   = PANDOC_RULE,
        source = 'Conclusion.pd',
        target = 'Conclusion.latex',
    )

    bld.add_group()

    bld(
        features = 'tex',
        type     = 'pdflatex',
        source   = 'main.latex',
        target   = 'main.pdf',
       )
