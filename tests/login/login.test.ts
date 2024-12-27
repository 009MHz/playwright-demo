// File: src/tests/login.spec.ts
import { test } from '@playwright/test';
import { LoginPage } from '../../pages/login/loginPage';
import { PreCond } from '../../pages/login/PreCond';

test.describe('Login Page - Unit Test', () => {
    let loginPage: LoginPage;
    let preCond: PreCond;

    test.beforeEach(async ({ page }) => {
        preCond = new PreCond(page);
        loginPage = new LoginPage(page);
        await preCond.loadLoginPage();
    });

    test('Login Page Initial State Check: Page Header & Information', async () => {
        await loginPage.look('h2'); // Header check
        await loginPage.look('.subheader'); // Sub-header check
    });

    test('Login Page Initial State Check: Login Form Component', async () => {
        await loginPage.look('#username'); // Username field check
        await loginPage.look('#password'); // Password field check
        await loginPage.look("//button[@type='submit']"); // Login button check
    });

    test('Normal Login Page Action Flow', async () => {
        await loginPage.usernameInsert('tomsmith');
        await loginPage.passwordInsert('SuperSecretPassword!');
        await loginPage.clickLoginBtn();
        await loginPage.validateLoginSuccess();
    });

    test.describe('Invalid Username Scenarios', () => {
        const invalidUsernameTests = [
            { scheme: 'incorrect', username: 'InvalidUser', description: 'Invalid username' },
            { scheme: 'empty', username: '', description: 'Empty username' },
        ];

        invalidUsernameTests.forEach(({ scheme, username, description }) => {
            test(`Invalid Username: ${description}`, async () => {
                if (scheme === 'incorrect') {
                    await loginPage.usernameInsert(username);
                }

                if (scheme === 'empty') {
                    // Leave username empty
                }

                await loginPage.passwordInsert('SuperSecretPassword!');
                await loginPage.clickLoginBtn();
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
                await loginPage.usernameInsert('tomsmith');

                if (scheme === 'incorrect') {
                    await loginPage.passwordInsert(password);
                }

                if (scheme === 'empty') {
                    // Leave password empty
                }

                await loginPage.clickLoginBtn();
                // Add assertions for invalid password banner
            });
        });
    });
});
