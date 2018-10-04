#!/usr/bin/env perl

use strict;
use warnings;

use Data::Dumper;

use strict;
use GD;
use CGI;
 
use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;


print "START";
# &main;
# &graph;
&graph2;
print "END";


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

sub graph
{

my $cgi = new CGI;
print $cgi->header( -type    => 'image/png',
                    -charset => 'euc-jp' );

# 新しいイメージを作成
my $im = new GD::Image(100,100);

# いくつかの色を確保
my $white = $im->colorAllocate(255,255,255);
my $black = $im->colorAllocate(0,0,0);       
my $red = $im->colorAllocate(255,0,0);      
my $blue = $im->colorAllocate(0,0,255);

# 背景色を透明にし、インターレース化
$im->transparent($white);
$im->interlaced('true');

# 絵の周りを黒く縁取り
$im->rectangle(0,0,99,99,$black);

# 青い楕円形を描画
$im->arc(50,50,95,75,0,360,$blue);

# 赤で塗りつぶし
$im->fill(50,50,$red);

# バイナリ・ストリームへ書きこむことを確実にする
binmode STDOUT;

# イメージをPNGに変換し、標準出力に出力
print $im->png;
}

sub graph2
{
	binmode STDOUT;
	use strict;

use CGI;
use GD::Graph::pie;

my $cgi = CGI->new();
print $cgi->header( -type => "image/jpeg" );

my @data = ( ["Apache","IIS","Other"], [ 67.2, 21.0, 11.8] );

my $graph = new GD::Graph::pie( 250, 200 );

$graph->set( title       => "Web server Usage, March 2004",
             dclrs       => [ qw( #D6D6FF #CECECE #FFFFFF ) ],
             pie_height  => 32,
             start_angle => 90 );

print STDOUT $graph->plot(\@data)->jpeg();
}