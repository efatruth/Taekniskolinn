using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*livinus bassey felix
 * 28/01/16
 */
namespace skilaverkefni2_livinus
{
    class skilaverkefni2
    {
        static void Main(string[] args)
        {
            // Lidur1: MinnstaTala2
            int tala1 = 0;
            int tala2 = 0;
            int tala3 = 0;
            Console.Write("Please enter first number of three: ");
            tala1 = Convert.ToInt32(Console.ReadLine());
            Console.Write("vinsamlegast enter annar tala af þrir: ");
            tala2 = Convert.ToInt32(Console.ReadLine());
            Console.Write("vinsamlegast settu þríðja tala af þrír: ");
            tala3 = Convert.ToInt32(Console.ReadLine());
            if (tala1 == tala2 || tala1 == tala3 || tala2 == tala3)
            {
                Console.WriteLine("Það má ekki slá inn sömu töluna tvisvar sinnum");
            }
            else if(tala1 < tala2 && tala1 < tala3)
            {
                Console.WriteLine(tala1 + " er minnst.");
            }
            else if(tala2 < tala1 && tala2 < tala3)
            {
                Console.WriteLine(tala2 + " er minnst.");
            }
            else if(tala3 < tala1 && tala3 < tala2)
            {
                Console.WriteLine(tala3 + " er minnst.");
            }

            // Lidur2: Tommur_Sentimetra
            string svar = null;
            double cm = 0;
            double inch = 0;
            Console.WriteLine("hvort vil þú breyta cm í tommur (cmToInch) eða tommur í cm (inchToCm)? ");
            svar = Console.ReadLine();

            if (svar == "cmToInch")
            {
                // spyrja um hve margar sentimetrar
                Console.WriteLine("hve margir sentimetrar?");
                cm = Convert.ToDouble(Console.ReadLine());
                inch = cm / 2.54;
                Console.WriteLine("kommutalan er " + inch);
            }
            else if (svar == "inchToCm")
                Console.WriteLine("hve margar sentimetrar?");
            inch = Convert.ToDouble(Console.ReadLine());
            
            {
                cm = inch * 2.54;
            }

        }
    }
}
