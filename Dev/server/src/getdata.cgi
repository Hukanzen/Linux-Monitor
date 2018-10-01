#!/usr/bin/env perl

use strict;
use warnings;
use CGI;

use Data::Dumper;
 
use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;
 
 

print "Content-type: text/html\n\n";

#
# POST / GET パラメータを取得
#
my $query = new CGI;

# 取得
my $ipaddr    = $query->param('ipaddr');    # IPアドレス
my $delay     = $query->param('delay');     # データ取得分
my $cpuUsage  = $query->param('cpu');       # 
my $memUsage  = $query->param('mem');       # 
my $diskUsage = $query->param('disk');      # 
my $hostname  = $query->param('hostname'); #


my $DB_ADDR="mysql";
my $DB_NAME="Machine";
my $PORT=3306;
my $USER="user1";
my $PASS="password";
my $db=mysqli_connection->new;

$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);
	
$db->db_do('INSERT INTO '.$DB_NAME.'.ReportData  VALUES ('.$ipaddr.','.$delay.','.$cpuUsage.','.$memUsage.','.$diskUsage.',"'.$hostname.'")');
	# $db->db_do('INSERT INTO '.$DB_NAME.'.ReportData  VALUES (2130706433,1,2,3,4,\'Test\')');


$db->disconnect;
	



exit;