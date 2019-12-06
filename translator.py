import os, sys, getopt
import http.client
import hashlib
import urllib
import random
import json
import re

# Baidu API URL
baiduapi_url = 'api.fanyi.baidu.com'
# Translate URI
base_uri = '/api/trans/vip/translate'
# APPID for Baidu Translate API
baidu_appid = 'xxx'
# Secret key for Authentication
baidu_secretkey = 'yyy'

salt = random.randint(32768, 65536)

# Get the sign
def get_sign(line):
    sign = baidu_appid + line + str(salt) + baidu_secretkey
    sign = hashlib.md5(sign.encode()).hexdigest()
    return sign

# Get the parent path of the file
def current_path():
    path = os.path.abspath(__file__)
    pare_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    return pare_path

# Translate the md files from source dir, and put the results into  dest dir.
# It only accept 2000 bytes(maxium) for translate in Baidu API, so we can optimze the curret tranverse logic.
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

                for line in iter_f:
                    # skip the field translate among "```"
                    if str(line).__contains__("```") or status:
                        if not status and str(line).__contains__("```"):
                            status = True
                            str_list.append(line)
                        elif status and str(line).__contains__("```"):
                            status = False
                            str_list.append(line)
                        else:
                            str_list.append(line)
                    else:
                        # if there's no line break, then translate
                        if not str(line).__eq__("\n"):
                            try:
                                # since "# " and "* " are special charator, and  it would delete any blank in translate api, I add the replace charator
                                if str(line).__contains__("# "):
                                    line = re.sub('# ', ' #ABC ', line)
                                if str(line).__contains__("* "):
                                    line = re.sub('\\* ', ' *CBA ', line)
                                #Call Baidu API
                                url = base_uri + '?appid=' + baidu_appid + '&q=' + urllib.parse.quote(
                                    line) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
                                    salt) + '&sign=' + get_sign(
                                    line)
                                httpclient = http.client.HTTPConnection(baiduapi_url)
                                httpclient.request('GET', url)

                                response = httpclient.getresponse()
                                result_all = response.read().decode("utf-8")
                                result = json.loads(result_all)
                                # Get the trans_result
                                line = result['trans_result'][0]['dst']
                                # Replace special charator
                                if str(line).__contains__("#ABC"):
                                    line = re.sub('#ABC', '# ', line)
                                if str(line).__contains__("*CBA"):
                                    line = re.sub('\\*CBA', '* ', line)
                                str_list.append(line)
                            except Exception as e:
                                print(e)
                            finally:
                                if httpclient:
                                    httpclient.close()
                        else:
                            str_list.append("\n")

                outfile.write("\n".join(str_list))
                infile.close()
                outfile.close()


def translator(argv):
    input = ''
    output = ''
    fromLang = 'en'
    toLang = 'zh'

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ipath=", "opath="])
    except getopt.GetoptError:
        print("translator.py -i <ipath> -o <opath>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("translator.py -i <ipath> -o <opath> -o <opath>")
            sys.exit()
        elif opt in ("-i", "--ipath"):
            input = argv[1]
            print("input path is ", input)

        elif opt in ("-o", "--opath"):
            output = argv[3]
            print("output path is ", output)
    baiduapi_translate(input, output, fromLang, toLang)


if __name__ == '__main__':
    translator(sys.argv[1:])
