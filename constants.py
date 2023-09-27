class Selectors:
    USER_EMAIL = "mat-input-0"
    USER_PASSWORD = 'input[formcontrolname="password"]'
    UA_LANGUAGE = "//nav[@class='nav nav--lang']/li[3]"
    FRAME = "//iframe"
    RECAPTCHA_CHECKBOX = "//span[contains(@class, 'recaptcha-checkbox-checked') and @role='checkbox']"
    LOGIN = 'button.btn.btn--submit'
    DEAL = "(//li[@class='nav__item'])[1]"
    PROFILE = 'td.ng-star-inserted'
    OPEN_CALENDAR = "(//div[@class='accordion__content'])[2]/button"
    PLACE_MENU = '//mat-select[@name="location"]'
    SELECT_PLACE = '(//mat-option[@class="mat-option mat-focus-indicator ng-tns-c62-19 ng-star-inserted"])[1]'
    QUEUE_MENU = "//mat-select[@name='queueName']"
    SELECT_QUEUE = '(//mat-option/span[@class="mat-option-text"])[2]'
    VERIFY = "//button[@class='mat-focus-indicator btn btn--mini mat-stroked-button mat-button-base']/span"
    SELECT_DATE = "//td[contains(@class, 'mat-calendar-body-cell')][not(contains(@class, 'mat-calendar-body-disabled'))][1]"

    SELECT_PLACE_2 = "//mat-option[@id='mat-option-3']"
    SELECT_PLACE_3 = "//mat-option[@id='mat-option-4']"
    NEXT_MONTH = "//button[@class='mat-focus-indicator mat-calendar-next-button mat-icon-button mat-button-base' and @aria-label='Next month']"
    FREE_DATE = "//td[contains(@class, 'mat-calendar-body-cell')][not(contains(@class, 'mat-calendar-body-disabled'))]"
