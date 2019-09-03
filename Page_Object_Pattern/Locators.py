
class Locator(object):
    # Локаторы страницы авторизации
    username = 'mailbox:login'
    password = 'mailbox:password'
    submit_button = 'input.o-control'
    mail_error_massege = 'mailbox:error'

    # Локаторы страницы облака
    upload_button = "//div[@id='toolbar-left']/div/div/div/div/span"
    input_picture_button = '//div[2]/div/input'
    replace_button = '//div[3]/button/span'
    save_both_button = '//div[3]/button[2]/span'
    check_upload_locator = 'span.b-upload-status.b-upload-panel__header__status.js-upload-panel-header-status'

    # Локаторы страницы картинки
    delete_button = "//div[@id='viewer']/div/div[2]/div/div/div/div[2]/div/div/span"
    confirm_delete_button = '//div[3]/div/button/span'
    download_button = '//div[2]/div/div/div/div/div/div/span'
    close_advertising1 = 'svg.Dialog__close--1rKyk > path'
    close_advertising2 = 'div.b-panel__close__icon'

    # Локаторы страницы mail.ru
    on_cloud_page_button = 'span.widget__ico.widget__ico_cloud'
