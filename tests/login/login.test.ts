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
    allure.feature('Login Page Unit Test');
    await preCond.loadLoginPage();
  });
  
  test('Login Page Initial State Check: Page Header & Information', async () => {
    allure.severity("Medium")
    await allure.step('Verify the header existence', async () => 
      logIn.HeaderPresence());

    await allure.step('Verify the subheader presence', async () => 
      logIn.SubheaderPresence());
  });
    

  test('Login Page Initial State Check: Login Form Component', async () => {
    allure.severity("Critical")
    await allure.step('Verify the "username" field', async() => 
      logIn.usernameFieldPresence());  

    await allure.step('Verify the "password" field', async() => 
      logIn.passwordFieldPresence());  

    await allure.step('Verify the "Login" button', async() => 
      logIn.loginButtonPresence());        
  });

  test('Normal Login Page Action Flow', async() => {
    allure.severity("Critical")
    await allure.step('1. Insert a valid username', async() => 
      logIn.usernameInsert('tomsmith'));

    await allure.step('2. Insert a valid password', async () =>
      logIn.passwordInsert('SuperSecretPassword!'));
      
    await allure.step('3. Click on the "Login" button', async() =>
      logIn.clickLoginBtn());
  });

  // test('Invalid Username should return the correct information', async () => {
  //   const flow = [
  //     { scheme: 'incorrect', username: 'InvalidUser' },
  //     { scheme: 'empty', username: '' }
  //   ];
    
  //   for (const { scheme, username } of flow) {
  //       await allure.step(`1. Insert \`${username}\` on the username field`, async () => {
  //         await logIn.usernameInsert(username);
  //       });

  //     await allure.step('2. Insert a valid password', async () => {
  //       await logIn.passwordInsert('SuperSecretPassword!');
  //     });

  //     await allure.step('3. Click on the Login button', async () => {
  //       await logIn.clickLoginBtn();
  //     });

  //     await allure.step(`4. Verify the ${scheme} banner`, async () => {
  //       await logIn.invalidBannerUsernamePresence();
  //     });
  //   }
  // });

});

    // test.describe('Invalid Username should return the correct banner', () => {
    //     const invalidUsernameTests = [
    //         { scheme: 'incorrect', username: 'InvalidUser', description: 'Invalid username' },
    //         { scheme: 'empty', username: '', description: 'Empty username' },
    //     ];
    //             if (scheme === 'incorrect') {
    //                 await logIn.usernameInsert(username);
    //             }

    //             if (scheme === 'empty') {
    //                 // Leave username empty
    //             }

    //             await logIn.passwordInsert('SuperSecretPassword!');
    //             await logIn.clickLoginBtn();
    //             // Add assertions for invalid username banner
    //         });
    //     });

//     test.describe('Invalid Password Scenarios', () => {
//         const invalidPasswordTests = [
//             { scheme: 'incorrect', password: 'InvalidPassword', description: 'Invalid password' },
//             { scheme: 'empty', password: '', description: 'Empty password' },
//         ];

//         invalidPasswordTests.forEach(({ scheme, password, description }) => {
//             test(`Invalid Password: ${description}`, async () => {
//                 await logIn.usernameInsert('tomsmith');

//                 if (scheme === 'incorrect') {
//                     await logIn.passwordInsert(password);
//                 }

//                 if (scheme === 'empty') {
//                     // Leave password empty
//                 }

//                 await logIn.clickLoginBtn();
//                 // Add assertions for invalid password banner
//             });
//         });
//     });


// test('Testing Step', async () => {
    //   await allure.step('1. Testing Step a', async() =>
    //     module.children1());  

    //   await allure.step('2. Testing Step b', async() =>
    //     module.children2());  

    //   await allure.step('3. Testing Step c', async() =>
    //     module.children3));  
    // });