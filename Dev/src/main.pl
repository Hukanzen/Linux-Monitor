#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use Data::Dumper;


&main;


sub main
{
	&initial;
	
	my @usage=split(/,/,`Clang/SystemAnalyzer.out`);
	
	print Dumper @usage;
	
	&clean;
	
	return 0;
}

sub initial
{
	chdir('Clang');
	system('make');
	chdir('../');
}

sub clean
{
	chdir('Clang');
	system('make clean');
	chdir('../');
}