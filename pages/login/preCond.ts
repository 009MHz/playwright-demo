import { BasePage } from '../__base';
import { PageInfo, PageForm } from '../../elements/login/LoginElements';
import { Page, expect } from '@playwright/test';

export class PreCond extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  async openLoginPage() {
    await this.page.goto(PageInfo.url);
  }

  async loadSuccessPage(username: string, password: string) {
    await this.openLoginPage();
    await this._type(PageForm.usernameInput, username);
    await this._type(PageForm.passInput, password);
    await this._click(PageForm.loginBtn);
    expect(this.page.url()).toContain('dashboard/index');
  }
}