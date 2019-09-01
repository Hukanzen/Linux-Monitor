#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;

use Net::SNMP;

use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;
use DBI;


my $DB_ADDR='127.0.0.1';
my $PORT='43306';
my $USER='user1';
my $PASS='password';

my $db=mysqli_connection->new;
$db->connect('List',$DB_ADDR,$PORT,$USER,$PASS);
my @conbi_data=$db->db_fetch_assoc_hash('SELECT ipaddridx,oididx FROM `Combination`');

print Dumper @conbi_data;

foreach my $conbi(@conbi_data)
{
	print Dumper $conbi->{'ipaddridx'};
	print Dumper $conbi->{'oididx'};
}
#my @mechine_list= $db->db_fetch_assoc_array('SELECT INET_NTOA(ipaddr) AS ipaddr FROM `Connection` WHERE ');

$db->disconnect; 

exit ;



#my $idx=0;
#foreach my $machine (@machine_list){
#	my $OID_sysUpTime = $old_list[$idx];
#	
#	my ($session, $error) = Net::SNMP->session(
#		-hostname  => $machine['addr'] , 
#		-community => 'public',
#	);
#	
#	if (!defined $session) {
#		printf "ERROR: %s.\n", $error;
#		exit 1;
#	}
#	
#	my $result = $session->get_request(-varbindlist => [ $OID_sysUpTime ],);
#	
#	if (!defined $result) {
#		printf "ERROR: %s.\n", $session->error();
#		$session->close();
#	#	exit 1;
#	}
#	
#	printf "The sysUpTime for host '%s' is %s.\n",
#		$session->hostname(), $result->{$OID_sysUpTime};
#		$session->close();
#
#	$idx++;
#}
#exit 0;
