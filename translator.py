import os, sys, getopt
import http.client
import hashlib
import time
import urllib
import random
import json
import re

baiduapi_url = 'api.fanyi.baidu.com'
base_uri = '/api/trans/vip/translate'
# 20191214000366079 20191205000363297
# SM6N72Y4DI575JaAUbRg _vlwuY6z8irtjcxjgnM4
baidu_appid = '20191214000366079'
baidu_secretkey = 'SM6N72Y4DI575JaAUbRg'
salt = random.randint(32768, 65536)


def get_sign(line):
    sign = baidu_appid + line + str(salt) + baidu_secretkey
    sign = hashlib.md5(sign.encode()).hexdigest()
    return sign


def current_path():
    path = os.path.abspath(__file__)
    pare_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    # print("path name is ", pare_path)
    return pare_path

    output_str = input_str
    return output_str


def get_url(fromLang, toLang, line):
    return base_uri + '?appid=' + baidu_appid + '&q=' + urllib.parse.quote(
        line) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + get_sign(
        line)


def splitranslationforch(line, fromLang, toLang, seprator):
    strsplit = str(line).split(seprator, 2)
    print("split data is ", strsplit[0], strsplit[1], strsplit[2])
    # url = get_url(fromLang, toLang, str(strsplit[1]))
    strsplit[0] = translation(get_url(fromLang, toLang, str(strsplit[0])))
    strsplit[1] = translation(get_url(fromLang, toLang, str(strsplit[1])))
    strsplit[2] = translation(get_url(fromLang, toLang, str(strsplit[2])))
    if len(strsplit[0]) == 0:
        return seprator + strsplit[1]
    return strsplit[0] + seprator + strsplit[1] + seprator + strsplit[2]


def splitranslation(line, fromLang, toLang, seprator):
    strsplit = str(line).split(seprator, 1)
    print("split data is ", strsplit[0], strsplit[1])
    # url = get_url(fromLang, toLang, str(strsplit[1]))

    if strsplit[1].strip().__eq__(''):
        strsplit[1] = ""
    if len(strsplit[1].strip()) != 0:
        strsplit[1] = translation(get_url(fromLang, toLang, str(strsplit[1])))
    if len(strsplit[0]) == 0:
        return seprator + strsplit[1]
    return strsplit[0] + seprator + strsplit[1]


def translation(url):
    result = {}
    try:
        httpclient = http.client.HTTPConnection(baiduapi_url)
        httpclient.request('GET', url)

        response = httpclient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        if "error_code" in result:
            while result["error_code"] == "52001" or result["error_code"] == "52003":
                time.sleep(1)
                httpclient = http.client.HTTPConnection(baiduapi_url)
                httpclient.request('GET', url)
                response = httpclient.getresponse()
                result_all = response.read().decode("utf-8")
                result = json.loads(result_all)
        print("translate line is ", result['trans_result'][0]['dst'])
    except Exception as e:
        print(e)
    finally:
        if httpclient:
            httpclient.close()

    return result['trans_result'][0]['dst']


def baiduapi_translate(source_dir, dest_dir, fromLang, toLang):
    files = os.listdir(source_dir)
    for file in files:
        if not os.path.isdir(file):
            if file.split(".")[-1].lower().__eq__("md"):
                infile = open(source_dir + "/" + file, 'r')
                outfile = open(dest_dir + "/" + file, 'w')
                iter_f = iter(infile)
                str_list = []
                status = False
                # strsplit = []
                url = ""

                for line in iter_f:
                    print("the origin line is: ", line)
                    time.sleep(1)
                    if str(line).__contains__("```") or status:
                        if not status and str(line).__contains__("```"):
                            status = True
                            str_list.append(line)
                        elif status and str(line).__contains__("```"):
                            status = False
                            str_list.append(line)
                        else:
                            str_list.append(line)

                    elif str(line).__contains__("&nbsp;"):
                        str_list.append(line)
                    # elif str(line).__eq__('\n'):
                    #     str_list.append(line)
                    elif str(line).__contains__("<span style=\"font-style:italic;\">") or str(line).__contains__(
                            "<td>") or str(line).__contains__("<span") or str(line).__contains__("<hr") or str(
                        line).__contains__("<img") or str(line).__contains__("assets/img"):
                        str_list.append(line)
                    elif str(line)[0] == "#" or str(line)[0] == "*":
                        if str(line).__contains__("# "):
                            str_list.append(splitranslation(line, fromLang, toLang, "# "))
                        elif str(line).__contains__("* "):
                            str_list.append(splitranslation(line, fromLang, toLang, "* "))
                    else:
                        if str(line).strip().__eq__(''):
                            str_list.append(line)
                        else:
                            str_list.append(translation(get_url(fromLang, toLang, line)))
                outfile.write("\n".join(str_list))
                infile.close()
                outfile.close()


def translator(args):
    input = ''
    output = ''
    fromLang = 'en'
    toLang = 'jp'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:f:t:x",
                                   ["help", "--input", "--output", "--from", "--to"])
    except getopt.GetoptError:
        print("translator.py -i <input> -o <output> -f <from> -t <to>")
        sys.exit(2)
    for op, value in opts:
        if op in ("-h", "--help"):
            print("translator.py -i <input> -o <output> -f <from> -t <to>")
        elif op in ("-i", "--input"):
            input = value
        elif op in ("-o", "--output"):
            output = value
        elif op in ("-f", "--from"):
            fromLang = value
        elif op in ("-t", "--to"):
            toLang = value

    baiduapi_translate(input, output, fromLang, toLang)


if __name__ == '__main__':
    translator(sys.argv[1:])
