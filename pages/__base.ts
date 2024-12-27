import { Page } from '@playwright/test';

export class BasePage {
    constructor(protected page: Page) {}

    protected _find(locator: string) {
        return this.page.locator(locator);
    }

    async _look(locator: string, timeout: number = 10000) {
        await this.page.waitForSelector(locator, { state: 'visible', timeout });
    }

    async _conceal(locator: string, timeout: number = 7000) {
        await this.page.waitForSelector(locator, { state: 'hidden', timeout });
    }

    async _touch(locator: string, timeout: number = 10000) {
        await this._look(locator);
        await this.page.locator(locator).isEnabled({ timeout });
    }

    async _type(locator: string, text: string, timeout: number = 10000) {
        await this._look(locator, timeout);
        await this.page.locator(locator).fill(text);
    }

    async _click(locator: string, timeout: number = 25000) {
        await this._touch(locator, timeout);
        await this.page.locator(locator).click();
    }

    async _doubleClick(locator: string, timeout: number = 10000) {
        await this._touch(locator, timeout);
        await this.page.locator(locator).dblclick();
    }

    async _forceClick(locator: string, timeout: number = 25000) {
        await this._touch(locator, timeout);
        await this.page.locator(locator).click({ force: true });
    }

    async _capture(filename: string) {
        const screenshotPath = `reports/screenshots/${filename.replace(/\s+/g, '_')}.png`;
        await this.page.screenshot({ path: screenshotPath, fullPage: true });
    }
}