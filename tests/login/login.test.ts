import * as allure from "allure-js-commons";
import { test } from '@playwright/test';
import { LoginPage } from '../../pages/login/loginPage';
import { PreCond } from '../../pages/login/PreCond';

test.describe('Login Page - Unit Test', () => {
  allure.epic('Login');
  allure.feature('Login Page Unit Test');
  let logIn: LoginPage;
  let preCond: PreCond;
  
  test.beforeEach(async ({ page }) => {
    preCond = new PreCond(page);
    logIn = new LoginPage(page);
    await preCond.loadLoginPage();
  });
  
  test('Login Page Initial State Check: Page Header & Information', async () => {
    await allure.step('Verify the header existence', async () => 
      logIn.HeaderPresence());

    await allure.step('Verify the subheader presence', async () => 
      logIn.SubheaderPresence());
  });
    

  test('Login Page Initial State Check: Login Form Component', async () => {
    await allure.step('Verify the "username" field', async() => 
      logIn.usernameFieldPresence());  

    await allure.step('Verify the "password" field', async() => 
      logIn.passwordFieldPresence());  

    await allure.step('Verify the "Login" button', async() => 
      logIn.loginButtonPresence());        
  });

  test('Normal Login Page Action Flow', async() => {
    await allure.step('1. Insert a valid username', async() => 
      logIn.usernameInsert('tomsmith'));

    await allure.step('2. Insert a valid password', async () =>
      logIn.passwordInsert('SuperSecretPassword!'));
      
    await allure.step('3. Click on the "Login" button', async() =>
      logIn.clickLoginBtn());
  });
});
