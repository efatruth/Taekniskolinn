using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace skilaverkefni3
{
    class Program
    {
        static void Main(string[] args)
        {
            // Verkefni 1 - númer mánaða
            int manadi = 0;
            Console.WriteLine("sláðu inn numer á mánuði");
            manadi = Convert.ToInt32(Console.ReadLine());
            switch (manadi)
            {
                case 1:
                    Console.WriteLine("januar er numer 1");
                    break;
                case 2:
                    Console.WriteLine("februar er numer 2");
                    break;
                case 3:
                    Console.WriteLine("mars er numer 3");
                    break;
                case 4:
                    Console.WriteLine("april er numer 4");
                    break;
                case 5:
                    Console.WriteLine("maí er numer 5");
                    break;
                case 6:
                    Console.WriteLine("juní er numer 6");
                    break;
                case 7:
                    Console.WriteLine("julí er numer 7");
                    break;
                case 8:
                    Console.WriteLine("águst er numer 8");
                    break;
                case 9:
                    Console.WriteLine("september er numer 9");
                    break;
                case 10:
                    Console.WriteLine("october er numer 10");
                    break;
                case 11:
                    Console.WriteLine("november er numer 11");
                    break;
                case 12:
                    Console.WriteLine("december er numer 12");
                    break;
                default:
                    Console.WriteLine("enginn manadur er numer " + manadi);
                    break;
            }// end switch manudi

            // Verkefni 2 - upphafsstafur mánaða
            string bokstafir = null;
            Console.WriteLine("slaðu inn upphastaf mánadi");
            bokstafir = Console.ReadLine().ToUpper();
            switch (bokstafir)
            {
                case "J":
                    Console.WriteLine("januar,juní og julí er byrja á j");
                    break;
                case "F":
                    Console.WriteLine("febrúar er byrja á f");
                    break;
                case "M":
                    Console.WriteLine("mars og maí er byrja á m");
                    break;
                case "A":
                    Console.WriteLine("apríl og ágúst er byrja á a");
                    break;
                case "S":
                    Console.WriteLine("aðeins september er byrja á s");
                    break;
                case "O":
                    Console.WriteLine("aðeins október byrja á o");
                    break;
                case "N":
                    Console.WriteLine("aðeins november byrja á n");
                    break;
                case "D":
                    Console.WriteLine("aðeins desember byrja á d");
                    break;


            }// end switch bokstafir
            Console.ReadKey();
        }// end Main


            // verkefni 3 - sentimetrum af radíus,hrings/kúlu


        
            


    }
}
