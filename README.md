# Shortener API

### Koncepcja serwisów i selektorów 
Pisząc to krótkie i proste API wykorzystałem bardzo fajną koncepcję serwisów i selektorów. 
> Funkcjonalność ma być ekstremalnie minimalistyczna, nie chodzi o dodawanie super features 
> (potraktuj to jako podpowiedź :) tu nie trzeba wiele kodować).

Zgadzam się — tak proste API można byłoby spokojnie załatwić za pomocą generic viewsów DRF. Jednak z mojego 
doświadczenia wynika, że w miarę szybkiego rozwoju aplikacji, ich zalety szybko przestają przeważać, a pojawia 
się proporcjonalnie więcej wad, które początkowo są niewidoczne.

Z tego powodu zdecydowałem się oprzeć widoki na APIView i rozdzielić logikę aplikacji na selektory (odczyt) 
oraz serwisy (logika biznesowa), co pozwala zachować przejrzystość.

### Endpointy
W aplikacji są dwa główne endpointy `/shorten` oraz `/resolve`.
* `/shorten` - zwraca skrócony link na podstawie podanego URL-a. W obecnej wersji jest on budowany na podstawie lokalnego hosta aplikacji. W praktyce – w docelowym wdrożeniu – prawdopodobnie wystarczyłoby, żeby backend zwracał jedynie wygenerowany slug, a finalny adres byłby składany po stronie frontendu.

Nie znam szczegółowej architektury docelowej aplikacji, ale bardzo możliwe, że backend działałby za jakimś proxy 
(np. aplikacją frontendową typu Next.js hostowaną pod inną domeną). W takim przypadku frontend i tak musi sam zbudować 
pełny URL, bazując na swoim środowisku.

* `/resolve` - zwraca przypisany adres URL do skróconego linka

Oraz dodatkowo 
* `/<slug:short_code>` - wpisując w przeglądarce odpowiedni kod po slash'u przekieruje ona na oryginalny URL, lecz tak jak pisałem o endpoincie `/shorten` na 99% to w rzeczywistości by tak nie wyglądało ;) 

### Generowanie krótkiego kodu
Do generowania short code'u wykorzystałem bibliotekę `secrets` zamiast standardowego `random`, ponieważ opiera się ona na algorytmach kryptograficznych. Dzięki temu prawdopodobieństwo wygenerowania powtarzającego się kodu jest znacznie mniejsze, co zwiększa bezpieczeństwo i unikalność linków.