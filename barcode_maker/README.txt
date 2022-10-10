

Within the folder you can find :

- A perl script (“barcode_maker.pl”). You can run the script on the commandline using: $ perl barcode_maker.pl . You might need to make it accessible by using chmod. (e.g. $ chmod 755 barcode_maker.pl). If you want to run the script with a smaller number of sequences you need to change the number in line 25 accordingly. The script might run some minutes, but will only stop if the desired amount of sequences are found.



- In addition you find example output files with 96 output sequences and the respective distance matrices. You might want to check those, and maybe run the script with <90 output sequences, since this reduces the time needed dramatically.

####

Note: the Perl script creates all possible combinations for the six letter code and then randomly pick sequences until it found the desired amount. This avoids creating the same sequence twice. 