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
	
my @select_data=$db->db_fetch_assoc_hash('SELECT DISTINCT INET_NTOA(ipaddr) AS ipaddr,hostname FROM '.$DB_NAME.'.ReportData');
$db->disconnect;

print "<table>\n";
foreach my $data (@select_data){
	print "<tr>";
	print "<td> <a href=showmachine.cgi?ipaddr=".%$data{'ipaddr'}.">".%$data{'ipaddr'}."</a></td>";
	print "<td>".%$data{'hostname'}."</td>";
	print "</tr>\n"
}

print "</table>\n";
