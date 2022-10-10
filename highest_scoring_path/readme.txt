
-The exercise was solved using a PERL script (path_dag.pl). It does not have any dependencies, except PERL, what should be available on most UNIX systems

-The script need a .txt file named “test_dag.txt” that is providing a directed weighted graph. There need to be three columns (either tab or space separated).The layout need to be as followed: Column 1= Outgoing Node Name, Column 2 = receiving Node Name, Column3 = Edge Weight

-After making the script executable (e.g. chmod 755 path_dag.pl) it can be called on the commandline via “perl path_dag.pl”

-Output is: 1, the topological order of the nodes and 2, the sum of the weights of the highest scoring path