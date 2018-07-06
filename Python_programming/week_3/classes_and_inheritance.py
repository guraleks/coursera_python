import os
import csv

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        if os.path.splitext(self.photo_file_name)[1] != '':
            return os.path.splitext(self.photo_file_name)[1]
        else:
            return os.path.splitext(self.photo_file_name)[0]


class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.carrying = carrying
        self.photo_file_name = photo_file_name
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if body_whl != '':
            params = body_whl.split('x')
            float_params = [float(params[i]) for i in range(len(params))]
        else:
            float_params = [0, 0, 0]
        self.body_length = float_params[0]
        self.body_width = float_params[1]
        self.body_height = float_params[2]

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            args = [value for value in row if value != '']
            if len(args) == 5:
                if args[0] == 'car':
                    car_list.append(Car(args[0],
                                        args[1],
                                        int(args[2]),
                                        args[3],
                                        float(args[4])))
                if args[0] == 'spec_machine':
                    car_list.append(SpecMachine(args[0],
                                                args[1],
                                                args[2],
                                                float(args[3]),
                                                args[4]))
                if args[0] == 'truck':
                    car_list.append(Truck(args[0],
                                          args[1],
                                          args[2],
                                          args[3],
                                          float(args[4])))
            elif len(args) == 4 and row[0] == 'truck' and row[4] == '':
                car_list.append(Truck(args[0],
                                      args[1],
                                      args[2],
                                      '',
                                      float(args[3])))

    return car_list



# if __name__ == '__main__':
#
#     truck = Truck('car', 'tr', 'path.png', '54x34x56', 44)
#     print(truck.get_photo_file_ext())
#
#     with open('coursera_week3_cars.csv') as csv_fd:
#         rr = csv.reader(csv_fd, delimiter=';')
#         next(rr)  # пропускаем заголовок
#         for r in rr:
#             print(r)
#             print([value for value in r if value != ''])
#
#     print(get_car_list('coursera_week3_cars.csv'))
