using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR1A3U_modulus_H2
{
    class modulus
    {
        static void Main(string[] args)
        {
            int talaFraNotanda = 0, deilitalaNotanda = 0;
            int venjulegDeiling = 0, afgangur = 0;
            Console.WriteLine("sláðu inn tölu.");
            talaFraNotanda = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("sláðu inn deilitölu.");
            deilitalaNotanda = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("nú deilum við með " + deilitalaNotanda);
            venjulegDeiling = talaFraNotanda / deilitalaNotanda;
            Console.WriteLine(talaFraNotanda + " / " + deilitalaNotanda + " = " + venjulegDeiling);
            Console.WriteLine("-----------------");
            Console.WriteLine("nú finnum við afang af sömu deilingu (modulus)");
            afgangur = talaFraNotanda % deilitalaNotanda;
            Console.WriteLine("afangurinn er: " + afgangur);
            Console.WriteLine("-----------------");
            Console.WriteLine("sjáum við muninn");
            Console.ReadKey();

            // dæmi 1 úr æfingaverkefni 4
            int talnalengd = 0;
            Console.WriteLine("hvað er tala löng (fjöldi tölustafa)?");
            talnalengd = Convert.ToInt32(Console.ReadLine());
            venjulegDeiling = talnalengd / 4;
            afgangur = talnalengd % 4;
            Console.WriteLine("talan skiptist í " + venjulegDeiling + "fjögurra talna hluta.");
            if (afgangur != 0)
            {
                Console.WriteLine("Fremst koma " + afgangur + " tölur.");
            }
            Console.ReadKey();

            // dÆmi 2 úr Æfingaverkefni 4
            int innsleginTala = 0;
            Console.WriteLine("hvað eru mjólkurfernunar margar?");
            innsleginTala = Convert.ToInt32(Console.ReadLine());
            venjulegDeiling = innsleginTala / (12 * 12);
            afgangur = innsleginTala % (12 * 12);
            Console.WriteLine("fjöldi grinda er: " + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " fernur eftir");
            venjulegDeiling = afgangur / 12;
            afgangur = afgangur % 12;
            Console.WriteLine("fjöldi pakka er: " + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " fernur eftir");
            Console.ReadKey();

            // dÆmi 3 úr Æfingaverkefni 4
            int tommur = 0;
            Console.WriteLine("hve eru langur húsveggur er í tommum?");
            tommur = Convert.ToInt32(Console.ReadLine());
            venjulegDeiling = tommur / (12 * 3);
            afgangur = tommur % (12 * 3);
            Console.WriteLine("fjölði yarda er: " + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " tommum eftir");
            venjulegDeiling = afgangur / 12;
            afgangur = afgangur % 12;
            Console.WriteLine("fjölði fet er:" + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " tommur eftir");
            Console.ReadKey();

            // dÆmi 4 úr Æfingaverkefni 4
            int bita = 0;
            Console.WriteLine("hve marga bita er verið að vinna með");
            bita = Convert.ToInt32(Console.ReadLine());
            venjulegDeiling = bita / 32;
            afgangur = bita % 32;
            Console.WriteLine("fjölði word er:" + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " bita eftir");
            venjulegDeiling = afgangur / 8;
            afgangur = afgangur % 8;
            Console.WriteLine("fjöldi byte er:" + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " bita eftir");
            venjulegDeiling = afgangur / 4;
            afgangur = afgangur % 4;
            Console.WriteLine("fjölði nybble er:" + venjulegDeiling);
            Console.WriteLine("þá eru " + afgangur + " bita eftir");
            Console.ReadLine();



            
        }
        
    }
}
