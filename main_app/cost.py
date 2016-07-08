import requests
from bs4 import BeautifulSoup as bs

def get_num(span):
    cost = 0
    for v in span:
        for ch in v:
            if (ch.isdigit()):
                cost = cost * 10 + int(ch)
    return cost

def car_cost(car_mark, car_model, car_is_year):

    page = 1
    prices = []
    cnt = 0
    total_sum = 0

    while True :
        domain = "http://kolesa.kz/cars/"
        request_link = domain+car_mark+"/"+car_model+"/"+"?year[from]="+str(int(car_is_year) - 1)+"&year[to]="+str(int(car_is_year) + 1)+"&page="+str(page)
        print(request_link)
        page += 1
        if (page > 3):
            break

        r = requests.get(request_link)
        soup = bs(r.content, 'html.parser')
        spans = soup.findAll('span', {'class' : 'price'})
        if (len(spans) == 0):
            break
        prices.append(spans)
        for span in spans:
            total_sum += get_num(span)
            cnt += 1

    if (cnt == 0):
        return 0
    return total_sum//cnt

if (__name__ == "__main__"):
    car_cost("toyota", "camry", "2000")
