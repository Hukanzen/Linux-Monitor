#!/usr/bin/env perl

use strict;
use warnings;
use CGI;

use Data::Dumper;
 
use lib qw(./lib);   # ./lib配下を読み込む
use my_MySQL_library::Perl::module::mysqli_connection.pm
 
 
#
# POST / GET パラメータを取得
#
my $query = new CGI;

# 取得
my $ipaddr    = $query->param{'ipaddr'}; # IPアドレス

my $delay     = $query->param{'delay'};  # データ取得分

my $cpuUsage  = $query->param{'cpu'};    # 
my $memUsage  = $query->param{'mem'};    # 
my $diskUsage = $query->param{'disk'};   # 

my $hostname   = $query->param{'hostname'}; #


print "Content-type: text/html\n\n";


