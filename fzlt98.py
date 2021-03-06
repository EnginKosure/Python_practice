lst, p = [1, 2, 3, 4], [[]]
for _ in lst:
    p = [[a] + b for a in lst for b in p if a not in b]
print(p)
# Second approach with explanation
# lst = [1,2,3]
# r = [[]]
# for _ in lst:
#     r = [i + [j] for i in r for j in lst if j not in i]
# print(r)
# Boş bir permütasyon listesi oluşturup bize verilen listedeki elemanları bu listeye ekleyerek yeni permütasyon listesi oluşturuyoruz. Bu işlemi de listenin eleman sayısı kadar tekrar ediyoruz.
# Başlangıçta r = [[]] boş bir dizi
# Bana verilen dizi lst = [1,2,3]
# lst listesi üzerinde ve r listesi üzerinde 2 tane for ile geziyorum.
# for i in r for j in lst
# r listesinde şu an üzerinde bulunduğum elemanda, lst listesinin şu anki elemanı yoksa, ikisini birleştiriyorum ve onu yeni listeme eleman olarak ekliyorum.
# if j not in i    # var mı diye kontrol
# i + [j]          # yoksa ikisini birleştir
# Bu işlem sonunda elde ettiğim yeni listeyi her seferinde r değişkenine atayarak yeni bir liste elde ediyorum.
#  r = [i + [j] for i in r for j in lst if j not in i]
# Bu işlemi de lst eleman sayısı kadar tekrar ediyorum.
# for _ in lst:
# Adım adım gidecek olursak: for _ in lst: ile başlıyoruz.
# 1. İterasyon
# şu an r = [[]]
# r ve lst elemanlarında geziyorum.
# ilk  eleman 1; r listesinin elemanı [] ve 1 bunun içinde yok, ikisini birleştiriyorum. [1] elde ediyorum ve bunu yeni listeme ekliyorum. yeni liste = [[1]]
# ikinci eleman 2; aynı işlemden sonra yeni liste = [[1],[2]]
# üçüncü eleman 3; aynı işlemden sonra yeni liste = [[1], [2], [3]]
# bu döngülerin hepsi tamamlandıktan sonra yeni listemi r değişkenine atıyorum ve r = [[1], [2], [3]] oluyor.
# 2. İterasyon
# şu an r = [[1], [2], [3]]
# r ve lst elemanlarında geziyorum.
# r listesinin ilk elemanı [1], sırayla lst elemanlarına bakıyorum.
# lst nin ilk elemanı 1, [1] içinde 1 olduğu için işlem yapmıyorum. yeni liste = []
# lst nin ikinci elemanı 2, [1] içinde 2 yok, o zaman ikisini birleştiriyorum [1,2] ve yeni listeme atıyorum yeni liste = [[1,2]]
# lst nin üçüncü elemanı 3, [1] içinde 3 yok, o zaman ikisini birleştiriyorum [1,3] ve yeni listeme atıyorum yeni liste = [[1,2], [1,3]]
# sonra r listesinin ikinci elemanı olan [2] için aynı işlemleri tekrar ediyorum. yeni liste = [[1, 2], [1, 3], [2, 1], [2, 3]] oluyor.
# sonra r listesinin üçüncü elemanı olan [3] için aynı işlemleri tekrar ediyorum. yeni liste = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]] oluyor.
# bu döngülerin hepsi tamamlandıktan sonra yeni listemi r değişkenine atıyorum ve r = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]] oluyor.
# 3. İterasyon
# şu an r = [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
# r ve lst elemanlarında geziyorum. Artık r nin eleman sayısı 6.
# r listesinin ilk elemanı [1,2], sırayla lst elemanlarına bakıyorum.
# lst nin ilk elemanı 1, [1,2] içinde 1 olduğu için işlem yapmıyorum. yeni liste = []
# lst nin ikinci elemanı 2, [1,2] içinde 2 olduğu için işlem yapmıyorum. yeni liste = []
# lst nin üçüncü elemanı 3, [1,2] içinde 3 yok, o zaman ikisini birleştiriyorum [1,2,3] ve yeni listeme atıyorum yeni liste = [[1,2,3]]
# sonra r listesinin ikinci elemanı olan [1,3] için aynı işlemleri tekrar ediyorum. yeni liste = [[1, 2, 3], [1, 3 ,2]] oluyor.
# sonra r listesinin üçüncü elemanı olan [2,1] için aynı işlemleri tekrar ediyorum. yeni liste = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] oluyor.
# r nin diğer elemanları için de aynı işlemi tekrar edince yeni liste = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] oluyor.
# bu döngülerin hepsi tamamlandıktan sonra yeni listemi r değişkenine atıyorum ve r = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] oluyor
