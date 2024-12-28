import { BasePage } from '../__base';
import { Interactor, PageInfo, Url } from '../../elements/__login';
import { expect, Page } from '@playwright/test';

export class LoginPage extends BasePage {
  constructor(page: Page) {
    super(page);
  }


  // Login Page Interaction
  async openPage() {
    await this.page.goto(Url.login);
    expect(this.page.url).toContain('/login');
  }

  async usernameInsert(username: string) {
    expect(await this._find(Interactor.username_input).isEditable()).toBeTruthy();
    await this._type(Interactor.username_input, username);
    await expect(this._find(Interactor.username_input)).toBeEditable();
    await this._capture('Username Insert');
  }

  async passwordInsert(password: string) {
    expect(await this._find(Interactor.password_input).isVisible()).toBeTruthy();
    await this._type(Interactor.password_input, password);
    await this._capture('Password Insert');
  }

  async clickLoginBtn() {
    await this._click(Interactor.login_btn);
  }

  async closeSuccessBanner() {
    await expect(this._find(PageInfo.banner_main)).toContainText('You logged out of the secure area!');
    await this._click(PageInfo.banner_close);
    await expect(this._find(PageInfo.banner_main)).not.toBeVisible();
  }

  async closeInvalidUserBanner() {
    await expect(this._find(PageInfo.banner_main)).toContainText('username is invalid!');
    await this._click(PageInfo.banner_close);
    await expect(this._find(PageInfo.banner_main)).not.toBeVisible();
  }

  async closeInvalidPasswordBanner() {
    await expect(this._find(PageInfo.banner_main)).toContainText('password is invalid!');
    await this._click(PageInfo.banner_close);
    await expect(this._find(PageInfo.banner_main)).not.toBeVisible();
  }

  // Login Page Validation
  async urlRedirection() {
    expect(this.page.url).toContainEqual('/login');
  }

  async HeaderPresence() {
    await this._look(PageInfo.header)
    const page_header = await this._find(PageInfo.header).textContent();
    expect(page_header).toBe("Login Page");
  }

  async SubheaderPresence() {
    await this._look(PageInfo.sub_header)
    await expect(this._find(PageInfo.sub_header)).toContainText(
      "This is where you can log into the secure area");
    await expect(this._find(PageInfo.sub_header)).toContainText(
      "If the information is wrong you should see error messages");
  }

  async usernameFieldPresence() {
    await this._look(Interactor.username_label)
    await expect(this._find(Interactor.username_label)).toHaveText("Username")

    await this._look(Interactor.username_input)
    await expect(this._find(Interactor.username_input)).toBeEnabled()
    await expect(this._find(Interactor.username_input)).toBeEmpty()
  }

  async passwordFieldPresence() {
    await this._look(Interactor.password_label)
    await expect(this._find(Interactor.password_label)).toHaveText("Password")

    await this._look(Interactor.password_input)
    await expect(this._find(Interactor.password_input)).toBeEnabled()
    await expect(this._find(Interactor.password_input)).toBeEmpty()
  }

  //Login Page Validation: Successful Banner
  async loginButtonPresence() {
    await this._look(Interactor.login_btn)
    await expect(this._find(Interactor.login_btn)).toBeEnabled()
    await expect(this._find(Interactor.login_btn)).toContainText("Login")
  }

  async logoutBannerPresence() {
    await this._look(PageInfo.banner_main)
    await expect(this._find(PageInfo.banner_main)).toContainText("You logged out of the secure area!")
    await this._capture("Logout Success Banner")
  }

  async logoutCloseBannerPresence() {
    await this._look(PageInfo.banner_close)
    await expect(this._find(PageInfo.banner_close)).toBeEnabled()
  }

  // Login Page Validation: Invalid Banner
  async invalidBannerUsernamePresence() {
    await this._look(PageInfo.banner_main)
    await expect(this._find(PageInfo.banner_main)).toContainText("username is invalid!")
    await expect(this._find(PageInfo.banner_close)).toBeEnabled()
    await this._capture("Invalid Username Banner")
  }

  async invalidBannerPasswordPresence() {
    await this._look(PageInfo.banner_main)
    await expect(this._find(PageInfo.banner_main)).toContainText("password is invalid!")
    await expect(this._find(PageInfo.banner_close)).toBeEnabled()
    await this._capture("Invalid Password Banner")
  }
}
