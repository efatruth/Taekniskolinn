using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR1A3U_synidæmi1
{
    class Syni1dæmi1
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
                //stigafjoldi - vægir 20 %
                case 1:
                    Console.WriteLine("hvað er mörg stig ");
                    int stig = Convert.ToInt32(Console.ReadLine());
                    if (stig >= 17)
                    {
                        Console.WriteLine("vel gert");
                    }
                    else
                    {
                        Console.WriteLine("það gengur betur næst");
                    }
                    if (stig >= 35)
                        Console.WriteLine("voru þeir einir á vellinum?");
                    break;
                //reikningsdæmi - vægi 20 %
                case 2:
                    int tal1 = 0;
                    int tal2 = 0;
                    int tal3 = 0;
                    int svar = 0;
                    Console.WriteLine("tölu 1");
                    tal1 = Convert.ToInt32(Console.ReadLine());

                    Console.WriteLine("tölu 2");
                    tal2 = Convert.ToInt32(Console.ReadLine());

                    Console.WriteLine("tolu 3");
                    tal3 = Convert.ToInt32(Console.ReadLine());

                    svar=(tal1 + tal2) - tal3;
                    Console.WriteLine("svar");

                //ymismal - vægi 30 %
                case 3:




                    
                            
                        

            }// end switch val

            
                
            


            



        } 
    }
}
