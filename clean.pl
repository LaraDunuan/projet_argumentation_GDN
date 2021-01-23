#!/usr/bin/perl
#  Lara DUNUAN et Siyu WANG
#  Projet Argumentation Grand Débat National, Mai 2019 
#  Fichier d'entrée : pretraitement.txt
#  Fichier de sortie : out_clean.txt

use LWP::Simple;
use File::Slurp;
use utf8;

open(IN, "<:encoding(utf-8)", "pretraitement.txt");
open(OUT, ">:encoding(utf-8)", "out_clean.txt");

print "Execution de clean.pl\n";

while (my $ligne = <IN>)
{
	chomp $ligne;
	#print $ligne;
	$ligne =~ s/ ?{S} ?//g;
	$ligne =~ s/ ?_ ?//g;


	while ($ligne =~ /(.+?)<marqueur>(.+?)<\/marqueur>(.+?)$/sg) 
	{
		my $gauche = $1;
		my $marker = $2;
		my $droit = $3;
		print OUT "<argument><premconc> $gauche</premconc><marqueur> $marker </marqueur><premconc> $droit</premconc></argument>.\n";

	} # end while
}

close IN;
close OUT;


