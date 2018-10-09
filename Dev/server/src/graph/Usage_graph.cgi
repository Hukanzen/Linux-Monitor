#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;
use CGI;

use lib qw(./../lib);   # ./../lib配下を読み込む
use mysqli_connection;

use GD::Graph::points;
use GD::Graph::pie;
use GD::Graph::bars;

binmode STDOUT;

my $query = new CGI;
print $query->header( -type => "image/jpeg",-charset => 'utf-8' );

my $ipaddr    = $query->param('ipaddr');    # IPアドレス
my $Usage     = $query->param('Usage');

my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);

my @ladata=$db->db_fetch_assoc_hash('SELECT gettime,'.$Usage.'Usage FROM '.$DB_NAME.'.ReportData WHERE ipaddr='.$ipaddr.';');


$db->disconnect;

my (@gettime,@usage);
foreach my $data (@ladata){
	push(@gettime,$data->{'gettime'});
	push(@usage,$data->{$Usage.'Usage'});
}

my @graphdata=(\@gettime,\@usage);

my $graph = GD::Graph::points->new( 350, 250 );
$graph->set(title => $Usage.'Usage');

my $image = $graph->plot(\@graphdata)->jpeg();
print STDOUT $image;