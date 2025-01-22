import { BasePage } from '../__base';
import { PageInfo } from '../../elements/dashboard/Dashboardelement';
import { expect, Page } from '@playwright/test';

export class DashboardPage extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  // Login Page Interaction
  async openPage() {
    await this.page.goto(PageInfo.url);
    await expect(this.page.url()).toContain('/dashboard/index');
  }

}