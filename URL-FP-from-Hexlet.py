'''Group defs for use URL in FP-style

Реализуйте абстракцию для работы с URL. Она должна извлекать и менять части адреса.

Интерфейс:

make(url) - Конструктор. Создает URL.

get_scheme(data) - Селектор (геттер). Извлекает схему.

set_scheme(data, scheme) - Сеттер. Меняет схему.

get_host(data) - Геттер. Извлекает host.

set_host(data, host) - Сеттер. Меняет host.

get_path(data) - Геттер. Извлекает путь.

set_path(data, path) - Сеттер. Меняет путь.

get_query_param(data, param_name, default=None) - Геттер. Извлекает значение для параметра запроса. Третьим параметром функция принимает значение по умолчанию, которое возвращается тогда, когда в запросе не было такого параметра

set_query_param(data, key, value) - Сеттер. Устанавливает значение для параметра запроса. Если передано значение None, то параметр отбрасывается.

to_string(data) - Геттер. Преобразует URL в строковой вид.

Все сеттеры должны возвращать новый изменённый URL, а старый оставлять неизменным.'''

# BEGIN (write your solution here)
def make(url):
    r1 = url.find(':')
    r2 = url.find('/', r1+3)
    r3 = url.find('?')
# collection params
    param = {}
    index = 0
    start = r3
    while index < len(url):
        index = url.find('=', index)
        end = url.find('&', index)
        if index == -1:
            break
        if end == -1:
            param[url[start+1:index]] = url[index+1:end]+url[-1]
        else:
            param[url[start+1:index]] = url[index+1:end]
        index += 1 
        start = end
    x = {
        'scheme' : url[:r1],
        'host' : url[r1+3:r2],
        'path' : url[r2:r3],
        'param' : param
    }
    if r3 == -1:
        x['path'] = url[r2:]
    return x


def get_scheme(data):
    return data['scheme']


def get_host(data):
    return data['host']


def get_path(data):
    return data['path']


def set_scheme(data, scheme):
    data1 = []
    data1 = data.copy()
    data1['scheme'] = scheme
    return data1


def set_host(data, host):
    data1 = []
    data1 = data.copy()
    data1['host'] = host
    return data1


def set_path(data, path):
    data1 = []
    data1 = data.copy()
    data1['path'] = path
    return data1


def to_string(data): 
    str_ = get_scheme(data) + '://' + get_host(data) + get_path(data)
    if len(data['param']) > 0:
        str_ += "?"
        for i in data['param']:
            str_ += i
            str_ += '='
            str_ += str(data['param'].get(i))
            str_ += '&'
        str_ = str_[0:-1]
    return str_


def get_query_param(data, param_name, default=None):
    if param_name in data['param']:
        return data['param'].get(param_name)
    else:
        return default
    

def set_query_param(data, key, value): 
    data1 = []
    data1 = data.copy()
    if value == None and key in data1['param']:
        del data1['param'][key]
    elif value == None:
        return data1
    else:
        data1['param'][key] = value
    return data1
# END
