#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;
use CGI;

use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;

use GD::Graph::points;
use GD::Graph::pie;
use GD::Graph::bars;

binmode STDOUT;

print "Content-type: text/html\n\n";
print "<!doctype html>";


my $query = new CGI;
# print $query->header( -type => "image/jpeg",-charset => 'utf-8' );

my $ipaddr    = $query->param('ipaddr');    # IPアドレス

my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);


my @select_data=$db->db_fetch_assoc_hash('SELECT INET_NTOA(ipaddr) AS ipaddr,hostname,la1min,la5min,la15min,delay,cpuUsage,memUsage,diskUsage,gettime FROM '.$DB_NAME.'.ReportData WHERE ipaddr='.$ipaddr.';');


$db->disconnect;

print '<html><body>';

print '<iframe src=./graph/lanmin_graph.cgi?ipaddr='.$ipaddr.'&min=1 width=360 height=260> iframe </iframe>'."\n";
print '<iframe src=./graph/lanmin_graph.cgi?ipaddr='.$ipaddr.'&min=5 width=360 height=260> iframe </iframe>'."\n";
print '<iframe src=./graph/lanmin_graph.cgi?ipaddr='.$ipaddr.'&min=15 width=360 height=260> iframe </iframe>'."\n";

print '<iframe src=./graph/Usage_graph.cgi?ipaddr='.$ipaddr.'&Usage=cpu width=360 height=260> iframe </iframe>'."\n";
print '<iframe src=./graph/Usage_graph.cgi?ipaddr='.$ipaddr.'&Usage=mem width=360 height=260> iframe </iframe>'."\n";
print '<iframe src=./graph/Usage_graph.cgi?ipaddr='.$ipaddr.'&Usage=disk width=360 height=260> iframe </iframe>'."\n";

print "<table border=1>\n";
print "<tr>";
print "<th>ipaddr</th><th>hostname</th><th>la1min</th><th>la5min</th><th>la15min</th><th>delay</th><th>cpuUsage</th><th>memUsage</th><th>diskUsage</th><th>gettime</th>";
print "</tr>\n";

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

print '</body></html>'

