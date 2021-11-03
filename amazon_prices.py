import requests
import re
def extract_url(url):

    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.in" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.in" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

url = extract_url('https://www.amazon.com/dp/B07YMJ57MB/ref=asc_df_B07YMJ57MB1619866800000?tag=cnet-pc-20&creative=395261&creativeASIN=B07YMJ57MB&linkCode=asn&ascsubtag=c82a83f9470a42e09d773a6f6388a71d%7C2a1b2a00-abac-11eb-b36d-6b11431fa5d0%7Cdtp')
print(url)

info = requests.get(url).text
start_price_idx = info.find("data-base-product-price")
price = re.findall("[0-9]{1,7}\.[0-9]{2}", )[0]
print(price)