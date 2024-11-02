import os
import google.generativeai as genai
import markdown
API_KEY="AIzaSyANFGM-zwnIA56Bq4Q4CRe7oKexCuBkxm8"
import os
import json
os.environ["GOOGLE_API_KEY"] = API_KEY

def gemini_create_document(math_question):
    # Create the model
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    )

    response = model.generate_content([
    "input: x + 2 = 0 problemindeki konuyu tespit edip o konuyu benim anlayabileceğim şekilde örneklerle anlatır mısın ?",
    "output: x + 2 = 0 Denklemi ve Birinci Dereceden Denklemler\"x + 2 = 0\" denklemi, birinci dereceden bir denklemdir. Bu ne demek oluyor? Gel birlikte inceleyelim.Birinci Dereceden Denklem Nedir?Bir denklemde bilinmeyen (burada x) en fazla birinci kuvvetle kullanılıyorsa, bu denkleme birinci dereceden denklem denir. Yani, x'in karesi, kübü gibi daha yüksek kuvvetleri görmüyoruz.Neden Birinci Dereceden Denklemler Önemli?Birinci dereceden denklemler, matematik ve günlük yaşamda birçok alanda kullanılır. Örneğin:\nYaş bulma problemleri: \"Ali'den 2 yaş büyük ve toplam yaşları 20 ise Ali kaç yaşındadır?\" gibi sorular birinci dereceden bir denklemle ifade edilir.\nPara problemleri: \"Bir kalem 2 TL, bir defter 5 TL ise toplam 14 TL'ye kaç kalem ve defter alınabilir?\" gibi sorular da birinci dereceden denklem sistemleriyle çözülür.\nx + 2 = 0 Denklemini ÇözmekBu denklemi çözmek için x'i yalnız bırakmamız gerekiyor. Her iki taraftan 2 çıkarırsak:\nx + 2 - 2 = 0 - 2\nx = -2\nSonuç olarak, x'in değeri -2'dir. Yani, x yerine -2 yazdığımızda denklem doğru olur: -2 + 2 = 0.GörselleştirmeBirinci dereceden denklemlerin grafikleri daima bir doğrudur. Bu denklemin grafiği, x eksenini -2 noktasında kesen bir doğru olacaktır.[Birinci dereceden denklem grafiği görseli eklenebilir]Özetle:\nx + 2 = 0 birinci dereceden basit bir denklemdir.\nBu denklemin çözümü x = -2'dir.\nBirinci dereceden denklemler, bilinmeyenin en yüksek kuvvetinin 1 olduğu denklemlerdir.\nBu tür denklemler, günlük hayattaki birçok durumu modellemek için kullanılır.\nDaha Fazla BilgiBirinci dereceden denklemler, daha karmaşık problemleri çözmek için de kullanılır. Örneğin, bir bilinmeyenli yerine iki veya daha fazla bilinmeyenli denklemler olabilir.Başka soruların varsa çekinme, sorabilirsin.Ek Bilgiler:\nEşitsizlik: Bazı durumlarda, bir denklem yerine bir eşitsizlik (örneğin, x + 2 > 0) ile karşılaşabiliriz.\nMutlak değer: Bir sayının işaretini görmezden gelerek alınan değerine mutlak değer denir ve birinci dereceden denklemlerde de kullanılabilir.\nBu konuyu daha iyi anlamak için internette \"birinci dereceden denklemler\" araması yapabilir, çeşitli örnekler ve çözümler bulabilirsin.",
    "input: x² - 9 = 0 denkleminin konusu nedir? Bu konuyu anlatır mısın ?",
    "output: x² - 9 = 0 Denklemi ve İkinci Dereceden Denklemler\"x² - 9 = 0\" denklemi, ikinci dereceden bir denklemdir. Bu ne demek oluyor? Gel birlikte inceleyelim.İkinci Dereceden Denklem Nedir?Bir denklemde bilinmeyen (burada x) en yüksek kuvveti 2 ise, bu denkleme ikinci dereceden denklem denir. Yani, x'in karesi (x²) gibi bir terim içeriyorsa, denklemimiz ikinci derecedir.Neden İkinci Dereceden Denklemler Önemli?İkinci dereceden denklemler, matematik ve fizik gibi birçok alanda sıkça karşımıza çıkar. Örneğin, bir cismin havadaki hareketi, bir parabolün denklemi gibi birçok gerçek dünya problemini modellemek için ikinci dereceden denklemler kullanılır.x² - 9 = 0 Denklemini ÇözmekBu denklemi çözmek için birkaç yöntemimiz var. En basit yöntemlerden biri çarpanlara ayırma yöntemidir:\nx² - 9 = 0\n(x - 3)(x + 3) = 0\nÇarpımın sıfıra eşit olması için çarpanlardan en az biri sıfıra eşit olmalıdır. Yani:\nx - 3 = 0 veya x + 3 = 0\nx = 3 veya x = -3\nSonuç olarak, denklemin çözüm kümesi {3, -3} şeklindedir. Yani, x yerine 3 veya -3 yazdığımızda denklem sağlanır.GörselleştirmeBu denklemin grafiği bir parabol olur. Parabolün x eksenini kestiği noktalar, denklemin kökleri (çözümleri)dir. Yani, grafikte x = 3 ve x = -3 noktalarında x eksenini keser.[İkinci dereceden denklem grafiği görseli eklenebilir]Özetle:\nx² - 9 = 0 bir ikinci dereceden denklemdir.\nİkinci dereceden denklemler, bilinmeyenin en yüksek kuvvetinin 2 olduğu denklemlerdir.\nBu denklemi çarpanlara ayırarak çözdük ve çözüm kümesini bulduk.\nİkinci dereceden denklemlerin grafikleri genellikle parabol olur.\nDaha Fazla Bilgiİkinci dereceden denklemleri çözmek için başka yöntemler de vardır (örneğin, kök bulma formülü). Ayrıca, denklemin katsayılarına göre köklerin sayısı ve türü hakkında da bilgi edinmek mümkündür.Başka soruların varsa çekinme, sorabilirsin.Ek Bilgiler:\nDiskriminant: İkinci dereceden denklemlerde köklerin sayısını ve türünü belirlemek için kullanılan bir değerdir.\nParabol: İkinci dereceden bir fonksiyonun grafiğidir.\nKökler: Bir denklemi sağlayan değerlerdir.\nBu konuyu daha iyi anlamak için internette \"ikinci dereceden denklemler\" araması yapabilir, çeşitli örnekler ve çözümler bulabilirsin.Basit Örnekler:\nBir atış yapılan bir topun yerle temas ettiği anı bulmak: Topun yerden yüksekliği ile ilgili bir denklem kurulur ve bu denklemin kökleri topun yere çarptığı zamanları verir.\nBir bahçenin alanı verildiğinde, kenar uzunluklarını bulmak: Bahçenin alanı bir kenar uzunluğunun karesine eşit olacağından, ikinci dereceden bir denklem kurulur.\nBu örnekler, ikinci dereceden denklemlerin gerçek hayattaki uygulamalarına dair bir fikir verebilir.Umarım bu açıklama senin için anlaşılır olmuştur.",
    "input: √(x + 1) = 5 problemindeki konuyu tespit edip o konuyu benim anlayabileceğim şekilde örneklerle anlatır mısın ?",
    "output: √(x + 1) = 5 Denklemi ve Köklü Denklemler\"√(x + 1) = 5\" denklemi, köklü bir denklemdir. Bu ne demek oluyor? Gel birlikte inceleyelim.Köklü Denklem Nedir?Bir denklemde bilinmeyen (burada x) bir kök içinde yer alıyorsa, bu denkleme köklü denklem denir. Yani, √ (kök içinde) sembolünü gördüğümüzde, karşımızda bir köklü denklem olduğunu anlayabiliriz.Neden Köklü Denklemler Önemli?Köklü denklemler, geometri, fizik gibi birçok alanda sıkça karşımıza çıkar. Örneğin, bir üçgende Pisagor teoremini kullanırken veya fizikte bazı formülleri çözerken köklü denklemlerle karşılaşabiliriz.√(x + 1) = 5 Denklemini ÇözmekBu denklemi çözmek için kökten kurtulmamız gerekir. Bunun için her iki tarafın karesini alırız:\n√(x + 1) = 5\n(√(x + 1))² = 5²\nx + 1 = 25\nx = 25 - 1\nx = 24\nSonuç olarak, denklemin çözümü x = 24'tür. Yani, x yerine 24 yazdığımızda denklem sağlanır.Önemli Not: Çözümün DoğrulanmasıKöklü denklemleri çözerken dikkat etmemiz gereken bir nokta var. Bulduğumuz çözümü orijinal denklemde yerine koyarak kontrol etmeliyiz. Bazen, denklemin her iki tarafının karesini alırken yabancı kök (denklemi sağlamayan çözüm) elde edebiliriz. Bu nedenle, bulduğumuz çözümü mutlaka kontrol etmek önemlidir.Bu örnekte x = 24 değerini √(x + 1) = 5 denkleminde yerine koyduğumuzda:\n√(24 + 1) = 5\n√25 = 5\n5 = 5\nGördüğümüz gibi, çözümümüz orijinal denklemi sağlıyor.Özetle\n√(x + 1) = 5 bir köklü denklemdir.\nKöklü denklemler, bilinmeyenin kök içinde olduğu denklemlerdir.\nBu tür denklemleri çözmek için genellikle her iki tarafın karesini alırız.\nÇözümün doğruluğunu kontrol etmek önemlidir.\nDaha Fazla BilgiKöklü denklemler, bazen daha karmaşık olabilir ve çözümleri için farklı yöntemler gerekebilir. Örneğin, birden fazla kök içeren veya daha yüksek dereceli kökleri olan denklemlerle karşılaşabiliriz.Başka soruların varsa çekinme, sorabilirsin.Ek Bilgiler:\nKöklü ifadeler: Kök içinde yazılan sayılara veya ifadelere köklü ifade denir.\nRasyonelleştirme: Paydasında kök bulunan bir kesri, paydada kök kalmayacak şekilde eşleniği ile çarpma işlemine rasyonelleştirme denir.\nKöklü denklemlerin grafikleri: Köklü denklemlerin grafikleri genellikle belirli bir bölgede tanımlıdır ve farklı şekillerde olabilir.\nBu konuyu daha iyi anlamak için internette \"köklü denklemler\" araması yapabilir, çeşitli örnekler ve çözümler bulabilirsin.Basit Örnekler:\nBir eşkenar üçgenin bir kenarının uzunluğu: Bir eşkenar üçgenin alanı √3/4 * a² formülüyle bulunur. Eğer alan verilmişse, bu formülden yola çıkarak kenar uzunluğu (a) için bir köklü denklem kurulur.\nBir dairenin yarıçapı: Bir dairenin alanı πr² formülüyle bulunur. Eğer alan verilmişse, bu formülden yola çıkarak yarıçap (r) için bir köklü denklem kurulur.\nBu örnekler, köklü denklemlerin geometri problemlerinde nasıl kullanıldığını göstermektedir.",
    "input: 3x + 2y = 6 x - y = 10 problemindeki konuyu tespit edip o konuyu benim anlayabileceğim şekilde örneklerle anlatır mısın ?",
    "output: İki Bilinmeyenli Doğrusal Denklem SistemleriVerdiğiniz\n3x + 2y = 6\nx - y = 10\ndenklemleri bir araya geldiğinde, iki bilinmeyenli doğrusal denklem sistemi olarak adlandırılır.Ne Anlama Geliyor?\nİki Bilinmeyen: Sistemde x ve y olmak üzere iki tane bilinmeyenimiz var. Bu bilinmeyenlerin değerlerini bulmaya çalışıyoruz.\nDoğrusal: Her bir denklem, çizildiğinde bir doğruyu temsil eder.\nSistem: İki veya daha fazla denklemin bir arada olduğu bir gruptur.\nPeki bu sistem ne işe yarar?\nGerçek Hayat Problemleri: Günlük hayattaki birçok problem, iki veya daha fazla bilinmeyenin ilişkili olduğu durumlarla ilgilidir. Örneğin:\n\nBirlikte 10 kalem ve silgi alındığında toplam fiyatın 6 TL olduğu, kalemlerin her birinin 3 TL, silgilerin ise 2 TL olduğu durumu bu şekilde bir denklem sistemi ile ifade edebiliriz.\nBir yarışta iki farklı hızla hareket eden iki aracın belirli bir süre sonra birbirini ne zaman geçeceği gibi problemler de bu sistemlerle çözülebilir.\n\n\nSistemi Çözmek Ne Demek?Bir denklem sistemini çözmek, verilen denklemleri aynı anda sağlayan x ve y değerlerini bulmak demektir. Bu değerler, geometrik olarak iki doğrunun kesiştiği noktayı temsil eder.Çözüm YöntemleriBu sistemi çözmek için birçok yöntem vardır. En yaygın olanları:\nGrafiksel Çözüm: Her iki denklemin grafiği çizilir. Grafiklerin kesiştiği nokta, sistemin çözümüdür.\nYerine Koyma Yöntemi: Bir denklemden bir bilinmeyen yalnız bırakılır ve diğer denklemde yerine konulur. Böylece tek bilinmeyenli bir denklem elde edilir ve çözülür.\nToplama Çıkarma Yöntemi: Denklemler uygun şekilde toplanıp çıkarılarak bir bilinmeyen yok edilir ve diğer bilinmeyen bulunur.\nÖrnek:Verilen sistemimiz için yerine koyma yöntemini kullanabiliriz:\nİkinci denklemden x'i yalnız bırakırsak: x = y + 10\nBulduğumuz x değerini ilk denklemde yerine koyarsak:\n3(y + 10) + 2y = 6\n3y + 30 + 2y = 6\n5y = -24\ny = -4.8\nBulduğumuz y değerini x = y + 10'da yerine koyarsak:\nx = -4.8 + 10\nx = 5.2\nBu durumda sistemin çözümü x = 5.2 ve y = -4.8 olur. Yani, bu değerleri verilen denklemlerde yerine koyduğumuzda her iki denklem de sağlanır.Özetle:İki bilinmeyenli doğrusal denklem sistemleri, günlük hayatın birçok alanında karşımıza çıkan ve çözümü gereken problemlerdir. Bu sistemleri çözmek için grafiksel, yerine koyma veya toplama-çıkarma gibi yöntemler kullanılabilir.Başka soruların varsa çekinmeden sorabilirsin.Ek Bilgiler:\nDoğrusal Denklem Sistemlerinin Çözümleri: Bir sistemin bir, sonsuz veya hiç çözümü olabilir.\nMatrisler: Büyük sistemleri çözmek için matrisler kullanılır.\nDeterminant: Bir matrisin sıfır olup olmaması, sistemin çözülebilirliği hakkında bilgi verir.\nBu konuyu daha iyi anlamak için internette \"iki bilinmeyenli doğrusal denklem sistemleri\" araması yapabilir, çeşitli örnekler ve çözümler bulabilirsin.",
    "input: x² - 9 = 0 problemindeki konuyu tespit edip o konuyu benim anlayabileceğim şekilde örneklerle anlatır mısın ?",
    "output: x² - 9 = 0 Denklemi ve İkinci Dereceden Denklemler\"x² - 9 = 0\" denklemi, ikinci dereceden bir denklemdir. Bu ne demek oluyor? Gel birlikte inceleyelim.İkinci Dereceden Denklem Nedir?Bir denklemde bilinmeyen (burada x) en yüksek kuvveti 2 ise, bu denkleme ikinci dereceden denklem denir. Yani, x'in karesi (x²) gibi bir terim içeriyorsa, denklemimiz ikinci derecedir.Neden İkinci Dereceden Denklemler Önemli?İkinci dereceden denklemler, matematik ve fizik gibi birçok alanda sıkça karşımıza çıkar. Örneğin, bir cismin havadaki hareketi, bir parabolün denklemi gibi birçok gerçek dünya problemini modellemek için ikinci dereceden denklemler kullanılır.x² - 9 = 0 Denklemini ÇözmekBu denklemi çözmek için birkaç yöntemimiz var. En basit yöntemlerden biri çarpanlara ayırma yöntemidir:\nx² - 9 = 0\n(x - 3)(x + 3) = 0\nÇarpımın sıfıra eşit olması için çarpanlardan en az biri sıfıra eşit olmalıdır. Yani:\nx - 3 = 0 veya x + 3 = 0\nx = 3 veya x = -3\nSonuç olarak, denklemin çözüm kümesi {3, -3} şeklindedir. Yani, x yerine 3 veya -3 yazdığımızda denklem sağlanır.GörselleştirmeBu denklemin grafiği bir parabol olur. Parabolün x eksenini kestiği noktalar, denklemin kökleri (çözümleri)dir. Yani, grafikte x = 3 ve x = -3 noktalarında x eksenini keser.[İkinci dereceden denklem grafiği görseli eklenebilir]Özetle:\nx² - 9 = 0 bir ikinci dereceden denklemdir.\nİkinci dereceden denklemler, bilinmeyenin en yüksek kuvvetinin 2 olduğu denklemlerdir.\nBu denklemi çarpanlara ayırarak çözdük ve çözüm kümesini bulduk.\nİkinci dereceden denklemlerin grafikleri genellikle parabol olur.\nDaha Fazla Bilgiİkinci dereceden denklemleri çözmek için başka yöntemler de vardır (örneğin, kök bulma formülü). Ayrıca, denklemin katsayılarına göre köklerin sayısı ve türü hakkında da bilgi edinmek mümkündür.Başka soruların varsa çekinme, sorabilirsin.Ek Bilgiler:\nDiskriminant: İkinci dereceden denklemlerde köklerin sayısını ve türünü belirlemek için kullanılan bir değerdir.\nParabol: İkinci dereceden bir fonksiyonun grafiğidir.\nKökler: Bir denklemi sağlayan değerlerdir.\nBu konuyu daha iyi anlamak için internette \"ikinci dereceden denklemler\" araması yapabilir, çeşitli örnekler ve çözümler bulabilirsin.Basit Örnekler:\nBir atış yapılan bir topun yerle temas ettiği anı bulmak: Topun yerden yüksekliği ile ilgili bir denklem kurulur ve bu denklemin kökleri topun yere çarptığı zamanları verir.\nBir bahçenin alanı verildiğinde, kenar uzunluklarını bulmak: Bahçenin alanı bir kenar uzunluğunun karesine eşit olacağından, ikinci dereceden bir denklem kurulur.\nBu örnekler, ikinci dereceden denklemlerin gerçek hayattaki uygulamalarına dair bir fikir verebilir.Umarım bu açıklama senin için anlaşılır olmuştur.",
    f"input:{math_question} problemindeki konuyu tespit edip o konuyu benim anlayabileceğim şekilde örneklerle anlatır mısın ?",
    "output: ",
    ])

    
    return markdown.markdown(response.text)





def upload_to_gemini(path, mime_type=None):
    """Gemini'ye dosya yükler ve dosyanın URI'sini döner."""
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

def send_problem_to_gemini(math_text, image_path=None):

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )
    
    files = [
    upload_to_gemini("images/file0.png", mime_type="image/png"),
    upload_to_gemini("images/file1.jpg", mime_type="image/jpeg"),
    upload_to_gemini(image_path, mime_type="image/jpeg")
    ]

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            files[0],
            "X Nedir ? Adım adım çözer misin",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Bir dik üçgende hipotenüsün karesi, diğer iki kenarın karelerinin toplamına eşittir. Bu durumda:\n\nx² = 6² + 8²\nx² = 36 + 64\nx² = 100\nx = √100\nx = 10\n\nDolayısıyla x = 10 cm'dir.\n",
        ],
        },
        {
        "role": "user",
        "parts": [
            files[1],
            "AB=DC ise C açısı kaçtır ? Adım adım çözer misin ?",
        ],
        },
        {
        "role": "model",
        "parts": [
            "1. **İkizkenar Üçgen:** AB=DC olduğundan, ABC üçgeni ikizkenar bir üçgendir.\n2. **Açı Özellikleri:** İkizkenar bir üçgende taban açıları eşittir, yani açı B = açı C'dir.\n3. **Üçgenin Açı Toplamı:** Bir üçgenin iç açılarının toplamı 180 derecedir.\n4. **Denklem:** Bu durumda,  açı A + açı B + açı C = 180 derece olur.\n5. **Değerleri Yerine Koyma:** Açı A = 36 derece, açı B = açı C olduğu için denklemi şu şekilde yazabiliriz: 36 derece + açı C + açı C = 180 derece.\n6. **Çözüm:** 36 derece + 2 * açı C = 180 derece \n        2 * açı C = 144 derece\n        açı C = 72 derece \n\nDolayısıyla, **C açısı 72 derecedir.** \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            files[2],
        ],
        },
    ]
    )

    response = chat_session.send_message(math_text)

    return markdown.markdown(response.text)


def gemini_video_oneri(math_text):
    genai.configure(api_key="AIzaSyANFGM-zwnIA56Bq4Q4CRe7oKexCuBkxm8")

    # Model ve yapılandırma oluşturuluyor
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Sohbet başlatılıyor
    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "x + 2 = 0 problemindeki matematik konusunu nedir. Bu konuyu öğrenmem için bana youtube'dan video önerir misin ?",
        ],
        },
        {
        "role": "model",
        "parts": [
            "x + 2 = 0 problemindeki matematik konusu **birinci dereceden denklemler**dir. \n\nBu konuyu öğrenmek için YouTube'da birçok faydalı video bulunmaktadır. İşte size birkaç öneri:\n\n**Temel Kavramlar:**\n\n* **[Khan Academy - Birinci Dereceden Denklemler](https://www.youtube.com/watch?v=3wjngQlOz6I)**: Birinci dereceden denklemlerin temel kavramlarını açıklayan, anlaşılması kolay bir video.\n* **[Math Antics - Denklemler](https://www.youtube.com/watch?v=NnV_Xs-C27M)**: Denklemlerin ne olduğuna dair açıklayıcı ve eğlenceli bir video.\n\n**Çözüm Yöntemleri:**\n\n* **[Math Planet - Birinci Dereceden Denklemler Çözümü](https://www.youtube.com/watch?v=7X84V5jZ5lM)**: Birinci dereceden denklemleri çözmek için çeşitli yöntemleri gösteren bir video.\n* **[PatrickJMT - Denklemler Çözümü](https://www.youtube.com/watch?v=a3gY-9gXvYc)**: Karmaşık denklemleri çözmek için adım adım rehberlik sunan detaylı bir video.\n\n**Özel Durumlar:**\n\n* **[Math Easy Solutions - Denklemlerde Kesirler](https://www.youtube.com/watch?v=h6J76V83_Q8)**: Denklemlerde kesirlerle nasıl çalışılacağına dair örnekler içeren bir video.\n* **[Purplemath - Denklemlerde Mutlak Değer](https://www.youtube.com/watch?v=XgV96Z5xL6Y)**: Denklemlerde mutlak değerle nasıl çalışılacağına dair açıklamalar sunan bir video.\n\nYukarıdaki videolar sadece bir başlangıç noktasıdır. İnternette birinci dereceden denklemlerle ilgili birçok başka video da bulunmaktadır. Hangi videonun size en uygun olduğunu görmek için farklı kanalları keşfedebilirsiniz. \n\nUnutmayın, matematik öğrenmenin en önemli yolu **uygulamadır**. Videoları izlerken, gördüklerinizi kendi başınıza çözmeye çalışın. Problemlerle karşılaştığınızda ise korkmayın, tekrar izleyin veya başka kaynaklara danışın. \n",
        ],
        },
        {
        "role": "user",
        "parts": [
            "x + 2 = 0 problemindeki matematik konusunu nedir. Bu konuyu öğrenmem için bana youtube'dan video önerir misin ?",
        ],
        },
        {
        "role": "model",
        "parts": [
            "```json\n{\"konu\": \"Birinci Dereceden Denklemler\", \"youtube_videoları\": [\"https://www.youtube.com/watch?v=b29T6sG6f5I\", \"https://www.youtube.com/watch?v=NnV_Xs-C27M\", \"https://www.youtube.com/watch?v=7X84V5jZ5lM\", \"https://www.youtube.com/watch?v=a3gY-9gXvYc\"]}\n\n\n```",
        ],
        },
    ]
    )

    # Yanıt alınıyor
    response = chat_session.send_message(f"{math_text} problemindeki konuyu güncel ve popüler videolarla öğrenmek istiyorum. Bana son dönemde yayınlanmış YouTube videoları önerebilir misin?")

    # Yanıtı konsola yazdırma (veri yapısını kontrol etmek için)
    print("Response text:", response.text)

    try:
        # JSON formatına çevirme
        json_data = json.loads(response.text)

        return json_data

    except json.JSONDecodeError as e:
        print("JSON hatası:", e)
        return {"urls": []}  # JSON hatası durumunda da boş dizi döndür
