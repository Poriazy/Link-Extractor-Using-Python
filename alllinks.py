import urllib.request #importing the request library

"""
Creating a function to read the url using request library.
Also decoding it to be easily useable.
"""
def from_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode()
            return html
    except Exception as e:
                return e

"""
Creating a function to extract the links from the recieved data.
"""
def get_next_target(s):
    start_link=s.find('<a href="htt')
    if start_link == -1:
        return None,0
    start_quote=s.find('"',start_link)
    end_quote=s.find('"',start_quote+1)
    url=s[start_quote+1:end_quote]
    return url,end_quote

"""
Creating a function to print the extracted links from the requested web page.
"""
def retrive_all_links(page):
    urls = []
    while True:
        url,endpos = get_next_target(page)        
        if url:
            # print (url)
            urls.append(url)
            page = page[endpos:]
        else:
            break
    return urls

web_page_address = input ("please enter your target web page: ")
file_format = input("now enter file format or string that you need (-a for all links): ")

urls_list = retrive_all_links(from_page(web_page_address))
all_link_size = len(urls_list)

custom_format_link_size = 0

for url in urls_list:
    if file_format in url:
        print (url)
        custom_format_link_size += 1
    elif file_format == "-a":
        custom_format_link_size = all_link_size
        print (url)
    
print ("match format size:", custom_format_link_size)
print ("links in webpage:", all_link_size)
