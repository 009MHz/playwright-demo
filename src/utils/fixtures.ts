import { test as base, type Page, type BrowserContext } from '@playwright/test';
import { AuthStarter } from './sessionHandler';

class AdminPage {
  page: Page;

  constructor(page: Page) {
    this.page = page;
  }
}

class GuestPage {
  page: Page;

  constructor(page: Page) {
    this.page = page;
  }
}

// Declare the types of your fixtures.
type MyFixtures = {
  adminPage: AdminPage;
  guestPage: GuestPage;
};

export * from '@playwright/test';
export const test = base.extend<MyFixtures>({
  adminPage: async ({ browser }, use) => {
    const context: BrowserContext = await browser.newContext();
    try {
      const page = await context.newPage();
      const authStarter = new AuthStarter(page);

      await authStarter.handleSession(context);

      const adminPage = new AdminPage(page);
      await use(adminPage);
    } finally {
      await context.close();
    }
  },

  guestPage: async ({ browser }, use) => {
    const context: BrowserContext = await browser.newContext();
    try {
      const page = await context.newPage();
      const guestPage = new GuestPage(page);
      await use(guestPage);
    } finally {
      await context.close();
    }
  },
});
