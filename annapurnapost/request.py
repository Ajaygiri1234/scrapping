import json
import requests
import re
import os
final_result = {}
#aa={"next_iter":1}

if not os.path.exists("output.json"):
    #print('okay')
    with open("output.json", "w+") as f:
        json.dump({}, f)

def find_article(query,next_iteration):
    with open('output.json',"r") as f:
        output = json.load(f)
    if  query in (output.keys()):
        length_from_file=len(output[query])
    else:
        length_from_file=0

    # query="जीतपु"
    each_result = []
    for page in range(next_iteration, 4):
        if len(each_result) <= 30:
            print(page,"="*50)
            url = "https://bg.annapurnapost.com/api/search?title=" + query + "&page=" + str(page)
            try:
                response = requests.get(url)
                status_code = response.status_code
                if status_code == 200:
                    response = response.json()
                    # print(response["status"], len(response["data"]["items"]))
                    # print(type(response["status"]), type(len(response["data"]["items"])))
                    # print(response["status"] == "success", len(response["data"]["items"]) == 0)
                    if (response["status"] == "success") & (len(response["data"]["items"]) == 0):
                        break
                    response = response["data"]["items"]
                    unwanted_keys = ['province', 'introText', 'newsHighlights', 'status', 'categories', 'caption',
                                     'videoLink', 'isFeatured', 'isBreakingNews', 'isImportantNews']
                    for index, item in enumerate(response):
                        for i in unwanted_keys:
                            del response[index][i]

                    for count, i in enumerate(response):
                        i["content"] = re.sub('<.*?>', '', i["content"])
                        i["content"] = i["content"].replace('&nbsp', " ");
                        # i["content"] = i["content"].replace('\r\n'," ")
                        # i["content"] = i["content"].replace('\r\t '," ")
                        # i["content"] = i["content"].replace('\r'," ")
                    each_result += response
                    count = len(each_result)  # just to count the length
                    # print(response)
                    # input(len(response))
                    with open('output.json', "r") as f:
                        output = json.load(f)
                    if query not in (output.keys()):
                        output[query] = []
                        output[query] += response

                    else:
                        output[query] += response

                    with open("output.json", "w") as f:
                        json.dump(output, f)
                    if len(each_result) >= 30:
                        break


                else:
                    break
            except Exception as e:

                print(page, "=" * 50)
                json_for_next_run["next_iter"]=page+1
                with open("next_file.json", "w") as f:
                    json.dump(json_for_next_run, f)
                    exit(1)
                    #response = requests.get(url)##to return the error and terminate program
                #print(page, "hello")
                #print(id(e))
                #print(type(e.args))
                #print(e.args[0])
                #continue


    final_result[query] = each_result


# list_of_items=["जीत",'शेरबहादुर','दर्ता']
#list_of_items = ["जीत", 'शेरबहादुर', 'दर्ता', "मोरङ", "हत्या", "मृत्यु", "महिला"]

try:
    with open("next_file.json","r") as f:
        json_for_next_run=json.load(f)
except:
    json_for_next_run={"next_iter":1}


search_item="जीत"
find_article(search_item,json_for_next_run["next_iter"])




print(type(final_result))
output = json.dumps(final_result, indent=3, ensure_ascii=False)

print(type(output))
print(output)
