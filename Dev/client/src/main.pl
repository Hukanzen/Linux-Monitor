#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use Data::Dumper;


&main;


sub main
{
	&make;

	&execute;
	print Dumper "END";
	
	# &clean;
	
	return 0;
}

sub make
{
	chdir('Clang');
	system('make');
	chdir('../');
}

sub execute
{
	chdir('Clang');
	system('./client.out');
	chdir('../');
}

sub clean
{
	chdir('Clang');
	system('make clean');
	chdir('../');
}