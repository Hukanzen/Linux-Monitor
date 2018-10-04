#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;
use CGI;

use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;



print "Content-type: text/html\n\n";


my $query = new CGI;
my $ipaddr    = $query->param('ipaddr');    # IPアドレス


my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);

my @select_data=$db->db_fetch_assoc_hash('SELECT * FROM '.$DB_NAME.'.ReportData WHERE ipaddr='.$ipaddr.';');

print "<table>\n";
foreach my $data (@select_data){
	print "<tr>";
	print "<td>".%$data{'ipaddr'}."</td>";
	print "<td>".%$data{'hostname'}."</td>";
	print "<td>".%$data{'la1min'}."</td>";
	print "<td>".%$data{'la5min'}."</td>";
	print "<td>".%$data{'la15min'}."</td>";
	print "<td>".%$data{'delay'}."</td>";
	print "<td>".%$data{'cpuUsage'}."</td>";
	print "<td>".%$data{'memUsage'}."</td>";
	print "<td>".%$data{'diskUsage'}."</td>";
	print "<td>".%$data{'gettime'}."</td>";
	print "</tr>\n"
}

print "</table>\n";

$db->disconnect;