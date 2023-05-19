SELECT fastanumer,tegund,litur
FROM bill
WHERE litur = "blue";

SELECT asett_verð
FROM bill
WHERE asett_verð > 500000;

SELECT KT,NAFN_Seljanda
FROM Seljandi
WHERE KT = 1984 OR KT= 1985;

SELECT  tegund,litur as pink
FROM bill
WHERE tegund = "BMW";


SELECT tegund,asett_verð = 1300000
FROM bill
WHERE tegund ="BMW";


SELECT seljandi.KT, seljandi.NAFN_seljanda, bill.fastanumer, bill.tegund
FROM seljandi
INNER JOIN bill ON seljandi.KT=bill.seljandi_kt;


SELECT solumadur.NAFN_solumadur, sala.solumadur_id
FROM solumadur
INNER JOIN sala ON solumadur.id=sala.solumadur_id;


SELECT seljandi.NAFN_seljanda, bill.tegund
FROM seljandi
INNER JOIN bill ON seljandi.KT=bill.seljandi_kt;


SELECT bill.tegund, bill.litur, bill.seljandi_kt, solumadur.NAFN_solumadur, seljandi.KT
FROM ((bill
INNER JOIN seljandi ON bill.seljandi_kt=seljandi.KT)
INNER JOIN solumadur ON bill.fastanumer=solumadur.id);


select NAFN_solumadur,asett_verð
FROM solumadur
JOIN bill
where asett_verð > 1000000;



