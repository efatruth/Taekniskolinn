using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/* felix bassey
 * 25.2.2016
 * skilaverkefni 5 - kaffihús siggu og grétars
 * unnið með lykkjur, ákvarðanatökur (if og eða switch) og mdulus
 */
namespace FOR1A3U_Skilaverkefni_5
{
    class skil5
    {
        static void Main(string[] args)
        {
            // athuga hvað þarf af breytum t.d.
            // nafn og kennitala og:
            string menuItem1 = "Cappuchino";
            string menuItem2 = "Caffé Latte";
            string menuItem3 = "Expresso";
            string menuItem4 = "Americano";
            string menuItem5 = "súkkulaðikaka";
            string menuItem6 = "kleina";
            string menuItem7 = "Ostakaka";
            string menuItem8 = "Rúnstykki með áleggi að eigin vali";
            // og svo framvegis upp í 8 (fjölda á menu)
            int fjMenu1 = 0;
            int fjMenu2 = 0;
            int fjMenu3 = 0;
            int fjMenu4 = 0;
            int fjMenu5 = 0;
            int fjMenu6 = 0;
            int fjMenu7 = 0;
            int fjMenu8 = 0;
            // og svo framvegis upp í 8 (fjölda á menu)
            int verðMenu1 = 350; //þið ráðið verði
            int verðMenu2 = 300;
            int verðMenu3 = 400;
            int verðMenu4 = 350;
            int verðMenu5 = 450;
            int verðMenu6 = 400;
            int verðMenu7 = 450;
            int verðMenu8 = 450;
            // og svo framvegis upp í 8 (fjölda á menu)
            int samtMenu1 = 0;
            int samtMenu2 = 0;
            int samtMenu3 = 0;
            int samtMenu4 = 0;
            int samtMenu5 = 0;
            int samtMenu6 = 0;
            int samtMenu7 = 0;
            int samtMenu8 = 0;
            // og svo framvegis upp í 8 (fjölda á menu)
            int heildaverð = 0;
            // þarf líka breytu til að velja úr menu
            // annað hvort eða bæði:
            int valMenu = 0;
            string svarMeira = null;
            // hér er spurt um nafn og kennitölu og tekið inn do
            do
            {
                // menu sett upp 
                Console.WriteLine("1. {0}\t\t{1}", menuItem1, verðMenu1);
                Console.WriteLine("2. {0}\t\t{1}", menuItem2, verðMenu2);
                Console.WriteLine("3. {0}\t\t{1}", menuItem3, verðMenu3);
                Console.WriteLine("4. {0}\t\t{1}", menuItem4, verðMenu4);
                Console.WriteLine("5. {0}\t\t{1}", menuItem5, verðMenu5);
                Console.WriteLine("6. {0}\t\t{1}", menuItem6, verðMenu6);
                Console.WriteLine("7. {0}\t\t{1}", menuItem7, verðMenu7);
                Console.WriteLine("8. {0}\t\t{1}", menuItem8, verðMenu8);
                // og svo framvegis upp í 8 (fjölda á menu)
                Console.WriteLine("0. Ekki fleyra takk.");
                valMenu = Convert.ToInt32(Console.ReadLine());
                //  switch settur upp til að vinna úr pöntun.
                switch (valMenu)
                {
                    case 1:
                        //  takið við fjölda
                        Console.WriteLine("hve margar " + menuItem1 + " má bjoða þér? ");
                        fjMenu1 = Convert.ToInt32(Console.ReadLine());
                        //  reiknið samtals menu1
                        samtMenu1 = fjMenu1 * verðMenu1;
                        break;
                    case 2:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem2 + " má bjóða þér? ");
                        fjMenu2 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu2
                        samtMenu2 = fjMenu2 * verðMenu2;
                        break;
                    case 3:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem3 + " má bjóða þér? ");
                        fjMenu3 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu3
                        samtMenu3 = fjMenu3 * verðMenu3;
                        break;
                    case 4:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem4 + " má bjóða þér? ");
                        fjMenu4 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu4
                        samtMenu4 = fjMenu4 * verðMenu4;
                        break;
                    case 5:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem5 + " má bjóða þér? ");
                        fjMenu5 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu5
                        samtMenu5 = fjMenu5 * verðMenu5;
                        break;
                    case 6:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem6 + " má bjóða þér? ");
                        fjMenu6 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu6
                        samtMenu6 = fjMenu6 * verðMenu6;
                        break;
                    case 7:
                        // takið við fjölda
                        Console.WriteLine("hve margar " + menuItem7 + " má bjóða þér? ");
                        fjMenu7 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu7
                        samtMenu7 = fjMenu7 * verðMenu7;
                        break;
                    case 8:
                        // takið við fjölda
                        Console.WriteLine("hve margar" + menuItem8 + " má bjóða þér? ");
                        fjMenu8 = Convert.ToInt32(Console.ReadLine());
                        // reiknið samtals menu8
                        samtMenu8 = fjMenu8 * verðMenu8;
                        break;
                    // og svo framvegis upp í (fjölda á menu)
                    case 0:
                        Console.WriteLine("takk fyrir viðskiptin, hér kemur reikningurinn");
                        break;
                }
                // þið setjið inn console.clear að eigin vali í forritið
                if (valMenu != 0)
                {
                    Console.WriteLine("viltu halda áfram? J/N");
                    svarMeira = Console.ReadLine().ToUpper();
                    if (svarMeira == "N")
                    {
                        Console.WriteLine("Takk fyrir viðskiptin, hér kemur reikningurinn");
                    }
                }
            } while (valMenu != 0 && svarMeira != "N");// sýni tvær leiðir út
            Console.Clear();
            heildaverð = samtMenu1 + samtMenu2 + samtMenu3 + samtMenu4 + samtMenu5 + samtMenu6 + samtMenu7 + samtMenu8;
            // hérna kemur hausinn á reikningum og nafn og kennitala viðskiptavinar
            Console.WriteLine("Þakk fyrir að versla við kaffi hús");
            // athugið með if (eingöngu if) hvort fjMenu er meira en 0
            // og birta viðeigandi upplýsingar
            if (fjMenu1 > 0)
            {
                Console.WriteLine(fjMenu1 + " stykki " + menuItem1 + " = " + samtMenu1);
            }
            if (fjMenu2 > 0)
            {
                Console.WriteLine(fjMenu2 + " stykki " + menuItem2 + " = " + samtMenu2);
            }
            if (fjMenu3 > 0)
            {
                Console.WriteLine(fjMenu3 + " stykki " + menuItem3 + " = " + samtMenu3);
            }
            if (fjMenu4 > 0)
            {
                Console.WriteLine(fjMenu4 + " stykki " + menuItem4 + " = " + samtMenu4);
            }
            if (fjMenu5 > 0)
            {
                Console.WriteLine(fjMenu5 + " stykki " + menuItem5 + " = " + samtMenu5);
            }
            if (fjMenu6 > 0)
            {
                Console.WriteLine(fjMenu6 + " stykki " + menuItem6 + " = " + samtMenu6);
            }
            if (fjMenu7 > 0)
            {
                Console.WriteLine(fjMenu7 + " stykki " + menuItem7 + " = " + samtMenu7);
            }
            if (fjMenu8 > 0)
            {
                Console.WriteLine(fjMenu8 + " stykk " + menuItem8 + " = " + samtMenu8);
            }
               
            // að lokum er heildarverð reiknað og birt
            Console.WriteLine("heildaverði er " + heildaverð);
            // þið megið gjarnan bæta við og skreyta reikninginn
            // t.d með ---------- eða ***************
            if (heildaverð % 3 == 0)
            {
                Console.WriteLine("til hamingju, þú hefur unnið");
            }
            Console.ReadKey();
        }
    }
}


