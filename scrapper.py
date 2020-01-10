from bs4 import BeautifulSoup as bs
import requests
import csv
import re


class MediaMarktScraper:
    __list_of_products_url = []
    __laptops_catalog_url = 'https://mediamarkt.pl/komputery-i-tablety/laptopy-laptopy-2-w-1?sort=0&limit=100&page='

    __price = None
    __tabs_amount = None

    __spec_core = None  # Ilość rdzeni
    __spec_ram = None  # Pamięć RAM
    __spec_disc_type = None  # Rodzaj dysku
    __spec_disc_capacity = None  # Dysk SSD
    __spec_display = None  # Przekątna ekranu
    __spec_operating_system = None  # System operacyjny
    __spec_guaranty = None  # Okres gwarancji

    def make_list_of_products_uls(self):

        for page_num in range(1, self.__tabs_amount):
            main_site_response = requests.get(self.__laptops_catalog_url + str(page_num))

            main_site_content = str(main_site_response.text)

            main_site_soup = bs(main_site_content, 'html.parser')

            list_of_link_dom_element = main_site_soup.find_all('a', attrs={'class': 'js-product-name'})

            for link_element in list_of_link_dom_element:
                url = link_element['href']
                self.__list_of_products_url.append('https://mediamarkt.pl/' + url)

    def save_computer_spec_to_file(self):
        main_string = str(self.__price) + ',' + str(self.__spec_core) + ',' + str(self.__spec_ram) + ',' + str(
            self.__spec_disc_type) + ',' + str(
            self.__spec_disc_capacity) + ',' + str(self.__spec_display) + ',' + str(
            self.__spec_operating_system) + ',' + str(self.__spec_guaranty)

        with open('computers-specification-media-markt.csv', 'a+', newline='') as data_file:
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

    def get_amount_of_tabs(self):
        main_site_response = requests.get(self.__laptops_catalog_url + '1')

        main_site_content = str(main_site_response.text)

        main_site_soup = bs(main_site_content, 'html.parser')

        amount_string_with_trash = main_site_soup.find('span', attrs={'class': 'm-pagination_count'}).text

        self.__tabs_amount = int(''.join(x for x in amount_string_with_trash if x.isdigit()))

    def main(self):
        self.get_amount_of_tabs()

        self.make_list_of_products_uls()

        for url in self.__list_of_products_url:
            self.get_computer_spec(url)


class MoreleNetScraper:
    __laptops_catalog_url = 'https://www.morele.net/laptopy/laptopy/notebooki-laptopy-ultrabooki-31/,,,,,,,,0,,,,/'
    __list_of_products_url = []

    __price = None
    __tabs_amount = None

    __spec_core = None  # Ilość rdzeni
    __spec_ram = None  # Pamięć RAM
    __spec_disc_type = None  # Rodzaj dysku
    __spec_disc_capacity = None  # Dysk SSD
    __spec_display = None  # Przekątna ekranu
    __spec_operating_system = None  # System operacyjny
    __spec_guaranty = None  # Okres gwarancji

    def get_amount_of_tabs(self):
        main_site_response = requests.get(self.__laptops_catalog_url)

        main_site_content = str(main_site_response.text)

        main_site_soup = bs(main_site_content, 'html.parser')

        list_of_pagintations_dom = main_site_soup.find_all('li', attrs={'class': 'pagination-lg btn'})
        list_of_pagintations = []

        for pagination in list_of_pagintations_dom:
            x = pagination.find('a')['data-page']
            list_of_pagintations.append(int(x))

        self.__tabs_amount = list_of_pagintations[-1]

        # self.__tabs_amount = int(''.join(x for x in amount_string_with_trash if x.isdigit()))

    def make_list_of_products_uls(self):

        # for page_num in range(1, self.__tabs_amount):
        for page_num in range(1, 4):
            main_site_response = requests.get(self.__laptops_catalog_url + str(page_num) + '/')

            main_site_content = str(main_site_response.text)

            main_site_soup = bs(main_site_content, 'html.parser')

            list_of_link_dom_element = main_site_soup.find_all('a', attrs={'class': 'productLink'})

            for link_element in list_of_link_dom_element:
                url = link_element['href']
                self.__list_of_products_url.append('https://www.morele.net/' + url)

    def save_computer_spec_to_file(self):
        main_string = str(self.__price) + ',' + str(self.__spec_core) + ',' + str(self.__spec_ram) + ',' + str(
            self.__spec_disc_type) + ',' + str(
            self.__spec_disc_capacity) + ',' + str(self.__spec_display) + ',' + str(
            self.__spec_operating_system) + ',' + str(self.__spec_guaranty)

        with open('computers-specification-morele-net.csv', 'a+', newline='') as data_file:
            csv_writer = csv.writer(data_file, delimiter=';', quotechar=' ')
            csv_writer.writerow((main_string,))

    def get_computer_spec(self, prod_url):
        product_site_response = requests.get(prod_url)

        product_site_content = str(product_site_response.text)

        product_site_soup = bs(product_site_content, 'html.parser')

        # get product price
        try:
            price_dom_obj = product_site_soup.find('div', attrs={'id': 'product_price_brutto'})

            final_price = price_dom_obj['content']

            self.__price = float(final_price)
        except:
            print('x')

        # get product specification
        specification_list = product_site_soup.find_all('div', attrs={'class': 'table-info-item'})

        for property in specification_list:
            try:
                spec_title = property.find('div', attrs={'class': 'table-info-inner name'}).find('a').text

                spec_value = property.find('div', attrs={'class', 'info-item'}).text

                if 'Liczba rdzeni / wątków' in spec_title:
                    self.__spec_core = int(re.search(r"^[0-9]{1,}", spec_value).group())

                if 'Pamięć RAM (zainstalowana)' in spec_title:
                    self.__spec_ram = int(re.search(r'\d+', spec_value).group())

                # ---- Disc type and capacity
                if 'Dysk HDD' in spec_title:
                    if 'Brak' in spec_value:
                        self.__spec_disc_type = 'SSD'
                    else:
                        self.__spec_disc_type = 'HDD'
                        self.__spec_disc_capacity = int(re.search(r"^[0-9]{1,}", spec_value).group())

                if 'Dysk SSD' == spec_title:
                    if 'Brak' not in spec_value:
                        self.__spec_disc_type = 'SSD'
                        self.__spec_disc_capacity = int(re.search(r"^[0-9]{1,}", spec_value).group())

                if 'Dysk SSD M.2' in spec_title:
                    if 'Brak' not in spec_value:
                        self.__spec_disc_type = 'SSD'
                        self.__spec_disc_capacity = int(re.search(r"^[0-9]{1,}", spec_value).group())

                if 'Dysk SSD M.2 PCIe' in spec_title:

                    if 'Brak' not in spec_value:
                        self.__spec_disc_type = 'SSD'
                        self.__spec_disc_capacity = int(re.search(r"^[0-9]{1,}", spec_value).group())

                if 'Przekątna ekranu [cal]' in spec_title:
                    self.__spec_display = float(spec_value)

                if 'System operacyjny' in spec_title:
                    if 'Windows' in spec_value:
                        self.__spec_operating_system = 'Windows'
                    elif 'macOS' in spec_value:
                        self.__spec_operating_system = 'macOS'
                    else:
                        self.__spec_operating_system = 'Other'

            except BaseException as err:
                # print(err)
                continue

        # get warranty
        # warranty_table = product_site_soup.find('div', attrs={'class': 'warranty-table specification-table'})
        # warranty_table_sections = warranty_table.find_all('div', attrs={'class', 'table-info'})
        #
        # for section in warranty_table_sections:
        #     rows = section.find_all('div', attrs={'class', 'table-info-item'})
        #
        #     for row in rows:
        #         name = row.find('div', attrs={'class', 'table-info-inner name'}).text
        #         value = row.find('div', attrs={'class', 'info-item'}).text
        #
        #         if 'Długość' in name:
        #             self.__spec_guaranty = int(re.search(r"[0-9]{1,}", value).group())

        # for test purpose only
        print(self.__price)
        print(self.__spec_core)
        print(self.__spec_ram)
        print(self.__spec_disc_type)
        print(self.__spec_disc_capacity)
        print(self.__spec_display)
        print(self.__spec_operating_system)
        print(self.__spec_guaranty)

        self.save_computer_spec_to_file()

    def main(self):
        self.get_amount_of_tabs()

        print('amount of tabs ---> ' + str(self.__tabs_amount))

        self.make_list_of_products_uls()

        counter = 0

        print('amount of products ---> ' + str(len(self.__list_of_products_url)))

        for url in self.__list_of_products_url:

            self.get_computer_spec(url)

            counter += 1

            if counter > 10:
                break


# main
mediaMarktScraper = MediaMarktScraper()
mediaMarktScraper.main()

# moreleNetScraper = MoreleNetScraper()
# moreleNetScraper.main()
# moreleNetScraper.get_computer_spec('https://www.morele.net/laptop-hp-15-db1010nw-7kc24ea-5940527/')
