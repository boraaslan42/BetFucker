1)Scraper.py içine tüm sitelerin linkleri eklenecek ve otomasyon yapılarak düzenli olarak veri çekilmesi sağlanacak. (Bitmedi)
2)hatbet ve meridianbet gibi dosyalar oluşacak (Bitmedi)
3)oddsmeridian.py ve oddshatbet.py gibi tüm siteler için sitenin içeriğine ve nasıl kodlandığına bağlı olarak veriyi çekmek adına kod yazılacak ve meridianbet.json, hatbet.json gibi dosyalar oluşmuş olacak. (Diğer sitelerden gelen tablo formatlarının oluşturduğum tablo formatıyla aynı olmasına dikkat edilmeli.) (Bitmedi)
4)MATCHFINDER.py kullanılarak en iyi oranlar bulunuyor ve games.json dosyası olarak kaydediliyor.
5)betfinder.py kullanılarak çarpanların ara değerleri bulunuyor öncelikle ve surebetresults.json olarak kaydediliyor.
6)multiplierfinder.py kullanılarak çarpanların asıl değerleri elde ediliyor. Bu da multipliers.json olarak kaydediliyor.
7)Bestbets.py kullanılarak minimum kar hesaplanıyor ve çok kardan az kara doğru maçlar listeleniyor. Sonuç ise Surebets.json olarak kaydediliyor.


Yapılması gerekenler aslında sadece scraperi yazmak ve scrape edilen datalardan maçlar için data json tablelarını çekmek için her siteye özgü oddsmeridian.py veya oddshatbet.py gibi dosyalar oluşacak. 
Oluşan tableların ve dosya isimlerinin benim oluşturduklarımla consistent olmasına dikkat edilmeli.
Scraper.py dışında hiçbir dosyanın içeriğiyle oynanmasına gerek yok.
Daha iyi bir practive için meridianbet.json gibi dosyalar aslında repo içinde farklı bir klasöre kaydedilebilir bu sayede MATCHFINDER.py dosyasının içinde 32. satırdaki json_files = [file for file in os.listdir() if file.endswith(".json") and file != "games.json" and file != "surebetresults.json" and file != "Multipliers.json" and file != "SUREBETS.json"]
içindeki exceptionları yazmaya gerek kalmaz. Bu çok da önemli bir bilgi değil ancak ara değerler için farklı json filelar üretilmesi gerekiyorsa (Maç ve bet dataları hariç) sıkıntı çıkabilir.
