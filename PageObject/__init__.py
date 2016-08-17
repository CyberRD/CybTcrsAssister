class PageObject(object):

    def __init__(self, driver, assert_page=True):
        self._web_driver = driver
        self._assert_page = assert_page
        if assert_page: self.assert_on_this_page()

    def _transfer_to_page(self, page_class):
        return page_class(self._driver, self._assert_page)

    def _find_element_by_locator(self, locator):
        parts = locator.split('=', 1)
        if locator.startswith('//'):
           strategy = 'xpath'
        elif len(parts) == 1:
           strategy = 'identifier'
        else:
            strategy = parts[0]
            if strategy not in ['identifier', 'id', 'name', 'dom', 'xpath', 'link', 'css']:
                raise ValueError('The locator provided %s is not valid.' % locator)
            locator = parts[1]

        driver = self._web_driver
        if strategy == 'identifier': # id -> name
            elements = driver.find_elements_by_id(locator)
            return elements[0] if elements else driver.find_element_by_name(locator)
        elif strategy == 'id':
            return driver.find_element_by_id(locator)
        elif strategy == 'name':
            return driver.find_element_by_name(locator)
        elif strategy == 'dom':
            return driver.execute_script('return %s' % locator)
        elif strategy == 'xpath':
            return driver.find_element_by_xpath(locator)
        elif strategy == 'link':
            return driver.find_element_by_link_text(locator)
        elif strategy == 'css':
            return driver.find_element_by_css_selector(locator)
        else: assert False, strategy

    def assert_on_this_page(self):
        raise NotImplementedError()

    def click_elsewhere(self):
        self._driver.click('css=body')

    def refresh_this_page(self):
        sel = self._driver
        sel.open(sel.get_location())
        return self
