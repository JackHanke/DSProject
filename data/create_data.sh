unzip gene+expression+cancer+rna+seq.zip
tar -xvzf TCGA-PANCAN-HiSeq-801x20531.tar.gz
rm TCGA-PANCAN-HiSeq-801x20531.tar.gz
mv TCGA-PANCAN-HiSeq-801x20531/* .
rmdir TCGA-PANCAN-HiSeq-801x20531
python3 reformat.py
# kinda scary
rm data.csv labels.csv