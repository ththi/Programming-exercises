#!/usr/bin/perl
use strict;
use warnings;

my(%from_node,%to_node,%edges,$key,@root_nodes,$key2,@sorted,$cou,$curr_node,%edges_fix,$node,%length_to);

#####
### first part: reading the Dag and keep track of edges and nodes
#####

open(in1,"test_dag.txt");

while(<in1>){
	chomp;
	if(/\#/){next}
	@_=split(/\s+/);
	
	#
	# save all nodes, either from or to, and count appearance
	# in addition keep all edges (from , to and weight)
	#
	
	$from_node{$_[0]}++;
	$to_node{$_[1]}++;
	$edges_fix{$_[0]}{$_[1]}=$_[2];
	$edges{$_[0]}{$_[1]}=$_[2];	

}

#
# identify root node(s) (has no edges incoming, therefore missing from $to_node)
#

for$key(keys %from_node){

	if(!exists $to_node{$key}){push @root_nodes,$key;}

}




#####
### second part: do topological sorting (least to max incoming edges)
#####

$cou=-1;

while(@root_nodes){
	$cou++;
	$curr_node=$root_nodes[$cou];	
	
	push @sorted,$curr_node;
	
	for$key2(keys %{$edges{$curr_node}}){
	
		#print "\t$key2 $edges{$curr_node}{$key2}\n";
		
		delete($edges{$curr_node}{$key2});
		
		if($to_node{$key2} ==1){ 
			push @root_nodes,$key2;	
		}
		$to_node{$key2}=$to_node{$key2}-1;
	
	}
	delete($root_nodes[$cou]);
	
}

print "Topological order: @sorted\n";

#####
### third part: looking for highest scoring path
#####

#
# initialize zero lengths
#

for$node(@sorted){
	$length_to{$node}=0;
}


#
# loop through top order, then examine all following nodes, keep highest incoming weight and sum up with previous weights
#

for$node(@sorted){

	#print "$node\n";

	for$key2(keys %{$edges_fix{$node}}){
		#print "\t$key2 $edges_fix{$node}{$key2}\n";
		
		if( $length_to{$key2} <=  $edges_fix{$node}{$key2} + $length_to{$node}){
			$length_to{$key2} =  $edges_fix{$node}{$key2} + $length_to{$node}
		}	
		
	}

}

#
# sort all nodes by total weight of edges leading to them, returning the highest scoring 
#

for$key(sort {$length_to{$b} <=> $length_to{$a}} keys %length_to){

	print "Max sum of weights path is: $length_to{$key}\n";
	
	last;

}