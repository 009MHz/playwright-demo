import * as allure from "allure-js-commons";
import { test } from '@playwright/test';
import { LoginPage } from '../../pages/login/loginPage';
import { PreCond } from '../../pages/login/PreCond';

test.describe('Login Page - Unit Test', () => {
  let logIn: LoginPage;
  let preCond: PreCond;
  
  test.beforeEach(async ({ page }) => {
    preCond = new PreCond(page);
    logIn = new LoginPage(page);
    allure.epic('Login');
    allure.story('Login Page Unit Test');
    await preCond.loadLoginPage();
  });
  
  test('Login Page Initial State Check: Page Header & Information', async () => {
    allure.feature("Login Page/ Header")
    allure.feature("Login Page/ Header/ Information")
    allure.severity("Medium")
    await allure.step('Verify the header existence', async () => 
      logIn.HeaderPresence());

    await allure.step('Verify the subheader presence', async () => 
      logIn.SubheaderPresence());
  });
    

  test('Login Page Initial State Check: Login Form Component', async () => {
    allure.feature("Login Page/ Login Form")
    allure.severity("Critical")

    allure.feature("Login Page/ Login Form/ Username")
    await allure.step('Verify the "username" field', async() => 
      logIn.usernameFieldPresence());
      

    allure.feature("Login Page/ Login Form/ Password")
    await allure.step('Verify the "password" field', async() => 
      logIn.passwordFieldPresence());  

    allure.feature("Login Page/ Login Form/ Login Button")
    await allure.step('Verify the "Login" button', async() => 
      logIn.loginButtonPresence());        
  });

  test('Normal Login Page Action Flow', async() => {
    allure.feature("Login Page/ Login Form")
    allure.feature("Login Page/ Login Form/ Username")
    allure.severity("Critical")
    await allure.step('1. Insert a valid username', async() => 
      logIn.usernameInsert('tomsmith'));

    allure.feature("Login Page/ Login Form/ Password")
    await allure.step('2. Insert a valid password', async () =>
      logIn.passwordInsert('SuperSecretPassword!'));
      
    allure.feature("Login Page/ Login Form/ Login Button")
    await allure.step('3. Click on the "Login" button', async() =>
      logIn.clickLoginBtn());
  });
  
  for (const { scheme, username } of [
    { scheme: "incorrect", username: "InvalidUser" },
    { scheme: "empty", username: "" },
  ]) {
    test(`'${scheme}' username scenario, should return the correct information`, async ({ page }) => {
      allure.feature("Login Page/ Banner/ Invalid Banner")
      allure.severity("Medium");
      allure.description(`Scenario: \`${scheme}\``);

      allure.feature("Login Page/ Login Form/ Username")
      await allure.step(`1. Insert \`${scheme}\` value on the username field`, async () => {
        await logIn.usernameInsert(username);
      });
  
      allure.feature("Login Page/ Login Form/ Password")
      await allure.step('2. Insert a valid password', async () => {
        await logIn.passwordInsert('SuperSecretPassword!');
      });
  
      allure.feature("Login Page/ Login Form/ Login Button")
      await allure.step('3. Click on the Login button', async () => {
        await logIn.clickLoginBtn();
      });
  
      allure.feature("Login Page/ Banner/ Invalid Banner/ Username")
      await allure.step(`4. Verify the ${scheme} banner presence`, async () => {
        await logIn.invalidBannerUsernamePresence();
      });
    });
  }

  for (const { scheme, password } of [
    { scheme: "incorrect", password: "InvalidPassword" },
    { scheme: "empty", password: "" },
  ]) {
    test(`'${scheme}' password scenario, should return the correct information`, async ({ page }) => {
      allure.severity("Medium");
      allure.description(`Scenario: \`${scheme}\``);
  
      await allure.step(`1. Insert a valid user on the username field`, async () => {
        await logIn.usernameInsert('tomsmith');
      });
  
      await allure.step(`2. Insert \`${scheme}\` value on the password field`, async () => {
        await logIn.passwordInsert(password);
      });
  
      await allure.step('3. Click on the Login button', async () => {
        await logIn.clickLoginBtn();
      });
  
      await allure.step(`4. Verify the ${scheme} banner presence`, async () => {
        await logIn.invalidBannerPasswordPresence();
      });
    });
  }
});
