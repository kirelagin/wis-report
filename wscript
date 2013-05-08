from waflib import TaskGen

def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal('pdflatex is required')
    conf.find_program('pandoc')

TaskGen.declare_chain(
    name         = 'pandoc', 
    rule         = '${PANDOC} -S -o ${TGT} --bibliography=../bib.bib --natbib ${SRC}', 
    shell        = False,
    ext_in       = '.pd', 
    ext_out      = '.latex', 
    reentrant    = False,
    install_path = False, 
)

def build(bld):
    bld(source='Introduction.pd Index.pd Search.pd Conclusion.pd')

    bld.add_group()

    bld(
        features = 'tex',
        type     = 'pdflatex',
        source   = 'main.latex',
        target   = 'main.pdf',
       )
