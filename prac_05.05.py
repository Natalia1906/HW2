import requests
import json

if __name__ =="__main__":
    try:
        # TODO сырые данные
        url = "https://api.binance.com/api/v3/ticker/price"
        data_raw = requests.get(url)

        #TODO проверка на положительный ответ
        if int(data_raw.status_code) == 200:
            valutes = data_raw.json()
            #print(valutes)

            #TODO фильтрация на более 10 000
            data_clear = []
            for valute in valutes:
                #print(valute["price"])
                if float(valute["price"]) > 10000.0:
                    data_clear.append(valute)
            #print(data_clear)

            #TODO сортировка массива по возрастанию
            data_asc = (sorted(data_clear, key=lambda valute: valute["price"], reverse= True))
            #print(data_asc)

            # TODO формативоранный вывод на экран
            with open("data.txt", mode="w") as file:
                for i in data_asc:
                    txt = f"{i['symbol']} | {i['price']}"
                    print(txt)
                    file.write(txt + "\n")
        else:
            print(data_raw.status_code)
    except Exception as error:
        print(error)



    