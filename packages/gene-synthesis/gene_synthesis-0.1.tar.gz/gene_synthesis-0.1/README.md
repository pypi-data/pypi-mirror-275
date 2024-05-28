### Gene synthesis design: A Pythonic approach
The script is used to produce the needed DNA fragments for merging into the full-length gene with PCR. All of the resultant DNA fragments have similar melting temperatures in the overlap regions, which is important for the successful assembly of target gene via PCR.

### 1. Installation
#### <font color=red> in macOS and in Windows </font>
(1) make sure you have installed Python 3.10.

(2) install the dependent packages with the following commands.
```zsh 
python3.10 -m pip install "biopython==1.79"
python3.10 -m pip install "matplotlib==3.6.3"
```

(3) install the program with the following command.
```zsh
python3.10 -m pip install gene_synthesis
```

### 2. Usage
#### 2.1 Run the script in terminal to get the needed DNA fragments for the synthesis of target gene with PCR
#### <font color=red> 2.1.1 macOS  </font>
During installation, the script gene_synthesis is copied to the PATH.
```zsh
 % which gene_synthesis
/Library/Frameworks/Python.framework/Versions/3.10/bin/gene_synthesis
```
The following steps show how to run the script.

(1) open terminal and cd to the Desktop with the following commands.
```zsh
% cd
% cd Desktop
```
(2) make a directory, for example, ‘gene_fragments’.
```zsh
% mkdir gene_fragments
```
(3) copy the target gene sequence file, for example, ‘beta_optimized.fasta’ (a test gene sequence that can be downloaded from the S3 directory of https://github.com/shiqiang-lin/gene-synthesis), which should be with fasta format, to the directory made in step (2). This step can be done with mouse drag and drop, or with terminal command cp. Please note that it is necessary to perform codon optimization to the target gene before running our script, which make it easier to get fragments with overlaps that have closer melting temperatures.

(4) cd to the directory made in step (2), with the following command.
```zsh
% cd gene_fragments
```
(5) run the following command. A figure showing the melting temperature of each DNA fragment will show up, and the DNA fragments are stored in a folder in the directory ‘gene_fragments’. 
```zsh
% gene_synthesis beta_optimized.fasta
```
#### <font color=red> 2.1.2 Windows  </font>
During installation, the script is copied to the PATH C:\python3.10.4\Scripts. You may cd to the directory to see if it is there. If not, you can search in 'My Computer' to find the directory where the script 'gene_synthesis' is.

The following steps show how to run the script.

(1) open terminal and cd to the Desktop with the following commands.
```zsh
> cd Desktop
```
(2) make a directory, for example, ‘gene_fragments’.
```zsh
> mkdir gene_fragments
```
(3) copy the target gene sequence file, for example, ‘beta_optimized.fasta’ (a test gene sequence that can be downloaded from the S3 directory of https://github.com/shiqiang-lin/gene-synthesis), which should be with fasta format, to the directory made in step (2). This step can be done with mouse drag and drop, or with terminal command copy. Please note that it is necessary to perform codon optimization to the target gene before running our script, which make it easier to get fragments with overlaps that have closer melting temperatures.

(4) cd to the directory made in step (2), with the following command.
```zsh
> cd gene_fragments
```
(5) run the following command. A figure showing the melting temperature of each DNA fragment will show up, and the DNA fragments are stored in a folder in the directory ‘gene_fragments’.
```zsh
> python3.10 C:\python3.10.4\Scripts\gene_synthesis beta_optimized.fasta
```
Please note that the 'C:\python3.10.4\Scripts\' is the directory in which the script gene_synthesis resides. If you install the Python 3.10. 4 elsewhere, you may need to change the above directory in the command accordingly.
#### 2.2 Use the function of the script
The function ‘get_overlap_by_Tm’ is used to get the optimal overlap sequence for the input DNA sequence. The input DNA sequence should be a string larger than 50. You also need to set a Tm value for searching the best overlap sequence from the 3’ of the DNA sequence.

An example is shown as follows.
```zsh
% python3.10
Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from gene_synthesis.lib import get_overlap_by_Tm
>>> gene_fragment = 'ATGCCCTTGGACAGTGTCAAAATGGACCACACGGTTAATCGGCGGAAGGCC'
>>> len(gene_fragment)
51
>>> Tm_set = 55
>>> get_overlap_by_Tm(gene_fragment,Tm_set)
('GGTTAATCGGCGGAAGGCC', 55.47568390601265, 0.4756839060126481)
```
The output is a tuple containing the overlap sequence, the melting temperature of the overlap sequence, and the distance between the melting temperature of the overlap sequence and Tm_set. The distance of the output overlap sequence is the smallest among all possible overlap sequences, according to which we define the optimal overlap sequence.

The minimal and maximal lengths of possible overlap sequences are set as min_overlap_len = 10 and max_overlap_len = 25, which should satisfy most cases of PCR merging of overlap DNA sequences. If you need to change the range, you may need to use the source code directly from the script in the S1 directory of https://github.com/shiqiang-lin/gene-synthesis.