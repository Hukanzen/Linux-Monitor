#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use Data::Dumper;

&main;

sub main
{
	my @usage=split(/,/,`Clang/SystemAnalyzer.out`);
	
	print Dumper @usage;
	
	return 0;
}