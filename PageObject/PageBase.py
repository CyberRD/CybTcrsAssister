# coding=UTF-8
import logging
import time, urlparse

from PageObject import PageObject

_logger = logging.getLogger(__name__)


class PageTcrsBase(PageObject):

    # def __init__(self):
    #     pass

    def assert_on_this_page(self):
        time.sleep(3)  # buffer time
        url = self._driver.get_location()

        actual = urlparse(url).path.split('/')[-1]
        expected = self._url_token
        if actual != expected:
            raise AssertionError(
                "The expected token should be '%s'. However, it is '%s'. The URL is '%s'" % (expected, actual, url))
        return self.wait_for_idle()

    # wait all locators have been loaded.
    def wait_for_idle(self, timeout_sec=120):
        sel = self._driver;

        timeout = time.time() + timeout_sec
        loaders = dict([(locator, True) for locator in self._get_loading_locators()])
        lastfor = False

        while time.time() < timeout:
            if self._is_ready_for_idle_testing():
                for locator in loaders:
                    loaders[locator] = sel.is_visible(locator) if sel.is_element_present(locator) else False

            if True in loaders.values():
                _logger.debug('The page is still loading; %s' % loaders)
                lastfor = False
                time.sleep(1)
            else:
                if lastfor:
                    _logger.debug('It DOES been fully loaded; %s' % loaders)
                    break
                _logger.debug('It seems like that the page is fully loaded; %s' % loaders)
                lastfor = True
                time.sleep(2) # at least last for n seconds
                for locator in loaders: loaders[locator] = True

        if True in loaders.values():
            raise Exception('Timeout; %s' % loaders)
        return self