"""Builds the Cat & Duck Studio site (EN at /, RU at /ru/) into the given folder.

Game pages and privacy policies stay on https://wobqqq.github.io/<slug>/."""
import json
import pathlib
import sys

SITE = pathlib.Path(sys.argv[1])

LOGO = '''<svg class="logo" viewBox="0 0 120 120" role="img" aria-label="Cat &amp; Duck Studio">
  <circle cx="60" cy="60" r="58" fill="var(--logo-bg)"/>
  <path d="M30 60 L28 30 L50 46 Z" fill="#f2994a"/>
  <path d="M90 60 L92 30 L70 46 Z" fill="#f2994a"/>
  <path d="M33 54 L32 37 L45 47 Z" fill="#ffc9a8"/>
  <path d="M87 54 L88 37 L75 47 Z" fill="#ffc9a8"/>
  <ellipse cx="60" cy="72" rx="35" ry="28" fill="#f2994a"/>
  <path d="M44 66 q4 -5 8 0" stroke="#3a2a1e" stroke-width="3.2" fill="none" stroke-linecap="round"/>
  <path d="M68 66 q4 -5 8 0" stroke="#3a2a1e" stroke-width="3.2" fill="none" stroke-linecap="round"/>
  <path d="M57 74 h6 l-3 3.5 z" fill="#c2553a"/>
  <path d="M60 77.5 q-4 5 -8 2 M60 77.5 q4 5 8 2" stroke="#3a2a1e" stroke-width="2.4" fill="none" stroke-linecap="round"/>
  <circle cx="41" cy="77" r="4.5" fill="#ff8f7a" opacity=".55"/>
  <circle cx="79" cy="77" r="4.5" fill="#ff8f7a" opacity=".55"/>
  <path d="M30 76 h-12 M31 82 h-11 M90 76 h12 M89 82 h11" stroke="#3a2a1e" stroke-width="1.8" stroke-linecap="round" opacity=".55"/>
  <g transform="translate(60 26) rotate(-6)">
    <ellipse cx="0" cy="10" rx="17" ry="11" fill="#ffd25a"/>
    <circle cx="-4" cy="-4" r="10" fill="#ffd25a"/>
    <path d="M-14 -4 q-9 1 -10 4 q6 2 11 0 z" fill="#f28c28"/>
    <circle cx="-6" cy="-6" r="2" fill="#3a2a1e"/>
    <path d="M6 6 q8 -6 12 2 q-6 4 -12 2 z" fill="#f5bf2e"/>
  </g>
</svg>'''

GAMES = [
    ('bag-of-bags', 'game', {
        'ru': ('Пакет с пакетами', 'Сложи все пакеты в один: складывай, поворачивай, вкладывай. 240 уровней.'),
        'en': ('Bag of Bags', 'Fit every bag into one bag: fold, turn and nest. 240 levels.')},
     'https://www.rustore.ru/catalog/app/com.bagofbags.game', '#ffd25a'),
    ('zakatki', 'game', {
        'ru': ('Закатки', 'Разложи огурцы, помидоры и варенье по банкам и закатай крышку. 1000 уровней.'),
        'en': ('Pickle Sort', 'Sort pickles, tomatoes and jam into jars and seal the lid. 1000 levels.')},
     'https://www.rustore.ru/catalog/app/com.picklesort.game', '#f6b93b'),
    ('kto-menya-zaper', 'game', {
        'ru': ('Кто меня запер?', 'Выпусти все машины со двора без единой царапины. 300 уровней.'),
        'en': ('Who Blocked Me?', 'Get every car out of the yard without a scratch. 300 levels.')},
     'https://www.rustore.ru/catalog/app/com.whoblockedme.game', '#ff8a3d'),
    ('dacha', 'game', {
        'ru': ('Дача', 'Посади, собери, продай: огород, теплица, курятник и кот на крыльце.'),
        'en': ('My Dacha', 'Plant, harvest, sell: garden beds, a greenhouse, hens and a cat on the porch.')},
     'https://www.rustore.ru/catalog/app/com.mydacha.game', '#5b9a3c'),
    ('skanvordy', 'game', {
        'ru': ('Уютные Сканворды и Филворды', 'Сканворды со стрелками и филворды на каждый день, крупные буквы.'),
        'en': ('Cozy Scanwords and Word Search', 'Arrow-word puzzles and word searches for every day, large letters.')},
     'https://www.rustore.ru/catalog/app/com.scanwordgames.words', '#c0392b'),
    ('dveri-zakryvayutsya', 'game', {
        'ru': ('Осторожно, двери закрываются!', 'Поезд подъезжает к станции: проведи выходящих пассажиров к дверям. 300 станций.'),
        'en': ('Mind the Doors!', 'The train is pulling in: get the passengers to the doors. 300 stations.')},
     'https://www.rustore.ru/catalog/app/com.mindthedoors.game', '#d3263a'),
    ('fabrika-ulybok', 'game', {
        'ru': ('Фабрика улыбок', 'Собери идеальную улыбку из зубов-пазлов: выступ в выемку, зуб в лунку. 300 уровней.'),
        'en': ('Smile Factory', 'Build the perfect smile from puzzle teeth: bump into dent, tooth into gap. 300 levels.')},
     'https://www.rustore.ru/catalog/app/com.smilefactory.game', '#14a38b'),
    ('kholodilnik-po-polochkam', 'game', {
        'ru': ('Холодильник по полочкам', 'Разложи продукты по полочкам: одна полка — один вид, без щелей, испорченное — в ведро. 300 уровней.'),
        'en': ('Tidy Fridge', 'Put the groceries away: one kind per shelf, no gaps, spoiled food in the bin. 300 levels.')},
     'https://www.rustore.ru/catalog/app/com.tidyfridge.game', '#3e8fd8'),
    ('florist', 'game', {
        'ru': ('Флорист', 'Поверни стебли, чтобы каждый цветок дотянулся до ленты, — и букет расцветёт. 40 букетов в портфолио.'),
        'en': ('Florist', 'Turn the stems until every flower reaches the ribbon, and the bouquet blooms. 40 bouquets to collect.')},
     'https://www.rustore.ru/catalog/app/com.florist.game', '#ff6f91'),
    ('skanvordy-sssr', 'game', {
        'ru': ('Сканворды из СССР', 'Сканворды и филворды о советской жизни: кино, мультики, гастроном, космос. Ведёт дядя Миша из киоска.'),
        'en': ('Scanwords from the USSR', 'Scanwords and word searches about everyday Soviet life: films, cartoons, the grocery, space.')},
     'https://www.rustore.ru/catalog/app/com.sovietscanwords.game', '#d42a1f'),
    ('skanvordy-18', 'game', {
        'ru': ('Сканворды для взрослых', 'Сканворды и филворды 18+ с пикантными вопросами: флирт, застолье, казино. Вечер ведёт мадам Роза.'),
        'en': ('Scanwords for Adults', 'Scanwords and word searches 18+ with cheeky clues: flirting, bars, casino. Hosted by Madame Rosa.')},
     'https://www.rustore.ru/catalog/app/com.adultscanwords.game', '#8e1f4f'),
    ('slova-otaku', 'game', {
        'ru': ('Слова Отаку', 'Аниме филворды: найди слова из любимых тайтлов и мира отаку вместе с лисичкой Юки.'),
        'en': ('Otaku Words', 'Anime word search: find words from your favourite shows and otaku culture with Yuki the fox girl.')},
     'https://www.rustore.ru/catalog/app/com.otakuwords.game', '#ff6fae'),
    ('kanalizatsiya', 'game', {
        'ru': ('Канализация', 'Поверни трубы, чтобы вода из квартиры утекла в канализацию, а зелёная химия — в свой сток. Крыса-сантехник и граффити.'),
        'en': ('Sewer Pipes', 'Turn the pipes so the water runs into the sewer and the green chemicals into their own drain. A plumber rat and graffiti.')},
     'https://www.rustore.ru/catalog/app/com.sewerpipes.game', '#1c86d1'),
    ('aviadispetcher', 'game', {
        'ru': ('Авиадиспетчер: Посадка', 'Посади самолёты и вертолёты, пока не кончилось топливо: 300 уровней в 12 аэропортах, ветер, грозы и ночные смены.'),
        'en': ('Air Dispatcher: Landing', 'Land every plane and helicopter before fuel runs out: 300 levels at 12 airports, wind, storms and night shifts.')},
     'https://www.rustore.ru/catalog/app/com.airdispatcher.game', '#4fb3ff'),
    ('zatyazhnoy-pryzhok', 'game', {
        'ru': ('Затяжной прыжок', 'Реалистичный затяжной прыжок: кольца, девять трюков и групповые прыжки, 300 прыжков над 10 зонами — от летнего луга до стратосферы.'),
        'en': ('Skydive Hero', 'A realistic freefall: rings, nine tricks and jumps with friends, 300 jumps over 10 drop zones, from a summer meadow to the stratosphere.')},
     'https://www.rustore.ru/catalog/app/com.skydivehero.game', '#38c6f4'),
]

# The real AppGallery pages of the games published there (each game's APPGALLERY_URL in tool/game.env);
# the rest fall back to the package link until they are published.
APPGALLERY = {
    'zakatki': 'https://appgallery.huawei.com/app/C119428039',
    'skanvordy': 'https://appgallery.huawei.com/app/C119427985',
    'dveri-zakryvayutsya': 'https://appgallery.huawei.com/app/C119428067',
    'fabrika-ulybok': 'https://appgallery.huawei.com/app/C119428149',
    'kholodilnik-po-polochkam': 'https://appgallery.huawei.com/app/C119428199',
    'bag-of-bags': 'https://appgallery.huawei.com/app/C119427897',
    'kto-menya-zaper': 'https://appgallery.huawei.com/app/C119427693',
    'dacha': 'https://appgallery.huawei.com/app/C119427941',
}

T = {
    'ru': {
        'title': 'Cat & Duck Studio — уютные игры и приложения',
        'desc': 'Cat & Duck Studio: уютные игры для Android. Без интернета, без регистрации, на русском.',
        'tag': 'Уютные игры и приложения',
        'lead': 'Делаем спокойные игры, в которые приятно возвращаться: головоломки, слова и дачу. Играть можно без интернета и без регистрации.',
        'all': 'Все', 'android': 'Android', 'web': 'Веб',
        'games': 'Игры', 'soon': 'скоро',
        'store': 'Скачать в RuStore', 'gallery': 'Скачать в AppGallery', 'more': 'Подробнее',
        'privacy': 'Конфиденциальность',
        'web_title': 'Скоро в браузере',
        'web_text': 'Наши игры появятся в вебе: открыл страницу — и играешь, ничего не устанавливая.',
        'f1': ('Без интернета', 'Все игры работают офлайн.'),
        'f2': ('Без регистрации', 'Никаких аккаунтов и паролей.'),
        'f3': ('Бережно к вам', 'Не собираем личные данные.'),
        'contact': 'Связаться с нами',
        'game': 'Игра', 'count': 'игр',
        'empty': 'Здесь пока пусто — но скоро будет.',
    },
    'en': {
        'title': 'Cat & Duck Studio — cozy games and apps',
        'desc': 'Cat & Duck Studio: cozy games for Android. Offline, no sign-up.',
        'tag': 'Cozy games and apps',
        'lead': 'We make calm games you like coming back to: puzzles, words and a country garden. Play offline, no sign-up.',
        'all': 'All', 'android': 'Android', 'web': 'Web',
        'games': 'Games', 'soon': 'soon',
        'store': 'Get it on RuStore', 'gallery': 'Get it on AppGallery', 'more': 'Details',
        'privacy': 'Privacy',
        'web_title': 'Coming to the browser',
        'web_text': 'Our games are coming to the web: open the page and play, nothing to install.',
        'f1': ('Offline', 'Every game works without the internet.'),
        'f2': ('No sign-up', 'No accounts, no passwords.'),
        'f3': ('Respectful', 'We do not collect personal data.'),
        'contact': 'Contact us',
        'game': 'Game', 'count': 'games',
        'empty': 'Nothing here yet — but soon.',
    },
}

CSS = '''
:root {
  --bg: #fff8ec; --bg2: #ffeccc; --card: #ffffff; --ink: #2d241c; --soft: #6b5d50;
  --accent: #b5481a; --accent-ink: #ffffff; --edge: #eadcc4; --chip: #fff1da; --logo-bg: #fff1da;
  --shadow: 0 2px 0 var(--edge), 0 10px 24px rgba(90, 55, 20, .08);
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1d1712; --bg2: #2a2018; --card: #2a221b; --ink: #f6ebdc; --soft: #c2b29f;
    --accent: #ff9a5c; --accent-ink: #1d1712; --edge: #3a2f25; --chip: #33291f; --logo-bg: #3a2e22;
    --shadow: 0 2px 0 #120e0a, 0 10px 24px rgba(0, 0, 0, .3);
  }
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 17px/1.55 "Nunito", system-ui, sans-serif; }
a { color: var(--accent); }
.wrap { max-width: 1120px; margin: 0 auto; padding: 0 16px; }
header.top { display: flex; align-items: center; justify-content: space-between; padding: 18px 0; }
.brand { display: flex; align-items: center; gap: 10px; color: var(--ink); text-decoration: none; font-weight: 800; font-size: 19px; }
.brand .logo { width: 40px; height: 40px; }
.switch { display: flex; gap: 2px; background: var(--chip); padding: 4px; border-radius: 999px; }
.switch a { color: var(--soft); text-decoration: none; font-weight: 800; font-size: 14px; padding: 5px 12px; border-radius: 999px; }
.switch a[aria-current="page"] { background: var(--card); color: var(--ink); box-shadow: 0 1px 0 var(--edge); }
.hero { position: relative; overflow: hidden; border-radius: 32px; padding: 48px 28px 40px; margin: 6px 0 28px;
  background: radial-gradient(circle at 85% 20%, rgba(255, 210, 90, .55), transparent 45%),
              radial-gradient(circle at 10% 90%, rgba(242, 153, 74, .35), transparent 50%), var(--bg2);
  display: grid; grid-template-columns: 1fr auto; gap: 28px; align-items: center; }
.hero h1 { font-size: clamp(34px, 6vw, 58px); line-height: 1.05; margin: 0 0 6px; letter-spacing: -.02em; font-weight: 900; }
.hero .tag { font-size: clamp(19px, 2.6vw, 24px); font-weight: 700; color: var(--accent); margin: 0 0 14px; }
.hero p.lead { max-width: 560px; margin: 0; color: var(--soft); font-size: 18px; }
.hero .logo { width: clamp(140px, 22vw, 230px); height: auto; filter: drop-shadow(0 12px 18px rgba(90, 55, 20, .18)); animation: bob 6s ease-in-out infinite; }
@keyframes bob { 50% { transform: translateY(-6px) rotate(-2deg); } }
@media (prefers-reduced-motion: reduce) { .hero .logo { animation: none; } }
.platforms { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 20px; }
.pill { display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 999px; background: var(--card); font-size: 14px; font-weight: 700; box-shadow: 0 1px 0 var(--edge); }
.pill small { font-weight: 600; color: var(--soft); }
.bar { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin: 8px 0 16px; }
.bar h2 { margin: 0; font-size: 28px; font-weight: 900; }
.tabs { display: flex; gap: 6px; background: var(--chip); padding: 4px; border-radius: 999px; }
.tabs button { border: 0; background: transparent; color: var(--soft); font: inherit; font-size: 15px; font-weight: 700; padding: 7px 14px; border-radius: 999px; cursor: pointer; }
.tabs button[aria-pressed="true"] { background: var(--card); color: var(--ink); box-shadow: 0 1px 0 var(--edge); }
.grid { list-style: none; padding: 0; margin: 0; display: grid; gap: 18px; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
.card { position: relative; background: var(--card); border-radius: 24px; padding: 18px; box-shadow: var(--shadow); display: flex; flex-direction: column; gap: 12px; transition: transform .18s ease, box-shadow .18s ease; }
.card::before { content: ""; position: absolute; inset: 0 0 auto 0; height: 72px; border-radius: 24px 24px 0 0; background: linear-gradient(180deg, var(--c), transparent); opacity: .22; pointer-events: none; }
.card:hover { transform: translateY(-4px); box-shadow: 0 2px 0 var(--edge), 0 18px 32px rgba(90, 55, 20, .14); }
.card .head { position: relative; display: flex; gap: 14px; align-items: center; color: var(--ink); text-decoration: none; }
.card img { width: 76px; height: 76px; border-radius: 20px; flex: none; box-shadow: 0 4px 10px rgba(90, 55, 20, .18); }
.card h3 { margin: 0; font-size: 19px; line-height: 1.2; font-weight: 800; }
.card .badges { display: flex; gap: 6px; margin-top: 6px; flex-wrap: wrap; }
.badge { font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 999px; background: var(--chip); color: var(--soft); }
.badge.soon { opacity: .75; }
.card p { margin: 0; color: var(--soft); font-size: 15px; flex: 1; }
.card .actions { display: flex; gap: 10px; align-items: center; justify-content: space-between; flex-wrap: wrap; }
.btn { display: inline-flex; align-items: center; justify-content: center; padding: 9px 14px; border-radius: 14px; background: var(--accent); color: var(--accent-ink); font-weight: 800; font-size: 14px; text-decoration: none; }
.card .stores { display: flex; gap: 8px; flex-wrap: wrap; }
.btn.ghost { background: var(--chip); color: var(--ink); }
.card .legal { font-size: 13px; color: var(--soft); }
.card.web { border: 2px dashed var(--edge); background: transparent; box-shadow: none; justify-content: center; text-align: center; align-items: center; min-height: 200px; }
.card.web p { flex: none; }
.card.web::before { display: none; }
.card.web .big { font-size: 44px; line-height: 1; }
.empty { color: var(--soft); padding: 24px 0; }
.features { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 44px 0 24px; }
.feature { background: var(--card); border-radius: 22px; padding: 18px; box-shadow: var(--shadow); }
.feature b { display: block; font-size: 17px; margin-bottom: 2px; }
.feature span { color: var(--soft); font-size: 15px; }
.feature i { font-style: normal; font-size: 26px; display: block; margin-bottom: 6px; }
footer { padding: 28px 0 48px; color: var(--soft); font-size: 15px; display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; border-top: 1px solid var(--edge); margin-top: 28px; }
[hidden] { display: none !important; }
.crumbs { font-size: 14px; color: var(--soft); margin: 0 0 10px; }
.crumbs ol { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; }
.crumbs li + li::before { content: "›"; margin: 0 8px; opacity: .6; }
.crumbs a { color: inherit; text-decoration: none; }
.crumbs a:hover { color: var(--accent); }
.crumbs [aria-current] { color: var(--ink); font-weight: 700; }
@media (max-width: 720px) {
  .hero { grid-template-columns: 1fr; padding: 30px 20px 28px; border-radius: 26px; text-align: left; }
  .hero .logo { order: -1; width: 120px; }
  .features { grid-template-columns: 1fr; }
  .bar h2 { font-size: 24px; }
}
@media (max-width: 420px) {
  .grid { grid-template-columns: 1fr; }
}
'''

JS = '''
(function () {
  var buttons = document.querySelectorAll('.tabs button');
  var cards = document.querySelectorAll('.grid > li');
  var empty = document.querySelector('.empty');
  function show(f) {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = f === 'all' || (' ' + c.dataset.p + ' ').indexOf(' ' + f + ' ') >= 0;
      c.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.f === f)); });
  }
  buttons.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.f); }); });
})();
'''


def page(lang):
    t = T[lang]
    # English is the main page (/), Russian lives in /ru/; game pages are
    # Russian at /<slug>/ and English at /<slug>/en/.
    up = '' if lang == 'en' else '../'
    games = 'https://wobqqq.github.io/'
    priv = 'privacy.html' if lang == 'ru' else 'en/privacy.html'
    home = '' if lang == 'ru' else 'en/'
    en_href, ru_href = ('./', 'ru/') if lang == 'en' else ('../', './')
    switch = (f'<nav class="switch" aria-label="Language"><a href="{en_href}" hreflang="en"'
              f'{" aria-current=\"page\"" if lang == "en" else ""}>EN</a><a href="{ru_href}" hreflang="ru"'
              f'{" aria-current=\"page\"" if lang == "ru" else ""}>RU</a></nav>')
    cards = []
    for slug, _kind, names, store, color in GAMES:
        name, text = names[lang]
        # AppGallery button on every game, even before the game is published there (owner, 2026-10-17).
        gallery = APPGALLERY.get(slug, 'https://appgallery.huawei.com/app/detail?id=' + store.rsplit('/', 1)[1])
        cards.append(f'''<li class="card" data-p="android" style="--c:{color}">
  <a class="head" href="{games}{slug}/{home}"><img src="{games}{slug}/icon_512.png" alt="" width="76" height="76" loading="lazy"><div><h3>{name}</h3><div class="badges"><span class="badge">Android</span></div></div></a>
  <p>{text}</p>
  <div class="actions"><span class="stores"><a class="btn" href="{store}">{t['store']}</a><a class="btn" href="{gallery}">{t['gallery']}</a></span><a class="legal" href="{games}{slug}/{priv}">{t['privacy']}</a></div>
</li>''')
    home_url = 'https://wobqqq.github.io/cat-and-duck-studio/'
    alt = (f'<link rel="alternate" hreflang="en" href="{home_url}">'
           f'<link rel="alternate" hreflang="ru" href="{home_url}ru/">'
           f'<link rel="alternate" hreflang="x-default" href="{home_url}">')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<link rel="icon" href="{up}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="{up}favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{up}favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{up}apple-touch-icon.png">
<link rel="manifest" href="{up}site.webmanifest">
<meta name="theme-color" content="#f2994a">
<meta property="og:title" content="Cat &amp; Duck Studio">
<meta property="og:description" content="{t['desc']}">
<meta property="og:image" content="https://wobqqq.github.io/cat-and-duck-studio/icon-512.png">
{alt}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"wobqqq","item":"https://wobqqq.github.io/"}},{{"@type":"ListItem","position":2,"name":"Cat & Duck Studio","item":"{home_url}{'ru/' if lang == 'ru' else ''}"}}]}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top"><a class="brand" href="./">{LOGO}<span>Cat &amp; Duck Studio</span></a>{switch}</header>
<nav class="crumbs" aria-label="{'Навигация' if lang == 'ru' else 'Breadcrumb'}"><ol><li><a href="https://wobqqq.github.io/">wobqqq</a></li><li><span aria-current="page">Cat &amp; Duck Studio</span></li></ol></nav>
<section class="hero">
  <div>
    <h1>Cat &amp; Duck Studio</h1>
    <p class="tag">{t['tag']}</p>
    <p class="lead">{t['lead']}</p>
    <div class="platforms"><span class="pill">🤖 Android</span><span class="pill">🎮 {len(GAMES)} {t['count']}</span></div>
  </div>
  {LOGO}
</section>
<main>
<div class="bar"><h2>{t['games']}</h2></div>
<ul class="grid">
{chr(10).join(cards)}
</ul>
<section class="features">
  <div class="feature"><i>📴</i><b>{t['f1'][0]}</b><span>{t['f1'][1]}</span></div>
  <div class="feature"><i>🙅</i><b>{t['f2'][0]}</b><span>{t['f2'][1]}</span></div>
  <div class="feature"><i>🛡️</i><b>{t['f3'][0]}</b><span>{t['f3'][1]}</span></div>
</section>
</main>
<footer><span>© <span class="year">2026</span> Cat &amp; Duck Studio</span><span>{t['contact']}: <a href="mailto:serzakharevich@yandex.by">serzakharevich@yandex.by</a></span></footer>
</div>
<script>document.querySelectorAll(".year").forEach(function (e) {{ e.textContent = new Date().getFullYear(); }});</script>
</body>
</html>
'''


(SITE / 'index.html').write_text(page('en'))
(SITE / 'ru').mkdir(exist_ok=True)
(SITE / 'ru' / 'index.html').write_text(page('ru'))
(SITE / 'tool' / 'logo.svg').write_text(
    LOGO.replace('class="logo" ', 'xmlns="http://www.w3.org/2000/svg" width="512" height="512" ')
        .replace('var(--logo-bg)', '#fff1da'))
manifest = {
    'name': 'Cat & Duck Studio', 'short_name': 'Cat & Duck', 'start_url': './', 'scope': './',
    'display': 'browser', 'background_color': '#fff8ec', 'theme_color': '#f2994a',
    'icons': [{'src': 'icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
              {'src': 'icon-512.png', 'sizes': '512x512', 'type': 'image/png'}],
}
(SITE / 'site.webmanifest').write_text(json.dumps(manifest, indent=1, ensure_ascii=False))
