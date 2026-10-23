"""English mirror of the blog data: every post and category gets an English
title, slug and excerpt so the English mockup shows the same layout as the
Portuguese one. Only the "languages" post has a real English page; post_links.py
points the rest at it."""
from common import posts as P, cats

CAT = {  # pt name: (en name, en slug)
    "Viva": ("Living", "living"), "Coaching": ("Coaching", "coaching"), "Homenagens": ("Tributes", "tributes"),
    "Casos de Sucesso": ("Success Stories", "success-stories"), "Inspiração": ("Inspiration", "inspiration"),
    "Irlanda": ("Ireland", "ireland"), "Geral": ("General", "general"), "Idiomas": ("Languages", "languages"),
    "Liderança": ("Leadership", "leadership"), "Presepadas": ("Mishaps", "mishaps"), "Viagens": ("Travel", "travel"),
    "Empreendedorismo": ("Entrepreneurship", "entrepreneurship"), "Gestão de tempo": ("Time Management", "time-management"),
    "Músicas": ("Music", "music"), "Princípios Básicos": ("Basic Principles", "basic-principles"),
}
CAT_SLUG = {c["slug"]: CAT[c["name"]][1] for c in cats}

POSTS = {  # pt slug: (en title, en slug, en excerpt, en alt)
    "um-turbo-para-metas-pessoais": ("A turbo boost for personal goals", "a-turbo-boost-for-personal-goals",
        "After failing a lot at personal goals, I decided to build a tool to manage myself better, and it has been working well.", "Dashboard for managing personal goals"),
    "quem-e-mineiro-me-entende": ("If you're from Minas, you get me", "if-youre-from-minas-you-get-me",
        "The culture of Minas Gerais is so unique that it has its own vocabulary, so obvious to us mineiros that it's almost hard to explain.", "The Minas Gerais 'trem'"),
    "mas-me-conta-como-voces-dois-se-conheceram": ("So tell me, how did you two meet?", "so-tell-me-how-did-you-two-meet",
        "If you're curious but don't have time for the whole story, here is the short version. But if you want, we can grab a beer and I'll gladly tell it again, because it's one of my favorite stories. 🙂", "Gui and Joice at Inhotim"),
    "psicologo-e-so-para-doidos": ("Therapy is only for crazy people", "therapy-is-only-for-crazy-people",
        "A different way to think about therapy, based on my own experience. And if it's only for crazy people, maybe I really am crazy.", "Man in a straitjacket in a bathtub"),
    "o-preco-da-midia-gratuita": ("The price of free media", "the-price-of-free-media",
        "Broadcast TV and \"free\" social networks have a much stronger influence on our lives than we imagine.", "Life without television"),
    "um-dia-de-batima": ("A day as Batman", "a-day-as-batman",
        "You know that silly thing that makes you laugh? One of mine was dressing up as Batman and goofing around the university in Viçosa.", "A day as Batman"),
    "invictus-o-poema-que-inspirou-nelson-mandela": ("Invictus: the poem that inspired Nelson Mandela", "invictus-the-poem-that-inspired-nelson-mandela",
        "The story of a short poem on a piece of paper that made a difference in Nelson Mandela's life during his 27 years in prison.", "Young Nelson Mandela"),
    "as-pequenas-grandes-hipoteses-do-dia-dia": ("The small big assumptions of everyday life", "the-small-big-assumptions-of-everyday-life",
        "A good tip on how to deal with the hundreds of assumptions we make up in our heads every day.", "Girl thinking"),
    "o-que-te-impede-de-aprender-outro-idioma": ("What stops you from learning another language?", "what-stops-you-from-learning-another-language",
        "Many of us dream of mastering a second language, but sometimes it takes lessons you won't find in any grammar book.", "Puzzle pieces painted with flags from different countries"),
    "aumentando-sua-auto-confianca-em-apenas-2-minutos": ("Boosting your self-confidence in just 2 minutes", "boosting-your-self-confidence-in-just-2-minutes",
        "It's no longer hard to believe that our body shows part of our thoughts through gestures. But what about the other way around?", "Hero body language"),
    "inspiracao-de-vida-e-empreendedora": ("An inspiring life and business story", "an-inspiring-life-and-business-story",
        "One of the most inspiring Brazilian life and business stories of our time. From street vendor to TV network owner, without losing his good humor.", "Silvio Santos and a Shih Tzu"),
    "welcome-back": ("Welcome back", "welcome-back",
        "The blog is back! After a year without posts, it has a brand-new look. Take a look and tell me what you think. 🙂", "We're back"),
    "lideranca-em-um-minuto": ("One-minute leadership", "one-minute-leadership",
        "In business it's sometimes easy to get confused about leadership and power, especially for managers. A manager only uses power when giving orders to the team without caring whether they are motivated to do it. The most common case is when employees do tasks only because they need the…", ""),
    "o-desapego-o-amor-e-os-ciclos-da-vida": ("Letting go, love and the cycles of life", "letting-go-love-and-the-cycles-of-life",
        "One thing I learned after taking a few hits from life is that it is made of cycles. We often hold on to something that was part of our past, hoping it will keep doing us good, or just because letting go is hard. It turns out that sometimes a cycle ends without…", ""),
    "feliz-dia-dos-pais": ("Happy Father's Day", "happy-fathers-day",
        "In Brazil, Father's Day is celebrated on the second Sunday of August, which in 2015 falls on the 9th, that is, today. I've been following the emotions of a friend who recently became a father, from the shock of the pregnancy news to the huge joy of his little one calming down when lying on his…", ""),
    "suporte-aos-desabrigados-na-irlanda": ("Supporting the homeless in Ireland", "supporting-the-homeless-in-ireland",
        "Even though Ireland is a well-developed European country, it has its social problems too. The best known is certainly alcoholism, which affects a good part of the population here, and smoking as well. Working as a flyer distributor, I met the simpler people of the city and could see that smoking…", ""),
    "sawabona-shikoba": ("Sawabona Shikoba", "sawabona-shikoba",
        "Something we sometimes pretend we can do is predict what will happen tomorrow but, even in a world full of technology, tomorrow is uncertain. And our everyday life is always a rush. We run to work, work to pay the bills, do the math to travel, travel…", ""),
    "o-dia-bonito-longe-do-equador": ("A lovely day far from the equator", "a-lovely-day-far-from-the-equator",
        "It's funny. I always saw on TV, mostly in foreign movies, people saying something like \"Isn't it a lovely day?\" about a sunny day with clear skies and little wind(*). And as nice as a hot sunny day is, deep down for me it still…", ""),
    "o-mercadinho-brasileiro-e-os-10-centavos": ("The Brazilian corner shop and the 10 cents", "the-brazilian-corner-shop-and-the-10-cents",
        "Last Saturday I decided to throw a barbecue to celebrate my birthday here in Dublin. Then came the rush to prepare some dishes the night before, wake up early on Saturday and buy everything in the morning for the barbecue that same afternoon. My mother has been trying to teach me for some 28 years not to leave…", ""),
    "o-slane-castle-e-o-rock-and-roll": ("Slane Castle and rock and roll", "slane-castle-and-rock-and-roll",
        "Last Saturday, May 30, 2015, came the long-awaited Foo Fighters and Kaiser Chiefs show at Slane Castle, in County Meath, Ireland. The castle has become known for hosting music acts like Queen, Bob Dylan, the Rolling Stones, Guns N' Roses, U2, Red Hot Chili Peppers, Bryan…", ""),
    "parabens-maes": ("Happy Mother's Day!", "happy-mothers-day",
        "Still in the mood for tributes, I'd simply like to wish a happy Mother's Day to my mothers (Guiomar, Fiinha and Sola) and to all mothers who so often give up their own wishes and needs to look after their children.", ""),
    "mulheres": ("Women", "women",
        "One thing I learned at home is to always deeply respect women, regardless of age, ethnicity, hair color or anything else. And that's what I've always done. So I'd like to share here a text that is already well known on the internet, but still excellent for dealing with such an important subject…", ""),
    "o-inicio-dos-sonhos": ("Where dreams begin", "where-dreams-begin",
        "A true story about the hard decision to chase your own dreams, and then make them come true.", ""),
}

posts = []
for p in P:
    title, slug, excerpt, alt = POSTS[p["slug"]]
    cname, cslug = CAT[p["cat"]]
    posts.append(dict(title=title, slug=slug, path=f"/en/{cslug}/{slug}/", cat=cname, cat_slug=cslug,
                      date=p["date"], excerpt=excerpt, cover=p["cover"], alt=alt, pt_slug=p["slug"], pt_path=p["path"]))
by_pt = {p["pt_slug"]: p for p in posts}
cats_en = [dict(c, name=CAT[c["name"]][0], slug=CAT[c["name"]][1], pt_name=c["name"], pt_slug=c["slug"]) for c in cats]

TAG = {"desenvolvimento-pessoal": ("Personal Growth", "personal-growth")}

CAT_OBJ = {"Living": "sprout", "Coaching": "target", "Tributes": "heart", "Success Stories": "trophy", "Inspiration": "bulb",
           "Ireland": "clover", "General": "mug", "Languages": "chat", "Leadership": "flag", "Mishaps": "laugh",
           "Travel": "suitcase", "Entrepreneurship": "rocket", "Time Management": "clock", "Music": "note", "Basic Principles": "book"}
