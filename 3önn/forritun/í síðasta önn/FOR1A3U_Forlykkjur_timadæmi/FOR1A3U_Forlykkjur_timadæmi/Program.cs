using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR1A3U_Forlykkjur_timadæmi
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int teljara = 0; teljara < 10; teljara++)
            {
                Console.Write(teljara + "sinn");
                Console.WriteLine("fyrsta forlykkjan mín! veiiii");
            }
            // birtum töluurnar 0-2-4-6-8-10 með forlykkju
            for (int i = 0; i <= 10; i++)
            {
                Console.Write(i + " ");
                i = i + 1;
            }
            Console.WriteLine();
            //birtum tölur á bill sem notandir velur 
            int start = 0;
            int stop = 0;
            Console.WriteLine("nú bið ég um tvær tölur");
            Console.WriteLine("hvar viltu byrja");
            start = Convert.ToInt32(Console.ReadLine());



            Console.WriteLine();


        }   
    }
}
