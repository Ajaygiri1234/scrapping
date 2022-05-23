import json
import requests
import re

final_result = {}


def find_article(query):
    # query="जीतपु"
    each_result = []
    for page in range(1, 30):
        if len(each_result) <= 30:

            url = "https://bg.annapurnapost.com/api/search?title=" + query + "&page=" + str(page)
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:

                response = response.json()
                print(response["status"], len(response["data"]["items"]))
                print(type(response["status"]), type(len(response["data"]["items"])))

                print(response["status"] == "success", len(response["data"]["items"]) == 0)
                if (response["status"] == "success") & (len(response["data"]["items"]) == 0):
                    break

                # print(a.keys())
                # print(a["data"])
                response = response["data"]["items"]

                # json.dumps(a,indent = 3,ensure_ascii=False)

                unwanted_keys = ['province', 'introText', 'newsHighlights', 'status', 'categories', 'caption',
                                 'videoLink', 'isFeatured', 'isBreakingNews', 'isImportantNews']
                for index, item in enumerate(response):
                    for i in remove_keys:
                        del response[index][i]

                for count, i in enumerate(response):
                    i["content"] = re.sub('<.*?>', '', i["content"])
                    i["content"] = i["content"].replace('&nbsp', " ");
                    # i["content"] = i["content"].replace('\r\n'," ")
                    # i["content"] = i["content"].replace('\r\t '," ")
                    # i["content"] = i["content"].replace('\r'," ")
                each_result += response
                if len(each_result) >= 30:
                    break


            else:
                break

    final_result[query] = each_result


# list_of_items=["जीत",'शेरबहादुर','दर्ता']
list_of_items = ["जीत", 'शेरबहादुर', 'दर्ता', "मोरङ", "हत्या", "मृत्यु", "महिला"]
for itemm in list_of_items:
    find_article(itemm)

# print(final_result)


print(type(final_result))
output = json.dumps(final_result, indent=3, ensure_ascii=False)
print(type(output))
print(output)
