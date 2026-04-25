import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# =====================
# 全局 driver fixture（夹具）：统一管理浏览器的创建和销毁
# =====================
# @pytest.fixture(scope="session")    # 整个测试会话只创建一个 driver 实例，所有测试用例共享这个实例，最后在测试结束时关闭浏览器
# def driver():
#     options = webdriver.ChromeOptions() # 创建浏览器配置
#     options.page_load_strategy = "eager"    # eager：页面 DOM 加载完成就继续执行
#     driver = webdriver.Chrome(options=options)
#     yield driver    # 把 driver 交给测试用例使用
#     driver.quit()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# 截图(用例测试失败)
def take_screenshot(driver, name="screenshot"):
    png = driver.get_screenshot_as_png()
    if png:
        allure.attach(png, name=name, attachment_type=allure.attachment_type.PNG)


@allure.feature("testing-management-platform")
@allure.story("登录功能")
@pytest.mark.parametrize(
    "email,password", [
    ("17201665342@163.com", "123456"),  # right account
    ("19283948437@163.com", "123456"),  # wrong account
    # ("taylor@163.com", "12345678"),
    # ("eric@163.com", "1234567890"),
])
@pytest.mark.smoke  # 使用：pytest -m smoke 来运行这个测试用例
def test_login(driver, email, password):
    with allure.step("打开登录页面"):
        driver.get("http://localhost:5173/login")

    with allure.step("输入邮箱密码"):
        wait = WebDriverWait(driver, 10) # 显式等待，等待元素加载完成

        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        email_input.clear()
        email_input.send_keys(email)

        password_input.clear()
        password_input.send_keys(password)

    with allure.step("点击登录按钮"):
        # 点击登录
        driver.find_element(By.CLASS_NAME, "submit-button").click()
    with allure.step("验证是否跳转到 ./dashboard 页面"):
        # 断言登录成功（URL变化）
        wait.until(lambda d: "dashboard" in d.current_url)

        try:
            wait.until(EC.url_contains("dashboard"))
            assert "dashboard" in driver.current_url, "应该跳转到 ./dashboard 页面"
        except (AssertionError, TimeoutException):
            take_screenshot(driver, "login_failed")
            raise