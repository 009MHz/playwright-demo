import { BasePage } from '../__base';
import { Url, Interactor } from '../../elements/__login';
import { Page, expect } from '@playwright/test';

export class PreCond extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  async loadLoginPage() {
    await this.page.goto(Url.login);
    expect(this.page.url()).toContain('/login');
  }

  async loadSuccessPage(username: string, password: string) {
    await this.loadLoginPage();
    await this._type(Interactor.username_input, username);
    await this._type(Interactor.password_input, password);
    await this._click(Interactor.login_btn);
    expect(this.page.url()).toContain('secure');
  }
}