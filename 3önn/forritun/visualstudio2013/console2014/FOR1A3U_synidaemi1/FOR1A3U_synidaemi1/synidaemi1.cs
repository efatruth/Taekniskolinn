using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR1A3U_synidaemi1
{
    class synidaemi1
    {
        static void Main(string[] args)
        {
            Kynning á C# og
Visual Studio Express
for Windows Desktop
FOR1A3U
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 1
Hvað munum við læra í FOR1A3U?
• Læra að skrifa í forritunarmálinu C#
• Læra að nota forritunarumhverfið Visual
Studio Express for Windows Desktop
• Í áfanganum fá nemendur þjálfun í
undirstöðuatriðum forritunar í hlutbundnu
forritunarmáli
• Lögð verður áhersla á að nemendur temji sér
öguð og viðurkennd vinnubrögð við greiningu,
hönnun og prófun tölvuforrita.
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 2
Hvað munum við læra í FOR1A3U (frh.)
• Eftirfarandi atriði verða æfð með fjölmörgum
verkefnum:
– breytur/gagnatög (int, double, string, char, bool)
– skilyrðissetningar (if-else,switch)
– slaufur(for, while/do-while – foreach)
– fylki(arrays)
– strengjavinnsla (string og char)
• Nemendur vinna verkefni í tímum sem reyna á
færni þeirra og getu varðandi þessi atriði.
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 3
Hvað er mikilvægt að muna
• Console Application er einfalt
• Getum einbeitt okkur af læra syntax-ið vel en
ekki að hafa áhyggjur af útlitini
• Dæmi um útlit á Console Application
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 4
Forritunarmálið C#
• Það var þróað af Microsoft fyrirtækinu seint á 10.
áratugnum. Alfa útgáfa þess kom út á miðju ári
2000 og það hefur hlotið mikla útbreiðslu síðan.
Styrkur þess liggur m.a. í því hversu líkt það er
bæði C++ og Java málunum. Vanir forritarar eiga
því auðvelt með að læra málið. Annar
meginstyrkur C# er að það hentar vel fyrir
forritun fyrir Microsoft kerfi, líklega í mörgum
tilfellum betur en Java. Bæði eru hlutbundinn frá
grunni, byggja á svipuðum hönnunarforsendum
og nota áþekka málfræði
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 5
Forritunarumhverfi
• Forritunarumhverfið sem við notum í þessum
áfanga er Visual Studio Express for Windows
Desktop
• Það er frítt - slóðin er hér:
https://www.visualstudio.com/enus/products/visual-studio-express-vs.aspx
• Hægt að setja upp á tölvunum heima hjá ykkur
• Sjá mynd á næstu glæru
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 6
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 7
Upphafsglugginn í
forritunarumhverfinu Visual Studio
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 8
Til þess að búa til nýtt Project
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 9
Þá kemur þessi gluggi
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 10
Velja Console Application
Projectinu er gefið nafn hér
Nafnið þarf að vera skýrt og skilmerkilegt
Láta nafnið vera fyrir það sem það stendur
Velja Visual C#
Valinn staður til að vista projectið
Ekki dreifa út um allt, velja öruggan stað
• Projectið fær nafnið, FOR1A3U_Synidaemi1
• Þegar það er komið þá sjáum við þetta á
skjánum
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 11
Solution Explorer
• Mjög gott að hafa þennan glugga opinn
(Ef glugginn er ekki opinn má alltaf finna hann undir view-flipanum)
• Solution Explorer er hægra megin á skjánum
• ATH. Allur C# kóði hefur .cs (file extension)
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 12
Endurskýra Program.cs
• Þurfum að endurskýra Program.cs
• Hægri smellum á Program.cs og veljum Rename
• Program.cs endurnefnt
• Gætum þess að
eyða ekki .cs
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 13
Endurskýra Program.cs (frh.)
• Breytum Program.cs í Synidaemi1.cs
• Fáum glugga sem spyr hvort við viljum breyta á
öllum stöðum
• Samþykkja það
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 14
Endurskýra Program.cs (frh.)
• Breytist á tveimur stöðum – Klasinn fær nýtt nafn
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 15
Eitt lítið forrit
• Textinn sem skrifast út:
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 16
Hvað kemur út í Console
• F5 eða eða
• Svo birtist þetta:
• Til þess að hætta er ýtt á einhvern takka (kannski þarf að ýta á console
gluggann fyrst)
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 17
Hvað er hvað í kóðanum?
• class
• static void Main
• Console
• WriteLine()
• ReadKey()
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 18
Class - Klasi
• Klasi er eining í hlutbundinni forritun sem
gegnir hlutverki sniðmáts. Klasi ákveðins
hlutar lýsir eiginleikum og aðgerðum tilviks
hans. Taka má sem dæmi klasann Bíll sem
hefði að geyma upplýsingar um lit og gerð
bílsins sem og fjölda hurða og dekkja. Þegar
klasinn er í hendi er hægt að búa til mörg tilvik
af honum með mismunandi eiginleika, tilvik af
grænum bíl með 4 hurðir og 15 dekk eða rautt
tilvik 2 hurðir og 4.
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 19
C# Using
• Það sem er fyrir aftan using hér að framan:
– System: algengustu grunnklasar
– System.Collection.Generic: Inniheldur viðmót og
klasa sem skilgreina almenn söfn.
– System.Linq: Inniheldur klasa og viðmót sem styðja
Language-Integrated Query (LINQ).
– System.Text: Klasar sem forma og meðhöndla texta.
– System.Threading.Tasks: Vinnur með svokallaða
þræði.
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 20
Static void Main
• Öll C# notendaforrit innihalda Main aðferð því
í henni hefst vinnsla forritssins
• Það er að segja að þarna er
útgangspunkturinn í forritinu
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 21
Console
• Að skrifa Console þá ertu að nota innbyggðan
klasa í C#
• Að skrifa Console og punktur þá kemur upp
það sem Console klasinn býður uppá
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 22
WriteLine()
• Þessi lína skrifar út línu þegar forritið keyrir
• Tilheyrir System.Console klasanum
• Það verður að muna að skrifa Console. á
undan
• Hafa það sem á að birtast á skjánum þarf að
vera innan svigans með gæsalöppum
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 23
ReadKey()
• Tilheyrir System.Console klasanum
• Þessi skipun er í lok keyrslunar til þess að
forritarinn sjái hvað hann var að gera.
• Ef þessi skipun er ekki þá keyrir forritið og
slekkur sjálfkrafa á sér án þess að nokkuð
sjáist á skjánum
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 24
ReadKey() (frh.)
• Prufum þetta – skrifum þetta forrit með
ReadKey() og án ReadKey()
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 25
Comment - Athugasemdir
Athugasemdir eru líka kallaðar skjölun. Þær eru grænar að lit í
kóðanum
//
Fyrir aftan tvö skástrik eru athugasemdir en mega bara vera í
einni línu í kóðanum
/* */
Á milli /* og */ eru líka athugasemdir en mega vera lengri en
ein lína
Það sem er fyrir // eða /**/ sleppir þýðandinn að þýða og
þetta hefur því enginn áhrif á forritið
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 26
Muna að gera athugasemdir efst
• Mjög mikilvægt er að gera athugasemdir efst í
kóðann sem líta þá svona út
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 27
{ }
Þetta er setningarbálkur eða block. Skilgreining:
Setningar sem afmarkast af slaufusvigapari
Það verður alltaf að passa að láta
slaufusviganana standast á
Þessir svigar eru notaðir til afmörkunar: t.d. Á
klasaskilgreiningu, main aðferðinni, lykkjum,
skilyrðissetningum o.s.frv.
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 28
• Athugar bara hvort það séu villur
• Keyrir forritið upp
• Debugging: ferli sem notast við að leiðrétta villur
stundum kallað aflúsun.
Láta forritið keyra/athuga villur
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 29
Setja inn númer á undan línum
afar hentugt þegar verið er að aflúsa
• Debug
– Options and Settings
– Text Editor
– All Language
– Undir Display þarf svo að haka við Line numbers
– Svo þarf að ýta á OK-hnappinn
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 30
Sýnt myndrænt hér
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 31
Núna gerum við lítið verkefni saman
• Þetta verkefni á að skrifa út texta
• Þið verðið að muna að gera athugasemdir efst
• Þið eigið líka að gera athugasemdir fyrir aftan
hvað hver og ein lína gerir
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 32
Dæmi um verkefni
8/23/2015 Guðrún Randalín (uppf.: Snorri Emilsson) 33
        }  
        
            
    }
}
