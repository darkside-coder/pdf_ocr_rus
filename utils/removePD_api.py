# https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html данные, которые распознает амазон
# Идея для презы: вот этот код поиска ПД должен выполнятся в каком нибудь блокчейне, чтоб ни у кого не было доступа к data, которое тут обрабатывается
# Суть в том, что некоторые данные определяются с помощью регулярок, а некоторые с помощью словарей. 
# Отсюда брала список ПД https://www.freshdoc.ru/zashita_personalnyh_dannyh/docs/other/perechen_personalnyh_dannyh_zashita_v_ispdn/
# Всякие имена организацией и людей будут опередлятся по признакам имен собственных. 
# Томита парсер https://yandex.ru/dev/tomita/
import re
from utils.natashaSearch import search

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

def detect_organization_name(data):
    # для определений мест работы. 
    pass

def detect_position(data):
    # для определений должностей
    pass

def detect_names(data=test_data):
    data = re.sub(r"\b[А-Я][а-я]+(ко|ла|на|ев|ин|ина|ева|ов|ова|ян|ей|ва|на|ич|ир|вy|го)\b", "<NAME_REG>", data)
    return data

def detect_url(data=test_data):
    ## для определений сайтов и урлов
    ul = '\u00a1-\uffff'  
    ipv4_re = r'(?:0|25[0-5]|2[0-4]\d|1\d?\d?|[1-9]\d?)(?:\.(?:0|25[0-5]|2[0-4]\d|1\d?\d?|[1-9]\d?)){3}'
    ipv6_re = r'\[?((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,'\
                    r'4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{'\
                    r'1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2['\
                    r'0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,'\
                    r'3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|['\
                    r'1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,'\
                    r'2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|((['\
                    r'0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2['\
                    r'0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:['\
                    r'0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2['\
                    r'0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,'\
                    r'5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\]?'
    hostname_re = r'[a-z' + ul + r'0-9](?:[a-z' + ul + r'0-9-]{0,61}[a-z' + ul + r'0-9])?'
    domain_re = r'(?:\.(?!-)[a-z' + ul + r'0-9-]{1,63}(?<!-))*'
    tld_re = (
            r'\.'                               
            r'(?!-)'                             
            r'(?:[a-z' + ul + '-]{2,63}'         
            r'|xn--[a-z0-9]{1,59})'              
            r'(?<!-)'                           
            r'\.?'                               
            )
    host_re = '(' + hostname_re + domain_re + tld_re + '|localhost)'
    url_re = re.compile(
            r'([a-z0-9.+-]*:?//)?'                                      
            r'(?:[^\s:@/]+(?::[^\s:@/]*)?@)?'                          
            r'(?:' + ipv4_re + '|' + ipv6_re + '|' + host_re + ')'
            r'(?::\d{2,5})?'                                           
            r'(?:[/?#][^\s]*)?',                                        
            re.IGNORECASE
            )
    data = re.sub(url_re, "<URL>", data) 
    return data

def detect_INN(data=test_data):
    # Для определений ИНН. Нужно сделать так, чтоб между словом ИНН и самими цифрами могли пройти спец.символы
    inn_re = r'ИНН\x20*(\d{10})'
    data = re.sub(inn_re, "<INN>", data)
    return data

def detect_passport(data):
    # для определения паспортных данных
    passport_re = r"\b[0-9]{4} \b([0-9]{6})\b"
    #passport_re = r"^(?!^0+$)[a-zA-Z0-9]{3,20}$"
    data = re.sub(passport_re, "<PASSPORT>", data)
    return data

def detect_edu(data):
    # для определения образования
    pass

def detect_dict(data):
    # для определений по ключевым словам из словаря
    pass

def detect_money(data):
    # для определения денежных сумм. Нужно подумать, как определять текстовые суммы
    re_money = re.compile('|'.join([ 
        r'(\d+\.?) руб',
        r'(\d+\.?) RUB'
        ]))
    data = re.sub(re_money, "<MONEY>", data)
    return data

def detect_medical(data):
    # для определений больничек, инвалидностей, болезней
    pass

def detect_post_codes(data=test_data):
    # для определения почтовых кодов
    data = re.sub(r"\b([0-9]{6})\b", "<POSTCODE>", data)
    return data

def detect_addr(data=test_data):
    # для определения адресов
    pass

def detect_dates(text=test_data):
    # для определения дат
    text = re.sub("\d{2}[- /.]\d{2}[- /.]\d{,4}", "<DATUM>", text)
    text = re.sub(
        "(\d{1,2}[^\w]{,2}(januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december)"
        "([- /.]{,2}(\d{4}|\d{2}))?)",
        "<DATE>", text)
    text = re.sub(
        "(\d{1,2}[^\w]{,2}(jan|feb|mrt|apr|mei|jun|jul|aug|sep|okt|nov|dec))[- /.](\d{4}|\d{2})?",
        "<DATE>", text)
    return text

def detect_email(data=test_data):
    # для определения почты
    return re.sub("(([a-zA-Z0-9_+]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?))"
                    "(?![^<]*>)",
                    "<EMAIL>",
                      data)

def removePersonalData(data: str):
    return detect_money(detect_url(detect_INN(detect_dates(detect_passport(detect_email(data))))))

def remove(data):
    data = search(data)
    data = detect_email(data)
    data = detect_passport(data)
    data = detect_post_codes(data)
    data = detect_dates(data)
    data = detect_INN(data)
    data = detect_url(data)
    data = detect_money(data)
    data = detect_names(data)
    return data

if __name__ == "__main__":
    data = remove(test_data)
    print(data)
