# from natasha.markup import show_markup, show_json
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,    
    PER,
    LOC,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,
    Doc
)

test_data = "Это некоторый текст с персональными данными. Старченко Даниэлла Геннадьевна \
            родилась в г.Белгород. Место прописки: Белгородская обл. Белгородский р-н. п.Северный \
            ул.Меловая, 4. Паспорт 1418 777777 выдан УМВД России по Белгородской области. \
            Дата рождения: 30.07.1998. Некоторый персональный сайт имеет адрес https://google.com. \
            Семейное положение: не замужем. Место работы ООО Глоубайт. Сайт организации: glowbyteconsulting.com \
            Занимаемая должность: старший консультант. Зароботная плара 1 руб. или 1 RUB. \
            Владение языками: русский, английский.  \
            История болезней: аневризма сонной артерии, аритмия. Еще тут адреса больничек можно скрывать: \
            Находилась на лечении в Курской обласной клинической больнице кардиология и НИИ Бурденко \
            нейрохирургическое отделение. ИНН 7727563778. Какие нибудь данные про банк, который обслуживает: \
            ПАО Сбербанк БИК 044525225 КПП 773643002. Еще что нибуль про инвалид 3 группы. Получает социальное пособие в \
            размере 10000 руб. (Десяти тысяч рублей). Еще что то про медицинстую сторону: произведена имплантация электро кардиостимулятора (ЭКС) \
            07.11.2019. Еще что то про доступы к паролям и технологическим данным можно было бы. Email: laliande7@gmail.com \
            образование: НИУ БелГУ"

test_data2 = '''
Благодарственное письмо   Хочу поблагодарить учителей моего, теперь уже бывшего, одиннадцатиклассника:  Бушуева Вячеслава Владимировича и Бушуеву Веру Константиновну. Они вовлекали сына в интересные внеурочные занятия, связанные с театром и походами.
Благодарю прекрасного учителя 1"А" класса - Волкову Наталью Николаевну, нашего наставника, тьютора - Ларису Ивановну, за огромнейший труд, чуткое отношение к детям, взаимопонимание! Огромное спасибо!
'''

def search(text=test_data):
    segmenter = Segmenter()
    morph_vocab = MorphVocab()

    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)

    names_extractor = NamesExtractor(morph_vocab)
    dates_extractor = DatesExtractor(morph_vocab)
    money_extractor = MoneyExtractor(morph_vocab)
    addr_extractor = AddrExtractor(morph_vocab)

    doc = Doc(text)
    doc.segment(segmenter) 
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    #находим даты в тексте
    # dates = dates_extractor(text)
    # facts = [i.fact.as_json for i in dates]
    # print(facts)
    
    #находим имена
    for span in doc.spans:
        if span.type == PER:
            span.extract_fact(names_extractor)
    names_dict = {_.normal: _.fact.as_dict for _ in doc.spans if _.fact}

if __name__ == '__main__':
    search()