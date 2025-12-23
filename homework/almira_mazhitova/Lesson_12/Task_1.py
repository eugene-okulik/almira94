class Flowers:
    def __init__(self, inv_num, color, stem_length, freshness, price, vase_life):
        self.inv_num = inv_num
        self.price = price  # стоимость 1-го цветка
        self.stem_length = stem_length  # длина стебля
        self.color = color  # цвет
        self.freshness = freshness  # свежесть (в днях от времени среза)
        self.vase_life = vase_life  # среднее время жизни срезанных цветов в вазе (в днях)


class Roses(Flowers):
    name = 'Роза'

    def __init__(self, inv_num, color, stem_length, freshness, price, vase_life, variety, having_thorns):
        super().__init__(inv_num, color, stem_length, freshness, price, vase_life)
        self.variety = variety  # сорт
        self.having_thorns = having_thorns  # наличие шипов
        self.vase_life = vase_life


class Peonies(Flowers):
    name = 'Пион'

    def __init__(self, inv_num, color, stem_length, freshness, price, vase_life, kind, flower_size):
        super().__init__(inv_num, color, stem_length, freshness, price, vase_life)
        self.kind = kind  # вид
        self.flower_size = flower_size  # диаметр цветка в см


class FillerFlowers(Flowers):
    def __init__(self, inv_num, name, color, stem_length, freshness, price, vase_life, volume, having_berries):
        super().__init__(inv_num, color, stem_length, freshness, price, vase_life)
        self.name = name  # наименование
        self.volume = volume  # объемность
        self.having_berries = having_berries  # наличие ягодок


class ExoticFlowers(Flowers):
    def __init__(self, inv_num, name, color, stem_length, freshness, price, vase_life, specificity):
        super().__init__(inv_num, color, stem_length, freshness, price, vase_life)
        self.name = name  # наименование
        self.specificity = specificity  # особенность


class Bouquet:
    def __init__(self, flowers_list):
        self.flowers_list = flowers_list

    def calc_bouquet_cost(self):
        cost = 0
        for flower in self.flowers_list:
            cost += flower.price
        return cost

    def calc_time_to_bouquet_wilt(self):
        sum_of_vase_life = 0
        for flower in self.flowers_list:
            sum_of_vase_life += flower.vase_life
        avg_vase_life = sum_of_vase_life / len(self.flowers_list)
        return avg_vase_life

    def sort_flowers_asc_order(self, attr_name):
        if attr_name not in ['inv_num', 'color', 'stem_length', 'freshness', 'price', 'vase_life']:
            return f"Нельзя отсортировать по параметру {attr_name}"
        new_sorted_list = self.flowers_list[:]
        n = len(new_sorted_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                value_1 = new_sorted_list[j].__dict__[attr_name]
                value_2 = new_sorted_list[j + 1].__dict__[attr_name]
                if value_1 > value_2:
                    new_sorted_list[j], new_sorted_list[j + 1] = new_sorted_list[j + 1], new_sorted_list[j]
        returned_list = []
        for flower in new_sorted_list:
            returned_list.append(flower.inv_num)

        return returned_list

    def sort_flowers_desc_order(self, attr_name):
        new_sorted_list = self.flowers_list[:]
        n = len(new_sorted_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                value_1 = new_sorted_list[j].__dict__[attr_name]
                value_2 = new_sorted_list[j + 1].__dict__[attr_name]
                if value_1 < value_2:
                    new_sorted_list[j], new_sorted_list[j + 1] = new_sorted_list[j + 1], new_sorted_list[j]

        returned_list = []
        for flower in new_sorted_list:
            returned_list.append(flower.inv_num)

        return returned_list

    def find_flower_by_attr_value(self, attr_name, attr_value):
        for flower in self.flowers_list:
            if flower.__dict__[attr_name] == attr_value:
                return f"Инвентарный номер цветка с искомым параметром: {flower.inv_num}"
        return f"В данном букете отсутствуют цветы с параметром {attr_name} = {attr_value}"


flwr_1 = Roses(1, 'красный', 110, 1, 280, 5, 'чайная', True)
flwr_2 = Roses(2, 'розовый', 110, 4, 289, 5, 'чайная', False)
flwr_3 = Roses(3, 'розовый', 45, 3, 340, 8, 'кустовая', False)
flwr_4 = Roses(4, 'белый', 45, 1, 340, 8, 'кустовая', False)
flwr_5 = Roses(5, 'персиковый', 45, 2, 340, 8, 'кустовая', False)
flwr_6 = Peonies(6, 'красный', 80, 1, 560, 9, 'сара бернар', 20)
flwr_7 = Peonies(7, 'розовый', 75, 2, 420, 9, 'корал шарм', 12)
flwr_8 = Peonies(8, 'розовый', 75, 1, 420, 9, 'корал шарм', 12)
flwr_9 = Peonies(9, 'розовый', 75, 1, 420, 9, 'корал шарм', 12)
flwr_10 = FillerFlowers(10, 'Рускус', 'зеленый', 60, 1, 190, 180, 'средняя', False)
flwr_11 = FillerFlowers(11, 'Гипсофила', 'белый', 60, 3, 200, 30, 'большая', False)
flwr_12 = FillerFlowers(12, 'Гипсофила', 'розовый', 60, 1, 200, 30, 'большая', False)
flwr_13 = ExoticFlowers(13, 'Протея', 'красный', 90, 2, 890, 45, 'крупный цветок, похожий на корону')
flwr_14 = ExoticFlowers(14, 'Антуриум', 'красный', 70, 1, 1100, 14, 'глянцевый сердцевидный цветок')
flwr_15 = ExoticFlowers(15, 'Антуриум', 'белый', 70, 2, 1100, 14, 'глянцевый сердцевидный цветок')

bouquet_1 = Bouquet([flwr_2, flwr_3, flwr_4, flwr_11])

print(bouquet_1.calc_bouquet_cost())
print(bouquet_1.calc_time_to_bouquet_wilt())
print(bouquet_1.sort_flowers_asc_order('freshness'))
print(bouquet_1.sort_flowers_desc_order('vase_life'))
print(bouquet_1.find_flower_by_attr_value('vase_life', 28))
