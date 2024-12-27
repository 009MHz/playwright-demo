import { BasePage } from '../__base';
import { Interactor, PageInfo, Url } from '../../elements/__login';
import { expect, Page } from '@playwright/test';

export class LoginPage extends BasePage {
    constructor(page: Page) {
        super(page);
    }

    async openPage() {
        await this.page.goto(Url.login);
        expect(this.page.url()).toContain('/login');
    }

    async usernameInsert(username: string) {
        expect(await this._find(Interactor.username_input).isVisible()).toBeTruthy();
        await this._type(Interactor.username_input, username);
        await this._capture("Username Insert");
    }

    async passwordInsert(password: string) {
        expect(await this._find(Interactor.password_input).isVisible()).toBeTruthy();
        await this._type(Interactor.password_input, password);
        await this._capture("Password Insert");
    }

    async _clickLoginBtn() {
        await this._click(Interactor.login_btn);
    }

    async validateLoginSuccess() {
        expect(this.page.url()).toContain('secure');
    }
}