from waflib import TaskGen, Task

def configure(conf):
    conf.load('tex')
    if not conf.env.PDFLATEX:
        conf.fatal('pdflatex is required')
    conf.find_program('pandoc')

@TaskGen.extension('.pd')
def process_pandoc(self, node):
    bib = getattr(self, 'bibliography', None)
    if bib:
        bib = self.to_nodes(bib)
        bib_str = "--natbib --bibliography={0}".format(bib[0].path_from(self.bld.bldnode))
    else:
        bib = []
        bib_str = ""
    out_source = node.change_ext('.latex', '.pd')
    Task.task_factory('pandoc',
        '${PANDOC} -S -o ${TGT} ${tsk.bib_str} ${SRC[0].abspath()}',
        shell        = False,
        ext_in       = '.pd', 
        ext_out      = '.latex', 
    )
    tsk = self.create_task('pandoc', [node] + bib, out_source)
    tsk.bib_str = bib_str

def build(bld):
    bld(source='Introduction.pd Index.pd Search.pd Infrastructure.pd Conclusion.pd', bibliography='bib.bib')

    bld.add_group()

    bld(
        features = 'tex',
        type     = 'pdflatex',
        source   = 'main.latex',
        target   = 'main.pdf',
       )
