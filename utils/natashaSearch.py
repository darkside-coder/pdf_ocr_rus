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
import re

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

def find_names(names_extractor,line):
    result = []
    names = names_extractor.find(line)
    if names is not None:
        first_name = names_extractor.find(line).fact.first
        last_name = names_extractor.find(line).fact.last
        middle = names_extractor.find(line).fact.middle
        if first_name is not None:
            result.append(first_name)
        if last_name is not None:
            result.append(last_name)
        if middle is not None:
            result.append(middle)
    return result

def find_addrs(addr_extractor, line):
    result = []
    addrs = addr_extractor.find(line)
    if addrs is not None:
        data = addrs.fact.parts
        for i in range(len(data)):
            result.append(addrs.fact.parts[i].value)
    return result

def find_dates(dates_extractor, line):
    result = []
    dates = dates_extractor.find(line)
    #тут нужно сделать так, чтоб дата собиралась в дату сразу
    if dates is not None:
        year = dates.fact.year
        if year is not None:
            result.append(year)
        month = dates.fact.month
        if month is not None:
            result.append(month)
        day = dates.fact.day
        if day is not None:
            result.append(day)
    return result

def find_money(money_extractor, line):
    result = []
    money = money_extractor.find(line)
    if money is not None:
        print(money)
    return result

def mute_text(data, addrs, money, names, dates):
    for i in range(len(data)):
        for elem in addrs:
            if data[i].startswith(str(elem)):
                data[i] =  "<ADDR>"

        for elem in money:
            if data[i].startswith(str(elem)):
                data[i] =  "<MONEY>"
        
        for elem in names:
            if data[i].startswith(str(elem)):
                data[i] =  "<NAME>"
        for elem in dates:
            if data[i].startswith(str(elem)):
                data[i] =  "<DATE>"
    return " ".join(data)

def search(text=test_data):
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)
    # типы данных, которые можно парсить
    names_extractor = NamesExtractor(morph_vocab)
    dates_extractor = DatesExtractor(morph_vocab)
    money_extractor = MoneyExtractor(morph_vocab)
    addr_extractor = AddrExtractor(morph_vocab)
    sentences = text.split(" ")
    lines = [sentences[i:i + 9] for i in range(0, len(sentences), 9)]
    names = []
    addrs = []
    money = []
    dates = []
    for line in lines:
        line = " ".join(line)
        names  += find_names(names_extractor, line)
        money += find_money(money_extractor, line)
        addrs += find_addrs(addr_extractor, line)
        dates += find_dates(dates_extractor, line)
    result = mute_text(sentences, addrs, money, names, dates)
    print(result)
    return result

if __name__ == '__main__':
    search()