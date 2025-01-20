import { chromium } from '@playwright/test';
import { LoginPage } from "../pages/login/loginPage"
import * as fs from 'fs';

async function saveLoginSession() {
  let logIn: LoginPage;

  // Perform login actions
  await logIn.LoginInit()
    await context.storageState({ path: 'storageState.json' });
  } else {
    console.error('Login failed!');
  }

  await browser.close();
}

saveLoginSession();
