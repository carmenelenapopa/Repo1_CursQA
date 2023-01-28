import unittest
from unittest import TestCase

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from webdriver_manager.firefox import GeckoDriverManager

import Keys


class Firefox2(TestCase):
    TEXT = (By.ID, "tinymce")
    DROPDOWN = (By.LINK_TEXT, "Dropdown")


# Definirea metodei de setUp
    def setUp(self) -> None:
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.get("https://the-internet.herokuapp.com/")
        self.firefox.maximize_window()

# Definirea metodei de tearDown
    def tearDown(self) -> None:
        self.firefox.quit()


    def test_frames(self):
        self.firefox.find_element(By.LINK_TEXT, "Frames").click()
        self.firefox.find_element(By.LINK_TEXT, "iFrame").click()
        time.sleep(2)
        self.firefox.switch_to.frame("mce_0_ifr")
        time.sleep(2)
        self.firefox.find_element(By.ID, "tinymce").click()
        self.firefox.find_element(By.ID, "tinymce").clear()
        self.firefox.find_element(By.ID, "tinymce").send_keys("I want chocolate!")
        time.sleep(2)


    def test_dropdown(self):
        self.firefox.find_element(*self.DROPDOWN).click()
        time.sleep(2)
        dropdown2 = Select(self.firefox.find_element(By.ID, "dropdown"))
        dropdown2.select_by_value('2')
        time.sleep(2)

        dropdown1 = Select(self.firefox.find_element(By.ID, "dropdown"))
        dropdown1.select_by_value("1")
        time.sleep(2)

    def test_checkboxes(self):
        self.firefox.get("https://the-internet.herokuapp.com/")
        self.firefox.find_element(By.LINK_TEXT, "Checkboxes").click()
        time.sleep(2)
        self.firefox.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]").click()
        time.sleep(2)
        self.firefox.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[2]").click()
        time.sleep(2)


    def test_switch_to_window(self):
        self.firefox.get("https://the-internet.herokuapp.com/")
        self.firefox.find_element(By.LINK_TEXT, "Multiple Windows").click()
        time.sleep(2)
        self.firefox.find_element(By.LINK_TEXT, "Click Here").click()
        time.sleep(2)
        windowids = self.firefox.window_handles
        parent_window_id = windowids[0]  #a745cfb5-7980-4510-a9ca-94b01bf74584 - id ul este dinamic; se schimba la fiecare accesare
        child_window_id = windowids[1]   #86020132-a3d7-4b8e-be33-02d778705a8c - id ul este dinamic; se schimba la fiecare accesare
        print(parent_window_id, child_window_id)
        time.sleep(2)
        self.firefox.switch_to.window(parent_window_id)
        print(parent_window_id.title())
        self.firefox.switch_to.window(child_window_id)
        print(child_window_id.title())