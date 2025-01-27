import { BasePage } from '../__base';
import { PageInfo, PageForm } from '@elements/login/LoginElements';
import { expect, Page } from '@playwright/test';

export class LoginPage extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  // Login Page Interaction
  async openPage() {
    await this.page.goto(PageInfo.url);
    await expect(this.page.url()).toContain('/auth/login');
  }

  async usernameInsert(username: string) {
    expect(await this._find(PageForm.usernameInput).isEditable()).toBeTruthy();
    await this._type(PageForm.usernameInput, username);
    // await expect(this._find(PageForm.usernameInput)).toBeEditable();
    await expect(this._find(PageForm.usernameInput)).not.toBeEmpty();
    await this._capture('Username Insert');
  }

  async passwordInsert(password: string) {
    expect(await this._find(PageForm.passInput).isVisible()).toBeTruthy();
    await this._type(PageForm.passInput, password);
    await expect(this._find(PageForm.passInput)).not.toBeEmpty();
    await this._capture('Password Insert');
  }

  async clickLoginBtn() {
    await this._click(PageForm.loginBtn);
  }

  // Login Page Validation
  async PageInfoPresence() {
    await this._look(PageInfo.brand)
    await expect(this._find(PageInfo.title)).toHaveText('Login')
  }

  async PageHintsPresence() {
    await this._look(PageInfo.hintsWrapper)
    
    await expect(this._find(PageInfo.hintsUser)).toContainText('Admin');
    await expect(this._find(PageInfo.hintsPassword)).toContainText('admin123');
  }

  async usernameInputPresence() {
    await this._look(PageForm.usernameLabel)
    await expect(this._find(PageForm.usernameLabel)).toHaveText('Username');

    await this._touch(PageForm.usernameInput)
    await expect(this._find(PageForm.usernameInput)).toBeEmpty();
    await expect(this._find(PageForm.usernameInput)).toHaveAttribute("placeholder", "Username");
  }

  async passwordInputPresence() {
    await this._look(PageForm.passLabel)
    await expect(this._find(PageForm.passLabel)).toHaveText('Password');

    await this._touch(PageForm.passInput)
    await expect(this._find(PageForm.passInput)).toBeEmpty();
    await expect(this._find(PageForm.passInput)).toHaveAttribute("placeholder", "Password");
  }

  async LoginButtonPresence() {
    await this._touch(PageForm.loginBtn)
    await expect(this._find(PageForm.loginBtn)).toHaveText('Login');
  }

    //Login Init action
    async LoginInit(username: string, password: string) {
      await this.openPage()
      await this.usernameInsert(username);
      await this.passwordInsert(password);
      await this.clickLoginBtn()
    };
}