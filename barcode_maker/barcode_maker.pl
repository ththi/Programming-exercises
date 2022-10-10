#!/usr/bin/perl

use strict;
use warnings;
use List::Util qw(shuffle); 

#####
### script by Thorsten Thiergart, July, 24th, 2022
#####

#####
### script will give a list with x DNA sequences (6 letters) that differ in at least 3 positions
#####

my($i,$ii,$iii,@letters,$dump_seq,@numbers,$pos,@all_seqs,$random,@seq_list,%seqs,$go,$test_seq,$diff,@bc1,@bc2,$key,$entry,$key2,%diff_counts,$num_seqs);


# give possible letters

@letters=("A","C","G","T");


# how many sequences?

$num_seqs=96;


# loop throught all combinations, using numbers as mock-set

for($i=111111;$i<=444444;$i++){

	# since we have only four letters, skip the useless numbers
	if($i=~/5|6|7|8|9|0/){next}
	
	@numbers=split(//,$i);
	$dump_seq="";
	
	# substitute numbers through letters
	
	for$pos(@numbers){
		$dump_seq=$dump_seq."".$letters[$pos-1];
	}
	push @all_seqs,$dump_seq;

		
}


# repeat loop until desired number of sequences is found

for(;;){
	
	# randomize array, important, since variation between loops is only based on this step. 	

	@all_seqs=shuffle(@all_seqs);


	for($i=1;$i<=$num_seqs;$i++){

		# ask if sequences already exists, if not loop through list with all sequences.
	
		if(! keys(%seqs) ){
			$random=int(rand(4095));
			$seqs{$i}=$all_seqs[$random];
			push @seq_list,$seqs{$i};
		}else{
			for$entry(@all_seqs){
				$go=1;
						
				$test_seq=$entry;
		
	
				# loop through all existing sequences so far
	
				for($ii=1;$ii<$i;$ii++){
		
		
					$diff=0;
					@bc1=split(//,$seqs{$ii});
					@bc2=split(//,$test_seq);
			
					# loop through characters and count differences
			
					for($iii=0;$iii<@bc1;$iii++){
									
						if($bc1[$iii] ne $bc2[$iii]){$diff++}
					}
			
			
					# if there are not enough differences, end loop and check next sequence
			
					if($diff <=2){
						$go=0;
						last;
					}
			
					# keep distances for matrix 
			
					$diff_counts{$i}{$ii}=$diff;
					$diff_counts{$ii}{$i}=$diff;
			
				}
				if($go==1){last;}
		
			}
			
		
			if($go==1){
				$seqs{$i}=$test_seq;
				push @seq_list,$test_seq;
			}
		
		}
	
	
	}

	if(scalar(@seq_list)==$num_seqs){last}
	else{
		undef(@seq_list);
		undef(%seqs);
		undef(%diff_counts);
	}
}


# open output files

open(out1,">seq_list_from_perl.txt");
open(out2,">dist_matrix_from_perl.txt");


# print list

print out1 join("\n",@seq_list);

# print header line, and then the complete matrix 

print out2 join("\t",@seq_list),"\n";

for$key(sort {$a <=> $b} keys %seqs){

	print out2 "$seqs{$key}";
	
	for$key2(sort {$a <=> $b} keys %seqs){
		
			if($key eq $key2){
				print out2 "\t0";
			}else{
				print out2 "\t$diff_counts{$key}{$key2}";
			}
	}
	
	print out2 "\n";

}
