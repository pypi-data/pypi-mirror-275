from selenium.webdriver.common.keys import Keys
from transstellar.framework import Element


class DatePicker(Element):
    XPATH_CURRENT = '//div[contains(@class, "ant-picker ")]'
    XPATH_RANGE_PICKER = '//div[contains(@class, "ant-picker ant-picker-range")]'
    XPATH_INPUT = '//div[contains(@class, "ant-picker-input")]/input'

    def pick_date(self, target_date):
        self.logger.info(f"pick date: {target_date}")

        dom_element = self.find_dom_element_by_xpath(self.XPATH_INPUT)

        self.__update_date(dom_element, target_date)

    def range(self, from_date, to_date):
        self.logger.info(f"pick date range, from: {from_date}, to: {to_date}")

        inputs = self.find_dom_elements_by_tag_name("input")
        from_date_input = inputs[0]
        to_date_input = inputs[1]

        self.__update_date(from_date_input, from_date)
        self.__update_date(to_date_input, to_date)

    def get_basic_date_value(self):
        dom_element = self.find_dom_element_by_xpath(self.XPATH_INPUT)

        return dom_element.get_attribute("value")

    def get_date_range_values(self):
        inputs = self.find_dom_elements_by_tag_name("input")

        return [inputs[0].get_attribute("value"), inputs[1].get_attribute("value")]

    def __update_date(self, input_element, date):
        formatted_date = date.strftime("%Y-%m-%d")

        input_element.send_keys(Keys.CONTROL + "a")
        input_element.send_keys(Keys.DELETE)
        input_element.send_keys(formatted_date)

        assert input_element.get_attribute("value") == formatted_date
