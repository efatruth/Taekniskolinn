using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/* felix bassey
 * 10.3.2016
 * verkefni úr tíma/glærum
 */
namespace æfing_verkefni_7
{
    class RandomVerkefni7
    {
        static void Main(string[] args)
        {
            //string svar = null
            int teljari = 0;
            int tilviljunartala = 0;
            Random random = new Random();
            do
            {

                tilviljunartala = random.Next(1, 667);
                Console.WriteLine(tilviljunartala);
                teljari++;

                //console.writeline("viltu halda áfram");
            } while (tilviljunartala != 666);
            Console.WriteLine("við fengum {0} tölur", teljari);
            Console.ReadKey();
            // köstum fjögur teningum og prófum að hafa fjögur random hluti

            int teningur1 = 0, teningur2 = 0, teningur3 = 0, teningur4 = 0;

            // vegna verkefnis skæri blað steinn
            int valNot = 0;
            int valTolvu = 0;
            // þarf líka teljara
            int jafntefli = 0;
            // nota do while lykkju sem héldur áfram meðan notandi velur ekki 4
            do
            {
                // spyrja notanda hvað hann vill með Console.WriteLine
                Console.WriteLine("Hvað velur notandi? ");
                Console.WriteLine("1. Skæri");

                valNot = Convert.ToInt32(Console.ReadLine());

                // ef notandi valdi ekki 4 þá fær tölva random tölu
                valTolvu = random.Next(1, 4);

                // eftir þetta þarf að bera saman og athuga hver vinnur eða jafntefli
                
            } while (valNot != 4);

            Console.WriteLine("Jafntefli: " + jafntefli);
           
        }
    }
}
