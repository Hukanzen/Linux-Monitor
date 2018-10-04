#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;
 
use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;


&main;

sub main
{
	my $DB_ADDR="mysql";
	my $DB_NAME="Machine";
	my $PORT=3306;
	my $USER="user1";
	my $PASS="password";
	
	
	my $db=mysqli_connection->new;
	$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);
	
	$db->db_do('INSERT INTO '.$DB_NAME.'.ReportData (ipaddr,delay,cpuUsage,memUsage,diskUsage,hostname) VALUES (2130706433,1,2,3,4,\'Test\')');
	
	
	$db->disconnect;
}