#!/usr/bin/env perl

use strict;
use warnings;
use Data::Dumper;

use Net::SNMP;

use lib qw(./lib);   # ./lib配下を読み込む
use mysqli_connection;


my $DB_NAME='List';
my $DB_ADDR='mysql';
my $PORT='3306';
my $USER='user1';
my $PASS='password2018';

my $db=mysqli_connection->new;
$db->connect($DB_NAME,$DB_ADDR,$PORT,$USER,$PASS);


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
