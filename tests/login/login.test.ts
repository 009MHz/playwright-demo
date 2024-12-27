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
        await preCond.loadLoginPage();
    });

    test('Login Page Initial State Check: Page Header & Information', async () => {
        await logIn.look('h2'); // Header check
        await logIn.look('.subheader'); // Sub-header check
    });

    test('Login Page Initial State Check: Login Form Component', async () => {
        await logIn.look('#username'); // Username field check
        await logIn.look('#password'); // Password field check
        await logIn.look("//button[@type='submit']"); // Login button check
    });

    test('Normal Login Page Action Flow', async () => {
        await logIn.usernameInsert('tomsmith');
        await logIn.passwordInsert('SuperSecretPassword!');
        await logIn.clickLoginBtn();
        await logIn.validateLoginSuccess();
    });

    test.describe('Invalid Username Scenarios', () => {
        const invalidUsernameTests = [
            { scheme: 'incorrect', username: 'InvalidUser', description: 'Invalid username' },
            { scheme: 'empty', username: '', description: 'Empty username' },
        ];

        invalidUsernameTests.forEach(({ scheme, username, description }) => {
            test(`Invalid Username: ${description}`, async () => {
                if (scheme === 'incorrect') {
                    await logIn.usernameInsert(username);
                }

                if (scheme === 'empty') {
                    // Leave username empty
                }

                await logIn.passwordInsert('SuperSecretPassword!');
                await logIn.clickLoginBtn();
                // Add assertions for invalid username banner
            });
        });
    });

    test.describe('Invalid Password Scenarios', () => {
        const invalidPasswordTests = [
            { scheme: 'incorrect', password: 'InvalidPassword', description: 'Invalid password' },
            { scheme: 'empty', password: '', description: 'Empty password' },
        ];

        invalidPasswordTests.forEach(({ scheme, password, description }) => {
            test(`Invalid Password: ${description}`, async () => {
                await logIn.usernameInsert('tomsmith');

                if (scheme === 'incorrect') {
                    await logIn.passwordInsert(password);
                }

                if (scheme === 'empty') {
                    // Leave password empty
                }

                await logIn.clickLoginBtn();
                // Add assertions for invalid password banner
            });
        });
    });
});
