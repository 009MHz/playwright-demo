import { Page } from '@playwright/test';
import * as allure from 'allure-js-commons';

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

    async _capture(filename: string): Promise<void> {
        /**
         * Captures a screenshot of the current step/function and uploads it directly to Allure.
         *
         * @param filename The name of the screenshot file (e.g., "Invalid Username Banner").
         */
        // const screenshotMode = process.env.screenshot;
        // if (screenshotMode !== "off" && screenshotMode !== undefined) {
            await allure.attachment(
              filename,
              await this.page.screenshot({ fullPage: true }),
              allure.ContentType.PNG
            );
        }
    // }
}
