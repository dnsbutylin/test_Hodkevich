

class Locator(object):

    # Локаторы страницы авторизации
    username = 'mailbox:login'
    password = 'mailbox:password'
    submit_button = 'input.o-control'
    mail_error_massege = 'mailbox:error'

    # Локаторы страницы облака
    upload_button = 'span.b-toolbar__btn__text.b-toolbar__btn__text_pad'
    input_picture_button = '//div[2]/div/input'
    replace_button = '//div[3]/button/span'
    save_both_button = '//div[3]/button[2]/span'

    #Локаторы страницы картинки
    delete_button = "div.b-toolbar__btn.b-toolbar__btn_invert.b-toolbar__btn_data-remove.b-toolbar__" \
                                    "btn_grouped.b-toolbar__btn_grouped_first.b-toolbar__btn_grouped_last > " \
                                    "span.b-toolbar__btn__text.b-toolbar__btn__text_pad"
    confirm_delete_button = '//div[3]/div/button/span'
    download_button = '//div[2]/div/div/div/div/div/div/span'
    close_advertising1 = 'svg.Dialog__close--1rKyk > path'
    close_advertising2 = 'div.b-panel__close__icon'
    #adversiting3 = "//div[@id = 'app']/div[2]/div[36]/div/div/div/div/div/div/div/div/div/div"

    # Локаторы страницы mail.ru
    on_cloud_page_button = 'span.widget__ico.widget__ico_cloud'