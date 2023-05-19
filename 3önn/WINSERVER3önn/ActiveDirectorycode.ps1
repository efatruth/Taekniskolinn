New-ADOrganizationalUnit -name starfmenn -protectedFromAccidentalDeletion $false
new-ADGroup -name ALLIRGRP -Path "OU=starfmenn, DC=ggp-BASSEY,DC=local" -GroupScope Global
$notendur = import-csv .\WIN2A3U_V15_notendur_verkefni4u.csv
foreach ($n in $notendur) {
    $deild = $n.deild
    if((Get-ADOrganizationalUnit -filter {name -eq $deild}).name -ne $deild) { 
      new-ADOrganizationalUnit -Name $deild -Path "OU=starfmenn, DC=ggp-BASSEY,DC=local" -protectedFromAccidentalDeletion $false
      New-ADGroup -name $deild -Path $("OU=" + $deild + ",OU=starfmenn, DC=ggp-BASSEY,DC=local" ) -GroupScope Global
      Add-ADGroupMember -Identity  ALLIRGRP -Members $deild
    }
    New-ADUser -name $n.nafn -displayname $n.nafn -givenname $n.fornafn -surname $n.eftirnafn -SamAccountName $n.Notendanafn -UserPrincipalName $($n.notendanafn + "@ggp-BASSEY.local") -Path $("OU=" + $deild + ",OU=starfmenn, DC=ggp-BASSEY,DC=local" ) -AccountPassword (ConvertTo-SecureString -AsPlainText "PASS.123" -force) -Enabled $true

    Add-ADGroupMember -Identity $deild -members $n.notendanafn
}