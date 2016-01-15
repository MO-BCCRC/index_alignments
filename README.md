#index_alignments : Bam file indexing using Samtools


```
Development information

date created : July 25 2014
last update  : July 25  2014
Developer    : Rad Aniba (raniba@bccrc.ca)
Input        : Sorted Bam file
Output       : Bam file index (.bai file)
Seed used    : Samtools

```


###Usage
This component should be used generally after sorting a bam file, Index sorted alignment for fast random access. Index file aln.bam.bai will be created.

###Dependencies

- python
- samtools


###Example

The behaviour of this components is equivalent to this command :

`samtools index alignment.sorted.bam`

> You need to sort the alignment first, use *sort_alignments component before using this one 


###Known issues



###Last updates



### test data
Reference : /genesis/extscratch/shahlab/raniba/Software/bowtie2/genomes/GRCh37-lite   
seq1 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R1_001.fastq 
seq2 : /extscratch/shahlab/raniba/Tasks/test_data/SA495-Normal_S8_L001_R2_001.fastq  
outfile : test.bam   

bowtie2 path : /genesis/extscratch/shahlab/raniba/Software/bowtie2/  
samtools path : /extscratch/shahlab/raniba/pipelines/miseq_pipeline/miseq_analysis_pipeline/miseq-pipeline/software/samtools-0.1.19/samtools 


