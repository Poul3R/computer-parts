from bs4 import BeautifulSoup as bs
import requests
import csv
import re


class MediaMarktScrapper:
    progress_bar = ''

    __list_of_products_url = []
    __laptops_catalog_url = 'https://mediamarkt.pl/komputery-i-tablety/laptopy-laptopy-2-w-1?sort=0&limit=100&page=1'

    __price = None
    __spec_core = None  # Ilość rdzeni
    __spec_ram = None  # Pamięć RAM
    __spec_disc_type = None  # Rodzaj dysku
    __spec_disc_capacity = None  # Dysk SSD
    __spec_display = None  # Przekątna ekranu
    __spec_work_time = None  # Maksymalny czas pracy
    __spec_operating_system = None  # System operacyjny
    __spec_guaranty = None  # Okres gwarancji

    def make_list_of_products_uls(self):
        main_site_response = requests.get(self.__laptops_catalog_url)

        main_site_content = str(main_site_response.text)

        main_site_soup = bs(main_site_content, 'html.parser')

        list_of_link_dom_element = main_site_soup.find_all('a', attrs={'class': 'js-product-name'})

        for link_element in list_of_link_dom_element:
            url = link_element['href']
            self.__list_of_products_url.append('https://mediamarkt.pl/' + url)

    def save_computer_spec_to_file(self):
        main_string = str(self.__price) + ',' + str(self.__spec_core) + ',' + str(self.__spec_ram) + ',' + str(
            self.__spec_disc_type) + ',' + str(
            self.__spec_disc_capacity) + ',' + str(self.__spec_display) + ',' + str(self.__spec_work_time) + ',' + str(
            self.__spec_operating_system) + ',' + str(self.__spec_guaranty)

        with open('computers-specification.csv', 'a+', newline='') as data_file:
            csv_writer = csv.writer(data_file, delimiter=';', quotechar=' ')
            csv_writer.writerow((main_string,))

    def get_computer_spec(self, prod_url):
        price_array = []
        final_price = ''

        product_site_response = requests.get(prod_url)

        product_site_content = str(product_site_response.text)

        product_site_soup = bs(product_site_content, 'html.parser')

        # get product price
        price_parts_array = product_site_soup.find('div', attrs={'class': 'm-productAction_price'}) \
            .find('div', attrs={'class': 'm-priceBox_price'}).find_all('span')

        for item in price_parts_array:
            if 'is-0' in item['class']:
                price_array.append(0)
                continue

            if 'is-1' in item['class']:
                price_array.append(1)
                continue

            if 'is-2' in item['class']:
                price_array.append(2)
                continue

            if 'is-3' in item['class']:
                price_array.append(3)
                continue

            if 'is-4' in item['class']:
                price_array.append(4)
                continue

            if 'is-5' in item['class']:
                price_array.append(5)
                continue

            if 'is-6' in item['class']:
                price_array.append(6)
                continue

            if 'is-7' in item['class']:
                price_array.append(7)
                continue

            if 'is-8' in item['class']:
                price_array.append(8)
                continue

            if 'is-9' in item['class']:
                price_array.append(9)
                continue

            if 'is-semicolon':
                break

        for num in price_array:
            final_price += str(num)

        self.__price = int(final_price)

        # get product specification
        specification_list = product_site_soup.find_all('dl', attrs={'class': 'm-offerShowData_row clearfix2'})

        for property in specification_list:
            try:
                spec_title = property.find('dt').find('p').find('span').string
                spec_value = property.find('dd').find('p').find('span').string

                if 'Ilość rdzeni' in spec_title:
                    self.__spec_core = int(''.join(x for x in spec_value if x.isdigit()))

                if 'Pamięć RAM' in spec_title:
                    self.__spec_ram = int(re.search(r'\d+', spec_value).group())

                if 'Rodzaj dysku' in spec_title:
                    if 'SSD' in spec_value:
                        self.__spec_disc_type = 'SSD'
                    else:
                        self.__spec_disc_type = 'HDD'

                if 'Dysk ' in spec_title:
                    self.__spec_disc_capacity = int(''.join(x for x in spec_value if x.isdigit()))

                if 'Przekątna ekranu' in spec_title:
                    self.__spec_display = float(spec_value)

                if 'Maksymalny czas pracy' in spec_title:
                    self.__spec_work_time = int(spec_value)

                if 'System operacyjny' in spec_title:
                    if 'Windows' in spec_value:
                        self.__spec_operating_system = 'Windows'
                    elif 'macOS' in spec_value:
                        self.__spec_operating_system = 'macOS'
                    else:
                        self.__spec_operating_system = 'Other'

                if 'Okres gwarancji' in spec_title:
                    self.__spec_guaranty = int(''.join(x for x in spec_value if x.isdigit()))

            except:
                continue

        self.save_computer_spec_to_file()
        self.progress_bar += '#'
        print(self.progress_bar)

    def main(self):
        self.make_list_of_products_uls()

        counter = 0

        for url in self.__list_of_products_url:
            self.get_computer_spec(url)
            counter += 1

            # if counter > 5:
            #     break


# main
scrapper = MediaMarktScrapper()

scrapper.main()
