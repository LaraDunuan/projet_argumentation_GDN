#!/usr/bin/perl
#  Lara DUNUAN et Siyu WANG
#  Projet Argumentation Grand Débat National, Mai 2019 
#  Fichier d'entrée : parsim_out.txt
#  Fichier de sortie : projet_ouput.txt

use LWP::Simple;
use File::Slurp;
use utf8;

open(IN, "<:encoding(utf-8)", "parsim_out.txt");
open(OUT, ">:encoding(utf-8)", "projet_ouput.txt");

print "Execution de post.pl\n";
while (my $ligne = <IN>)
{
	chomp $ligne;
	#print $ligne;

	if ($ligne =~ /INPUT: (.+?)$/sg) 
	{
		my $phrase = $1;
		#print $phrase;
		print OUT "$phrase\n";
	} # end while

	if ($ligne =~ /<Node called "prop" matching (.+?)>$/sg) 
	{
		my $match = $1;
		#print $match;
		print OUT "$match\n";
	} # end while
}
print "Fichier généré: projet_ouput.txt\n";
close IN;
close OUT;


