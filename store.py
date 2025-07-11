class Store:
    def __init__(self, name, address, ):
        self.name = name    # название
        self.address = address
        self.items = {}
    def add_item (self,name_item,price):
        self.items[name_item] = price

    def del_item (self,name_item):
         if name_item in self.items:
             del self.items[name_item]

    def get_price (self,name_item):
       print(self.items.get(name_item,'Не найден'))

    def list_items(self):
        print(f'Список товаров для магазина {self.name} :')
        for key in self.items:
            print(f"   Тoвар : {key}  Цена: {self.items[key]} ")
    def upd_price(self,name_item,new_price):
        if name_item in self.items:
            self.items[name_item] = new_price
            print (f'Изменили цену для {name_item}')
        else :
            print(f'Нет такого товара в магазине {self.name}')




mag1 = Store('magazin1','москва 1')
mag1.add_item('it1',34.3)
mag1.list_items()
mag1.add_item('товар2',15)
mag1.add_item('tovar3',33.55)
mag1.list_items()
mag1.get_price('товар2')
mag1.del_item('товар2')
print ('удалили товар2')
mag1.list_items()
mag1.upd_price('товар3',89)
mag1.upd_price('tovar3',89)

mag1.list_items()


