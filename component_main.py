'''
Created on July 25, 2014
Last update July 25, 2014
@author: raniba
'''

import os

from kronos.utils import ComponentAbstract


class Component(ComponentAbstract):

    '''
    Index a bam file using samtools
    '''
    def __init__(self, component_name='index_alignments', component_parent_dir=None, seed_dir=None):
       self.version = "0.0.1"

        ## initialize ComponentAbstract
       super(Component, self).__init__(component_name, component_parent_dir, seed_dir)

    def make_cmd(self, chunk=None):
        '''
        Index a bam file alignment
        '''

        sorted_bam = self.args.sorted_bam

        cmd = self.requirements['samtools']

        cmd_args = [
            'index',
            sorted_bam,
        ]

        return cmd, cmd_args


# to run as stand alone
def _main():
    '''main function'''
    index_alignments = Component()
    index_alignments.args = component_ui.args
    index_alignments.run()

if __name__ == '__main__':

    import component_ui

    _main()
