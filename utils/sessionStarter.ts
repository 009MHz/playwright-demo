import { chromium } from '@playwright/test';
import { LoginPage } from '../pages/login/LoginPage';

(async () => {
  const browser = await chromium.launch(); // Launch browser
  const context = await browser.newContext(); // Create a new context
  const page = await context.newPage(); // Create a new page

  const loginPage = new LoginPage(page); // Use your existing LoginPage class
  await loginPage.LoginInit(); // Perform the login action

  // Save the storage state after login
  await context.storageState({ path: '../.auth/session.json' });

  await browser.close(); // Close the browser
})();
