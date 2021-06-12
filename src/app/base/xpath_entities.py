class LoginFormXpaths:
    input_username = "//*[@id='loginForm']/div/div[1]/div/label/input"
    input_password = "//*[@id='loginForm']/div/div[2]/div/label/input"
    button_submit = '//*[@id="loginForm"]/div/div[3]/button/div'
    button_has_account = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/div/div[1]/button'


class IndexPageXpaths:
    button_disable_notifications = '/html/body/div[4]/div/div/div/div[3]/button[2]'
    button_save_data = '//*[@id="react-root"]/section/main/div/div/div/section/div/button'
    button_logout = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div'
    menu_header_profile = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]'


class ProfilePageXpaths:
    visibility_profile = '//div/article/div/div/h2'
    post_url_template = '(//a[not(@class)])[{}]'
    post_template = '(//a[@href]/div/div[2])[{}]'
    post_time = '//div[3]/div[2]/a/time'
    post_likes_counter = '//section/div/div/a/span'
    post_like_status = '(//span/*[name()="svg"])[6]'
    button_close_post = '//body/div/div[3]/button'
    button_post_like = '//section/span/button'
    button_send_message = '//button/div[contains(text(), "Отправить сообщение")]'
    button_subscribe = '(//button[contains(text(), "Подписаться")])[1]'

