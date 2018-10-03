#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;
 
use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;



print "Content-type: text/html\n\n";



my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);
	
# $db->db_do('INSERT INTO '.$DB_NAME.'.ReportData (ipaddr,la1min,la5min,la15min,delay,cpuUsage,memUsage,diskUsage,hostname) VALUES ('.$ipaddr.','.$la1min.','.$la5min.','.$la15min.','.$delay.','.$cpuUsage.','.$memUsage.','.$diskUsage.',"'.$hostname.'")');
my @select_data=$db->db_fetch_assoc_array('SELECT ipaddr,hostname FROM '.$DB_NAME.'.ReportData');

foreach my $data (@select_data){
	print $data."<br>";
}
