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

# print "Content-type: text/html\n\n";


my $query = new CGI;
print $query->header( -type => "image/jpeg",-charset => 'utf-8' );

my $ipaddr    = $query->param('ipaddr');    # IPアドレス

my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);

my @ladata=$db->db_fetch_assoc_hash('SELECT gettime,la1min,la5min,la15min FROM '.$DB_NAME.'.ReportData WHERE ipaddr='.$ipaddr.';');

my @select_data=$db->db_fetch_assoc_hash('SELECT * FROM '.$DB_NAME.'.ReportData WHERE ipaddr='.$ipaddr.';');

$db->disconnect;

my (@gettime,@la1min,@la5min,@la15min);
foreach my $data (@ladata){
	push(@gettime,$data->{'gettime'});
	push(@la1min ,$data->{'la1min'});
	push(@la5min ,$data->{'la5min'});
	push(@la15min,$data->{'la15min'});
}

my @graphdata=(\@gettime,\@la1min);

my $graph = GD::Graph::bars->new( 800, 600 );
$graph->set(title => "Load Average 1min");

my $image = $graph->plot(\@graphdata)->jpeg();
print STDOUT $image;

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

