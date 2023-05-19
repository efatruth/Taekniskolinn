using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR1A3U_Hlutapróf1
{
    class hlutapróf1
    {
        static void Main(string[] args)
        {

            //kveðja - vægi
            string notandann = null;
            int skonumer = 0;
            string skoverslun = null;

            int val = 0;

            Console.WriteLine("sladu in nafn sem er wizguy");
            notandann = Console.ReadLine();
            Console.WriteLine("hvað er skonumer þú er að nota");
            skonumer = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("hvað er skóbuð þú er að versla oftast");
            skoverslun = Console.ReadLine();

            Console.WriteLine("góðan dag: " + notandann);
            Console.WriteLine("þú nota skonumer " + skonumer);
            Console.WriteLine("þú verslar oftast sko í skobuðinni " + skoverslun);
            Console.ReadKey();



            //valmynd - vægi
            Console.WriteLine(" 1.  stigafjöldi.");
            Console.WriteLine(" 2.  reikningsdæmi");
            Console.WriteLine(" 3.  reikna ýmis mál");

            val = Convert.ToInt32(Console.ReadLine());

            switch (val)
            {
                case 1:
                    int stigafjoldi = 0;
            //stigafjoldi - vægi 


                    if (stigafjoldi>=17)
                    {
                        Console.WriteLine("Vel gert");
                    }
                    else 
                    {
                        Console.WriteLine("það gengur betur næst");
                    }
                
            
            if (stigafjoldi > 35) 
            {
                Console.WriteLine("voru þeir á vellinum?");
            }
           
                break;

                case 2:
                int tala1 = 0, tala2 = 0, tala3 = 0;
                int summa = 0;
            //reikningsdæmi - vægi               
            Console.WriteLine("sláðu inn fyrstu töluna");
            tala1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("sláðu inn aðra töluna");
            tala2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("sláðu inn þriðju töluna");
            tala3 = Convert.ToInt32(Console.ReadLine());

            summa = tala1 + tala2 - tala3;
            Console.WriteLine("(" + tala1 + " + " + tala2 +")" + " - " + tala3 + " = " + summa);
                break;

                case 3:
                int lengd = 0, breidd = 0;
                double radius = 0;
                double nidurstada = 0;
                int velja = 0;
            //ymismal - vægi
            Console.WriteLine("1. reikna ummál ferhyrnings:(2 * lengd) + (2 * breid)");                 
            Console.WriteLine("2. reikna rúmmálsílvalnings:(radíus * radíus * 3.14)");                 
            Console.WriteLine("3. reikna flatarmálhrings:(radíus * radíus * 3.14");
                 
            //case 1 nidurstada = (2*lengd)+(2*breidd);
            Console.WriteLine("Ummál ferhyrningsins er " + nidurstada);

            //case 2 nidurstada = (radíus * radíus * 3.14)
            Console.WriteLine("rúmmál sílvalnings er " + nidurstada);

            //case 3 nidurstada = (radíus * radíus * 3.14")
            Console.WriteLine("flatarmálhrings er " + nidurstada);
            break;

            }// end switch val
            Console.ReadKey();





        }
    }
}
