import { test as base } from '@playwright/test';
import { LoginPage } from '../pages/login/loginPage';

// Extend the base test with a custom fixture
export const test = base.extend<{
  loggedInPage: LoginPage;
}>({
  loggedInPage: async ({ browser }, use) => {
    // Load the saved storage state
    const context = await browser.newContext({ storageState: '.auth/session.json' });
    const page = await context.newPage();

    // Initialize the LoginPage with the pre-authenticated context
    const loginPage = new LoginPage(page);
    await use(loginPage); // Pass the instance to the test

    await context.close(); // Clean up context
  },
});

export const expect = test.expect; // Re-export expect for consistency
